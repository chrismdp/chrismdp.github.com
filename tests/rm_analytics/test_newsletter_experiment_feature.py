"""Deterministic coverage for the newsletter popup headline experiment
bridge: `rm_newsletter_experiment_assigned` and the explicit
`$feature/newsletter-popup-headline` property on the matching
`rm_offer_viewed` / `rm_form_submitted` events. Only the one native
RightMessage split test named in tests/rm_analytics/README.md (widget
wdg_trpf409s, offer ofr_VqL5OY0S, pid 1563064411) is ever attributed.
"""

import json

from fixture_helpers import (
    emit_offer_exposure,
    new_fixture_page,
    ph_events,
    settle,
    trigger_form_submitted_hook,
)
from harness import (
    ALLOWED_PROP_KEYS,
    POPUP_FLOW_ID,
    POPUP_OFFER_ID,
    POPUP_SPLIT_TEST_PID,
    POPUP_VARIANT_ID,
    POPUP_WIDGET_ID,
)

FEATURE_KEY = "$feature/newsletter-popup-headline"

POPUP_BODY = (
    '<div class="rm-widget rm-' + POPUP_WIDGET_ID + '" style="height:200px">'
    '<form class="rm-form">Offer</form></div>'
)

POPUP_BODY_HIDDEN = (
    '<div class="rm-widget rm-' + POPUP_WIDGET_ID + '" style="display:none">'
    '<form class="rm-form">Offer</form></div>'
)


def popup_config(widget_id=POPUP_WIDGET_ID, offer_id=POPUP_OFFER_ID, pid=POPUP_SPLIT_TEST_PID, variant_id=POPUP_VARIANT_ID):
    return {
        "rightCta": {"widgets": [{"id": widget_id, "type": "modal", "contentId": POPUP_FLOW_ID}]},
        "splitTests": [
            {
                "resource_type": "offer",
                "resource_id": offer_id,
                "pid": pid,
                "variants": [{"id": variant_id}],
            }
        ],
    }


def popup_setup(assigned_value, widget_id=POPUP_WIDGET_ID, offer_id=POPUP_OFFER_ID, pid=POPUP_SPLIT_TEST_PID, variant_id=POPUP_VARIANT_ID):
    """extra_setup that gives the fixture RightMessage instance a real
    assignment cache (sources.splitTests.data) plus the config the tracker
    needs to recognise the split test, while keeping integration.hooks so
    onFormSubmitted can still be installed."""
    data_key = "offer_" + offer_id
    return (
        "window.RightMessage = { integration: { hooks: {} }, sources: { splitTests: { data: "
        + json.dumps({data_key: assigned_value})
        + " } } };\n"
        "window.rmConfig = " + json.dumps(popup_config(widget_id, offer_id, pid, variant_id)) + ";"
    )


def emit_popup_offer_exposure(page, widget_id=POPUP_WIDGET_ID, offer_id=POPUP_OFFER_ID):
    emit_offer_exposure(page, widget_id=widget_id, offer_id=offer_id, flow_id=POPUP_FLOW_ID)


def test_known_control_variant_gets_assignment_event_before_visible(context):
    page = new_fixture_page(context, POPUP_BODY_HIDDEN, extra_setup=popup_setup("control"))
    emit_popup_offer_exposure(page)
    settle(page)
    assigned = ph_events(page, "rm_newsletter_experiment_assigned")
    assert len(assigned) == 1
    props = assigned[0]["props"]
    assert props["experiment_id"] == POPUP_SPLIT_TEST_PID
    assert props["experiment_variant"] == "control"
    assert props[FEATURE_KEY] == "control"
    assert props["offer_id"] == POPUP_OFFER_ID
    assert props["widget_id"] == POPUP_WIDGET_ID
    assert not ph_events(page, "rm_offer_viewed"), "the widget is not on screen - only assignment fires"


def test_known_named_variant_gets_assignment_event_before_visible(context):
    page = new_fixture_page(context, POPUP_BODY_HIDDEN, extra_setup=popup_setup(POPUP_VARIANT_ID))
    emit_popup_offer_exposure(page)
    settle(page)
    assigned = ph_events(page, "rm_newsletter_experiment_assigned")
    assert len(assigned) == 1
    props = assigned[0]["props"]
    assert props["experiment_variant"] == POPUP_VARIANT_ID
    assert props[FEATURE_KEY] == POPUP_VARIANT_ID


def test_view_and_form_submitted_carry_the_same_feature_property(context):
    page = new_fixture_page(context, POPUP_BODY, extra_setup=popup_setup("control"))
    emit_popup_offer_exposure(page)
    settle(page)

    view_events = ph_events(page, "rm_offer_viewed")
    assert len(view_events) == 1
    assert view_events[0]["props"][FEATURE_KEY] == "control"

    trigger_form_submitted_hook(page, widget_id=POPUP_WIDGET_ID, offer_id=POPUP_OFFER_ID, flow_id=POPUP_FLOW_ID)
    settle(page)
    submit_events = ph_events(page, "rm_form_submitted")
    assert len(submit_events) == 1
    assert submit_events[0]["props"][FEATURE_KEY] == "control"
    assert set(submit_events[0]["props"].keys()) <= ALLOWED_PROP_KEYS


def test_repeated_bus_events_do_not_duplicate_the_assignment_event(context):
    page = new_fixture_page(context, POPUP_BODY_HIDDEN, extra_setup=popup_setup("control"))
    emit_popup_offer_exposure(page)
    emit_popup_offer_exposure(page)
    emit_popup_offer_exposure(page)
    settle(page)
    assert len(ph_events(page, "rm_newsletter_experiment_assigned")) == 1


def test_unknown_stale_variant_never_attributed(context):
    page = new_fixture_page(context, POPUP_BODY, extra_setup=popup_setup("var_stale_removed"))
    emit_popup_offer_exposure(page)
    settle(page)
    assert not ph_events(page, "rm_newsletter_experiment_assigned")
    view_events = ph_events(page, "rm_offer_viewed")
    assert view_events, "sanity: the offer view itself must still fire"
    assert FEATURE_KEY not in view_events[0]["props"]
    assert "experiment_variant" not in view_events[0]["props"]


def test_other_widget_with_the_same_offer_never_attributed(context):
    other_widget_id = "wdg_other"
    body = '<div class="rm-widget rm-' + other_widget_id + '" style="height:200px"><form class="rm-form">Offer</form></div>'
    page = new_fixture_page(context, body, extra_setup=popup_setup("control", widget_id=other_widget_id))
    emit_popup_offer_exposure(page, widget_id=other_widget_id)
    settle(page)
    assert not ph_events(page, "rm_newsletter_experiment_assigned")
    view_events = ph_events(page, "rm_offer_viewed")
    assert view_events, "sanity: the offer view itself must still fire"
    assert FEATURE_KEY not in view_events[0]["props"]


def test_other_offer_on_the_matching_widget_never_attributed(context):
    other_offer_id = "ofr_xi6l3r4n"
    page = new_fixture_page(context, POPUP_BODY, extra_setup=popup_setup("control", offer_id=other_offer_id))
    emit_popup_offer_exposure(page, offer_id=other_offer_id)
    settle(page)
    assert not ph_events(page, "rm_newsletter_experiment_assigned")
    view_events = ph_events(page, "rm_offer_viewed")
    assert view_events, "sanity: the offer view itself must still fire"
    assert FEATURE_KEY not in view_events[0]["props"]


def test_suppression_blocks_the_assignment_event_too(context):
    page = new_fixture_page(
        context,
        POPUP_BODY_HIDDEN,
        extra_setup=popup_setup("control") + "\nwindow.__phOptedOut = true;",
    )
    emit_popup_offer_exposure(page)
    settle(page)
    assert not ph_events(page, "rm_newsletter_experiment_assigned")


def test_assignment_retries_on_a_later_recheck_if_capture_was_first_unavailable(context):
    # posthog is unavailable at the moment the bus event arrives - capture()
    # returns false, so the page must not be marked as sent, and a later
    # recheck (not a visibility change of the widget itself) must retry it
    # rather than losing the assignment for the rest of the page's life.
    page = new_fixture_page(context, POPUP_BODY_HIDDEN, extra_setup=popup_setup("control") + "\ndelete window.posthog;")
    emit_popup_offer_exposure(page)
    settle(page)
    assert not ph_events(page, "rm_newsletter_experiment_assigned")

    page.evaluate(
        "window.posthog = { capture: function (event, props) { window.__phEvents.push({ event: event, props: props }); },"
        " has_opted_out_capturing: function () { return false; } };"
    )
    page.evaluate("document.dispatchEvent(new Event('visibilitychange'))")
    settle(page)
    events = ph_events(page, "rm_newsletter_experiment_assigned")
    assert len(events) == 1
    assert events[0]["props"]["experiment_variant"] == "control"
