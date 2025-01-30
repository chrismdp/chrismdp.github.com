---
layout: post
title: "Prompting Sucks (And What We Can Do About It)"
date: 2025-01-30 08:00:00 +0000
categories:
- ai
- productivity
- prompting

---

Prompting sucks. If you have spent any time working with LLMs, you already know this.

It is not just that prompting is difficult - it is fundamentally broken as an approach to working with AI. It is brittle, model-specific, and endlessly repetitive.

Here is why we need to move beyond prompting, and what we can do about it.

<!--more-->

## The problem with prompting

Prompting is situational and brittle. A carefully crafted prompt that works perfectly can completely break with seemingly minor changes to the input.

If you have only used more expensive models from OpenAI, you might not have experienced this acutely. But try working with cheaper models, and you will quickly discover just how fragile prompting can be.

This brittleness is compounded by the fact that prompts are highly model-specific. You cannot simply take prompts designed for one model and expect them to work with another. It feels like trying to use a horse to pull an express train, or a steam engine to power a spaceship. It is not a good fit.

The result is endless tweaking and repetition, where you are going around in circles without knowing if you are actually making progress.

## We have been here before

Working with LLMs today feels remarkably similar to the early days of computing when people punched cards for a living.

The parallels are striking:

- **Machine specificity**: Just as each manufacturer had their own punch card standard (80 holes for IBM, 90 for Remington Rand), each LLM requires its own specific prompt engineering process.

- **Specialist knowledge**: prompts, like punch cards, are indecipherable to the non-programmer. They might be written in natural language, but seemingly spurious details matter hugely to the outcome. These have been painstakingly discovered through iteration and their removal could break the system.

- **Slow feedback loops**: While we are not waiting hours for results like in the punch card days, the process of iterating on prompts is still painfully slow and inefficient.

## The false promise of prompt engineering

Companies are now hiring "Prompt Engineers". They are training their developers in better prompting. This is treating the symptom, not the cause.

Creating a new job title around a broken paradigm will not fix the underlying problems. We do not need the 20th century version of punchcard operators. We need to fundamentally rethink how we interact with AI systems.

When you are stuck in a particular way of doing things, it can be hard to imagine alternatives. Even the most fanciest computers in people's imagination, such as the BATCOMPUTER, were still just expensive and futuristic looking punch card machines.

## Moving beyond prompting

The answer is to look at our history.  We need to take the lessons learned from software engineering's evolution and apply them to working with AI.

Three key principles will help us move forward:

- **Abstraction**: Moving beyond raw prompts to higher-level concepts
- **Automated Testing**: Ensuring reliability at scale
- **Auditing**: Understanding what our systems are actually doing

## More soon

The solution is not to get better at prompting - it is to move beyond it.

Just as we moved from punch cards to high-level programming languages, we need to develop better paradigms for working with AI. More on these ideas, and how to implement them, in a future update to this post.
