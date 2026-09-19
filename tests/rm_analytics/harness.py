"""Shared helpers for the rm-analytics browser tests.

Two kinds of test live alongside this file:

- fixture tests (test_fixture_*.py) build a tiny local HTML page with a fake
  RightMessage bus, so the exact edge case (a tall offer, a stale question
  node, a hidden tab, an unassigned split test) is fully under the test's
  control and runs fast, with no network access.
- real site tests (test_real_site_*.py) fetch the actual production page and
  the actual published RightMessage bundle, and splice in this repo's copy
  of assets/js/rm-analytics.js before the RightMessage loader script - the
  same shape of change the layout makes. They need network access to
  https://www.chrismdp.com and https://t.rightmessage.com, and they never
  let a real form submission reach RightMessage's backend (see
  install_safety_routes below).
"""

import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = REPO_ROOT / "assets" / "js" / "rm-analytics.js"

ARTICLE_URL = "https://www.chrismdp.com/the-harness-is-the-bottleneck/"

POPUP_WIDGET_ID = "wdg_trpf409s"
POPUP_OFFER_ID = "ofr_VqL5OY0S"
POPUP_FLOW_ID = "ofn_0734qg3l"
POPUP_SPLIT_TEST_PID = "1563064411"
POPUP_VARIANT_ID = "var_newsletter_benefit_202609"

ARTICLE_WIDGET_ID = "wdg_1rpmdd1j"
ARTICLE_OFFER_ID = "ofr_xi6l3r4n"

ALLOWED_PROP_KEYS = {
    "widget_id",
    "widget_type",
    "flow_id",
    "offer_id",
    "is_newsletter",
    "experiment_id",
    "experiment_variant",
    "page_path",
}

# RightMessage's own integration code calls other posthog methods too (e.g.
# identify) when syncing a captured lead - stub the same method surface the
# real posthog-js snippet queues, from _includes/head.html, so those calls
# no-op instead of throwing and aborting the submission before our event
# handler runs.
_POSTHOG_STUB_METHODS = (
    "init register register_once register_for_session unregister opt_out_capturing "
    "opt_in_capturing reset isFeatureEnabled getFeatureFlag getFeatureFlagPayload "
    "reloadFeatureFlags group identify setPersonProperties setPersonPropertiesForFlags "
    "resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags "
    "resetGroups onFeatureFlags addFeatureFlagsHandler onSessionId getSurveys "
    "getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep"
).split()

FAKE_POSTHOG_SNIPPET = (
    """
<script>
  window.__phEvents = [];
  window.__phOptedOut = false;
  window.posthog = {
    capture: function (event, props) {
      window.__phEvents.push({ event: event, props: props });
      // Also logged to the console: a real cross-document redirect destroys
      // this page's JS state before a Playwright page.evaluate() can read
      // it back, but console messages are still delivered - this is how
      // tests prove the capture happened before the redirect, not merely
      // before the test noticed.
      console.log('__PH_CAPTURE__' + JSON.stringify({ event: event, props: props }));
    },
    has_opted_out_capturing: function () { return window.__phOptedOut === true; },
    """
    + ",\n    ".join(f"{name}: function () {{}}" for name in _POSTHOG_STUB_METHODS)
    + """
  };
</script>
"""
)

# Matches the inline PostHog loader snippet in _includes/head.html, so it can
# be replaced with the mock above. Real network calls to PostHog would
# otherwise queue silently inside the stub and never be observable to a test.
POSTHOG_SNIPPET_RE = re.compile(r"<script>\s*!function\(t,e\)\{var o,n,p,r.*?</script>", re.S)


def rm_analytics_source():
    return SCRIPT_PATH.read_text()


def fetch_html(url):
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (rm-analytics tests)"})
    with urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8")


def build_spliced_html(url):
    """Fetch the real production page and inject this repo's analytics
    script before the RightMessage loader, and a mock posthog in place of
    the real one."""
    html = fetch_html(url)
    # Replace the deployed tracker too, so this suite still tests one copy
    # of the local implementation after the first deployment.
    html = re.sub(r'<script\s+src="[^"]*/assets/js/rm-analytics\.js"\s*></script>', '', html)
    assert POSTHOG_SNIPPET_RE.search(html), "posthog init snippet not found - has head.html changed?"
    html = POSTHOG_SNIPPET_RE.sub(FAKE_POSTHOG_SNIPPET, html, count=1)
    marker = "<!-- RightMessage -->"
    assert marker in html, "RightMessage loader marker not found - has default.html changed?"
    inject = "<script>\n" + rm_analytics_source() + "\n</script>\n"
    html = html.replace(marker, inject + marker, 1)
    return html


def install_safety_routes(page, submit_mode="abort"):
    """Blocks every non-GET request so no test can ever cause a real signup
    or send real telemetry. submit_mode controls what the lead-capture
    endpoint sees: 'abort' simulates a network failure, 'success' fulfils it
    with a canned response so the code's happy path runs for real."""

    def handler(route):
        req = route.request
        if req.method != "GET":
            if "convertkit/submitForms" in req.url and submit_mode == "success":
                route.fulfill(status=200, content_type="application/json", body="{}")
            elif "convertkit/submitForms" in req.url and submit_mode == "failure":
                route.fulfill(status=500, content_type="application/json", body='{"error":"QA simulated failure"}')
            else:
                route.abort()
            return
        route.continue_()

    page.route("**/*", handler)


def install_document_route(page, base_url, html):
    """Serves our spliced HTML for the page's own document request, and lets
    every other GET (RightMessage's script, images, fonts) go to the real
    network."""

    def handler(route):
        req = route.request
        if req.resource_type == "document" and req.url.split("?")[0] == base_url:
            route.fulfill(status=200, content_type="text/html; charset=utf-8", body=html)
            return
        route.fallback()

    page.route("**/*", handler)


def load_real_site_page(context, url, submit_mode="abort", variant_override=None):
    base_url = url.split("?")[0]
    html = build_spliced_html(base_url)
    page = context.new_page()
    if variant_override is not None:
        override = json.dumps({"offer": {POPUP_OFFER_ID: variant_override}})
        page.add_init_script(
            "window.RightMessage = window.RightMessage || {}; "
            "window.RightMessage.previewSplitTestOverrides = " + override + ";"
        )
    install_safety_routes(page, submit_mode)
    install_document_route(page, base_url, html)
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_function("window.RightMessage && window.RightMessage.sources && window.RightMessage.sources.splitTests")
    return page


def ph_events(page, name=None, widget_id=None):
    events = page.evaluate("window.__phEvents || []")
    if name:
        events = [e for e in events if e["event"] == name]
    if widget_id:
        events = [e for e in events if e["props"].get("widget_id") == widget_id]
    return events


def collect_console_captures(page):
    """Returns a plain Python list that fills up with every posthog.capture()
    call logged to the console, surviving a real navigation that would
    otherwise destroy the page's JS state before page.evaluate() could read
    it back. Attach before triggering the action under test."""
    captured = []

    def on_console(msg):
        if msg.text.startswith("__PH_CAPTURE__"):
            captured.append(json.loads(msg.text[len("__PH_CAPTURE__") :]))

    page.on("console", on_console)
    return captured


def assert_allowlisted_props(events):
    for e in events:
        extra = set(e["props"].keys()) - ALLOWED_PROP_KEYS
        assert not extra, f"event {e['event']} has non-allowlisted properties: {extra}"
        blob = json.dumps(e["props"]).lower()
        assert "@" not in blob, f"event {e['event']} properties look like they contain an email: {e['props']}"
