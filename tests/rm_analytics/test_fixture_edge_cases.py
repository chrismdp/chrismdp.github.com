"""Deterministic edge-case coverage using a fake RightMessage bus.

Covers visibility, occlusion, deduplication, successful submissions, and
read-only split-test assignment.
"""

from fixture_helpers import (
    emit_offer_exposure,
    emit_question_exposure,
    new_fixture_page,
    ph_events,
    settle,
    trigger_form_submitted_hook,
)
from harness import ALLOWED_PROP_KEYS


def test_tall_offer_counts_without_covering_the_whole_viewport(context):
    # A 1800px-tall offer in a 900px-tall viewport can never put 50% of its
    # own box on screen - it must still count once any of it is genuinely
    # on screen, not CSS-hidden, and not covered by something else.
    page = new_fixture_page(context, '<div class="rm-widget rm-wdg_test" style="height:1800px"><form class="rm-form">Offer</form></div>')
    emit_offer_exposure(page)
    settle(page)
    assert ph_events(page, "rm_offer_viewed"), "a tall offer that is genuinely on screen must still be counted"


def test_question_step_is_not_counted_as_the_offer(context):
    page = new_fixture_page(context, '<div class="rm-widget rm-wdg_test" style="height:200px"><div class="rm-answers">Pick one</div></div>')
    emit_question_exposure(page)
    settle(page)
    assert not ph_events(page, "rm_offer_viewed"), "a question screen must never be reported as the offer"


def test_offer_bus_event_ahead_of_dom_waits_for_the_real_offer_node(context):
    # RightMessage's bus can announce the offer a tick before the DOM
    # re-renders it. The widget should not count as showing the offer until
    # the actual form/CTA markup lands.
    page = new_fixture_page(context, '<div class="rm-widget rm-wdg_test" style="height:200px"><div class="rm-answers">Pick one</div></div>')
    emit_offer_exposure(page)
    settle(page)
    assert not ph_events(page, "rm_offer_viewed"), "must not fire while the DOM still shows the question"

    page.evaluate(
        "document.querySelector('.rm-wdg_test').innerHTML = '<form class=\"rm-form\">Offer</form>'"
    )
    settle(page)
    assert ph_events(page, "rm_offer_viewed"), "must fire once the DOM actually shows the offer"


def test_offer_form_node_itself_hidden_is_not_counted_until_it_is_shown(context):
    # The widget container can be fully on screen while the form/CTA inside
    # it is still individually hidden (e.g. behind its own fade-in, or a
    # loading placeholder swapped out later) - existence in the DOM is not
    # enough, the offer node itself must be genuinely visible.
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px">'
        '<form class="rm-form" style="visibility:hidden">Offer</form>'
        "</div>",
    )
    emit_offer_exposure(page)
    settle(page)
    assert not ph_events(page, "rm_offer_viewed"), "a hidden form must not count even though it exists in the DOM"

    page.evaluate("document.querySelector('.rm-form').style.visibility = 'visible'")
    page.evaluate("document.dispatchEvent(new Event('visibilitychange'))")  # nudge a recheck
    settle(page)
    assert ph_events(page, "rm_offer_viewed"), "must count once the form itself becomes visible"


def test_hidden_tab_then_visible_counts_without_any_scroll(context):
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>',
        extra_setup=(
            'window.__vis = "hidden";'
            'Object.defineProperty(document, "visibilityState", { get: function () { return window.__vis; }, configurable: true });'
        ),
    )
    emit_offer_exposure(page)
    settle(page)
    assert not ph_events(page, "rm_offer_viewed"), "must not fire while the tab is hidden"

    page.evaluate('window.__vis = "visible"; document.dispatchEvent(new Event("visibilitychange"));')
    settle(page)
    assert ph_events(page, "rm_offer_viewed"), "must fire once the tab is visible again, with no geometry change at all"


def test_rmpreview_query_param_suppresses_everything(context):
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>',
        url="https://fixture.rm-analytics.test/?rmpreview=1",
    )
    emit_offer_exposure(page)
    settle(page)
    assert not ph_events(page), "RightMessage preview mode must not send any live analytics"


def test_disable_analytics_query_param_suppresses_everything(context):
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>',
        url="https://fixture.rm-analytics.test/?__rm_disable_analytics=true",
    )
    emit_offer_exposure(page)
    settle(page)
    assert not ph_events(page), "__rm_disable_analytics=true must not send any live analytics"


def test_inline_offer_covered_by_a_modal_is_not_counted(context):
    # A full-screen overlay sitting on top of an inline offer should stop it
    # from counting as visible, even though it geometrically intersects the
    # viewport.
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>'
        '<div id="cover" style="position:fixed;inset:0;background:white;z-index:999"></div>',
    )
    emit_offer_exposure(page)
    settle(page)
    assert not ph_events(page, "rm_offer_viewed"), "an offer fully covered by another element must not count as viewed"

    page.evaluate('document.getElementById("cover").remove()')
    page.evaluate("document.dispatchEvent(new Event('visibilitychange'))")  # nudge a recheck
    settle(page)
    assert ph_events(page, "rm_offer_viewed"), "removing the cover must let the now-visible offer count"


def test_repeated_visibility_toggles_do_not_duplicate_events(context):
    page = new_fixture_page(context, '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>')
    emit_offer_exposure(page)
    settle(page)
    for _ in range(3):
        page.evaluate("document.dispatchEvent(new Event('visibilitychange'))")
    settle(page)
    assert len(ph_events(page, "rm_widget_viewed")) == 1
    assert len(ph_events(page, "rm_offer_viewed")) == 1


def test_experiment_fields_omitted_when_rm_has_not_assigned_yet(context):
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>',
        extra_setup="window.RightMessage = { sources: { splitTests: { data: {} } } };",
    )
    emit_offer_exposure(page)
    settle(page)
    events = ph_events(page, "rm_offer_viewed")
    assert events, "sanity: offer view should still fire"
    props = events[0]["props"]
    assert "experiment_id" not in props and "experiment_variant" not in props, (
        "an unassigned split test must never be reported, and must never be guessed as control"
    )


def test_experiment_fields_read_without_ever_calling_the_assigning_method(context):
    # sources.splitTests exposes only `.data` here - no getVariantForResource
    # or hasActiveTest method at all. If the tracker called either, this
    # would throw and the test would fail.
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>',
        extra_setup="window.RightMessage = { sources: { splitTests: { data: { offer_ofr_xi6l3r4n: 'control' } } } };",
    )
    emit_offer_exposure(page)
    settle(page)
    events = ph_events(page, "rm_offer_viewed")
    assert events
    assert events[0]["props"]["experiment_id"] == "999"
    assert events[0]["props"]["experiment_variant"] == "control"


def test_unknown_assignment_value_is_omitted_not_misreported(context):
    # The cached value does not match any of the test's current variant ids
    # (e.g. a stale localStorage entry from a since-changed test).
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>',
        extra_setup="window.RightMessage = { sources: { splitTests: { data: { offer_ofr_xi6l3r4n: 'var_stale_removed' } } } };",
    )
    emit_offer_exposure(page)
    settle(page)
    props = ph_events(page, "rm_offer_viewed")[0]["props"]
    assert "experiment_id" not in props and "experiment_variant" not in props


def test_offer_conversions_bus_event_alone_never_triggers_a_submission(context):
    # RightMessage emits this bus event with isLeadCapture: true even when
    # the lead-capture request fails (its own catch branch) - it must never
    # be read as a success signal on its own.
    page = new_fixture_page(context, '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>')
    emit_offer_exposure(page)
    page.evaluate(
        "rmbus.emit('event', {collection: 'offer_conversions', data: "
        "{widgetId: 'wdg_test', offerId: 'ofr_xi6l3r4n', offerFunnelId: 'ofn_test', isLeadCapture: true}})"
    )
    settle(page)
    assert not ph_events(page, "rm_form_submitted"), "the bus event alone must never be treated as success"


def test_successful_submission_fires_with_no_personal_data(context):
    page = new_fixture_page(context, '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>')
    emit_offer_exposure(page)  # any bus event installs the onFormSubmitted hook wrapper
    trigger_form_submitted_hook(page)
    settle(page)
    events = ph_events(page, "rm_form_submitted")
    assert events
    props = events[0]["props"]
    assert set(props.keys()) <= ALLOWED_PROP_KEYS
    assert "email" not in str(props).lower() and "@" not in str(props)
    assert props["is_newsletter"] is True


def test_existing_onFormSubmitted_hook_is_chained_not_replaced(context):
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>',
        extra_setup="window.__existingHookCalls = []; "
        "window.RightMessage = { integration: { hooks: { onFormSubmitted: function (p) { window.__existingHookCalls.push(p); } } } };",
    )
    emit_offer_exposure(page)
    trigger_form_submitted_hook(page)
    settle(page)
    assert page.evaluate("window.__existingHookCalls.length") == 1, "a pre-existing hook must still be called"
    assert ph_events(page, "rm_form_submitted"), "and our own tracking must still run"


def test_graceful_when_posthog_is_not_loaded(context):
    page = new_fixture_page(
        context,
        '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Offer</form></div>',
        extra_setup="delete window.posthog;",
    )
    emit_offer_exposure(page)
    trigger_form_submitted_hook(page)
    settle(page)
    # No exception means the page survived; there is nothing to assert on
    # __phEvents since posthog never existed.
    assert page.evaluate("document.title") is not None
