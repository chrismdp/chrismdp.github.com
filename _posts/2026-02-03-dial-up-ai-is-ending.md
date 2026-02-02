---
layout: post
title: "Dial-Up AI Is Ending"
date: 2026-02-03 09:00:00 +0000
series: "Local AI"
image: /assets/img/dial-up-ai-comic.jpg
image_portrait: true
categories:
- ai
- local-ai
- economics
---

In the mid-90s, I remember horse-trading computer time with my sister. She wanted to call her friends; I wanted to get online. We had one phone line between us, and it was a zero-sum game that required constant negotiation and the occasional bribe.

When I won, I would count the minutes carefully, dialling up to Yahoo, doing what I needed, and disconnecting as quickly as possible. Every minute online was a minute my sister could not use the phone, and a minute on the bill my parents would notice. Being online was an *event* that you planned and rationed carefully. Streaming video, background downloads, always-on chat: these were fantasies for a future we could barely imagine.

Then broadband arrived, and everything changed. It was flat rate and always on, which meant the phone line was finally freed up. But the real shift was not that the internet got faster; it was that it became *unmetered*.

AI is about to have its broadband moment.

<!--more-->

## The Metered Mind

To be fair, we already have "unlimited" plans. Claude Max, ChatGPT Plus, and similar subscriptions are expensive but they allow unlimited usage for the cases we can imagine. For interactive work, the meter has effectively stopped.

But what else might we do if AI was truly unlimited? I have written before about how [real work with AI became 150 times cheaper](/doing-real-work-with-ai-just-became-150x-cheaper/) as open source models matured. That shift was about cloud pricing. The next shift is about ownership: when you run AI locally on hardware you already paid for, the meter stops entirely, and new possibilities open up.

## What Happens When the Meter Stops

A friend of mine, [Romilly Cocking](https://www.linkedin.com/in/romilly/){:target="_blank"}, is building something that would not even occur to you with a chat subscription. He has a Raspberry Pi with a DVB-T dongle receiving Freeview broadcasts, and Whisper transcribes every word from BBC News, twenty-four hours a day, seven days a week.

The elegance is that it is completely legitimate: just watching television and taking notes, automated, with no APIs, no authentication, and no terms of service concerns. "What was in the news this week?" becomes a semantic search over transcribed broadcasts.

Via cloud APIs, this would cost hundreds per month, but via local Whisper on a Raspberry Pi it costs nothing after the hardware. The idea only makes sense when AI is unmetered, and the point is not just the cost savings. Romilly never had to ask "is this worth it?" because the question stopped existing.

This is just one example, and we have no idea what will become possible when the constraints disappear entirely. When you stop counting, new categories of use become obvious.

**Speculative processing** becomes natural. You can summarise everything just in case, process your entire email archive, transcribe every meeting, and index every document. The "waste" becomes valuable because you never know what you will need, and you stop treating AI as something to be used sparingly and start treating it as ambient infrastructure.

**Exploratory experimentation** becomes free. "Let us see what happens if..." no longer carries budget anxiety, and you can try ten different approaches to a problem without worrying about which one is most token-efficient. The cost of being wrong drops to zero.

**Ambient AI** becomes possible. Voice assistants that do not cost per query, background agents monitoring and processing, AI that runs continuously rather than on-demand: the model that seemed wasteful yesterday becomes obvious tomorrow.

## The Counterintuitive Economics

Per-token, local inference is more expensive than cloud inference. Cloud providers batch requests across thousands of users, sharing the cost of loading model weights into memory. Your Raspberry Pi runs batch-size-one, bearing the full cost alone.[^piotr]

But you have already paid for the hardware, there is no meter running, and the "expensive" tokens are free.

This is exactly the dial-up to broadband dynamic. Per-minute, dial-up was probably cheaper than the monthly broadband fee divided by your actual usage. But the flat rate changed everything because you stopped counting. The psychological shift mattered more than the economics.

The same shift is happening with AI. When you own the hardware, the marginal cost drops to electricity. You stop asking "should I use AI for this?" and start asking "why would I not?"

## The Closing Gap

The gap between local and cloud model quality is shrinking fast. [AI progress is not slowing down](/ai-progress-is-not-slowing-down/) the way sceptics claim. Every few months, a new open model matches what was state-of-the-art a year ago. DeepSeek, Qwen, Llama, and now OpenAI's own open source releases are converging on frontier performance.

To be clear, running the absolute frontier locally still requires serious hardware. Kimi K2.5, the trillion-parameter thinking model from Moonshot AI, needs at least eight H100 GPUs to run in quantised form, or fourteen for full precision.[^kimi] A single DGX H100 unit with eight GPUs costs around four hundred thousand dollars including electricity and cooling over six years. But the point is not that frontier models run on Raspberry Pis; the point is that useful models already do. Whisper handles transcription, Llama handles text, and Stable Diffusion handles images. You do not need frontier performance for continuous background processing, just good enough performance at zero marginal cost.

When state-of-the-art equivalent models run on commodity hardware, every cost-prohibitive use case becomes viable. The interesting applications will not be "do the same things cheaper." They will be entirely new categories that we cannot justify today, the same way always-on video calls and background downloads were unjustifiable in the dial-up era.

## Stop Counting

The shift is already happening for those paying attention. [I predicted](/my-ai-predictions-for-2026/) that Chinese models would reach frontier levels in 2026, enabling cheap API access for cost-sensitive applications. Local models are even cheaper than that.

The mindset change matters more than the technology. Stop thinking about AI as a service you pay per use and start thinking about it as infrastructure you own. The use cases that seem wasteful today, like continuous transcription, speculative processing, and ambient AI, become obvious when the meter stops running.

Unmetered internet gave us social media, video on demand, and an explosion of content so vast that it birthed the large language models we use today. What will unmetered AI give us?

We are limited only by our imagination.

[^piotr]: For more on why batch size matters for inference economics, see Piotr Mazurek's [LLM Inference Economics from First Principles](https://blog.basingse.ai/p/the-economics-of-ai-inference){:target="_blank"}.

[^kimi]: Kimi K2.5 is a one trillion parameter mixture-of-experts model that activates 32 billion parameters per token across 384 experts. Full precision requires approximately 500GB of VRAM for model weights alone, leaving limited headroom for the KV cache needed during inference. See Caleb Bryce's breakdown of [the total cost of ownership for running state-of-the-art models locally](https://www.youtube.com/watch?v=SmYNK0kqaDI){:target="_blank"} for detailed calculations.
