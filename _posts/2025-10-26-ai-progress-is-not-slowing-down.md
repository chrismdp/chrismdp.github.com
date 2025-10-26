---
layout: post
title: "It Feels AI Progress Is Slowing Down. It Isn't"
date: 2025-10-26 09:00:00 +0000
image: /assets/img/metr-time-horizon-chart.png
categories:
- ai
- industry
- analysis
---

*AI's ability to complete longer software engineering tasks has been doubling roughly every seven months, reaching approximately two hours by 2025. Source: METR*

When GPT-5 launched, Reddit exploded with disappointment. One paying customer called it "the biggest piece of garbage" they had ever seen. Within hours, OpenAI's CEO held an emergency Q&A to defend the model's performance. Gary Marcus summarised it as "overdue, overhyped and underwhelming." Technical founders declared AI had plateaued, engineering leaders dismissed the release as underwhelming, and some began abandoning their AI implementations entirely.

The same week, whilst people were declaring the end of progress, two measurement systems told a completely different story. METR published data showing GPT-5's time-horizon for completing software engineering tasks had doubled from roughly 30 minutes to 2 hours, continuing an exponential trend that has seen this metric double approximately every seven months since 2019.[^metr-blog] [^metr-paper] GDPval, which has industry experts blind-grade AI deliverables for actual tasks across 44 occupations, showed frontier models now approach expert quality, with performance more than doubling from GPT-4o to GPT-5 in roughly a year.[^gdpval] These were not 10% bumps on benchmark scores but fundamental expansions in the complexity and duration of work models could reliably complete.

The gap between what the data shows and what people believe is one of the most consequential misunderstandings in technology right now. Not because the sceptics are wrong to notice something feels different, but because they are measuring the wrong things at precisely the moment when incremental improvements are compounding into breakthrough capabilities. The question is not whether progress is happening but why it feels like it is not.

<!--more-->

## Why Progress Feels Like Stagnation

### We Are Measuring the Wrong Things

Traditional benchmarks measure performance on maths problems, coding challenges, and academic exams. These metrics dominated AI evaluation for years because they were easy to track and compare. Each generation scored higher than the last (GPT-4 over GPT-3.5, GPT-5 over GPT-4), and progress looked linear and predictable.

Then these benchmarks started saturating. Models began hitting ceiling effects on popular tests. The Massive Multitask Language Understanding benchmark, once a key measure of progress, now sees frontier models approaching human-expert scores with diminishing headroom for gains. Incremental improvements yield smaller returns. The obvious conclusion: we are hitting limits.

This conclusion feels intuitive because some limits are genuinely real. We are approaching fundamental constraints that make continued scaling harder. The world contains roughly 300 trillion tokens of high-quality human text suitable for training. At current consumption rates, frontier models will exhaust essentially all available internet text by 2026-2032.[^data-limits] Training on AI-generated content to continue scaling leads to model collapse, where models progressively lose nuance and misperceive reality as errors compound across generations.[^model-collapse] The easy gains from throwing more data at larger models are genuinely diminishing.

The critical mistake is conflating these real constraints on one dimension of progress (raw model scale and benchmark performance) with overall progress on what actually matters for deployment.

A model that scores 5% higher on coding tests but still makes the same frustrating mistakes in production does not feel meaningfully better. When developers shrug at new releases despite higher benchmark scores, they are not wrong to notice the disconnect. They are just measuring performance (test scores) instead of competence (reliable completion of real work).

This is the **performance versus competence gap**, and it explains the blasé attitude perfectly.

GDPval and METR target competence directly. Can the model reliably complete messy, multi-step, real-world work? The answer, measured properly, shows steady exponential progress even as traditional benchmarks plateau.[^gdpval] [^metr-blog] [^metr-paper] We are hitting real limits on one type of scaling whilst experiencing exponential progress on another. We are measuring the wrong things and then declaring progress has stopped.

### Breakthroughs Arrive as Thresholds, Not Smooth Curves

Consider an AI handling a workflow with ten sequential steps, each requiring an independent decision. If each step succeeds 70% of the time, the entire workflow completes successfully only about 3% of the time. Bump that per-step reliability to 85%, and suddenly the end-to-end success rate jumps to 20%. Push it to 95%, and you hit 60% completion.

This is not linear improvement but crossing a threshold where a workflow flips from "fails constantly" to "works most of the time."

When reliability improvements push workflows from 40% success to 60% success, that might cross the viability threshold for production deployment. But it does not create obvious "this is so much smarter" moments in casual conversation. The model still makes mistakes. It just makes fewer of them in ways that matter for multi-step tasks.

This explains why companies often report sudden breakthroughs with AI tools. They are not experiencing smooth capability curves. They are hitting thresholds where compounding reliability crosses into viability for their specific workflow.

The danger is walking away at 40% success, unaware that you are one reliability improvement from 60% success and production viability. The incremental improvement feels pointless until it suddenly is not.

### The Improvements Are Invisible

The technical innovations driving threshold crossings are less about making models "smarter" in ways that show up in casual conversation, and more about making them reliably complete multi-step tasks. Progress has shifted from raw scale to engineering across the entire stack.

**Test-time compute for reasoning.** Models now allocate "thinking time" before responding, using reinforcement learning to determine how to use that time effectively. Performance improves both with more training and with more time spent thinking.[^o1] Systems like Claude's "extended thinking" feature let you toggle a thinking budget to trade latency for reliability.[^extended-thinking] [^think-tool] But there is nuance here: research has identified five failure modes when models reason longer, including distraction by irrelevant details and overfitting to spurious patterns.[^reasoning-failures] Extended reasoning can help or hurt depending on task complexity. The innovation is not just allowing longer thought, but training systems to allocate reasoning time strategically.

**Agentic tool use and verification.** Instead of generating a complete answer in one go, models can now call external tools, check their work, and retry when something fails. This converts brittle text generation into plans plus actions plus verification loops. Research like Meta's Toolformer showed that many LLM limitations can be overcome not by scaling models larger, but by giving them access to calculators, search engines, and domain-specific APIs.[^toolformer] METR explicitly attributes time-horizon gains to improved tool use and error recovery.[^metr-paper] Retrieval-augmented generation systems pair models with external knowledge bases, addressing both knowledge cutoffs and hallucinations by letting models query information on the fly rather than memorising everything during training. The challenge is context pollution, where retrieving too much irrelevant information degrades performance, requiring careful filtering and relevance ranking.

**Self-verification and reflective reasoning.** Models are gaining the ability to critique and refine their own outputs. Self-consistency techniques generate multiple solutions and pick the most common result. More sophisticated systems like GeneAgent implement four-stage cycles: generation, self-verification against domain databases, correction, and summary.[^self-verification] This metacognitive approach catches hallucinations and enforces evidence-based claims, dramatically improving factual accuracy without requiring larger base models. The overhead is latency and compute, but selective application to high-stakes queries makes it practical.

**Sparse expert routing.** Mixture-of-Experts architectures activate only a subset of parameters for each token, allowing much higher capacity at similar latency and cost. Recent MoE implementations achieve roughly 2.5× parameter efficiency, matching dense 7B model performance with only 2.8B active parameters per token.[^moe-efficiency] This decouples total model capacity from computational cost, enabling models to scale knowledge breadth without proportional runtime increases. Combined with techniques like Gemini 1.5's approach,[^gemini-moe] this delivers better competence at the same price point, which feels like no improvement if you are not tracking costs.

**Long-context capabilities.** Models can now maintain and retrieve information from increasingly large working sets, reducing failures on multi-document or multi-hour tasks. Position encoding advances like LongRoPE extend usable context towards the multi-million-token regime.[^longrope] Early models handled thousands of tokens; current systems manage hundreds of thousands. This enables new categories of work like analysing entire codebases or maintaining conversation state across hours-long sessions, though attention mechanisms' quadratic scaling still imposes practical limits.

**Infrastructure and efficiency improvements.** Speculative decoding delivers 2-3× faster generation whilst matching base model quality.[^speculative] PagedAttention increases throughput 2-4× through better memory management.[^paged-attention] FlashAttention-2 doubles attention speed whilst reducing memory usage.[^flash-attention] Low-precision arithmetic (8-bit and 4-bit quantization) cuts inference costs substantially without meaningful quality loss,[^nvfp4] making frontier models deployable on fewer GPUs. NVIDIA's H100 provides roughly 3-4× faster training and inference throughput compared to previous generation accelerators.[^h100-performance] Model distillation compresses large models into smaller ones whilst preserving most capability. These engineering advances make existing model architectures dramatically cheaper and faster to deploy, effectively extending the runway of current approaches.

You cannot easily demo "look how much faster the attention kernel is" or "see how we route to sparse experts." These improvements show up in reliability, throughput, and cost, not in conversation quality. But together they push per-step reliability past the threshold where entire categories of work become viable. More importantly, they enable the exponential competence gains measured by GDPval and METR even as traditional benchmarks plateau.

### We Warped Our Sense of Time

The cadence of major releases has been remarkably consistent: GPT-3 in June 2020, GPT-4 in March 2022, GPT-5 in late 2024. Roughly two years between each.

But that is not how it felt.

ChatGPT launched in November 2022, more than two years after GPT-3. It used GPT-3.5, which was not fundamentally more capable than GPT-3 but was packaged in an interface that made AI accessible to everyone. The cultural moment was so explosive that it compressed our sense of time. GPT-3 had been quietly improving for years. We just did not notice until ChatGPT made it undeniable.

This created a warped baseline. We expect ChatGPT-level shocks every few months. When steady two-year cycles continue delivering improvements, they feel slow by comparison. We recalibrated expectations based on a compressed moment, then declared the natural cadence a slowdown.

The novelty wore off. Once you have a fluent conversational AI, making it more reliable or faster or cheaper does not produce the same shock. But those "boring" improvements compound into order-of-magnitude shifts in what is economically viable.

## What Is Actually at Stake

The perception gap shapes investment decisions, hiring strategies, and product roadmaps across the industry. When people believe AI has plateaued whilst it is actually crossing reliability thresholds into new categories of viable work, they abandon promising approaches one improvement away from viability. When they cargo-cult the bubble narrative, they swing from believing AI will solve everything to believing it will solve nothing. Both positions miss the actual story: incremental reliability improvements compounding into breakthrough capabilities for specific workflows.

The companies making good decisions track the right metrics: not "does this feel smarter in casual conversation" but "can this reliably complete economically valuable multi-step tasks." Training compute for frontier models has grown roughly 4-5× per year through 2024,[^compute-trends] but algorithmic efficiency improvements have been halving the compute required approximately every eight months.[^algorithmic-progress] We are not in a holding pattern waiting for new models but in a phase where progress comes from engineering across the entire stack. GDPval and METR measure the combined effect, and both show exponential progress continuing.[^gdpval] [^metr-blog] [^metr-paper]

## What This Means for You

Stop expecting revolutionary leaps every quarter. Start tracking time-horizons for economically valuable work in your domain. Deploy AI where threshold effects have already crossed viability. Monitor adjacent categories where another 20% reliability improvement might flip workflows from broken to viable.

The perception gap itself is the story. We are living through continuous exponential improvement in AI's ability to complete real work whilst simultaneously feeling like progress has stalled because casual conversations do not feel dramatically different. GDPval shows expert-level work quality more than doubling in a year, METR shows task time-horizons doubling every seven months, and infrastructure innovations are pushing reliability past viability thresholds. But these improvements arrive as invisible systems work and threshold crossings rather than flashy conversational breakthroughs.

Progress has not slowed down. It crossed a threshold where the improvements that matter most are invisible to casual observation but transformative for production deployment. The question is whether you are measuring the right things to see it.

[^gdpval]: See [Measuring the performance of our models on real-world tasks](https://openai.com/index/gdpval/){:target="_blank"}. GDPval evaluation framework showing frontier models approaching expert quality with >2× improvement from GPT-4o to GPT-5.

[^metr-blog]: See [Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/). Blog post introducing time-horizon measurement showing exponential growth in task completion capability.

[^metr-paper]: See [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499){:target="_blank"}. Academic paper showing time-horizon doubling approximately every 7 months, driven by reliability, error recovery, reasoning, and tool use.

[^o1]: [Learning to reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/){:target="_blank"}. OpenAI o1 technical report showing performance improvements with both more training and test-time compute ("thinking time").

[^extended-thinking]: [Claude's extended thinking](https://www.anthropic.com/news/visible-extended-thinking){:target="_blank"}. Introduction of thinking budget toggle in Claude 3.7 Sonnet, trading latency for reliability.

[^think-tool]: [The "think" tool: Enabling Claude to stop and think](https://www.anthropic.com/engineering/claude-think-tool){:target="_blank"}. Technical explanation of explicit thinking tool for reducing mistakes during multi-step reasoning.

[^speculative]: [Looking back at speculative decoding](https://research.google/blog/looking-back-at-speculative-decoding/){:target="_blank"}. Retrospective on speculative decoding achieving 2-3× faster inference without quality loss.

[^flash-attention]: [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691){:target="_blank"}. Paper describing ~2× faster attention kernels with improved memory efficiency.

[^paged-attention]: [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180){:target="_blank"}. vLLM paper showing 2-4× throughput improvements via KV-cache paging and sharing.

[^longrope]: [LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens](https://arxiv.org/html/2402.13753v1){:target="_blank"}. Position encoding technique extending usable context to multi-million-token regime.

[^gemini-moe]: [Introducing Gemini 1.5, Google's next-generation AI model](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/){:target="_blank"}. Announcement of Gemini 1.5 using Mixture-of-Experts for efficient training and serving.

[^algorithmic-progress]: [Algorithmic Progress in Language Models](https://arxiv.org/pdf/2403.05812){:target="_blank"}. Epoch AI research showing algorithmic efficiency improvements halving required compute approximately every 8 months.

[^compute-trends]: [Machine Learning Trends](https://epoch.ai/trends){:target="_blank"}. Dataset tracking frontier training compute growth at roughly 4-5× per year through 2024.

[^nvfp4]: [Introducing NVFP4 for Efficient and Accurate Low-Precision Inference](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/){:target="_blank"}. Technical introduction to 4-bit inference on Blackwell-generation GPUs with near-FP8 quality.

[^data-limits]: [Will we run out of data? Limits of LLM scaling based on human-generated data](https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data){:target="_blank"}. Analysis estimating ~300 trillion tokens of quality training data, potentially exhausted by frontier models between 2026-2032.

[^model-collapse]: [AI models collapse when trained on recursively generated data](https://www.nature.com/articles/s41586-024-07566-y){:target="_blank"}. Research demonstrating how training on AI-generated content causes models to progressively lose distributional accuracy and nuance.

[^reasoning-failures]: [Longer reasoning can mislead LLMs](https://www.anthropic.com/research/longer-reasoning-can-mislead){:target="_blank"}. Study identifying five failure modes when models reason longer, including distraction and spurious pattern overfitting.

[^toolformer]: [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761){:target="_blank"}. Meta research showing LLM limitations addressed through API access to calculators, search engines, and domain tools rather than scaling alone.

[^self-verification]: [GeneAgent: Self-verification in LLM-based automatic literature mining for gene function](https://www.nature.com/articles/s41467-024-52851-2){:target="_blank"}. System implementing generation-verification-correction cycles to catch hallucinations and enforce evidence-based claims in biomedical domain.

[^moe-efficiency]: [Mixture-of-Experts Meets Instruction Tuning](https://arxiv.org/abs/2305.14705){:target="_blank"}. Research showing MoE achieving ~2.5× parameter efficiency, matching dense 7B performance with 2.8B active parameters.

[^h100-performance]: [NVIDIA H100 Tensor Core GPU](https://www.nvidia.com/en-us/data-center/h100/){:target="_blank"}. Technical specifications showing 3-4× training and inference throughput improvements over A100 generation.
