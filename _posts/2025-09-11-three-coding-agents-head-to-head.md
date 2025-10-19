---
layout: post
title: "Three Coding Agents Head-to-Head: A Complex Refactoring Challenge"
date: 2025-10-19 09:00:00 +0000
categories:
- ai
- coding
- agents
image: /assets/img/coding-agents-boxing-ring.png
---

I tested three major coding agents - Claude Code, Codex, and Z.ai - first on a controlled refactoring challenge, then on real development work. My conclusions evolved significantly.

<!--more-->

## The Initial Experiment

I started by testing three agents on a complex refactoring challenge in my [kaijo.ai](https://kaijo.ai) project: replace a boolean sandboxing system with flexible arbitrary scopes. Three terminals, same task, clock ticking.

**[Claude Code](https://claude.ai/code)** analysed deeply, then delivered a comprehensive rewrite with updated tests and edge cases handled. Anonymous code review praised the professional, maintainable code. No bugs found.

**[Codex](https://codex.anthr.co/)** moved faster with targeted changes. But it did not run tests until prompted, and the anonymous reviewer spotted a critical API key bug that could have caused production issues.

**[Z.ai](https://docs.z.ai/scenario-example/develop-tools/claude)** used Claude Code's interface with GLM-4.5 underneath - clever architecture, but painfully slow with frequent timeouts. I gave up waiting.

**My conclusion at the time: Claude Code was the clear winner.** It delivered everything perfectly in one go, whilst Codex felt incomplete and Z.ai was unusable.

**My assessment evolved.** I had spent months tuning Claude Code with custom rules whilst giving Codex default settings and insufficient context. A single controlled test did not tell the full story about how these tools would perform in real development work.

{% include ai-newsletter-short.html %}

## What Real Development Work Revealed

I went back to Codex a few weeks later for some actual development work: building a complex feature requiring substantial refactoring whilst simultaneously making small UI tweaks across the same codebase.

After a few hours, different patterns emerged.

## Codex: The "Just Talk To It" Winner for Coding

[Peter Steinberger's article on agentic coding](https://steipete.me/posts/just-talk-to-it){:target="_blank"} includes a brilliant curve showing two approaches: tools that need careful direction versus tools you can "just talk to". Codex firmly sits in the "just talk to it" category. Claude Code requires substantially more prompting and guidance to achieve similar results.

**The personality difference matters.** Codex feels like working with a matter-of-fact, introverted senior developer. It reads your request, thinks for a moment, then cracks on with sensible, logical steps. No performative enthusiasm. No "you're absolutely right!" responses. Just calm, quiet assistance that sorts things out without fanfare.

When you need to fix a button or refactor an API handler, you do not want a thought partner analysing philosophical implications. You want someone who will just get it done. Codex delivers exactly that.

**The practical workflow wins:** Running multiple Codex instances in separate terminal windows lets you queue up different tasks simultaneously. One handling architectural refactoring, another making UI tweaks. The `/status` command shows limits clearly. The Rust-based TUI feels noticeably snappier than Claude Code.

Yes, Codex can overwrite files if you are not clear. But it rewards precise communication. After a few iterations, you learn to be explicit about what should and should not change.

**The original test had limitations.** I had months of Claude Code tuning versus default Codex settings. I had not provided enough context. Turns out Codex does not need elaborate rule files - just clear task descriptions.

The AI coding landscape changes monthly. What felt limited in September worked smoothly by October. Any single test is just a snapshot.

## Claude Code: Better for Writing and Thinking

Claude Code excels at different work. When I need to draft blog posts like this one, work through complex architectural decisions, or explore strategic implications of technical choices, the collaborative approach shines. It asks questions, challenges assumptions, helps clarify fuzzy requirements.

The user experience features remain superior for sustained work. Background tasks mean you can let it work whilst doing other things. Session resumption lets you pick up exactly where you left off. Double-escape checkpoint revert proves invaluable when exploring different approaches.

But for straightforward coding tasks, that collaborative tendency becomes exhausting. The "you're absolutely right!" responses. The lengthy explanations of what it is about to do. The desire to be a thought partner when you just want someone to fix a button. It all feels performative and inefficient compared to Codex's matter-of-fact approach.

**The original test likely reflected my months of setup investment.** I had tuned Claude Code with custom rules and detailed configuration files. Those prompts shaped it into something that worked exceptionally well for that specific test. Looking back at Peter Steinberger's curve, I had moved Claude Code towards the "just talk to it" end through careful direction - but that investment should not be necessary for basic coding work.

## The Winner: Different Tools for Different Jobs

After the original test, I concluded Claude Code was the clear winner. After returning to Codex for real development work, my assessment evolved.

**For coding work, Codex wins decisively.** It is faster, more straightforward, and easier to work with for the vast majority of development tasks. The "just talk to it" nature means less friction, less performative conversation, and more time actually building things.

**For writing and thinking work, I still use Claude Code.** When drafting this very article, Claude Code's collaborative approach proved valuable. It asked clarifying questions, helped structure arguments, and acted as the thought partner that makes sense for creative work.

**The cost calculation has shifted.** I was paying £75 monthly for Claude Code. I have downgraded to the £15 plan now that I am primarily using it for writing. Codex costs £200 monthly - not cheap, but worth it given how much more productive it makes me for development work.

A single complex refactoring challenge cannot capture how you will work with a tool across different contexts. The personality fit, the workflow friction, the mental overhead of interaction patterns - these factors revealed themselves through actual usage rather than controlled tests.

## Detailed Results

Here is a detailed view of what I found:

| Agent       | Speed | Testing | UI | Correctness | Code Quality | Cost | Setup/Tuning Required | Communication Style |
|-------------|-------|---------|----|-----------|-----------|----- |-----|-----|
| Claude Code | 🟢<br>Good pace with comprehensive analysis | 🟢<br>Updated all tests automatically, handled edge cases without prompting | 🟢<br>Background tasks, session resumption, checkpoint revert (Esc twice), works whilst doing other tasks | 🟢<br>Complete scope-based system with proper fallback handling, no bugs found in anonymous review | 🟢<br>Professional, maintainable code with consistent TypeScript patterns praised by anonymous reviewer | 🟠<br>£75/month (now downgraded to £15 for writing-only use) | 🟠<br>Requires months of rule tuning and detailed configuration to achieve "just talk to it" simplicity | 🟠<br>Verbose and collaborative. "You're absolutely right!" responses. Lengthy explanations. Best for writing and thinking work where thought partnership is valuable |
| Codex | 🟢<br>Fast initial implementation, conservative approach | 🟠<br>Made no attempt to run tests until explicitly prompted (in original test with insufficient context) | 🟢<br>Clearer limits via /status, snappier Rust-based TUI, works well with multiple instances | 🟡<br>Critical bug in original test likely due to insufficient context - performs well with clear prompting | 🟢<br>Matter-of-fact senior dev approach, clean logical steps, easy to follow | 🟠<br>£200/month but worth it for primary coding work | 🟢<br>"Just talk to it" tool - minimal setup needed, rewards clear communication | 🟢<br>Concise and matter-of-fact. Calm, introverted senior dev style. No performative enthusiasm. Just gets things done without fanfare |
| Z.ai (CC) | 🔴<br>Painfully slow - 5x slower than others with frequent timeouts | ❓<br>Task abandoned due to performance issues | 🟢<br>Smart architecture using Claude Code interface with GLM-4.5 underneath | ❓<br>Could not complete task to evaluate | ❓<br>Could not complete task to evaluate | 🟢<br>Cheapest option but hit timeouts and rate limits before completion | ❓<br>Could not evaluate | ❓<br>Could not evaluate |

## What This Means for Tool Evaluation

**These tools evolve at an astonishing pace.** What felt like a limitation in September worked flawlessly by October. Interface improvements, model updates, and subtle changes in behaviour can shift the value proposition in weeks.

My evolving assessment highlights an important lesson: single tests have limited value. Real insight emerges from using tools across different contexts and task types. The tool that wins a carefully controlled refactoring challenge might perform differently in actual development work.

The best approach: try multiple tools on your actual work. Pay attention to personality fit and workflow friction, not just technical correctness on benchmarks. These factors matter more than you might expect.
