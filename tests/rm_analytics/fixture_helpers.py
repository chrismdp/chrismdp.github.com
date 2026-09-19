"""Helpers for the fast, deterministic fixture tests.

These build a minimal page with a fake RightMessage bus (the same shape as
the real one: `.on(event, cb)` replays history, `.emit(event, payload)` calls
handlers synchronously) so a specific edge case can be driven directly,
without depending on network access or the live experiment's current state.
"""

import json

from harness import rm_analytics_source

FIXTURE_SETUP = """
window.__phEvents = [];
window.__phOptedOut = false;
window.posthog = {
  capture: function (event, props) { window.__phEvents.push({ event: event, props: props }); },
  has_opted_out_capturing: function () { return window.__phOptedOut === true; }
};

window.makeBus = function () {
  var handlers = {};
  var history = {};
  return {
    on: function (event, fn) {
      (handlers[event] = handlers[event] || []).push(fn);
      (history[event] || []).forEach(fn);
    },
    emit: function (event, payload) {
      (history[event] = history[event] || []).push(payload);
      (handlers[event] || []).forEach(function (fn) { fn(payload); });
    },
  };
};

window.rmConfig = {
  rightCta: { widgets: [{ id: "wdg_test", type: "inline", contentId: "ofn_test" }] },
  splitTests: [
    {
      resource_type: "offer",
      resource_id: "ofr_xi6l3r4n",
      pid: "999",
      variants: [{ id: "var_a" }],
    },
  ],
};

// The success signal is RightMessage's own integration.hooks.onFormSubmitted,
// installed lazily by the tracker the first time it sees a bus "event". This
// default gives it something to install onto.
window.RightMessage = { integration: { hooks: {} } };
"""


def new_fixture_page(context, body_html, extra_setup="", url="https://fixture.rm-analytics.test/"):
    """Serves a tiny fulfilled HTML page, wires up a fake rmbus + posthog
    mock, loads the real assets/js/rm-analytics.js into it, then emits the
    fake config. Returns the page with `window.rmbus` ready to drive."""
    page = context.new_page()
    page.route("**/*", lambda route: route.fulfill(status=200, content_type="text/html", body="<html><body>" + body_html + "</body></html>"))
    page.goto(url)
    page.evaluate(FIXTURE_SETUP + extra_setup)
    page.add_script_tag(content=rm_analytics_source())
    page.evaluate("window.rmbus = makeBus(); rmbus.emit('config', rmConfig);")
    return page


def emit_offer_exposure(page, widget_id="wdg_test", offer_id="ofr_xi6l3r4n", flow_id="ofn_test"):
    page.evaluate(
        "rmbus.emit('event', {collection: 'offer_exposures', data: "
        + json.dumps({"widgetId": widget_id, "offerId": offer_id, "offerFunnelId": flow_id, "isLeadCapture": True})
        + "})"
    )


def emit_question_exposure(page, widget_id="wdg_test", question_id="raq_test"):
    page.evaluate(
        "rmbus.emit('event', {collection: 'question_exposures', data: "
        + json.dumps({"widgetId": widget_id, "questionId": question_id})
        + "})"
    )


def trigger_form_submitted_hook(page, widget_id="wdg_test", widget_type="inline", offer_id="ofr_xi6l3r4n", flow_id="ofn_test"):
    """Simulates RightMessage calling its own success hook - the only thing
    that ever invokes integration.hooks.onFormSubmitted in the real SDK.
    emit_offer_exposure() (or any other bus event) must run first, since the
    tracker only installs its wrapper the first time it sees a bus event."""
    page.evaluate(
        "window.RightMessage.integration.hooks.onFormSubmitted("
        + json.dumps(
            {
                "widgetId": widget_id,
                "widgetType": widget_type,
                "flowId": flow_id,
                "offerId": offer_id,
                "offerName": "Test offer",
                "formData": {"email": "should-never-be-forwarded@example.invalid"},
                "visitorContext": {"subscriberId": "123"},
            }
        )
        + ")"
    )


def ph_events(page, name=None):
    events = page.evaluate("window.__phEvents || []")
    if name:
        events = [e for e in events if e["event"] == name]
    return events


def settle(page):
    page.wait_for_timeout(100)
