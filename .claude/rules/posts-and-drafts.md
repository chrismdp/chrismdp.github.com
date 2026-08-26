---
paths:
  - "_posts/**"
  - "_drafts/**"
  - "case-studies/**"
---

# Writing posts

Load `/blog` for the full workflow and `/writing-style` for voice. This file holds the mechanics that are specific to this repo.

## Front matter

Post files are named `YYYY-MM-DD-title.md`.

```markdown
---
layout: post
title: "YOUR TITLE HERE"
date: YYYY-MM-DD HH:MM:SS +0000
categories:
- ai
- engineering
- rag
---

TOP PARAGRAPH OR TWO TO HOOK THE READER

<!--more-->

EVERYTHING ELSE
```

## Writing process

- Start with a strong hook and a clear statement of the main argument.
- Put the `<!--more-->` break after the introduction.
- End with concrete takeaways or next steps.
- Aim for 1500+ words on long-form pieces.
- Link to related posts in `_posts/`.
- Use British English spelling.
- Use markdown footnotes for asides, extra detail, and references.
- No vertical bar (`|`) in link titles.
- No numbered or unnumbered lists. Prefer short paragraphs with headings.
- Use H2 (`##`) and below. Never use H1 (`#`).
- No blank line before a footnote reference.
- Research-heavy posts lead with data or statistics that challenge an assumption, and use footnotes for detailed sourcing and added context.
- Keep the main text generic and high level. Move specific detail such as costs, percentages, and technical specifics into footnotes. If a fact appears in both, cut it from the text.

## Links

- **Internal links use the slug only**: `/coding-with-ai/`, never `/2025/03/07/coding-with-ai/`. This matches the `/:title/` permalink in `_config.yml`.
- **Only internal links go inline.** Every external link goes in a footnote with `{:target="_blank"}` so it opens in a new tab.
- Avoid "check out this post" phrasing. Integrate internal links into the sentence instead.
- Footnotes carry more than citations. Use them for actionable advice and deeper insight that adds to the main narrative.
- **Footnote spacing**: no space between punctuation and the footnote, so `methodology.[^1]` and not `methodology. [^1]`. Always put a space between consecutive footnote references, so `[^1] [^2]` and not `[^1][^2]`.

## Crediting people

- **Feedback on a draft**: "Thanks to [Name] for feedback on an earlier version of this post." Do not say what the feedback was about.
- **Contributed insight** from comments, conversations, or feedback: add an unformatted thanks line at the very end of the article, after the footnotes. Format: `Thanks to Name and Name for conversations that shaped this post.` No italics, and no LinkedIn links unless Chris asks for them. Never attribute a specific point inline. Work the insight into the prose and thank everyone collectively at the end.

## Images

- **The main image is the motif.** When you create an infographic, extract its central visual motif and set it as `image:` in the front matter. That is the hero image at the top of the post.
- **Infographics render from front matter.** Add `infographic: /assets/img/filename.jpg`. The layout renders the full infographic at 50% width at the end of the content.
- **Portrait heroes need a flag.** Comics are usually portrait. Add `image_portrait: true` so the layout handles them.
- **Resize infographics for the blog** to about 512px on the longest side. Full resolution goes to the Newsletter Vault only.
- **Webinar adverts and extracted motifs stay high resolution.** Do not resize them. Copy them at full resolution.
- **Resize with `magick` on this machine.** `sips` is macOS only and is not available here. Give one dimension only so the aspect ratio is preserved. `/blog` and its `references/assets.md` are written for macOS and use `sips` — substitute `magick`.
- Always save images as JPG, never PNG, for a smaller file.
- Screenshots and diagrams in the body use full width or whatever size suits them.
- When Chris supplies an image, check whether the file needs copying into `/assets/img/`.

## Chris's style

`.claude/references/chris-writing-patterns.md` records how Chris structures and phrases a post — title habits, narrative shape, paragraph rhythm, and recurring moves. Read it when polishing a draft.
