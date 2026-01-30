---
layout: post
title: "Where Did My Day Go? A Claude Code Skill for Remembering"
date: 2026-01-16 12:00:00 +0000
permalink: /where-did-my-day-go/
redirect_from: /today-in-claude-code/
categories:
- ai
- claude-code
- tools
image: /assets/img/today-in-claude-code-motif.jpg
infographic: /assets/img/today-in-claude-code-infographic.jpg
---

You know that feeling at the end of a day with Claude Code? You have been productive. You know you have. But when someone asks what you accomplished, your mind goes blank. The work happened so fast that you cannot remember half of it.

<!--more-->

This is the strange paradox of working with AI coding assistants. The speed that makes them valuable also makes your work invisible. You finish a task, move to the next one, finish that, move again. Hours later you have shipped features, fixed bugs, written documentation, and refactored code, but the details have blurred together into a vague sense of having been busy.

I built a [Claude Code skill](https://gist.github.com/chrismdp/29b3c5504504fe9ad2ff3310fa2a2a99){:target="_blank"} to solve this problem. It generates a comprehensive daily summary of everything you accomplished, grouped by theme, with token usage and costs included. At the end of each day, you run the skill and get a clear picture of what you actually did.

## The Output

The skill produces markdown output that looks like this:

```markdown
## Claude Code Activity

### Token Usage
- **Output tokens:** 139,838
- **Input tokens:** 74,844
- **Cache read:** 225M
- **Cost:** $204.36

### Webinar Research (morning)
- Compared OpenAI, Anthropic, Google Gemini policies
- Created comparison slides with presenter notes
- Sourced shadow AI breach statistics

### Blog/Content (afternoon)
- Running Ralph in Production post: multiple edits
- Created Gemini image generation skill
- Generated infographics and motif extraction

### Development
- Updated Ralph.md: escalation rules
- UI: mic button to finish checkmark
- Fixed bead sync issues, submitted bug to GitHub

### Other
- Migrated skills to private submodule repo
- Follow-up email drafted
```

The format works well for daily standups, personal records, or just satisfying that nagging feeling of wanting to know where your time went. I paste mine into my daily notes in Obsidian.

## How It Works

The skill pulls data from two sources. First, it runs `ccusage` to get authoritative token counts and costs for the day. Second, it extracts every prompt you sent from Claude Code's history file, grouped by project.

The analysis step is where the value comes from. Rather than listing every interaction, the skill groups your work into meaningful themes based on what was actually done. It focuses on substantial work that took ten to fifteen minutes or more, and bundles quick fixes and minor tweaks into an "Other" section to keep the summary readable.

The skill also uses timestamps to indicate when work happened. Knowing that you did research in the morning and coding in the afternoon helps reconstruct the shape of your day.

## Get The Skill

[Download it from GitHub Gist](https://gist.github.com/chrismdp/29b3c5504504fe9ad2ff3310fa2a2a99){:target="_blank"} and save as `skill.md` in a folder called `today-in-claude-code` inside your Claude Code skills directory (usually `~/.claude/skills/`). Then run `/today-in-claude-code` at the end of your day.

You will need `ccusage` installed for token tracking. Install it with `npm install -g ccusage` and ensure you have `jq` available for the history parsing.

I have been extracting my various large CLAUDE.md files into separate skills. I now have around fifteen of them, many refined over the last few months. Some I will release publicly like this one. Others contain proprietary methods or client IP that need to stay private. Managing this growing library is becoming a challenge in itself, and I am still figuring out the best approach.

## See Your Patterns

Tracking your AI-assisted work helps you make better decisions about where AI helps most. You might discover that certain types of tasks flow faster than others, or that you spend more time on refactoring than you realised. This visibility compounds when working with Claude Code as part of your [broader coding workflow](/coding-with-ai/), helping you optimise your patterns over time. And when someone asks what you did today, you will have an answer.
