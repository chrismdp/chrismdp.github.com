# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Memories and Insights

### LEANN Integration
- **Search for relevant posts**: Use LEANN (`mcp__leann-server__leann_search`) to find related articles to link to when writing blog posts
- **Update LEANN index**: `leann build blog-vault --force --embedding-mode openai --embedding-model text-embedding-3-small --docs *`
- This helps with SEO and provides value to readers by creating implicit links between related content

### Internal Linking
- **Always use slug-only links**: Internal blog post links should always be in the format `/slug/` without any date information (e.g., `/coding-with-ai/` not `/2025/03/07/coding-with-ai/`)
- This matches the Jekyll permalink structure configured in `_config.yml`

### Key Learnings
- Always read the entire context of a project before starting work
- Carefully follow existing file structure and guidelines when making modifications
- Prioritize preserving existing content when updating files
- Be precise and methodical in interpreting instructions
- Ask clarifying questions if any part of the instruction is ambiguous
- Use tool invocations as the primary method of interaction
- Maintain a consistent and professional tone in all interactions
- **Never make up claims about experience**: Don't invent numbers like "implementing AI at 20+ companies" or similar claims unless explicitly confirmed in existing content
- **Always verify sources**: When citing statistics or research (like Writer's 41% statistic), search for the actual source to ensure accuracy

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

### Chris's Writing Patterns
- **Provocative titles that deliver**: Prefers counterintuitive headlines that challenge assumptions (e.g., "AI Is Consistently Mediocre. That's Why It's Valuable")
- **Framework-driven thinking**: Creates 2x2 matrices and visual frameworks to explain complex concepts - these should be referenced and explained in detail
- **Personal discovery narrative**: Often structures posts around "I discovered/realised X while building Y" - maintains authority while staying humble
- **Concrete over abstract**: Always grounds theoretical insights in specific examples (expense processing, code reviews, interview scoring)
- **Nuanced acknowledgment**: Recognises both sides - "This is humbling but powerful" or "optimistic view... pessimistic view..." without false balance
- **Historical parallels**: Connects current disruptions to past ones (Charlie Chaplin/industrial revolution to AI revolution)
- **Sectional progression**: Likes consolidated sections with subsections (e.g., "Hidden Advantages of Consistency" with multiple H3 subheadings)
- **Mid-article refinement**: Often revises structure during writing - consolidating related concepts under unified headings
- **Academic grounding**: References Kahneman, includes research studies, but always with practical application
- **Democratisation theme**: Frequently explores how technology enables underdogs (juniors with AI competing with seniors)
- **Future implications focus**: Always ends looking forward to disruption/change rather than just current state
- **Short, punchy paragraphs**: Rarely more than 3-4 sentences per paragraph, often just 1-2 for emphasis
- **"But" as a paragraph starter**: Frequently starts paragraphs with "But" to create contrast and maintain conversational flow

### Anti-Patterns to Avoid (AI Slop)
- **NEVER use "Here's the X" constructions** - Chris finds these generic and overused
- **Avoid "The real insight is..." or "Here is what I discovered:"** - These are AI writing clichés that feel inauthentic
- **No rhetorical question hooks** - Don't start with "What if I told you..." or similar
- **Avoid generic transitions** - "Let me tell you", "The brutal truth", "You won't believe this"
- **Don't use numbered lists** - Chris prefers short paragraphs with headings over bullet points
- **No false build-up** - Lead with the most interesting insight, don't save it for the end
- **Avoid abstract conclusions** - Always end with concrete implications and future-looking statements

### Webinar Blog Post Guidelines
- **Opening hook**: Use compelling statistics or reframe broad claims (e.g., "95% of technical teams cannot ship their AI agents" rather than specific anecdotes)
- **Webinar context**: Always establish that content comes from a specific webinar with date - "On [date], I gave a webinar about..."
- **Virtual vs physical**: Use "virtual room" for webinars, not just "room"
- **Brand consistency**: Cherrypick is always spelled "Cherrypick" (not "CherryPick") and should link to cherrypick.co
- **Case study linking**: Link to relevant case studies when mentioning specific examples (e.g., meal generator case study)
- **Avoid clunky phrasing**: Don't spell out percentages in prose - use "80% success rate" not "eighty percent good responses"
- **Tools and resources**: Extract tools mentioned in webinars as markdown link lists for easy reference
- **Key takeaways**: Always include a clear takeaway and actionable "try this week" suggestion

### Standard Post-Webinar Process
After each webinar, follow these steps to archive the content and prepare for the next month:

#### 1. Create Webinar Write-Up Blog Post
- [ ] Wait for the webinar transcript to be provided
- [ ] Create a new post in `_posts/` with format: `YYYY-MM-DD-webinar-title.md`
- [ ] Use the current date for the post date
- [ ] Convert the webinar transcript into a blog post following the webinar blog post guidelines above
- [ ] Add categories: `ai`, `webinar`, and any other relevant categories
- [ ] Include the webinar image if one exists (check `/assets/img/`)
- [ ] Add "Tools and Resources" section with markdown link list
- [ ] Add "Key Takeaway to Remember" section summarising main insights
- [ ] Add "One Thing to Try This Week" section with actionable next steps

#### 2. Extract Kit Newsletter Content
- [ ] Create markdown summary with three sections:
  - "Tools & Resources I Mentioned" (bulleted list with descriptions)
  - "Key Takeaway to Remember" (paragraph format)
  - "One Thing to Try This Week" (paragraph format with specific prompt)
- [ ] Format for pasting into Kit email editor
- [ ] Verify all links use absolute URLs (not relative paths)
- [ ] Check referral links are included where applicable

#### 3. Update Webinar Pages for Next Month
- [ ] **Main webinar page** (`pages/webinar.md`):
  - Increment the `kit_tag` number from current value (e.g., if current is `webinar7` → `webinar8`)
  - Set `webinar_date` to the first Thursday of the next month at 14:00 UK local time
  - Use correct timezone offset: `+01:00` for BST (British Summer Time, late March to late October) or `+00:00` for GMT
    - Example: `"2025-10-02T14:00:00+01:00"` for October 2025 (BST)
    - Example: `"2025-11-06T14:00:00+00:00"` for November 2025 (GMT)
- [ ] **Specific webinar landing page** (e.g., `pages/webinar-advanced-prompting.md`):
  - Remove the `redirect_from: /webinar` field (so it no longer redirects the main URL)

#### 4. Commit and Push Changes
- [ ] Commit the new blog post with message like: "Add webinar write-up: [Title]"
- [ ] Commit the updated webinar page with message like: "Update webinar page for next month (webinar8)"
- [ ] Push all changes to GitHub

## Coder Template Management

### Pushing Templates

When working with Coder templates, the correct syntax for pushing templates is:

```bash
# Push template from current directory (must contain main.tf)
coder templates push -y template-name

# Push template from specific directory
cd /path/to/templates/parent && coder templates push -d template-folder -y template-name

# Push with update message
coder templates push -d template-folder -y -m "Update description" template-name

# Example for blog template
cd .coder/templates && coder templates push -d blog -y blog
```

**Key Points:**

- Template name goes at the END of the command
- Use `-d` flag to specify directory containing main.tf
- Use `-y` to bypass confirmation prompts
- Must be run from parent directory of template folder when using `-d`
- Template directory must contain main.tf file

### Common Errors:

- ❌ `coder templates push blog .coder/templates/blog/` (wrong argument order)
- ❌ `coder templates push --directory .coder/templates/blog/ blog` (wrong flag syntax)
- ✅ `coder templates push -d blog -y blog` (correct from templates parent dir)

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

**Important**: When updating existing blog posts, update the date in the front matter to reflect the update date, but NEVER rename the file itself - the filename should always retain the original publication date. This preserves URL structure and history.

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

### Social Media Posts
**IMPORTANT**: When writing for social media or LinkedIn, you MUST ALWAYS read and follow ALL instruction files in the `_roles/sally-social-media-manager/` folder FIRST before creating any social content. This includes:

- Voice & tone standards (no contractions, direct conversational style, Grade 5-7 reading level)
- Hook writing requirements (62/0/50 character format, authority-based openings)
- Content structure guidelines (1,250-3,000 characters optimal, 14+ short paragraphs)
- LinkedIn formatting standards:
  - NO bold text formatting - LinkedIn doesn't render markdown bold
  - Use emojis (🚨, 💡, ⚡, 🎯, etc.) to structure sections instead of headers
  - Use numbered emojis (1️⃣ 2️⃣ 3️⃣ 4️⃣) for ordered lists instead of plain numbers or bullets
  - Convert numbered lists to separate paragraphs with emoji numbers
  - No hashtags needed
- Performance optimization techniques (engagement hierarchy, timing strategy)
- **LinkedIn mentions**: Use @ mentions for profile links (e.g., "@Chris Parsons" and "@AI In Action By Chris Parsons")
- **Draft storage**: Store LinkedIn post drafts in `_drafts/` folder for easy editing and iteration

**CRITICAL**: Always refer to Sally's instructions (`_roles/sally-social-media-manager/instructions.md`) for the latest content structure requirements, paragraph formatting, and performance data. These guidelines override ALL other writing rules when creating social content.

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

