---
layout: post
title: "Open Models Are Ready"
date: 2026-05-15 07:00:00 +0000
image: /assets/img/daily-driver-deepseek-barchart.jpg
image_portrait: true
categories:
- ai
- open-source
- economics
- agents
---

I run a custom Kanban board as markdown files in an Obsidian vault, with multi-step projects for everything and background worker agents doing the work using systemd, cron and `claude -p`. Useful but expensive: the whole thing runs on a Claude Max subscription at about $200 per month, and I was hitting the limits before the cycle ended.

So I spent this week migrating my background worker fleet to [Pi](https://pi.dev) running on DeepSeek V4 Pro via OpenRouter. Within a few hours the system was making the decisions I would make, at a fraction of the token cost, and the cheapest model in my stack caught the most bugs. I have also been running my own interactive coding through Pi on the same model, and although it costs a little more than Claude Max today, the gap is closing and the path off Claude is proven.

Here is which models worked, which ones did not, how to set it up with OpenRouter so your data stays private, and whether the economics hold up under production conditions.

<!--more-->

## The Metered Bill Changes Everything

Anthropic's announcement about `claude -p` and the Agent SDK moving to metered pricing made me think harder about whether I wanted this dependency to deepen. Running all my Claude Code use at metered rates would cost about $10,000 a month, and the June change only hits about a quarter of that (the workers that run through `claude -p`), but I read it as a signal. Unmetered plans are not going to last, and I would rather drive my per-token cost down across the stack before the rest follows. I started porting everything to Pi and testing every open source model I could get my hands on.

## Three Failures, One Winner

I spent two days cycling through models: Kimi K2.6, MiniMax M1, Tencent's Hy3 preview. None of them delivered. They were competent at simple completions but could not hold context across a multi-step worker task. Every one of them felt like June 2025 frontier: impressive in isolation, unreliable under load.[^fn-june2025]

My workers do not answer one question and stop. They read a project file, understand where the previous agent left off, make a decision about what to do next, execute tool calls, check the result, and write an update before exiting. That requires sustained reasoning across a sequence of decisions, not single-turn Q&A. The open weight models I tested fell apart after two or three steps.

One Model rose above the rest. DeepSeek V4 Pro held the thread across the full worker cycle from the first test.

I moved my background worker to it on Friday morning and by the afternoon I was running production tasks through it.

## The Cheapest Reviewer

When you swap the model your agent system runs on, how do you know it is still working correctly? The problem is invisible: agents build things in a black box, and you are not watching every output. I had to know this was working before I could trust it, so I built evals into the system itself.

Every thirty minutes, Pi spawns three sub-agents in parallel to check that the primary worker is doing its job correctly: one running Claude Opus 4.7 (my reference standard), one running DeepSeek V4 Pro, and one running DeepSeek V4 Flash.[^1] Each reads the latest worker and heartbeat logs, evaluates whether the decisions are sound and the instructions are being followed, and reports back.[^fn-evals]

All three reviewers found only minor issues: the workers are doing fine on DeepSeek V4 Pro at about 10% of the cost of Opus. The sub-agent that picked up the most inconsistencies was Flash.

Flash surprised me: it is the smaller, cheaper variant, $0.14 per million input tokens and $0.28 per million output tokens.[^2] I expected the weakest reviewer but it was the most alert, catching edge cases the larger models glossed over.

{% include inline-image.html src="/assets/img/open-models-are-ready-comic.jpg" alt="Which model would you trust?" width="35%" %}

It is also a little overeager, like a junior developer: thorough and looking hard, but raising things that are not actually problems. That is a feature, not a bug. I would rather filter false positives than miss real ones. The lesson here is not just that cheap models can review. It is that cheap models with focused context — a clear job, specific success criteria, a narrow scope — outperform expensive general-purpose models on that job. Opus is trying to understand everything. Flash just needs to catch what looks off.

What happens when the reviewers disagree? You do not know which one is right, so you run more models. When Opus and Flash conflict on a call, I send a third arbiter, usually another Pro instance, to break the tie.

## What It Actually Costs

Yesterday came in at $47 on DeepSeek V4 Pro: workers, monitoring sub-agents, and some interactive coding alongside. The baseline for workers and monitoring on their own looks closer to $25-30 a day, but it is early and I want more runs before I trust the figures.[^3] That is still too much, even though it is a small fraction of the equivalent on Opus metered. Shifting more of the workload to Flash should bring it down, and I will know in a couple of weeks how much.

## Your Data Is Not Their Training Data

I access DeepSeek V4 Pro through OpenRouter rather than DeepSeek's own API. OpenRouter gives you a single endpoint that routes to multiple providers and handles billing. The killer feature for privacy-conscious setups is the **do not train** setting: in your OpenRouter account settings, turn off data sharing so your prompts and completions are not used for model training. DeepSeek's own API is cheaper by a notable margin but trains on your data by default. OpenRouter makes the privacy choice simpler and lets you switch between providers without changing your code.

If privacy is a hard requirement, look for OpenRouter providers that offer Zero Data Retention (ZDR). I use these for the same reason I wrote about in [Stop AI Stealing From You](/stop-ai-stealing-from-you/).

Pi made the rest of the migration straightforward. The extension model, where the agent writes its own NPM packages to add capabilities, meant I never had to fork the harness. I asked Pi to build an extension that prevents it from running commands I have flagged as irreversible decisions. It read my existing guidance, understood the pattern, and built it. When running as a bot it denies irreversible actions by default; when running interactively it asks first.[^4]

## Good Enough Changes Everything

I wrote about the open source cost argument in August last year, [Doing Real Work with AI Just Became 150x Cheaper](/doing-real-work-with-ai-just-became-150x-cheaper/), when OpenAI released their first open models and the economics flipped. At the time the argument was theoretical: the cost advantage was clear but the capability gap still required caveats.

George Hotz made the same point more sharply in April: frontier closed-source models cost at least 10x more to produce than the best open-weight alternatives, and the open models are only about six months behind on capability. At that gap-closure rate, any moat based on model quality depreciates within months.[^6]

For the work my system does, reading project notes, making bounded decisions, executing tool calls, writing updates, DeepSeek V4 Pro is good enough. And good enough at 10% of the cost changes the game.

The workers are done, and my interactive Claude Code use is tested on the same stack and ready to move when Max follows `claude -p` into metered pricing. The only reason my interactive work is still on Claude is that Max remains the cheapest option this month.

Thanks to Willem van den Ende for the [Pi setup guide](https://willemvandenende.com/blog/engineering/how-to-get-started-with-the-pi-coding-agent-on-a-vps) and the conversations that shaped this migration.

[^fn-evals]: I wrote about model evaluation and the need for continuous monitoring in [How to React to a New Frontier Model](/how-to-react-to-a-new-frontier-model/) last year. The same principle applies when you swap model families entirely.

[^fn-june2025]: I wrote about the state of AI tooling in June last year in [AI Needs More From You](/ai-needs-more-from-you/) — the landscape has changed faster than anyone expected. I ran a webinar that month and it's painful to look back at: the models stumbled on things the current generation handles easily, and the writing I could get with AI assistance was much worse than what comes out now. Sorry.

[^fn-pi-philosophy]: Pi ships with powerful defaults and explicitly skips features like plan mode and sub-agent displays. The philosophy, quoting Mario Zechner's design, is that "simplicity is achieved when there is nothing left to take away." The Agentic Harness Engineering paper showed Terminal-Bench scores improving from 69.7% to 77.0% through ten iterations of harness refinement alone, beating a human-designed baseline with fewer tokens. The latest Artificial Analysis Coding Agent Index measures model-plus-harness pairs rather than models in isolation, and finds cost per task varying by more than 30x across the same models in different harnesses. For engineering leaders the point is straightforward: the toolchain that gives you the most leverage is not the most expensive model but the most minimal harness.

[^1]: Pi does not have explicit sub-agent features in its UI, but I just got it to build a subagent module using the builtin template. It took about five minutes: one simple task agent that Pi spawns via its own extension system.

[^2]: DeepSeek V4 Flash pricing via the official API. At OpenRouter prices may vary slightly but remain in the same order of magnitude. Flash is the 284B total, 13B active parameter variant; Pro is the 1.6T total, 49B active parameter MoE.

[^3]: Throughput is roughly equivalent to what I was running on Claude Max: continuous worker polling, project scanning, and health checks across about a dozen active projects. The number bounces day to day depending on how much interactive coding runs alongside, so I am treating early figures as a ballpark.

[^4]: Pi's extension system is TypeScript distributed via NPM. You ask Pi to write the extension, it hot-reloads into the running session, and you iterate live. Most harnesses are built for the model to use. Pi is built to be extended by the model.

[^6]: George Hotz, "AI Has No Moat," April 2026. Hotz's broader argument is that the model layer itself is indefensible given the pace of open weight release. The harness layer, tools, orchestration, feedback loops, is where durable value accumulates.