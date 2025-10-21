---
layout: post
title: "Three Coding Agents Head-to-Head"
date: 2025-10-21 09:00:00 +0000
categories:
- ai
- coding
- agents
image: /assets/img/coding-agents-boxing-ring.png
---

**October 2025:** Codex with GPT-5 is now my primary coding agent. It just works out the box.

Back in September, I tested three coding agents on a controlled refactoring challenge. Claude Code won decisively. But last week, after Claude's quality seemed to nose-dive, I went back to Codex for real development work.

These tools move fast. What lost in September won in October. Here is how my assessment evolved.

<!--more-->

## My Current Winner: Codex (October 2025)

Codex with GPT-5 is like working with that quiet senior developer who just gets stuff done. No "you are absolutely right!" cheerleading. No essays about what it is about to do. Just reads your request, thinks for a moment, then cracks on with sensible, logical steps.

The "just talk to it" nature means minimal friction. You can run multiple Codex instances in separate terminal windows, queuing up different tasks simultaneously. One handling architectural refactoring, another making UI tweaks. The `/status` command shows limits clearly. The Rust-based TUI feels noticeably snappier than Claude Code.

For straightforward coding tasks, Codex wins decisively. It is faster, more direct, and easier to work with for the vast majority of development work.

**Claude Code still excels for writing and thinking work.** When I need to draft blog posts like this one, work through complex architectural decisions, or explore strategic implications, the collaborative approach shines. It asks questions, challenges assumptions, helps clarify fuzzy requirements. The background tasks, session resumption, and double-escape checkpoint revert remain invaluable for sustained creative work.

But for coding? Not right now. At least not for me. It might all change again in November.

## How We Got Here: The September Experiment

Back in September, I tested three agents on a complex refactoring challenge in my [kaijo.ai](https://kaijo.ai) project: replace a boolean sandboxing system with flexible arbitrary scopes. Three terminals, same task, clock ticking.

**[Claude Code](https://claude.ai/code)** analysed deeply, then delivered a comprehensive rewrite with updated tests and edge cases handled. Anonymous code review praised the professional, maintainable code. No bugs found.

**[Codex](https://codex.anthr.co/)** moved faster with targeted changes. But it did not run tests until prompted, and the anonymous reviewer spotted a critical API key bug that could have caused production issues.

**[Z.ai](https://docs.z.ai/scenario-example/develop-tools/claude)** used Claude Code's interface with GLM-4.5 underneath - clever architecture, but painfully slow with frequent timeouts. I gave up waiting.

**My conclusion in September: Claude Code was the clear winner.** It delivered everything perfectly in one go, whilst Codex felt incomplete and Z.ai was unusable.

But that test had limitations. I had spent months tuning Claude Code with custom rules whilst giving Codex default settings and insufficient context. A single controlled test did not tell the full story about how these tools would perform in real development work.

{% include ai-newsletter-short.html %}

## Why My Assessment Changed

A few weeks after the September test, I went back to Codex for actual development work: building a complex feature requiring substantial refactoring whilst simultaneously making small UI tweaks across the same codebase.

After a few hours, different patterns emerged.

**The personality difference mattered more than I expected.** When you need to fix a button or refactor an API handler, you do not want a thought partner analysing philosophical implications. You want someone who will just get it done. Codex delivers exactly that.

[Peter Steinberger's article on agentic coding](https://steipete.me/posts/just-talk-to-it){:target="_blank"} includes a brilliant curve showing two approaches: tools that need careful direction versus tools you can "just talk to". Codex firmly sits in the "just talk to it" category. Claude Code requires substantially more prompting and guidance to achieve similar results.

**Codex rewards precise communication.** Yes, it can overwrite files if you are not clear. But after a few iterations, you learn to be explicit about what should and should not change. Turns out Codex does not need elaborate rule files - just clear task descriptions.

**The original test had limitations.** I had months of Claude Code tuning versus default Codex settings. I had not provided enough context. The AI coding landscape changes monthly. What felt limited in September worked smoothly by October. Any single test is just a snapshot.

Then in October, Claude's quality seemed to nose-dive. At the same time, Codex got GPT-5. The gap widened significantly.

**The cost calculation shifted.** I was paying £75 monthly for Claude Code. I have downgraded to the £15 plan now that I am primarily using it for writing. Codex costs £200 monthly - not cheap, but worth it given how much more productive it makes me for development work.

## The Real Lesson: Tools Evolve Fast

A single complex refactoring challenge cannot capture how you will work with a tool across different contexts. The personality fit, the workflow friction, the mental overhead of interaction patterns - these factors revealed themselves through actual usage rather than controlled tests.

More importantly, these tools evolve at an astonishing pace. What felt like a limitation in September worked flawlessly by October. Interface improvements, model updates, and subtle changes in behaviour can shift the value proposition in weeks.

My September conclusion was correct for September. My October conclusion is correct for October. Both can be true.

**Do not lock into long-term contracts.** Even with hefty discounts, avoid committing to a single tool for more than 2-3 months. The landscape is moving too fast. The tool that wins today might lag behind next quarter. Pay monthly, stay flexible, and be ready to switch when the fundamentals shift.

The best approach: try multiple tools on your actual work. Pay attention to personality fit and workflow friction, not just technical correctness on benchmarks. And expect your assessment to evolve as the tools themselves evolve.

## Detailed Results

Here is a detailed view of what I found:

| Agent       | Speed | Testing | UI | Correctness | Code Quality | Cost | Setup/Tuning Required | Communication Style |
|-------------|-------|---------|----|-----------|-----------|----- |-----|-----|
| Claude Code | 🟢<br>Good pace with comprehensive analysis | 🟢<br>Updated all tests automatically, handled edge cases without prompting | 🟢<br>Background tasks, session resumption, checkpoint revert (Esc twice), works whilst doing other tasks | 🟢<br>Complete scope-based system with proper fallback handling, no bugs found in anonymous review | 🟢<br>Professional, maintainable code with consistent TypeScript patterns praised by anonymous reviewer | 🟠<br>£75/month (now downgraded to £15 for writing-only use) | 🟠<br>Requires months of rule tuning and detailed configuration to achieve "just talk to it" simplicity | 🟠<br>Verbose and collaborative. "You're absolutely right!" responses. Lengthy explanations. Best for writing and thinking work where thought partnership is valuable |
| Codex | 🟢<br>Fast initial implementation, conservative approach | 🟠<br>Made no attempt to run tests until explicitly prompted (in original test with insufficient context) | 🟢<br>Clearer limits via /status, snappier Rust-based TUI, works well with multiple instances | 🟡<br>Critical bug in original test likely due to insufficient context - performs well with clear prompting | 🟢<br>Matter-of-fact senior dev approach, clean logical steps, easy to follow | 🟠<br>£200/month but worth it for primary coding work | 🟢<br>"Just talk to it" tool - minimal setup needed, rewards clear communication | 🟢<br>Concise and matter-of-fact. Calm, introverted senior dev style. No performative enthusiasm. Just gets things done without fanfare |
| Z.ai (CC) | 🔴<br>Painfully slow - 5x slower than others with frequent timeouts | ❓<br>Task abandoned due to performance issues | 🟢<br>Smart architecture using Claude Code interface with GLM-4.5 underneath | ❓<br>Could not complete task to evaluate | ❓<br>Could not complete task to evaluate | 🟢<br>Cheapest option but hit timeouts and rate limits before completion | ❓<br>Could not evaluate | ❓<br>Could not evaluate |

## What This Means for Tool Evaluation

The landscape evolves too fast for single tests or long-term commitments. What wins this month might lag next month. Interface improvements, model updates, and quality shifts can change everything in weeks.

Real insight emerges from using tools across different contexts and task types over time. The tool that wins a carefully controlled refactoring challenge might perform differently in actual development work. And both assessments can become outdated within weeks.

Stay flexible. Try multiple tools. Pay attention to personality fit and workflow friction, not just technical correctness on benchmarks. And never lock yourself into contracts longer than 2-3 months, no matter how tempting the discount.
