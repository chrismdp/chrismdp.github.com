---
layout: post
title: "Webinar: Escape the Great AI Lock-In"
date: 2026-06-04 14:00:00 +0100
categories:
- ai
- webinar
- leadership
- strategy
image: /assets/img/escape-the-great-ai-lock-in-webinar.jpg
image_portrait: true
series: "AI In Action Webinars"
description: "The flat-rate AI era is ending. Cheap tokens, metered pricing, and how local and open-source models let technical leaders escape dependence on frontier AI they do not control."
---

On 4 June 2026, I gave a webinar about the moment cheap AI stops being cheap. One team I spoke to recently was handed a $10,000 monthly token budget by their management and blew through the whole thing in a day and a half. For two years AI has felt magical and effectively free, and we have quietly built our workflows on that feeling. The meter is coming back on, and the workflows we built are more exposed than they look.

<!--more-->

## What's changed

When I started, a useful AI subscription cost fifteen or twenty dollars a month. Then OpenAI launched a £150 a month plan and I remember thinking that was an absurd amount to spend on AI. I now pay for about three of those, somewhere north of £700 a month just for my own use, and somehow that feels fine. What has not changed is the structure underneath: most of us are still paying a flat monthly fee while the true cost of what we are doing climbs out of sight.

The thing that crystallised it for me was Anthropic changing Claude Max. They raised the interactive limits, currently 50% higher than usual, so it is hard to max out your Max plan by chatting. But they also started metering *programmatic* usage: anything you run from the command line, through the SDK, or in an automated loop. You get roughly $200 of free credits a month, which for my own workflows would last about an hour and a half. After that, you pay per token.

Unmetered became metered, and that is the whole story in miniature. If you are on a team or enterprise plan, you noticed this months ago, because those have always been metered, they just had a honeymoon period while everyone was still learning the tools and usage was low. The moment you use these tools the way they are meant to be used, you burn ten or a hundred times more tokens, and the bill follows.

![A taxi fare meter clocking up the year, little robots polishing it: the meter just came back on for AI.](/assets/img/the-meter-came-back-on-slide.jpg)

I pulled my own numbers to make it concrete. Last month, on one machine, with a couple of weeks off for the bank holidays, I racked up about $5,000 of equivalent Claude usage. My heaviest single day was around $300 to $400. One weekend, building a small side project while not even sitting at my desk, just prompting at odd moments and running a few [Ralph loops](https://chrismdp.com/running-ralph-in-production), came to $540 of effective use. I do not actually pay that, because I am on the flat Max plan. But that is the number staring back at me if the flat plan goes away. At the moment you can still run Codex in a genuinely unmetered way. I do a lot of that. I fully expect it to disappear too. Uber has already hit this problem: after Bloomberg reported that it burned through its 2026 AI coding budget in four months, the company capped agentic coding tools at $1,500 a month per employee per tool.[^uber]

## Cheap tokens hid the real problem

While tokens were effectively free, none of this mattered. You could experiment, waste tokens, and feel productive. Developers self-report being three to twenty times faster, and individually that is often true. But team throughput, across almost every measure I have seen, stays flat. The old DORA research[^dora] showed only a small slice of teams turning AI into more frequent, more stable releases. Everyone else saw a flat line.

The reason is that AI speeds up one step while every other delay stays exactly where it was. You still wait for sign-off. You still wait for information, for connectors, for the second reviewer. Getting your bit done faster does not make the organisation faster; it just moves the bottleneck and makes it more visible. I have [written](https://chrismdp.com/always-be-unblocking) and [spoken about theory of constraints at length](https://chrismdp.com/webinar-unblock-your-team), and this is the same lesson wearing a new hat.

This was a harmless curiosity when AI cost tens of dollars per person, but it becomes a board-level conversation when it costs thousands. A CFO is entirely right to ask whether to spend that money on an unproven technology or hire more people, and right now we do not have a clean way to demonstrate the return. That is exactly why, when I run training, I survey teams before and after, and spend most of the time on how the *team* captures value rather than how an individual goes faster. If all your people learn to do is ship more, you will have no credible answer when the tokens get expensive.

## Lock-in is bigger than the bill

Cost is only the obvious face of lock-in. Two others matter more over time.

The first I call the AI God problem, and I [wrote about it recently](https://chrismdp.com/i-dont-want-an-ai-god). The logical thing to do is funnel everything into one big, all-knowing assistant that has access to all your tools and context. What you get is a single sprawling system that is hard to relate to, hard to reason about, and impossible to swap out. You stop experimenting because experimenting is expensive, and you end up shaped by one vendor's idea of how AI should be used.

![A glum robot locked in a birdcage holding a sign reading "The Anthropic Way (+ Codex)": locked into one vendor's way of working.](/assets/img/locked-into-the-anthropic-way-slide.jpg)

When you adopt a model you are buying more than a tool, you are buying an ideology: a set of values and a worldview baked into the weights, which you then drip-feed into everything your company produces. Your people start writing like the model. The model's way of seeing the world becomes your house style. That is not necessarily a problem, but it is something to be awake to, and it is part of [the slow loss of self](https://chrismdp.com/the-slow-and-dangerous-loss-of-self) I worry about. Honestly, what I would love is a UK model with UK values. We do not have one yet.

And switching is harder than it feels. Zapier found[^zapier] that 89% of executives believed they could change AI vendors within four weeks, 41% reckoning two to five business days. But of the two-thirds who had actually attempted a migration, 58% said it either failed outright or took far more effort than expected. It is never just an API migration. Your context, your workflows, your institutional memory and your training are all tangled into the tool you chose. You are probably already more locked in than you think.

## Open models are closer than they look

Open models are not as far behind as the gap feels. On benchmarks they lag the frontier by roughly four to eight months, and benchmarks flatter them, but my own month of heavy use lines up with that. DeepSeek's flash model feels about a year behind a frontier model, and it is only a flash model. DeepSeek Pro feels like where the frontier was last September or October. Something clicked at the end of November 2025 when Opus 4.5 crossed a threshold and AI felt much better; open models are not there yet, but there is every reason to expect a similar tipping point for them. By April, roughly one in three teams was running some kind of open model, and Google has now shipped Gemma 4 as a 12B multimodal open model with quantisation-aware checkpoints designed for mobile and laptop hardware.[^gemma12b][^gemmaqat]

"Local" just means open-weight models you can realistically download and run yourself. To run something near the open frontier you want about 48GB of RAM at the floor and really 128GB to be comfortable. But the smartest model you can run on a laptop has improved nearly fivefold in two years, faster than Moore's Law.[^moore] Nvidia is pushing the same shift from data centre to desktop; The Economist describes Jensen Huang's AI strategy as coming to the PC.[^nvidia] Small models also need a harness: strong rules, skills and prompting wrapped around them. Evaluation is getting easier too: Google is making Kaggle benchmarks runnable locally, because open models only help when you can prove which workflows they can safely carry.[^kaggle]

{% include inline-image.html src="/assets/img/harness-small-model-beats-frontier-slide.jpg" alt="A small robot driving a powered mech suit, knocking out a much larger frontier robot." align="center" width="100%" caption="We are far better at building harnesses than we were a year ago, and a well-harnessed flash model can do real work." %}

How far does this go? Tomasz Tunguz ran 1,400 agentic tasks over five weeks, split between a local model on his MacBook and Claude Opus.[^tunguz] Roughly half of his daily work ran correctly on the local model, at effectively zero marginal cost and 2.1 times the speed. The catch: it was the lower-complexity work like email triage, scheduling, summarising and admin, not architecture or deep research. That matches my own setup, where I run email triage on a local model but would not dream of using it for nuanced vault work. It is a direction of travel rather than a finished destination. When laptops refresh on their natural cycle over the next two or three years, this capability arrives almost by osmosis.

## What to do about it

You do not need to buy everyone a gaming rig, you need to stop being trapped. A few moves I would make now.

Put one or two people on open models as part of their actual job, always pushing on what is now possible with Minimax 3, GLM 4.6, Kimi or DeepSeek, and working out the ROI of renting your own GPUs. Running DeepSeek Pro on reserved cloud GPUs costs roughly $25 an hour; spread across a team, that can be far cheaper than per-seat frontier subscriptions, and far more flexible.

Then do the sums. If a slightly-less-capable but much cheaper open model can carry most of a developer's routine work, and you have 400 developers, a 10% to 90% saving per head is a real number. The same logic applies outside engineering: an open model behind a tool like Goose may beat going all-in on whatever your big vendor bundles.

{% include inline-image.html src="/assets/img/my-little-telegram-bots.png" alt="A Telegram chat list showing six of my single-purpose bots, each reporting on its own job." align="right" width="40%" %}

The real prize in all of this is that owning your AI setup, rather than renting one vendor's way of working, is what lets you experiment. Once you are not locked in, you can run different models, swap them when one gets expensive or slow, and build your own small tools instead of pouring everything into one assistant. This week I put that freedom to work and built myself six little bots, each doing one job: content publishing, keeping an eye on the other bots, email triage, consolidating saved links into my vault, reconciling my accounts, and tidying my project notes. They all run through a layer that lets me switch model providers via [Open Router](https://chrismdp.com/open-models-are-ready), so my email triage runs on DeepSeek while other work runs on Codex. I will have more to say about running a fleet of small bots another time; for now it is the individual end of the [I Don't Want an AI God](https://chrismdp.com/i-dont-want-an-ai-god) argument made concrete. I am not sure six little bots is the right shape, and I may yet change my mind. But because I am not locked in, I can branch out and try more things. None of us knows yet how any of this will play out, and that is exactly why the right to keep learning is worth protecting: it is the first thing you hand over when you commit to a single vendor's single way of working.

One last warning: people lose the skills they stop using. Be careful you do not let your team forget how to do the very things a vendor will later charge you a fortune to do for them.

## Key takeaway to remember

Cheap, unlimited frontier tokens feel like the floor you build on. They are a rental, and the landlord is about to put the rent up. If your competitive advantage depends on tokens you do not control, you do not own that advantage. The hedge is to know, before you are forced to find out, which of your workflows are locked to the frontier and which could run on open models you control.

## One thing to try this week

Pick your single most token-hungry workflow, the one you would never dare run if the meter were ticking, and do two things with it. First, price it as if the meter were already on: roughly what would one run cost at per-token rates? Second, run it once on an open model (a hosted DeepSeek through Open Router, or a local model if you have the RAM) and see how close it gets. Nothing needs migrating this week. The point is simply to learn, while it is still cheap to learn, which of your workflows you actually own.

[^dora]: Google's DORA programme, [2024 Accelerate State of DevOps Report](https://dora.dev/research/2024/dora-report/).

[^zapier]: Zapier, ["AI vendor lock-in survey"](https://zapier.com/blog/ai-vendor-lock-in-survey/), based on 542 US C-level executives with active paid AI contracts, surveyed late January to early February 2026.

[^uber]: Simon Willison, ["Uber Caps Usage of AI Tools Like Claude Code to Manage Costs"](https://simonwillison.net/2026/Jun/3/uber-caps-usage/), citing Bloomberg reporting that Uber burned through its 2026 AI coding budget in four months and introduced a $1,500 monthly cap per employee per agentic coding tool.

[^moore]: ["Two Years of Local AI on a Laptop: When Open Models Outpaced Moore's Law"](https://huggingface.co/blog/mishig/local-moores-law). The smartest open-weight model on a 128GB MacBook Pro rose from a score of 10 (Llama 3 70B, May 2024) to 47 (DeepSeek V4 Flash, May 2026) on unchanged hardware.

[^gemma12b]: Google, ["Introducing Gemma 4 12B: a unified, encoder-free multimodal model"](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/), 3 June 2026.

[^gemmaqat]: Google, ["Gemma 4 QAT models: Optimizing model compression for mobile and laptop efficiency"](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/), 5 June 2026.

[^nvidia]: The Economist, ["Nvidia wants to supercharge your laptop"](https://www.economist.com/business/2026/06/02/nvidia-wants-to-supercharge-your-laptop), 2 June 2026.

[^kaggle]: Google, ["Kaggle is making AI benchmark creation effortless"](https://blog.google/innovation-and-ai/technology/developers-tools/build-kaggle--benchmarks-locally/), 4 June 2026.

[^tunguz]: Tomasz Tunguz, ["Localmaxxing"](https://tomtunguz.com/localmaxxing/), 11 May 2026: 1,400 tasks tracked over five weeks, roughly half succeeding on a local 35B model at a 2.1x speed-up over Opus 4.5.
