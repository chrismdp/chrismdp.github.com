"""End-to-end evidence against the real, published site: the actual
production HTML, the actual published RightMessage bundle, and the actual
live split test - with this repo's assets/js/rm-analytics.js spliced in
before the RightMessage loader, exactly where the layout change puts it.

Needs network access to https://www.chrismdp.com and https://t.rightmessage.com.
No test ever lets a real signup happen: every non-GET request is blocked
(harness.install_safety_routes), and the one lead-capture endpoint is either
aborted (failure path) or answered with a canned response (success path) -
never the real RightMessage backend.
"""

from harness import (
    ARTICLE_OFFER_ID,
    ARTICLE_URL,
    ARTICLE_WIDGET_ID,
    POPUP_FLOW_ID,
    POPUP_OFFER_ID,
    POPUP_SPLIT_TEST_PID,
    POPUP_VARIANT_ID,
    POPUP_WIDGET_ID,
    assert_allowlisted_props,
    collect_console_captures,
    load_real_site_page,
    ph_events,
)


def scroll_to(page, selector):
    page.locator(selector).scroll_into_view_if_needed()
    page.wait_for_timeout(700)


def test_inline_offer_below_the_fold_is_not_counted_until_scrolled_to(context):
    page = load_real_site_page(context, ARTICLE_URL)
    page.wait_for_timeout(800)
    assert not ph_events(page, "rm_offer_viewed", widget_id=ARTICLE_WIDGET_ID), "must not count while still below the fold"

    # Scrolling this far down also crosses the popup's own 30%-scroll
    # trigger, and the popup then covers the inline widget - dismiss it
    # (a normal thing a real visitor does) so the inline offer is not
    # obscured, and to exercise the "obscured by a modal" rule on the real
    # DOM rather than only the fixture.
    scroll_to(page, ".rm-" + ARTICLE_WIDGET_ID)
    assert not ph_events(page, "rm_offer_viewed", widget_id=ARTICLE_WIDGET_ID), "must not count while covered by the popup"
    modal = page.locator(".rm-" + POPUP_WIDGET_ID)
    if modal.is_visible():
        modal.locator(".rm-dismiss-button").click()
        page.wait_for_timeout(600)

    events = ph_events(page, "rm_offer_viewed", widget_id=ARTICLE_WIDGET_ID)
    assert events, "must count once scrolled into view and no longer covered"
    props = events[0]["props"]
    assert props["offer_id"] == ARTICLE_OFFER_ID
    assert props["is_newsletter"] is True
    assert props["widget_type"] == "inline"
    assert_allowlisted_props(events)


def test_scrolling_the_inline_offer_in_and_out_does_not_duplicate_events(context):
    page = load_real_site_page(context, ARTICLE_URL)
    page.wait_for_timeout(800)
    scroll_to(page, ".rm-" + ARTICLE_WIDGET_ID)
    modal = page.locator(".rm-" + POPUP_WIDGET_ID)
    if modal.is_visible():
        modal.locator(".rm-dismiss-button").click()
        page.wait_for_timeout(600)
    assert len(ph_events(page, "rm_offer_viewed", widget_id=ARTICLE_WIDGET_ID)) == 1

    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(400)
    scroll_to(page, ".rm-" + ARTICLE_WIDGET_ID)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(400)
    scroll_to(page, ".rm-" + ARTICLE_WIDGET_ID)

    assert len(ph_events(page, "rm_widget_viewed", widget_id=ARTICLE_WIDGET_ID)) == 1
    assert len(ph_events(page, "rm_offer_viewed", widget_id=ARTICLE_WIDGET_ID)) == 1


def test_popup_is_hidden_at_load_and_shown_after_its_real_scroll_trigger(context):
    page = load_real_site_page(context, ARTICLE_URL)
    page.wait_for_timeout(800)
    assert not ph_events(page, "rm_widget_viewed", widget_id=POPUP_WIDGET_ID)
    assert not ph_events(page, "rm_offer_viewed", widget_id=POPUP_WIDGET_ID)

    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight * 0.45)")
    page.locator(".rm-" + POPUP_WIDGET_ID).wait_for(state="visible")
    page.wait_for_timeout(800)

    widget_events = ph_events(page, "rm_widget_viewed", widget_id=POPUP_WIDGET_ID)
    offer_events = ph_events(page, "rm_offer_viewed", widget_id=POPUP_WIDGET_ID)
    assert widget_events and offer_events
    assert widget_events[0]["props"]["widget_type"] == "modal"
    assert offer_events[0]["props"]["flow_id"] == POPUP_FLOW_ID
    assert offer_events[0]["props"]["offer_id"] == POPUP_OFFER_ID
    assert_allowlisted_props(widget_events + offer_events)


def test_control_variant_is_reported_as_control(context):
    page = load_real_site_page(context, ARTICLE_URL, variant_override="control")
    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight * 0.45)")
    page.locator(".rm-" + POPUP_WIDGET_ID).wait_for(state="visible")
    page.wait_for_timeout(800)
    events = ph_events(page, "rm_offer_viewed", widget_id=POPUP_WIDGET_ID)
    assert events
    assert events[0]["props"]["experiment_id"] == POPUP_SPLIT_TEST_PID
    assert events[0]["props"]["experiment_variant"] == "control"


def test_treatment_variant_is_reported(context):
    page = load_real_site_page(context, ARTICLE_URL, variant_override=POPUP_VARIANT_ID)
    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight * 0.45)")
    page.locator(".rm-" + POPUP_WIDGET_ID).wait_for(state="visible")
    page.wait_for_timeout(800)
    events = ph_events(page, "rm_offer_viewed", widget_id=POPUP_WIDGET_ID)
    assert events
    assert events[0]["props"]["experiment_id"] == POPUP_SPLIT_TEST_PID
    assert events[0]["props"]["experiment_variant"] == POPUP_VARIANT_ID


def test_invalid_email_never_submits_and_never_fires(context):
    page = load_real_site_page(context, ARTICLE_URL, submit_mode="abort")
    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight * 0.45)")
    modal = page.locator(".rm-" + POPUP_WIDGET_ID)
    modal.wait_for(state="visible")
    page.wait_for_timeout(500)

    modal.locator("input[type=email]").fill("not-an-email")
    assert not modal.locator("input[type=email]").evaluate("(e) => e.checkValidity()")
    modal.locator("button[type=submit]").click()
    page.wait_for_timeout(800)

    assert not ph_events(page, "rm_form_submitted"), "an invalid email must never reach a submission event"
    assert page.url == ARTICLE_URL, "an invalid form must never navigate away"


def test_valid_email_but_failed_network_request_does_not_fire(context):
    # A valid, well-formed email that RightMessage's own submitForms call
    # fails to deliver (network error) must not count as a submission -
    # RightMessage's own "offer_conversions" bus event fires here too
    # (its own bug, not ours to fix), but onFormSubmitted, which this
    # tracker actually listens to, is only ever called on real success.
    page = load_real_site_page(context, ARTICLE_URL, submit_mode="failure")
    captured = collect_console_captures(page)
    submit_responses = []
    page.on("response", lambda response: submit_responses.append(response.status) if "convertkit/submitForms" in response.url else None)
    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight * 0.45)")
    modal = page.locator(".rm-" + POPUP_WIDGET_ID)
    modal.wait_for(state="visible")
    page.wait_for_timeout(500)

    modal.locator("input[type=email]").fill("chris+newsletter-analytics-failure@chrismdp.com")
    modal.locator("button[type=submit]").click()
    page.wait_for_url("**/thanks/**", timeout=10000)

    assert submit_responses == [500]
    assert not [e for e in captured if e["event"] == "rm_form_submitted"], "a failed network request must never count as a submission, including before redirect"


def test_successful_submission_fires_before_redirect_with_no_personal_data(context):
    page = load_real_site_page(context, ARTICLE_URL, submit_mode="success")
    # A real cross-document redirect destroys this page's JS state before
    # page.evaluate() could read it back, so capture via the console instead
    # - that is delivered even across the navigation, and proves the event
    # was sent during the original document's lifetime, before it redirects.
    captured = collect_console_captures(page)
    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight * 0.45)")
    modal = page.locator(".rm-" + POPUP_WIDGET_ID)
    modal.wait_for(state="visible")
    page.wait_for_timeout(500)

    modal.locator("input[type=email]").fill("chris+newsletter-analytics@chrismdp.com")
    modal.locator("button[type=submit]").click()
    page.wait_for_url("**/thanks/**", timeout=5000)

    events = [e for e in captured if e["event"] == "rm_form_submitted"]
    assert events, "the success event must be captured before the redirect navigates away"

    props = events[0]["props"]
    assert props["offer_id"] == POPUP_OFFER_ID
    assert props["is_newsletter"] is True
    assert_allowlisted_props(events)
    assert "newsletter-analytics" not in str(props) and "@" not in str(props)


def test_cta_only_click_is_never_treated_as_a_submission(context):
    # The popup's own dismiss (not a CTA offer) must never be mistaken for a
    # lead capture; only a real isLeadCapture:true conversion counts.
    page = load_real_site_page(context, ARTICLE_URL)
    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight * 0.45)")
    modal = page.locator(".rm-" + POPUP_WIDGET_ID)
    modal.wait_for(state="visible")
    page.wait_for_timeout(500)
    modal.locator(".rm-dismiss-button").click()
    page.wait_for_timeout(500)
    assert not ph_events(page, "rm_form_submitted")
