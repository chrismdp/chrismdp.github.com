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
- `_layouts/page.html` - Simple page template with title and content
- `_includes/ai-newsletter-short.html` - Newsletter signup component
- Custom Tailwind config with brand colors: `brand-white`, `brand-turquoise`, `brand-deep-turquoise`, `brand-light-blue`, `brand-black`, `brand-orange`

### Content Architecture
- **Posts** (`_posts/`) - Blog articles with date-based naming: `YYYY-MM-DD-title.md`
- **Newsletters** (`_newsletters/`) - Newsletter content collection
- **Pages** (`pages/`) - Static pages like services, archive, search
  - Articles page uses markdown formatting - avoid HTML, let page layout handle styling
- **Research** (`_research/`) - Internal research documents
- **Case Studies** (`case-studies/`) - Use `post` layout for proper formatting like blog articles

### Writing Style System
The project uses Cursor rules (`.cursor/rules/`) that define strict content guidelines:

#### Writing Style Rules (from `style.mdc`)
**Voice and Tone:**
- Write in a direct, conversational style
- Use first person when sharing personal experiences
- Be confident but not arrogant
- Challenge conventional wisdom
- Keep a casual, approachable tone while maintaining expertise

**Structure:**
- Start with a clear, bold statement of the main argument
- Follow with a brief explanation of why this matters

**Content:**
- Draw from personal experience and lessons learned
- Acknowledge counterarguments but be bold with opinions
- Focus on practical, actionable insights
- Call out mistakes and what was learned from them

**Format:**
- Use bold text sparingly for emphasis
- Break up long paragraphs
- Use code blocks or quotes when relevant
- Remove all dashes, endashes, emdashes and hyphens
- Keep sections focused and concise

**Language:**
- Prefer active voice
- NEVER use contractions
- Avoid jargon unless necessary
- Define technical terms when used
- Keep sentences crisp and direct

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

### Reusable Components
The project uses Jekyll includes for commonly repeated elements:

- `_includes/five-star.html` - Consistent 5-star rating display using brand orange SVG stars
  - Usage: `{% include five-star.html %}` 
  - Always use this instead of emoji stars or inline SVG for testimonials and reviews
  - Maintains consistent styling and color (`brand-orange: #fc8745`) across the site
- `_includes/testimonial-tfc.html` - Tom Foster Carter testimonial component (currently commented out)

### Icons
- **Use Lucide icons** (lucide.dev) for all icons throughout the site
- Never use emojis for UI elements, navigation, or decoration
- Lucide icons should be inline SVG with appropriate sizing and brand colors
- Standard icon size: 24x24 for inline, 32x32 for section headers, 40x40 for feature cards
- Apply `text-brand-deep-turquoise` class for colored icons

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