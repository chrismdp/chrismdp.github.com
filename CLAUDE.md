# CLAUDE.md

chrismdp.github.com is the Jekyll site behind https://www.chrismdp.com. It builds on GitHub Pages through the `github-pages` gem, with Tailwind CSS loaded from a CDN. Permalinks are `/:title/` and carry no date. The excerpt separator is `<!--more-->`. Plugins are `jekyll-sitemap` and `jekyll-redirect-from`.

## Safety rails

- **This repo is public.** Everything committed here is published. Never commit anything Chris has not agreed to make public.
- **Never rename a post file.** To update an existing post, change `date:` in the front matter and leave the filename alone. The filename holds the original publication date. Renaming it breaks the URL and every link that points at it.
- **Never invent claims about Chris's experience.** Numbers such as "implementing AI at 20+ companies" must come from existing published content or from Chris himself.
- **Always verify a source before citing it.** Find the real article or paper. Never cite a statistic you have not traced to its origin.
- **Never name a client in public content.** Anonymise every reference, such as "inbound sales lead" or "training enquiry". Only name a client who has a published case study.

## Publishing schedule

`future: false` in `_config.yml` keeps future-dated posts out of the build. The `.github/workflows/daily-publish.yml` action triggers a Pages rebuild at 09:00 UTC each day. Give every post a date of `07:00:00 +0000` so it is live when that rebuild runs.

## Commands

```bash
bundle install
bundle exec jekyll serve --future   # local preview; --future shows scheduled posts
bundle exec jekyll build
docker-compose up -d                # containerised alternative, Jekyll 3.8
```

**Chris runs the Jekyll server and build himself.** A live server is already serving http://localhost:4000. Do not start `jekyll serve` and do not run `jekyll build`. For a production deployment from the container, remove the bundle volume mount.

## British English

Use British English everywhere — posts, pages, UI text, and code comments. Watch for "ise" and "isation" not "ize" and "ization" (realise, organisation, optimisation), "our" not "or" (colour, behaviour, flavour), "re" not "er" (centre, theatre), "ence" not "ense" (defence, licence as a noun), and a single "l" in words such as modelling and travelling.

## Where the rest of the guidance lives

Global skills own most of this work. Load them rather than working from memory:

- `/blog` — the whole post workflow: titles, retrieval of Chris's own material, polish, comics, infographics, slop check, LinkedIn promotion. Chris writes the first draft, and the skill takes over after that.
- `/case-studies` — everything about pages in `case-studies/`.
- `/writing-style` and `/slop-check` — voice, titles, and AI slop patterns.
- `/seo` — discoverability and AI citation.
- `/images` — infographics, comics, motif extraction, provenance records.
- `/content`, `/linkedin`, `/newsletter` — post tracking, LinkedIn, and the newsletter.
- `/gws` — every `gog` and `gws` command, including Drive uploads.

Repo rules in `.claude/rules/` load when you open a file they match. Background material sits in `.claude/references/`:
`chris-writing-patterns.md` for post shape and phrasing, `newsletter-and-social.md` for the older newsletter and LinkedIn notes, and `working-practice.md` for general working notes and the VPS clipboard workaround.
