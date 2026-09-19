Run with Python, pytest and Playwright Chromium installed:

```sh
python3 -m pytest tests/rm_analytics -q
```

Fixture tests run locally. `test_real_site_smoke.py` fetches the published
article and RightMessage script and injects the local tracker. It replaces
PostHog with a recorder and blocks all outbound non-GET requests. Signup
requests receive mocked success or failure responses; no subscriber is added.
These smoke tests depend on the current published widget and experiment IDs.

The tracker emits `rm_widget_viewed`, `rm_offer_viewed`, `rm_form_submitted`,
and `rm_newsletter_experiment_assigned`. Views require visible content in a
visible tab and count once per widget/offer per page. Successful submissions
come from RightMessage's `integration.hooks.onFormSubmitted`; its
`offer_conversions` bus event also fires after failed requests and must not
be used as a success signal.

`rm_newsletter_experiment_assigned` fires once per page, the moment
RightMessage's bus reports the visitor's native assignment for the
newsletter popup headline split test (widget `wdg_trpf409s`, offer
`ofr_VqL5OY0S`, experiment pid `1563064411`) - before the popup is on
screen, not on visibility. For that exact widget+offer only, `rm_offer_viewed`,
`rm_form_submitted`, and `rm_newsletter_experiment_assigned` also carry an
explicit `$feature/newsletter-popup-headline` property set to RightMessage's
own variant id (`control` or `var_newsletter_benefit_202609`), so PostHog
uses RightMessage's real assignment instead of evaluating its own flag. This
only fires once the variant is one of those two known ids - an unassigned or
stale/unknown value is left off every event, never guessed as control, and
no other offer or experiment ever gets the property.

Keep RightMessage's native PostHog integration disabled to avoid a second
producer of `rm_form_submitted`. New RightMessage placements are discovered
automatically. When cloning a newsletter offer, add its offer ID to
`NEWSLETTER_OFFER_IDS` so the newsletter-only placement chart includes it.
