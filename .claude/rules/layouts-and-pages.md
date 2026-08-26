---
paths:
  - "_layouts/**"
  - "_includes/**"
  - "pages/**"
  - "assets/**"
  - "case-studies/**"
---

# Layouts, includes, and pages

## Always verify layout with a screenshot

When you change anything visual — a new page, a layout, CSS, an include — **do not rely on the built HTML alone. Capture a screenshot, look at it, then iterate.** The live server already serves http://localhost:4000, and headless Chrome is available:

```bash
google-chrome-stable --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size=900,2400 --screenshot=/tmp/check.png "http://localhost:4000/<path>/"
```

Then `Read` the PNG. Grepping the HTML catches missing content and **misses rendered bugs**. Turquoise button text on a turquoise background reads as "present" in the HTML and is invisible on screen.

One page taught this lesson. The `.content-styled` wrapper has specificity `0,1,1` and silently overrode Tailwind utilities (`text-white`, `no-underline`, image `margin` and `height`). The result was an empty-looking CTA and a misplaced avatar that only a screenshot revealed. Fix an override like that with an inline `style="..."` attribute, following the `_includes/testimonial.html` pattern, or with a higher-specificity selector.

## Layouts

- `_layouts/default.html` — base template holding the Tailwind config and the brand colours.
  - **Overlay header exclusion list**: a page with its own `{% include header.html style="overlay" %}` has a transparent hero nav. Add it to the exclusion list in `default.html` (around line 45) so a duplicate default white header does not render. The list currently excludes `/`, `/training/`, `/services/`, `/ai-leader-accelerator/`, and `/ai-leader-accelerator/thanks/`. Add any new page with an overlay hero.
- `_layouts/post.html` — post template with newsletter signup, social sharing, and webinar links.
  - Webinar posts get a "Previous Webinars" section after the infographic.
  - A webinar write-up has no `kit_tag`, so it also gets the "Join Future Webinars" CTA and the newsletter signup.
  - A webinar landing page has a `kit_tag`, so it skips both. Its signup form lives in the content.
- `_layouts/page.html` — a simple page template with a title and content.

## Includes

- **Extract a shared section as soon as it repeats.** When the same HTML block goes on a second page, pull it into an `_includes/` partial straight away. Do not duplicate HTML across pages and wait for Chris to notice.
- `_includes/ai-newsletter-short.html` — newsletter signup component.
- `_includes/about-chris.html` — the "More About Chris" bio, shared by the homepage and `/services`.
- `_includes/five-star.html` — the 5-star rating display, built from brand-orange SVG stars. Use `{% include five-star.html %}` for every testimonial and review rating. Never use emoji stars and never inline your own SVG. It keeps the styling and the colour (`brand-orange: #fc8745`) consistent across the site.

## Brand colours

The custom Tailwind config defines `brand-white`, `brand-turquoise`, `brand-deep-turquoise`, `brand-light-blue`, `brand-black`, and `brand-orange`.

## Icons

- Use **Lucide** icons (lucide.dev) for every icon on the site.
- Never use an emoji for a UI element, navigation, or decoration.
- Lucide icons go in as inline SVG with the right size and a brand colour.
- Standard sizes: 24x24 inline, 32x32 for section headers, 40x40 for feature cards.
- Apply `text-brand-deep-turquoise` for a coloured icon.

## Pages

Pages live in `pages/`. The Articles page uses markdown formatting. Avoid HTML there and let the page layout handle the styling.
