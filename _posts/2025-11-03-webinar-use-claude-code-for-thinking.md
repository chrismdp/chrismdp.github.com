---
layout: post
title: "How To Use Claude Code for Thinking"
date: 2025-11-06 09:00:00 +0000
permalink: /webinar-claude-code-thinking/
image: /assets/img/use-claude-code-webinar-thinking.png
image_portrait: false
categories:
- ai
- webinar
---

On November 6, 2025, I gave a webinar about something slightly unconventional: using a coding tool for thinking, writing, and strategy work rather than code.

Claude Code is designed for [writing production code](/coding-with-ai/){:target="_blank"}. The name makes that obvious. But I've discovered something unexpected: whilst I use Cursor for actual coding, Claude Code has become my primary tool for strategic thinking, content creation, and knowledge management.

<!-- more -->

## Why Claude Code Works Better for Thinking

Claude Code is chattier than [Codex](/three-coding-agents-head-to-head/). For coding, that chattiness can feel like friction. For thinking, it's exactly what you need.

**Context that persists.** Chat interfaces like Claude.ai or ChatGPT use memory features that are opaque and unreliable. Projects help, but you're always fighting against the limitations of the interface. Claude Code runs within the context of a file system, giving you explicit control over what context matters.

**Tools that extend capability.** Claude Code can read files, search semantically through notes, execute commands, and interact with your actual working environment. This turns it from a conversation partner into a thought partner that can actually help manage your knowledge.

**Obsidian integration that just works.** Because Claude Code works with markdown files on disk, and Obsidian is just a viewer for markdown files on disk, they combine naturally. Write in Obsidian, think with Claude Code, and let them work together.

The key insight: give the AI more power, more context, and more persistent memory, and it becomes genuinely useful for complex thinking tasks.

## My Morning Routine

Every morning, I start Claude Code in my journal repository and say: "Good morning, please start my morning routine."

What happens next demonstrates the power of combining rules, context, and conversation. Claude Code reads my monthly goals, weekly goals, and yesterday's notes. It checks my calendar using gcalcli.[^gcalcli] It searches through my note repository using semantic search to find relevant context about what I'm working on.

Then it asks me questions.

**"How are you feeling today?"** I dictate my response using [Wispr Flow](https://wisprflow.ai/r?CHRIS104){:target="_blank"}, which transcribes my rambling thoughts, removes the ums and ahs, adds punctuation, and pastes clean text.

**"What specifically is worrying you most?"** I answer honestly. Maybe I'm not sure how to approach validation for a new cohort programme I'm considering. Maybe I need help thinking through a client challenge.

**One question at a time.** This is crucial. Get AI to ask you questions, not give you answers. Answer the questions, get more questions, and let the AI help you think.

When we're done, Claude Code creates a daily note in my Obsidian vault with everything we discussed, formatted clearly, linked to relevant existing notes, and marked with "AI update" so I know I didn't write it myself.

I never write my own journal entries anymore. Claude Code does it for me, better than I would have done manually, in a fraction of the time.

## Thinking Through Strategy

During the webinar, I demonstrated thinking through validation strategy for a real business idea: an AI leadership cohort for technical leaders.

I started with: "Right, time to think about the validation strategy for my AI leaders cohort."

Claude Code immediately asked: "What specifically do you want to validate?"

I answered honestly: "I want to ensure I'm solving a real problem and that the curriculum works. Not sure which is more important."

The conversation continued, one question at a time, drilling down:

**What problem would the cohort solve?** Cutting through the chaos, helping leaders roll out AI effectively, avoiding shadow IT, maximising productivity.

**What type of leader feels this most acutely?** After exploring the options, I realised: CTOs specifically, because the explosion of coding assistants is causing control problems right now.

This is exactly the kind of strategic thinking that's hard to do alone. AI doesn't give you the answers. It asks better questions than you'd ask yourself, surfaces assumptions you didn't know you were making, and helps you think more clearly.

When we finished, Claude Code updated my repository with useful notes, created connections to related thoughts, and updated my daily note to track that I'd done the thinking work.

## Writing Articles from Research

For content creation, I combine Obsidian's web clipper with Claude Code's context management.

When I find an interesting article, like Apple's billion-dollar deal with Google for Siri rather than using their own models, I clip it to my Obsidian vault using a browser extension. Then I add my own quick thoughts as a note at the top.

In Claude Code, I say: "I want to write a LinkedIn post about that Apple billion-dollar article. Prepare a concise briefing note, paying attention to my comment. Look up other things in this repository that might help, and ask me questions to get more insight."

It searches through my notes, finds related thinking, and asks targeted questions:

**What's your core thesis about why this deal matters?** I think it's a signal about market consolidation. Apple is hedging against the bubble bursting.

**Have you written about AI winters or bubble bursts before?** In a real repository, it would find several related notes and articles I've saved.

After answering a few questions, I tell it: "That's enough. Update the briefing note and copy it to my paste buffer."

Then I switch to my blog repository, which has completely different Claude Code rules focused on writing style, British English, and anti-patterns to avoid. I paste the briefing note and say: "Write a LinkedIn post from this."

The result is polished, incorporates my actual thinking, avoids AI slop patterns, and reads like something I could have written myself if I'd spent significantly more time on it.

## The Tools That Make This Work

The setup is straightforward: [Claude Code](https://claude.ai/code){:target="_blank"} for the AI agent, [Obsidian](https://obsidian.md){:target="_blank"} for note editing, [Wispr Flow](https://wisprflow.ai/r?CHRIS104){:target="_blank"} for dictation, and a few command-line tools like [gcalcli](https://github.com/insanum/gcalcli){:target="_blank"} for calendar integration.[^gcalcli]

The real power comes from CLAUDE.md files that tell Claude Code how to behave in each repository. My journal repository asks questions and structures my thinking. My blog repository focuses on writing style and British English. These rules evolve over time like scar tissue, built up from experience of what works and what doesn't.

**Start simple.** Create a folder, add a CLAUDE.md file with some basic rules about how you want to think, and run `claude` in that folder. Ask it to help you think through one decision. Tell it to ask you questions, not give you answers.

You don't need Obsidian yet. You don't need embeddings or calendar integration. Just start with conversation and see where it takes you.

## Key Takeaway to Remember

**AI works best as a question generator, not an answer generator.** Get it to ask you one question at a time, answer thoughtfully, and let the process reveal what you actually think. Combined with persistent context in a file system, this becomes a genuinely powerful way to externalise and structure your thinking.

The best way to think with AI is to stop asking it what to think and start letting it ask you better questions.

[^gcalcli]: I use MCP tools occasionally, but I prefer command-line tools because they're simpler and I can use them anyway. Gcalcli is just a way of seeing a particular calendar without needing complex integrations.
