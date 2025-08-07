# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Memories and Insights

### Key Learnings
- Always read the entire context of a project before starting work
- Carefully follow existing file structure and guidelines when making modifications
- Prioritize preserving existing content when updating files
- Be precise and methodical in interpreting instructions
- Ask clarifying questions if any part of the instruction is ambiguous
- Use tool invocations as the primary method of interaction
- Maintain a consistent and professional tone in all interactions

### Content Creation Insights
- When writing blog posts from transcripts, focus on extracting key insights rather than following the transcript structure
- Transform "I showed people X" language into "What I learned/discovered" for a more humble, authoritative tone
- Avoid appearing arrogant or preachy - aim for confident but approachable expertise
- For webinar posts, emphasise personal discovery and honest admissions of limitations
- Always include image references when provided - check if image files need to be copied to `/assets/img/`
- **Research-heavy posts**: Lead with compelling data/statistics that challenge assumptions, use footnotes for detailed sourcing and additional context
- **Linking strategy**: Use implicit links naturally within sentences, avoid "check out this post" style linking - prefer contextual integration. Use `{:target="_blank"}` for external links to open in new windows
- **Footnotes for additional value**: Use footnotes not just for citations but to provide actionable advice and deeper insights that enhance the main narrative
- **Always search for recent articles**: Before writing any blog post, search through recent posts in `_posts/` folder to identify relevant articles to link to implicitly within the content - this improves SEO and provides value to readers

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
- `_layouts/post.html` - Post template with newsletter integration, social sharing, and webinar links
  - **Webinar posts**: Posts tagged 'webinar' automatically show "Join Future Webinars" section after article content
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

#### Blog Post Guidelines (from `blog-posts.mdc`)
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

**Blog Post Writing Process:**
- Start with strong hook and clear statement of main argument
- Use 1-3-1 sentence pattern (1-2 summary sentences in own paragraph, 3 explanatory sentences in new paragraph, 1-2 summary/transition in new paragraph)
- Include `<!--more-->` break after introduction
- End with concrete takeaways or next steps
- Aim for 1500+ words for long-form pieces
- Link to related posts in `_posts/` folder
- Use British English spelling throughout
- Use markdown footnotes for asides, extra detail, and references
- No vertical bar (|) in link titles
- No numbered/unnumbered lists - prefer short paragraphs with headings
- Only use H2 (##) and below, never H1 (#)
- No blank lines before footnote references

### Newsletter System (from `newsletter.mdc`)
Newsletter content uses Kit platform following rough template of one story, one idea, one question weekly. 

**Newsletter Style:**
- Less formal and more intimate than blog posts
- More enthusiastic tone
- Do not make things up - only use what is known to be true
- Ask for stories as needed

**Newsletter Context:**
People expect content about using AI to build agents and products at high speed, generating revenue quickly, with weekly notes sharing stories, learnings, and tips on getting ahead with AI.

### LinkedIn Posts (from `linkedin-posts.mdc`)
**Target Audience:**
- Primary: Technical leaders (CTOs, engineering managers, teams) interested in practical AI solutions
- Secondary: Startup tech teams with similar needs

**LinkedIn Hook Types:**
1. How I - Personal guide on achieving dream outcome
2. How to - Comprehensive guide on skill/outcome
3. Start a story - Inspirational story building authority
4. Captivating quote - Topic-related quote that resonates
5. Surprising statistic - Powerful statistic related to topic

**LinkedIn Formatting:**
- 3 lines of space before 'see more'
- Line 1 & 2: Max 62 characters
- Line 3: Max 50 characters
- No bold, italics, or unnecessary emojis
- Keep hooks short and create curiosity

**LinkedIn Process:**
1. Ask questions about topic one at a time
2. Create five hooks based on guidelines
3. Write post based on style.mdc
4. Create whimsical cartoon pencil style image prompt for OpenAI (portrait style)
5. No hashtags

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

## LinkedIn Content Formatting
When creating LinkedIn content that needs clipboard copying:

### Bold and Italic Formatting
- LinkedIn doesn't support markdown natively
- Convey emphasis without markdown through clever phrasing

### Clipboard Copy Process
- Always use `pbcopy` to copy formatted content to clipboard
- Preserve line breaks and paragraph structure
- Remove escape characters (ensure ! not \!)
