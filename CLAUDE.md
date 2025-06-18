# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Local Development
```bash
# Install dependencies
bundle install

# Serve locally with live reload (use this for development)
bundle exec jekyll serve

# Build site for production
bundle exec jekyll build

# Build with Docker (alternative)
docker-compose up -d
```

### Container Development
The project includes `docker-compose.yaml` for containerized development using Jekyll 3.8. Remove the bundle volume mount for production deployments.

## Architecture Overview

### Jekyll Site Structure
This is a GitHub Pages-compatible Jekyll blog using a Tailwind CSS theme. The site architecture follows Jekyll conventions with some key customizations:

- **GitHub Pages deployment** - Uses `github-pages` gem for compatibility
- **Tailwind CSS via CDN** - Configured in `_layouts/default.html` with custom brand colors
- **Custom post layout** - Enhanced with newsletter signup, share buttons, and related articles
- **Content collections** - Standard Jekyll posts plus newsletter collection

### Key Layout Components
- `_layouts/default.html` - Base template with Tailwind config and custom brand colors
- `_layouts/post.html` - Post template with newsletter integration and social sharing
- `_includes/ai-newsletter-short.html` - Newsletter signup component
- Custom Tailwind config with brand colors: `brand-white`, `brand-turquoise`, `brand-deep-turquoise`, `brand-light-blue`, `brand-black`

### Content Architecture
- **Posts** (`_posts/`) - Blog articles with date-based naming: `YYYY-MM-DD-title.md`
- **Newsletters** (`_newsletters/`) - Newsletter content collection
- **Pages** (`pages/`) - Static pages like services, archive, search
- **Research** (`_research/`) - Internal research documents

### Writing Style System
The project uses Cursor rules (`.cursor/rules/`) that define strict content guidelines:

#### Blog Post Template (from `blog-posts.mdc`)
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

ADD TOP PARAGRAPH OR TWO HERE TO HOOK IN READER

<!--more-->

EVERYTHING ELSE HERE
```

#### Writing Style Rules (from `style.mdc`)
- Direct, conversational style with first person for personal experiences
- No contractions, active voice preferred
- Bold text sparingly, no dashes/hyphens
- Clear section headings (H2 and below only)
- Start with bold statement, follow with brief explanation

#### Content Guidelines
- Use 1-3-1 sentence pattern (1-2 summary, 3 explanatory, 1-2 transition)
- Include `<!--more-->` break after introduction
- Link to related posts in `_posts/` folder
- Use British English spelling
- Markdown footnotes for citations and references
- No numbered/unnumbered lists - prefer short paragraphs with headings

### Newsletter System
Newsletter content follows specific format with intimate, enthusiastic tone focused on AI journey and practical tips for building with AI.

## Configuration
- Site config in `_config.yml` - includes social media links, author info, and Jekyll settings
- Uses `jekyll-sitemap` and `jekyll-redirect-from` plugins
- Permalink structure: `/:title/`
- Custom excerpt separator: `<!--more-->`

## Language and Spelling
- **Always use British English spelling** throughout the site
- Common differences to watch for:
  - "ise/isation" not "ize/ization" (realise, organisation, optimisation)
  - "our" not "or" (colour, behaviour, flavour)
  - "re" not "er" (centre, theatre)
  - "ence" not "ense" (defence, licence as noun)
  - Single "l" in words like "modelling", "travelling"
- Apply British spelling to all content: pages, posts, UI text, and code comments