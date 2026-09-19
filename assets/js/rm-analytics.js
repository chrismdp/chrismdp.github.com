/*
 * True on-screen visibility tracking for RightMessage widgets, plus successful
 * lead-form submissions, sent to PostHog.
 *
 * Loads before the RightMessage snippet. RM's own exposure tracking fires the
 * moment a step becomes the "current step" in the funnel, not when it is
 * actually painted on screen (an inline widget can be marked exposed at
 * mount time even if it sits below the fold, and the DOM can still show the
 * previous step for a tick after the bus event fires). This script gates our
 * own events on a fresh, from-scratch visibility check every time anything
 * relevant changes, and only uses RightMessage's bus events to learn which
 * offer/flow/experiment is involved.
 *
 * Events:
 *   rm_widget_viewed   - once per widget per page, when its DOM node has a
 *                         positive on-screen rectangle, is not CSS-hidden or
 *                         occluded, and the tab is visible.
 *   rm_offer_viewed    - once per widget+offer per page, when that offer is
 *                         both on screen (as above) AND actually rendered
 *                         (a form or CTA is in the DOM, not a leftover
 *                         question screen).
 *   rm_form_submitted  - once per widget+offer, on RightMessage's own
 *                         lead-capture success signal, before it redirects.
 *   rm_newsletter_experiment_assigned - once per page, the moment RightMessage's
 *                         bus reports the visitor is on the known native
 *                         variant of the newsletter popup headline test (see
 *                         below), regardless of whether the popup has been
 *                         shown on screen yet. This is an assignment event,
 *                         not a visibility event.
 *
 * Property allowlist: widget_id, widget_type, flow_id, offer_id, is_newsletter,
 * experiment_id, experiment_variant, page_path. Never email, name, form
 * answers, or the raw RightMessage payload.
 *
 * Newsletter popup headline experiment bridge: for the one native
 * RightMessage split test that PostHog needs to analyse (pid 1563064411, on
 * widget wdg_trpf409s / offer ofr_VqL5OY0S), every rm_offer_viewed,
 * rm_form_submitted and rm_newsletter_experiment_assigned event for that
 * exact widget+offer also carries an explicit
 * "$feature/newsletter-popup-headline" property, set to RightMessage's own
 * variant id (never PostHog's getFeatureFlag - this is a read of RM's
 * existing assignment, not a call into PostHog's own flag/experiment
 * evaluation). PostHog treats a "$feature/<key>" event property as an
 * explicit override of that flag's value for the event, taking precedence
 * over whatever PostHog would otherwise have assigned. Only fires once the
 * variant is one of the two known native variant ids - an unassigned or
 * stale/unknown value is left off, never guessed as control. No other offer
 * or experiment ever gets this property.
 *
 * RightMessage's own PostHog integration (RM dashboard > Settings >
 * Integrations, config.settings.integrations) sends a differently-shaped
 * "rm_form_submitted" event if enabled there. Keep that integration OFF -
 * this script is the single source for that event name.
 *
 * Success comes from RightMessage's own `integration.hooks.onFormSubmitted`
 * hook, not the "offer_conversions" bus event: RM emits "offer_conversions"
 * (isLeadCapture: true) even when the lead-capture request fails (its own
 * catch branch after "Integration sync failed during form submission"), but
 * only calls onFormSubmitted after a real success.
 */
(function () {
  "use strict";

  // The two offers that are newsletter sign-ups (shared original + the
  // active split-test clone).
  var NEWSLETTER_OFFER_IDS = ["ofr_xi6l3r4n", "ofr_VqL5OY0S"];

  // The one native RightMessage split test bridged to a PostHog feature
  // flag - see the file header comment above.
  var NEWSLETTER_EXPERIMENT_WIDGET_ID = "wdg_trpf409s";
  var NEWSLETTER_EXPERIMENT_OFFER_ID = "ofr_VqL5OY0S";
  var NEWSLETTER_EXPERIMENT_PID = "1563064411";
  var NEWSLETTER_EXPERIMENT_FEATURE_KEY = "newsletter-popup-headline";
  var NEWSLETTER_EXPERIMENT_KNOWN_VARIANTS = ["control", "var_newsletter_benefit_202609"];

  var widgetState = {}; // widgetId -> { el, visible, currentOffer, widgetViewedSent, offerViewedSent: {offerId:true}, formSubmittedSent: {offerId:true} }
  var newsletterExperimentAssignedSent = false; // once per page, not per widget - there is only one such experiment
  var splitTestIndex = []; // [{resourceType, resourceId, pid, variantIds:[...]}]
  var widgetMeta = {}; // widgetId -> { type, flowId }
  var observedElements = typeof WeakSet === "function" ? new WeakSet() : null;

  function getState(widgetId) {
    if (!widgetState[widgetId]) {
      widgetState[widgetId] = {
        el: null,
        visible: false,
        currentOffer: null,
        widgetViewedSent: false,
        offerViewedSent: {},
        formSubmittedSent: {},
      };
    }
    return widgetState[widgetId];
  }

  // --- Visibility: recomputed from scratch every time, never trusted stale ---

  function isElementActuallyVisible(el) {
    if (typeof el.checkVisibility === "function") {
      return el.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true });
    }
    var style = window.getComputedStyle(el);
    return style.display !== "none" && style.visibility !== "hidden" && parseFloat(style.opacity) !== 0;
  }

  // Positive on-screen rectangle (any overlap counts - a widget taller than
  // the viewport must not need 50% of its own height to qualify), not
  // CSS-hidden, and not covered by something else (e.g. a modal on top of an
  // inline offer), in a visible tab.
  function computeVisibility(el) {
    if (document.visibilityState !== "visible") return false;
    if (!document.documentElement.contains(el)) return false;
    var rect = el.getBoundingClientRect();
    var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
    var viewportHeight = window.innerHeight || document.documentElement.clientHeight;
    var visLeft = Math.max(rect.left, 0);
    var visTop = Math.max(rect.top, 0);
    var visRight = Math.min(rect.right, viewportWidth);
    var visBottom = Math.min(rect.bottom, viewportHeight);
    if (visRight <= visLeft || visBottom <= visTop) return false;
    if (!isElementActuallyVisible(el)) return false;
    var sampleX = (visLeft + visRight) / 2;
    var sampleY = (visTop + visBottom) / 2;
    var topEl = document.elementFromPoint(sampleX, sampleY);
    if (topEl && topEl !== el && !el.contains(topEl) && !topEl.contains(el)) return false;
    return true;
  }

  // A step becoming "current" on the bus can arrive a tick before RM
  // re-renders it - require the actual offer markup (form or CTA) to be in
  // the DOM, and itself genuinely on screen (not merely present - it can
  // exist behind its own fade-in or a loading placeholder), before treating
  // the offer as visible.
  function widgetShowsOfferNode(el) {
    var offerNode = el.querySelector(".rm-form, .rm-action-area, button.rm-submit");
    return !!offerNode && computeVisibility(offerNode);
  }

  function recheckWidget(widgetId) {
    var state = widgetState[widgetId];
    if (!state || !state.el) return;
    // Assignment is not a visibility event - attempt it (and retry it if an
    // earlier attempt could not reach PostHog) on every recheck, ahead of
    // the visibility gate below.
    if (state.currentOffer) {
      maybeEmitNewsletterExperimentAssigned(widgetId, state.currentOffer.offerId, state.currentOffer.flowId);
    }
    state.visible = computeVisibility(state.el);
    if (state.visible) {
      maybeEmitWidgetViewed(widgetId);
      maybeEmitOfferViewed(widgetId);
    }
  }

  function recheckAllWidgets() {
    Object.keys(widgetState).forEach(recheckWidget);
  }

  // --- Suppression + PostHog capture ---

  // window.RightMessage.analyticsSuppressed is not actually exported by the
  // shipped SDK (it lives on RM's internal state only), so preview/disable
  // is checked from the URL directly - this also works before RM has
  // initialised. Once RM is up, also defer to its own already-computed gate,
  // sources.metrics.isAnalyticsEnabled(), which additionally covers debug
  // mode, __rm_test, and any hostname/IP suppression rules configured in
  // the RM dashboard. Neither covers RM's own preview mode, so that is
  // checked separately via RightMessage.previewing.
  function isAnalyticsSuppressed() {
    try {
      var params = new URLSearchParams(window.location.search);
      if (params.get("__rm_disable_analytics") === "true") return true;
      if (params.has("rmpreview") || params.has("preview")) return true;
    } catch (e) {
      /* ignore */
    }
    if (window.RightMessage && window.RightMessage.previewing === true) return true;
    var metrics = window.RightMessage && window.RightMessage.sources && window.RightMessage.sources.metrics;
    if (metrics && typeof metrics.isAnalyticsEnabled === "function") {
      try {
        if (!metrics.isAnalyticsEnabled()) return true;
      } catch (e) {
        /* ignore */
      }
    }
    return false;
  }

  // Returns true only if the event was actually handed to PostHog, so
  // callers can avoid marking a suppressed/unavailable send as sent.
  function capture(event, props, options) {
    if (isAnalyticsSuppressed()) return false;
    if (typeof posthog === "undefined" || !posthog || typeof posthog.capture !== "function") {
      return false;
    }
    try {
      if (typeof posthog.has_opted_out_capturing === "function" && posthog.has_opted_out_capturing()) {
        return false;
      }
      posthog.capture(event, props, options);
      return true;
    } catch (e) {
      return false;
    }
  }

  // --- RightMessage's own split-test assignment, read-only ---
  //
  // splitTests.getVariantForResource() has a side effect: it assigns a
  // variant if one is not already stored. Reading sources.splitTests.data
  // directly (the same cache RM itself writes to and keys as
  // "<type>_<id>" or "<type>_<id>_<pid>") reports an assignment RM has
  // already made without ever making one ourselves.

  function findSplitTest(resourceType, resourceId) {
    for (var i = 0; i < splitTestIndex.length; i++) {
      var t = splitTestIndex[i];
      if (t.resourceType === resourceType && t.resourceId === resourceId) return t;
    }
    return null;
  }

  function getExperimentFields(resourceType, resourceId) {
    if (!resourceType || !resourceId) return {};
    var test = findSplitTest(resourceType, resourceId);
    if (!test) return {};
    var splitTests = window.RightMessage && window.RightMessage.sources && window.RightMessage.sources.splitTests;
    if (!splitTests || !splitTests.data) return {};
    var key = resourceType === "flow" ? resourceType + "_" + resourceId + "_" + test.pid : resourceType + "_" + resourceId;
    var assigned = splitTests.data[key];
    if (!assigned) return {}; // RM has not assigned this visitor yet - never guess
    if (assigned !== "control" && test.variantIds.indexOf(assigned) === -1) return {}; // stale/unknown value - omit rather than misreport
    return { experiment_id: test.pid, experiment_variant: assigned };
  }

  // Prefers an offer-level experiment over a flow-level one, since that is
  // the granularity of the live split test.
  function getExperimentFieldsForOffer(offerId, flowId) {
    var offerFields = getExperimentFields("offer", offerId);
    if (offerFields.experiment_id) return offerFields;
    return getExperimentFields("flow", flowId);
  }

  // Only for the one exact widget+offer+experiment this bridge covers, and
  // only once RightMessage has assigned one of its two known native
  // variants - never for any other offer/experiment, and never a guess.
  function newsletterExperimentFeatureProps(widgetId, offerId, experimentFields) {
    if (widgetId !== NEWSLETTER_EXPERIMENT_WIDGET_ID) return {};
    if (offerId !== NEWSLETTER_EXPERIMENT_OFFER_ID) return {};
    if (!experimentFields || experimentFields.experiment_id !== NEWSLETTER_EXPERIMENT_PID) return {};
    if (NEWSLETTER_EXPERIMENT_KNOWN_VARIANTS.indexOf(experimentFields.experiment_variant) === -1) return {};
    var props = {};
    props["$feature/" + NEWSLETTER_EXPERIMENT_FEATURE_KEY] = experimentFields.experiment_variant;
    return props;
  }

  // --- Building allowlisted properties ---

  function baseWidgetProps(widgetId, flowId) {
    var meta = widgetMeta[widgetId];
    var props = {
      widget_id: widgetId,
      page_path: window.location.pathname,
    };
    if (meta && meta.type) props.widget_type = meta.type;
    var resolvedFlowId = flowId || (meta && meta.flowId);
    if (resolvedFlowId) props.flow_id = resolvedFlowId;
    return props;
  }

  function maybeEmitWidgetViewed(widgetId) {
    var state = getState(widgetId);
    if (!state.visible || state.widgetViewedSent) return;
    var props = baseWidgetProps(widgetId);
    var experimentFields = getExperimentFields("flow", props.flow_id);
    for (var k in experimentFields) props[k] = experimentFields[k];
    if (capture("rm_widget_viewed", props)) state.widgetViewedSent = true;
  }

  function maybeEmitOfferViewed(widgetId) {
    var state = getState(widgetId);
    if (!state.visible || !state.currentOffer || !state.el) return;
    if (!widgetShowsOfferNode(state.el)) return;
    var offerId = state.currentOffer.offerId;
    if (state.offerViewedSent[offerId]) return;
    var props = baseWidgetProps(widgetId, state.currentOffer.flowId);
    props.offer_id = offerId;
    props.is_newsletter = NEWSLETTER_OFFER_IDS.indexOf(offerId) !== -1;
    var experimentFields = getExperimentFieldsForOffer(offerId, props.flow_id);
    for (var k in experimentFields) props[k] = experimentFields[k];
    var featureProps = newsletterExperimentFeatureProps(widgetId, offerId, experimentFields);
    for (var fk in featureProps) props[fk] = featureProps[fk];
    if (capture("rm_offer_viewed", props)) state.offerViewedSent[offerId] = true;
  }

  // Fires the moment RightMessage's bus reports the visitor on the known
  // native variant of the bridged experiment - before any visibility check,
  // and once per page. If capture() could not reach PostHog (suppressed,
  // not loaded yet, opted out), the page is not marked as sent, so the next
  // recheckWidget() retries it; an unknown/unassigned variant is likewise
  // never marked as sent, and never reported as control.
  function maybeEmitNewsletterExperimentAssigned(widgetId, offerId, flowId) {
    if (newsletterExperimentAssignedSent) return;
    var experimentFields = getExperimentFieldsForOffer(offerId, flowId);
    var featureProps = newsletterExperimentFeatureProps(widgetId, offerId, experimentFields);
    if (!featureProps["$feature/" + NEWSLETTER_EXPERIMENT_FEATURE_KEY]) return;
    var props = baseWidgetProps(widgetId, flowId);
    props.offer_id = offerId;
    props.is_newsletter = NEWSLETTER_OFFER_IDS.indexOf(offerId) !== -1;
    for (var k in experimentFields) props[k] = experimentFields[k];
    for (var fk in featureProps) props[fk] = featureProps[fk];
    if (capture("rm_newsletter_experiment_assigned", props)) newsletterExperimentAssignedSent = true;
  }

  function handleOfferExposure(data) {
    var widgetId = data.widgetId;
    if (!widgetId) return;
    getState(widgetId).currentOffer = { offerId: data.offerId, flowId: data.offerFunnelId };
    maybeEmitNewsletterExperimentAssigned(widgetId, data.offerId, data.offerFunnelId);
    recheckWidget(widgetId); // the DOM may not show the offer yet; recheckWidget re-verifies
  }

  function handleQuestionExposure(data) {
    var widgetId = data.widgetId;
    if (!widgetId) return;
    // The widget is currently showing a question, not an offer - clear so a
    // later visibility recheck does not attribute a stale offer to it.
    getState(widgetId).currentOffer = null;
  }

  // RightMessage calls integration.hooks.onFormSubmitted only from the
  // success path of a lead-capture submission (after its own network call
  // resolves), and never from the failure path - unlike the
  // "offer_conversions" bus event, which fires either way. The payload also
  // carries formData and visitorContext; only the four listed fields are
  // ever read from it.
  function handleFormSubmittedHook(payload) {
    if (!payload) return;
    var widgetId = payload.widgetId;
    var offerId = payload.offerId;
    if (!widgetId || !offerId) return;
    var state = getState(widgetId);
    if (state.formSubmittedSent[offerId]) return;
    var props = baseWidgetProps(widgetId, payload.flowId);
    if (payload.widgetType) props.widget_type = payload.widgetType;
    props.offer_id = offerId;
    props.is_newsletter = NEWSLETTER_OFFER_IDS.indexOf(offerId) !== -1;
    var experimentFields = getExperimentFieldsForOffer(offerId, props.flow_id);
    for (var k in experimentFields) props[k] = experimentFields[k];
    var featureProps = newsletterExperimentFeatureProps(widgetId, offerId, experimentFields);
    for (var fk in featureProps) props[fk] = featureProps[fk];
    // A real browser transport (sendBeacon) so the request has the best
    // chance of reaching the network before RightMessage's post-submission
    // redirect unloads the page.
    if (capture("rm_form_submitted", props, { send_instantly: true, transport: "sendBeacon" })) {
      state.formSubmittedSent[offerId] = true;
    }
  }

  var formSubmittedHookInstalled = false;

  // Installed lazily because window.RightMessage.integration does not exist
  // until RM's own init has run. An offer exposure always happens before any
  // submission, so trying this on every bus event is always in time.
  // Chains any hook already configured in the RM dashboard rather than
  // replacing it.
  function installFormSubmittedHookIfPossible() {
    if (formSubmittedHookInstalled) return;
    var integration = window.RightMessage && window.RightMessage.integration;
    if (!integration || !integration.hooks) return;
    formSubmittedHookInstalled = true;
    var previous = integration.hooks.onFormSubmitted;
    integration.hooks.onFormSubmitted = function (payload) {
      handleFormSubmittedHook(payload);
      if (typeof previous === "function") {
        return previous.apply(this, arguments);
      }
    };
  }

  function handleBusEvent(collection, data) {
    installFormSubmittedHookIfPossible();
    if (!data) return;
    if (collection === "offer_exposures") handleOfferExposure(data);
    else if (collection === "question_exposures") handleQuestionExposure(data);
  }

  function onConfigLoaded(config) {
    widgetMeta = {};
    var widgets = (config.rightCta && config.rightCta.widgets) || [];
    for (var i = 0; i < widgets.length; i++) {
      widgetMeta[widgets[i].id] = { type: widgets[i].type, flowId: widgets[i].contentId };
    }
    splitTestIndex = [];
    var tests = config.splitTests || [];
    for (var j = 0; j < tests.length; j++) {
      splitTestIndex.push({
        resourceType: tests[j].resource_type,
        resourceId: tests[j].resource_id,
        pid: tests[j].pid,
        variantIds: (tests[j].variants || []).map(function (v) {
          return v.id;
        }),
      });
    }
  }

  function onRmbusReady(bus) {
    if (!bus || typeof bus.on !== "function") return;
    bus.on("config", onConfigLoaded);
    bus.on("event", function (payload) {
      if (payload) handleBusEvent(payload.collection, payload.data);
    });
  }

  function installRmbusHook() {
    var current = window.rmbus;
    try {
      Object.defineProperty(window, "rmbus", {
        configurable: true,
        get: function () {
          return current;
        },
        set: function (bus) {
          current = bus;
          onRmbusReady(bus);
        },
      });
    } catch (e) {
      return; // if rmbus is already non-configurable, there is nothing safe to hook
    }
    if (current) onRmbusReady(current);
  }

  // --- Widget DOM discovery ---

  var WIDGET_CLASS_RE = /(?:^|\s)(rm-(wdg_[A-Za-z0-9]+))(?:\s|$)/;

  function widgetIdFromElement(el) {
    if (!el.className || typeof el.className !== "string") return null;
    var match = WIDGET_CLASS_RE.exec(" " + el.className + " ");
    return match ? match[2] : null;
  }

  function observeWidgetElement(el, widgetId) {
    if (observedElements) {
      if (observedElements.has(el)) return;
      observedElements.add(el);
    }
    getState(widgetId).el = el;
    if (typeof IntersectionObserver === "function") {
      new IntersectionObserver(function () {
        recheckWidget(widgetId);
      }).observe(el);
    }
    recheckWidget(widgetId);
  }

  function scanForWidgets(root) {
    if (!root || root.nodeType !== 1) return;
    var widgetId = widgetIdFromElement(root);
    if (widgetId) observeWidgetElement(root, widgetId);
    var candidates = root.querySelectorAll('[class*="rm-wdg_"]');
    for (var i = 0; i < candidates.length; i++) {
      var id = widgetIdFromElement(candidates[i]);
      if (id) observeWidgetElement(candidates[i], id);
    }
  }

  function installDomWatcher() {
    scanForWidgets(document.documentElement);
    if (typeof MutationObserver === "function") {
      new MutationObserver(function (mutations) {
        mutations.forEach(function (mutation) {
          mutation.addedNodes.forEach(function (node) {
            if (node.nodeType === 1) scanForWidgets(node);
          });
        });
        // A step transition (question -> offer, or an entrance animation
        // finishing) can change what a tracked widget shows without moving
        // it, so re-verify every tracked widget on every relevant mutation.
        recheckAllWidgets();
      }).observe(document.documentElement, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ["style", "class"],
      });
    }
  }

  function widgetIdForNode(node) {
    while (node && node.nodeType === 1) {
      var id = widgetIdFromElement(node);
      if (id) return id;
      node = node.parentNode;
    }
    return null;
  }

  document.addEventListener("visibilitychange", recheckAllWidgets);
  // The widget can already intersect while its form is below the viewport.
  // Recheck on scroll even when the widget's intersection state stays true.
  var scrollCheckPending = false;
  window.addEventListener("scroll", function () {
    if (scrollCheckPending) return;
    scrollCheckPending = true;
    window.requestAnimationFrame(function () {
      scrollCheckPending = false;
      recheckAllWidgets();
    });
  }, { passive: true, capture: true });
  window.addEventListener("resize", recheckAllWidgets);
  // A CSS entrance transition (e.g. a modal fading/sliding in) can finish
  // without any further DOM mutation - recheck once it completes.
  document.addEventListener(
    "transitionend",
    function (e) {
      var widgetId = widgetIdForNode(e.target);
      if (widgetId) recheckWidget(widgetId);
    },
    true
  );
  document.addEventListener(
    "animationend",
    function (e) {
      var widgetId = widgetIdForNode(e.target);
      if (widgetId) recheckWidget(widgetId);
    },
    true
  );

  installRmbusHook();

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", installDomWatcher);
  } else {
    installDomWatcher();
  }
})();
