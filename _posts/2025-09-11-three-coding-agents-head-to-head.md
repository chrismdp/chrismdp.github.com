---
layout: post
title: "Three Coding Agents Head-to-Head: A Complex Refactoring Challenge"
date: 2025-09-11 09:00:00 +0000
categories:
- ai
- coding
- agents
image: /assets/img/coding-agents-boxing-ring.png
---

I stared at my screen, frustrated. The sandboxing system I had just implemented in my [kaijo.ai](https://kaijo.ai) project felt clunky - a simple boolean flag that could not handle the complexity I needed. What I really wanted was arbitrary scopes that could be defined and applied flexibly across evaluations and prompt generation.

Rather than manually refactor this myself, I decided to run an experiment: pit three major coding agents against each other on this genuinely challenging task. Not a simple "write me a function" request, but something that would test their limits - modifying an existing commit in a well-factored, well-tested codebase with proper linting, integration tests, and end-to-end tests.

{% include ai-newsletter-short.html %}

<!--more-->

## The Setup: Three Contenders Enter

I launched three terminals and set up the challengers:

**[Claude Code](https://claude.ai/code)** - The premium option, known for its polished interface and comprehensive capabilities.

**[Codex](https://codex.anthr.co/)** - The scrappy alternative with a completely different CLI approach and attractive pricing.

**[Z.ai](https://docs.z.ai/scenario-example/develop-tools/claude)** - The clever newcomer that piggybacks on Claude Code's interface using environment variables whilst running GLM-4.5 underneath.

Each agent got the same brief: back out my boolean sandboxing system and replace it with a flexible arbitrary scopes system. The clock started ticking.[^1]

[^1]: I also experimented with [GPT-OSS](https://github.com/openai/gpt-oss) based on the recent GitHub git flow responses from OpenAI's first open-source language models. Despite using a proxy setup, I could not get it stable enough for practical coding work - perhaps another day when the tooling matures.

## Round One: First Impressions

![My actual setup running three coding agents simultaneously](/assets/img/three-coding-agents-terminals.png)
*My setup: three terminal windows running Claude Code, Codex, and Z.ai simultaneously on the same complex refactoring task*

Codex came out swinging. It read my CLAUDE.md configuration file - a promising sign of project awareness - and immediately started making changes. Conservative, methodical, but moving fast. Within minutes, it had a basic implementation working.

Claude Code took a different approach. It spent more time analysing the existing code, understanding the broader context, then launched into what looked like a more comprehensive rewrite.

Z.ai... well, Z.ai was thinking. And thinking. And still thinking. The interface showed progress, but at a glacial pace that had me checking if something had frozen.

## The Waiting Game

As the agents worked, the differences became stark. Codex and Claude Code were both moving at a good clip, but Z.ai felt like it was running underwater - perhaps five times slower than the others. I found myself losing patience, switching between terminals to check progress.

Codex finished first with what looked like a solid implementation. But when I went to run the tests... nothing. It had not even attempted to run them. When I prompted it to do so, it dutifully complied, but this felt like a basic oversight.

Claude Code was still churning away, but I could see it was doing more - modifying tests, updating documentation, handling edge cases that I had not even thought to mention.

## The User Experience Reality

Working with these agents revealed crucial differences beyond raw coding ability. Codex operates in a sandbox by default, but this is poorly explained. When I tried to run additional commands or step away and return, the context was lost. No session resumption meant starting over each time.

Claude Code offered background tasks - I could let it work whilst I did other things, then return to see progress. Session resumption meant I could pick up exactly where I left off. The double-escape checkpoint revert feature proved invaluable when I wanted to try different approaches.

Z.ai benefited from Claude Code's superior interface, but the underlying performance was so sluggish that I eventually lost patience and moved on.

## Z.ai: Promising Concept, Frustrating Reality

[Z.ai](https://docs.z.ai/scenario-example/develop-tools/claude) had the cleverest approach - piggyback on Claude Code's superior interface using environment variables whilst running GLM-4.5 underneath. This architectural decision made sense since Claude Code definitely has the best UI of the three.

Unfortunately, the execution was painfully slow. Z.ai felt like it was running underwater - perhaps five times slower than the other agents, with frequent timeouts that made the experience genuinely frustrating. I found myself switching between terminals, checking if something had frozen, losing patience with each passing minute.

To make matters worse, it had to compact immediately as it ran out of context window space, losing valuable information about the codebase and task requirements that the other agents retained throughout the process.

The interface strategy was smart, but when you cannot complete tasks due to performance issues and context limitations, clever architecture means nothing. I eventually gave up waiting for it to finish the refactoring. There may be circumstances where it works better, but for complex development work under time pressure, it was simply not viable.

## Codex: The Scrappy Contender

Codex came out swinging and showed genuine promise. It read my CLAUDE.md configuration file - a good sign of project awareness - and immediately started making changes. Conservative and methodical, but moving at a decent pace. Within minutes, it had a basic implementation working.

**Important caveat**: I have spent considerable time tuning my Claude Code setup with custom rules and configurations, whilst Codex was running with essentially default settings. This is a significant unfair advantage for Claude Code in this comparison. However, Codex did mention that it read my CLAUDE.md rules file, suggesting it was attempting to use my project-specific guidance, so perhaps the disadvantage was not as severe as it might initially appear. Still, it's a major caveat to keep in mind.

The approach was more cautious than I expected. Rather than the comprehensive rewrite I was hoping for, Codex made targeted changes that got basic functionality working without touching too much of the existing codebase. This conservatism has merit - smaller changes mean fewer things that can break.

However, the limitations became apparent quickly. When I went to check test output.. nothing. It had not even attempted to run them. When I prompted it to do so, it dutifully complied, but this felt like a basic oversight for a refactoring task - though this might well be addressable with proper rule configuration.

The user experience had significant gaps. Codex operates in a network-restricted sandbox by default, but this is poorly explained and not easily configurable. Without session resumption, stepping away and returning meant losing context and starting over. No background jobs meant waiting for long operations to complete rather than continuing with other work.

Most critically, my anonymous code review later spotted a bug in API key selection that could have caused production issues - exactly the kind of subtle error that makes incomplete implementations dangerous.

Codex is significantly cheaper and shows genuine promise. With dedicated time spent on customisation and rule tuning, it could likely close much of the capability gap with Claude Code. However, given Claude Code's clear superiority out-of-the-box, there is little incentive to invest that tuning effort when the premium option delivers everything immediately.

## The Anonymous Verdict

My initial reaction favoured Codex. It finished quicker, required more interaction from me, and I got to test the implementation myself - everything seemed to work fine. I assumed this hands-on approach meant it was the better implementation.

When I checked Claude Code's output later, it had not finished as quickly but had been the most autonomous, accomplishing the most with the least input from me. I found myself thinking that because it took longer, maybe it was not as good a solution.

How wrong I was.

To remove my own bias, I anonymised all the outputs and fed them to another AI for code quality analysis. GPT-5 refused the task due to size, but Opus 4.1 handled it well. I ran the analysis twice to ensure consistency.

The anonymous reviewer confirmed my subjective experience whilst spotting details I had missed. The critical bug in Codex's implementation could have caused production issues. Meanwhile, one agent's output was praised for professional, maintainable code with consistent patterns and proper TypeScript usage.

## Claude Code: The Complete Solution

Claude Code took a different approach from the start. Rather than rushing into changes, it spent time analysing the existing code and understanding the broader context. Then it launched into what looked like a comprehensive rewrite.

This patience paid off. Claude Code was the only agent that delivered everything in one go: backed out the existing sandboxing implementation, wrote the new scopes system, updated all the tests, handled edge cases I had not even mentioned, and got everything working flawlessly.

The user experience was genuinely superior. Background tasks meant I could let it work whilst doing other things, then return to see progress. Session resumption let me pick up exactly where I left off. The double-escape checkpoint revert feature proved invaluable when I wanted to try different approaches - small details that add up to a dramatically better development experience.

There was slight ambiguity around fallback prompts for new scopes, the same issue that tripped up Codex, but Claude Code resolved this smoothly without additional prompting.

Most importantly, it delivered complete, professional code that the anonymous reviewer praised for maintainability and consistent patterns. No critical bugs, no missing functionality, no gaps that would require follow-up work.

## The Winner: Sometimes You Get What You Pay For

This is just one change, and I plan to retest. However, this time around, **Claude Code was the clear victor despite being the most expensive option.** When facing complex refactoring with tight deadlines, you want the tool that will get everything right the first time. The combination of technical capability and polished user experience justifies the premium pricing.

User experience matters as much as raw capability. Features like session resumption, background tasks, and checkpoint reverting might seem minor until you desperately need them during complex development work.

For straightforward tasks, cheaper alternatives might suffice. But when the stakes are high and the task is complex, the premium option proved its worth by simply getting everything right in one go. This saved me a lot of time, which is more than worth the extra monthly spend for me.

## Detailed Results

Here is a detailed view of what I found:

| Agent       | Speed | Testing | UI | Correctness | Code Quality | Cost |
|-------------|-------|---------|----|-----------|-----------|----- |
| Claude Code | 🟢<br>Good pace with comprehensive analysis | 🟢<br>Updated all tests automatically, handled edge cases without prompting | 🟢<br>Background tasks, session resumption, checkpoint revert (Esc twice), works whilst doing other tasks | 🟢<br>Complete scope-based system with proper fallback handling, no bugs found in anonymous review | 🟢<br>Professional, maintainable code with consistent TypeScript patterns praised by anonymous reviewer | 🟠<br>Most expensive but delivers everything in one go |
| Codex | 🟢<br>Fast initial implementation, conservative approach | 🟠<br>Made no attempt to run tests until explicitly prompted | 🟠<br>Sandbox restrictions poorly explained, no session resumption, no background jobs, context lost when switching tasks | 🔴<br>Critical API key selection bug spotted by anonymous review, incomplete scope implementation | 🟡<br>Readable but inconsistent, missing key functionality, conservative changes | 🟢<br>Significantly cheaper, promising with more tuning |
| Z.ai (CC) | 🔴<br>Painfully slow - 5x slower than others with frequent timeouts | ❓<br>Task abandoned due to performance issues | 🟢<br>Smart architecture using Claude Code interface with GLM-4.5 underneath | ❓<br>Could not complete task to evaluate | ❓<br>Could not complete task to evaluate | 🔴<br>Hit timeouts and rate limits before completion |

## Next Steps

These comparisons are snapshots in time. AI model performance can be notoriously variable - sometimes changing over the course of a single day as API quality fluctuates. The results I experienced today might differ from what you encounter tomorrow.

Regular re-testing of these agents will be necessary as they evolve, improve their interfaces, and potentially close performance gaps.

I also need to test Gemini CLI in a future comparison. Google's offering could bring interesting capabilities to the coding agent landscape, and it would be valuable to see how it performs against these established players.
