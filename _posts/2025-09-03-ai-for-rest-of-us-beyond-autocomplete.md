---
layout: post
title: "Beyond Autocomplete: Mastering AI Coding Tools for Real Production Work"
date: 2025-09-03 12:00:00 +0000
categories:
- talk
- ai
- developer-experience
- coding
image: /assets/img/ai-for-rest-of-us-talk.jpg
event_name: "AI for the Rest of Us"
venue: "Museum of London"
talk_date: 2025-10-15
talk_url: "https://aifortherestofus.live/london-2025"
talk_title: "Beyond Autocomplete: Mastering AI Coding Tools for Real Production Work"
---

Most developers have tried AI coding assistants, but few use them effectively. There is a vast gap between impressive demos and production reality, where your AI is wrong 70 percent of the time, and that is actually fine.

I spoke at [AI for the Rest of Us London 2025](https://aifortherestofus.live/london-2025) about mastering AI coding tools for real production work, with no vibe coding, no magic demos, just practical techniques that work. What I found was brilliant: the community feel, the audience interaction, and the energy in the room made it an absolute blast.

<!--more-->

## The Prompt Cycle Framework

I delivered the Prompt Cycle framework in this talk, which is five steps that turn [AI coding](/coding-with-ai/) from one-shot attempts into a system that gets better every time you use it. The core principle is simple but powerful: your first AI attempt will always fail, and that is fine. Bad outputs are not failure, they are data you can learn from.

<img src="/assets/img/prompt-cycle-diagram.png" alt="The Prompt Cycle Framework" style="float: right; margin-left: 20px; margin-bottom: 20px; max-width: 400px; width: 100%;" />

**Project Context.** Start with repository-specific rules that prevent repeated mistakes. These rules live in files like CLAUDE.md and give AI the guardrails it needs to understand your codebase conventions. This is your foundation.

**Add Instructions.** Train AI to question you about how to do the task before executing. This is where most people go wrong, they throw vague requests at AI and expect magic. Instead, teach it to understand your technical approach and constraints.

**Specific Task.** Get AI to ask you questions to discover what the task actually is. When you say "add payment" there are actually about twenty questions that should follow. What payment provider? What currencies? How do we handle failures? What about refunds? The questioning reveals the true scope.

**Reset and Refine.** Know when to [reset and refine](/coding-with-ai/#less-context-is-more-reset-and-refine) by throwing away and starting fresh when things are not working. The 90 percent rule applies here: if your code is not at least 90 percent good, throw it away and start fresh. Text is cheap, your time is not.

**Update Project Context.** Feed learnings back into the system so every cycle makes the next one better. Ask AI: "What do you wish you had known at the start?" This is the step most people skip, and it is the biggest mistake. Your system compounds over time.

## Beyond Basic Autocomplete

Many teams use AI as slightly smarter autocomplete and miss the real power. The journey progresses through distinct stages: context-aware suggestions that understand your codebase, prompt stacking for complex tasks, or autonomous agents that handle entire features.

Each stage requires different mental models and guardrails, because traditional development techniques fail with AI collaboration and new cognitive strategies are needed to prevent overwhelm while maintaining code quality.

The spectrum of [AI coding tools](/three-coding-agents-head-to-head/) ranges from basic autocomplete all the way to cloud-based autonomy. Autocomplete gives you real-time code completion with contextual suggestions, which is where it all started. Smart tooling provides little utilities like commit messages and CLI commands. Inline assist brings AI suggestions directly into your workflow with chat-based modifications. Agent mode operates autonomously within your IDE boundaries, handling file management and execution. [Autonomous mode](/independent-coding-agents-tools-arent-ready/) takes this further with complete task execution across multiple files and steps. Cloud-based autonomy operates on GitHub issues and submits pull requests without you being in the IDE at all.

The sweet spot for most production work is agent mode and autonomous mode. These give you the most value for the least effort, and this is where you can actually get started with production work. The Prompt Cycle applies here most powerfully.

## Core Principles for Production AI Coding

Your first attempt will always fail, because [AI produces plausible but incorrect code](/ai-is-consistently-mediocre/) about 70 percent of the time. This is actually fine because it is still faster than writing from scratch, and the Japanese manufacturing principle of Kaizen applies here: continuous improvement. The key mindset shift is that bad outputs are not failures but data you learn from to improve your system.

Working with specs rather than vague requests is critical, because vague requests produce vague results. When you say "add payment" there are actually about twenty questions that should follow: what payment provider, what currencies, how do we handle failures, what about refunds? Use a spec, but keep it fluid rather than rigid documentation, understand every word of your spec and iterate it as you learn. Do not let AI overwrite your specs because they are your source of truth, and [train AI to ask you questions](/webinar-advanced-prompting/) one at a time whilst building.

The [cognitive load of AI pairing](/coding-with-ai/#the-unique-cognitive-load-of-ai-pairing) is different from human pairing, because you need constant verification whilst managing context switching between AI output and your mental model. You need to recognise when to take breaks and spot cognitive fatigue signals, as afternoon sessions feel very different from morning fresh starts.

## The Demo That Showed Real Power

The demo I showed really captured the questioning side of things. I walked through a hypothetical conversation where I felt uneasy about a meeting with my boss, and through systematic questioning, AI helped me uncover how to properly prep for the meeting. Not some vague technical request like "add payment" but real human complexity revealed through asking the right questions. What struck me most was how the audience got it immediately. They have all lived the frustration of AI going sideways on them, of trying to fix something that just keeps getting more tangled.

## Making It Work in Production

At [Cherrypick](https://cherrypick.co), we ship AI-assisted code daily to tens of thousands of users where every bug matters. We have discovered what works through thousands of hours of real production development, and the Prompt Cycle is how we maintain quality whilst moving fast.

The critical piece is [guardrails](/coding-with-ai/#guardrails-matter-more-than-ever), where testing is your safety net for AI code and type hints and strict linting catch mistakes early, often before you even run the code. [Comprehensive tests](/how-to-build-a-robust-llm-application/) give you confidence to move fast because you know if something breaks. When you have these guardrails, you can accept AI code that is 70 percent correct because your systems will catch the problems, but without them you need to review every line meticulously, which destroys the productivity gains.

## Action Plan

Start with creating initial context using something like Claude Code's `/init` command, add one instruction "Ask me one question at a time to build enough context before you write any code", run through one cycle with a real task, and update your context with what you learned.

That is it. One cycle. Then repeat.

AI amplifies your practices, both good and bad. If you have sloppy documentation, AI will produce sloppy code. If you have clear conventions and comprehensive tests, AI will follow those patterns and help you maintain quality. Every cycle makes the next one better.

The goal is not to code faster by removing your judgment. The goal is to code better by focusing your judgment where it matters most. AI handles the boilerplate, the repetitive patterns, the tedious setup. You focus on architecture decisions, business logic, and ensuring the system does what users actually need.

That is how you make demo speed sustainable for real production work. Not by expecting perfection on attempt one, but by building a system that compounds your judgment instead of replacing it.

[AI for the Rest of Us](https://aifortherestofus.live) brought together practitioners shipping real code to real users. The conference had an incredible community feel, with speakers and attendees genuinely interested in practical techniques that work rather than hype and demos. If you missed this one, watch for future events.