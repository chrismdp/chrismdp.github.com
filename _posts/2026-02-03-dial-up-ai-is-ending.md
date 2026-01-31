---
layout: post
title: "Dial-Up AI Is Ending"
date: 2026-02-03 09:00:00 +0000
series: "Local AI"
image: /assets/img/dial-up-ai-motif.jpg
infographic: /assets/img/dial-up-ai-comic.jpg
categories:
- ai
- local-ai
- economics
---

I remember horse-trading computer time with my sister. She wanted to call her friends; I wanted to get online. Same phone line, zero-sum game.

When I won, I would count the minutes carefully. Dial up to AOL, do what I needed, disconnect. Every minute online was a minute my sister could not use the phone, a minute on the bill my parents would notice. Being online was an *event*. You planned it. You rationed it. Streaming video? Absurd. Background downloads? Wasteful. Always-on chat? A fantasy.

Then broadband arrived. Flat rate. Always on. The phone line freed up. Everything changed, not because the internet got faster, but because it became *unmetered*.

AI is about to have its broadband moment.

<!--more-->

## The Metered Mind

Right now, we use AI surgically. We craft prompts carefully. We justify each task. Cost anxiety hovers over every request. "Is this worth the tokens?" We think twice before asking Claude to do something speculative, before running an experiment that might not work.

This shapes what we build. We optimise for token efficiency. We batch requests. We treat AI as a scarce resource to be rationed rather than infrastructure to be used freely.

I have written before about how [real work with AI became 150 times cheaper](/doing-real-work-with-ai-just-became-150x-cheaper/) as open source models matured. That shift was about cloud pricing. The next shift is about ownership: when you run AI locally on hardware you already paid for, the meter stops entirely.

## What Happens When the Meter Stops

A friend of mine, [Romilly Cocking](https://www.linkedin.com/in/romilly/){:target="_blank"}, is building something that would be absurd with per-token billing. He has a Raspberry Pi with a DVB-T dongle receiving Freeview broadcasts. Whisper transcribes every word from BBC News. Twenty-four hours a day, seven days a week.

The elegance is that it is completely legitimate. Just watching television and taking notes, automated. No APIs, no authentication, no terms of service concerns. "What was in the news this week?" becomes a semantic search over transcribed broadcasts.

Via cloud APIs, this would cost hundreds per month. Via local Whisper on a Raspberry Pi, it costs nothing after the hardware. The idea only makes sense when AI is unmetered. The point is not just the cost savings. The point is that Romilly never had to ask "is this worth it?" The question stopped existing.

When you stop counting, new categories of use become obvious.

**Speculative processing** becomes natural. Summarise everything, just in case. Process your entire email archive. Transcribe every meeting. Index every document. The "waste" becomes valuable because you never know what you will need. You stop treating AI as something to be used sparingly and start treating it as ambient infrastructure.

**Exploratory experimentation** becomes free. "Let us see what happens if..." no longer carries budget anxiety. You can try ten different approaches to a problem without worrying about which one is most token-efficient. The cost of being wrong drops to zero.

**Ambient AI** becomes possible. Voice assistants that do not cost per query. Background agents monitoring and processing. AI that runs continuously rather than on-demand. The model that seemed wasteful yesterday becomes obvious tomorrow.

## The Counterintuitive Economics

Per-token, local inference is more expensive than cloud inference. Cloud providers batch requests across thousands of users, sharing the cost of loading model weights into memory. Your Raspberry Pi runs batch-size-one, bearing the full cost alone.[^piotr]

But you have already paid for the hardware. There is no meter running. The "expensive" tokens are free.

This is exactly the dial-up to broadband dynamic. Per-minute, dial-up was probably cheaper than the monthly broadband fee divided by your actual usage. But the flat rate changed everything because you stopped counting. The psychological shift mattered more than the economics.

The same shift is happening with AI. When you own the hardware, the marginal cost drops to electricity. You stop asking "should I use AI for this?" and start asking "why would I not?"

## The Closing Gap

The gap between local and cloud model quality is shrinking fast. [AI progress is not slowing down](/ai-progress-is-not-slowing-down/) the way sceptics claim. Every few months, a new open model matches what was state-of-the-art a year ago. DeepSeek, Qwen, Llama, and now OpenAI's own open source releases are converging on frontier performance.

To be clear, running the absolute frontier locally still requires serious hardware. Kimi K2, the trillion-parameter model from Moonshot AI, needs four A100 80GB GPUs and 512GB of RAM to run at full precision.[^kimi] That is enterprise hardware worth tens of thousands of pounds. But the point is not that frontier models run on Raspberry Pis. The point is that useful models already do. Whisper handles transcription. Llama handles text. Stable Diffusion handles images. You do not need frontier performance for continuous background processing. You need good enough performance at zero marginal cost.

When state-of-the-art equivalent models run on commodity hardware, every cost-prohibitive use case becomes viable. The interesting applications will not be "do the same things cheaper." They will be entirely new categories that we cannot justify today, the same way always-on video calls and background downloads were unjustifiable in the dial-up era.

## Stop Counting

The shift is already happening for those paying attention. [I predicted](/my-ai-predictions-for-2026/) that Chinese models would reach frontier levels in 2026, enabling cheap API access for cost-sensitive applications. Local models are even cheaper than that.

The mindset change matters more than the technology. Stop thinking about AI as a service you pay per use. Start thinking about it as infrastructure you own. The use cases that seem wasteful today, continuous transcription, speculative processing, ambient AI, become obvious when the meter stops running.

The question to ask yourself is not "what can I afford to use AI for?" It is "what would I build if AI cost nothing?"

Because for practical purposes, it already does.

[^piotr]: For more on why batch size matters for inference economics, see Piotr Mazurek's [LLM Inference Economics from First Principles](https://blog.basingse.ai/p/the-economics-of-ai-inference){:target="_blank"}.

[^kimi]: See the [Kimi K2 deployment guide](https://kimi-k2.org/blog/02-deployment-guide-en){:target="_blank"} for full hardware requirements. The model weights alone are 1.8TB.
