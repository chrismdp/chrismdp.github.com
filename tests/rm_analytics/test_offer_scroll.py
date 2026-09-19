from fixture_helpers import new_fixture_page, emit_offer_exposure, ph_events, settle


def test_form_enters_view_after_its_widget_header(context):
    page = new_fixture_page(context, '<div class="rm-widget rm-wdg_test" style="height:2400px"><h2>Newsletter</h2><div style="height:1300px"></div><form class="rm-form" style="height:300px;background:gray">Signup</form></div>')
    emit_offer_exposure(page)
    settle(page)
    assert ph_events(page, 'rm_widget_viewed')
    assert not ph_events(page, 'rm_offer_viewed')
    page.evaluate('scrollTo(0,1000)')
    page.wait_for_timeout(200)
    assert len(ph_events(page, 'rm_offer_viewed')) == 1
