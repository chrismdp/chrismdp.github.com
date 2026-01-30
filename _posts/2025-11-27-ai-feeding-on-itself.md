---
layout: post
title: "AI Slop Is Real. Model Collapse Isn't."
date: 2025-11-27 09:00:00 +0000
permalink: /ai-slop-is-real-model-collapse-isnt/
redirect_from: /ai-feeding-on-itself/
categories:
- ai
- writing
- productivity
image: /assets/img/ai-feeding-on-itself-title.jpg
infographic: /assets/img/ai-content-fork-infographic.jpg
---

There is a growing concern in AI circles about "model collapse."

The fear is that as AI-generated content floods the internet, future AI models will train on that generated content instead of human-created content. This creates a feedback loop where each generation of models gets slightly worse, like a photocopy of a photocopy.

<!--more-->

Research bears this out. When models are trained recursively on synthetic data, they converge towards bland, unimodal distributions, losing the nuanced patterns and tail information that make them useful.[^collapse] By April 2025, 74.2 percent of newly created webpages contained some AI-generated text.[^webpages] The slop is real, and it is multiplying.

But this concern only holds water if the AI-generated output is actually worse than what humans would have created.

What if it is not?

What if we use AI to enhance our thinking and produce demonstrably better output? Then we get a virtuous cycle instead of a vicious one.

## The Fork in the Road

Right now, we are creating the training data for tomorrow's AI models. Every piece of content you publish with AI assistance becomes part of that data set. Not just for today's models, but for the models that will shape the next decade of AI capability.

We are at a fork with two very different paths.

### Path One: The Vicious Cycle

People use AI as a "generate and ship" button. They produce mediocre content quickly. It floods the internet with slop. Future models train on this increasingly bland output. The next generation of AI produces even more generic results. Everything gets progressively more mediocre.

You can recognise this content immediately. Generic transitions like "here is the thing" and "the brutal truth." Triplet sentence patterns that sound robotic. Rhetorical questions followed by "the answer is..." You scroll past it without thinking because it adds nothing.

This is not just annoying. It is actively degrading the training data for future models. Research shows that repeated training on synthetic data causes distributions to converge to simpler, Gaussian-like shapes, losing the distinctive features that made the original data useful.[^shumailov] The statistical mechanism is clear: each iteration smooths out nuanced patterns until only bland averages remain.

### Path Two: The Virtuous Cycle

People use AI as a thinking partner. They ask it to interview them, to extract ideas from their heads. They use it to surface connections their brains make naturally but have not yet articulated. The final output is demonstrably better than they could have created alone.

Future models train on this enhanced human thinking. The next generation produces even better starting points for human collaboration. Quality compounds over time instead of degrading.

This is not theoretical. I use this approach for [every article I write](/writing-and-thinking-with-ai-why-repositories-beat-chatbots/), including this one.

## How To Use AI Without Creating Slop

I use AI to help me write almost everything now. But I do not ask it to write for me. I ask it to interview me, to pull out the ideas I cannot quite articulate yet, to help me see connections between concepts I have not linked before. The final output is mine, but it is better than I could have produced alone.

Because I have more context than any model. Decades of lived experience. Specific knowledge from building real systems. Patterns I have internalised but not yet verbalised. AI helps me surface that, acting as a thinking partner that asks the questions I need to hear but would not think to ask myself.

When I publish that enhanced thinking, I am contributing to a virtuous cycle instead of a vicious one. The key is treating AI as a question generator, not an answer generator. [Get it to ask you one question at a time](/claude-code-is-for-everything/), answer thoughtfully, and let the process reveal what you actually think. This is fundamentally different from asking AI to generate content for you.

## The Stakes Are Higher Than You Think

This is not about being altruistic. This is practical. Thoughtfully crafted content stands out, and as slop multiplies, quality becomes more valuable. You want to be on the quality side of that divide, where your work cuts through the noise rather than adding to it.

But more importantly, you are not just creating content for today. You are shaping the tools your future self will use. If models train on garbage, they will produce garbage. If models train on enhanced human thinking, they will help us think better.

Research on preventing model collapse shows that the critical factor is whether training data is replaced or accumulated.[^accumulation] When high-quality human data accumulates alongside synthetic data, models remain stable. When low-quality synthetic data replaces human data, collapse occurs. Your choice about how to use AI directly influences which future we get.

## What This Looks Like In Practice

Do not ask AI to write your LinkedIn post. Instead, ask it to interview you about your idea, answer its questions with your specific experience, and let it help you articulate what you already know but have not yet said clearly. Then write the post yourself, using that clarity. The AI helped you think, but the content remains authentically yours.

Do not ask AI to write your article. Give it your messy transcript or bullet points, ask it to identify the strongest ideas, then build the piece around those ideas in your own voice. The pattern is consistent: use AI to enhance your thinking, not replace it. Use it to surface ideas you already have but have not yet articulated, to make connections you might have missed. Then create the final output yourself, informed by that enhanced thinking.

## The Choice

We are not just choosing between lazy and thoughtful. We are choosing between two different futures for AI capability.

One where models get progressively worse at helping us think. One where they get progressively better.

The difference is whether we use them to replace thinking or enhance it.

Every piece of content you create with AI is a vote. Which future are you voting for?

[^collapse]: Recent research has documented the "model collapse" phenomenon extensively. See [Shumailov et al. (2024), "AI Models Collapse When Trained on Recursively Generated Data"](https://arxiv.org/html/2410.12954v1){:target="_blank"} for the foundational analysis of this problem.

[^webpages]: By April 2025, 74.2 percent of newly created webpages contained some AI-generated text, with AI-written pages in top-20 Google results climbing from 11.11 percent to 19.56 percent between May 2024 and July 2025. Source: [WinsSolutions analysis of web content trends](https://www.winssolutions.org/ai-model-collapse-2025-recursive-training/){:target="_blank"}.

[^shumailov]: [Shumailov et al. (2024)](https://arxiv.org/html/2410.12954v1){:target="_blank"} demonstrated that regardless of input complexity, distributions converge to unimodal Gaussian-like shapes after 30+ iterations of recursive training. This represents significant information loss as the system converges to simpler, more generic distributions. The research measured degradation using KL divergence and Wasserstein distance, showing continuous drift from original distributions.

[^accumulation]: Research in 2024 found that the critical factor determining model collapse is whether data are replaced or accumulated. Replacement causes collapse; accumulation prevents it. When synthetic data accumulates alongside original real data, models remain stable across sizes and modalities. Source: ["Escaping Model Collapse via Synthetic Data Verification" (arXiv, 2024)](https://arxiv.org/html/2510.16657v1){:target="_blank"}.
