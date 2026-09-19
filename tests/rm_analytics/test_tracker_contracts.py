import pytest

from fixture_helpers import new_fixture_page, emit_offer_exposure, ph_events, settle


@pytest.mark.parametrize('setup', [
    'window.RightMessage.sources = {metrics: {isAnalyticsEnabled: function() { return false; }}};',
    'window.RightMessage.previewing = true;',
    'window.__phOptedOut = true;',
])
def test_runtime_analytics_gates_suppress_views(context, setup):
    page = new_fixture_page(context, '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Signup</form></div>', extra_setup=setup)
    emit_offer_exposure(page)
    settle(page)
    assert not ph_events(page)


def test_existing_success_hook_retains_context_arguments_and_return(context):
    page = new_fixture_page(context, '<div class="rm-widget rm-wdg_test" style="height:200px"><form class="rm-form">Signup</form></div>', extra_setup='RightMessage.integration.hooks.onFormSubmitted = function(payload, extra) { return this.marker + extra; };')
    emit_offer_exposure(page)
    result = page.evaluate("RightMessage.integration.hooks.onFormSubmitted.call({marker: 40}, {widgetId:'wdg_test', offerId:'ofr_xi6l3r4n', flowId:'ofn_test'}, 2)")
    assert result == 42
    assert len(ph_events(page, 'rm_form_submitted')) == 1
