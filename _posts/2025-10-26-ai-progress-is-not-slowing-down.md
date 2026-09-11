---
layout: post
title: AI Progress Is Accelerating. Here Is Why It Feels Slow
date: 2026-09-11 07:00:00.000000000 +00:00
image: "/assets/img/metr-time-horizons-september-2026.jpg"
image_caption: METR Time Horizon 1.1 at 50% predicted success. Task length is measured
  in human work time. Estimates above 16 hours are unreliable. Chart retrieved September
  2026; data last updated May 2026.
categories:
- ai
- industry
- analysis
excerpt: AI progress still compounds through longer task horizons, better tools and
  lower costs. See which measures leaders should track beyond benchmark hype.
permalink: "/ai-progress-is-not-slowing-down/"
---
AI systems can finish longer tasks and recover from more mistakes. Falling model prices make more work worth trying. Those gains are easy to miss if you judge progress by asking a chatbot the same questions. The clearer test is what it can now finish that it could not finish before.

Progress in technical tasks is compounding. That does not guarantee a saving for your team: a better model can still create more review work than it removes.

<!--more-->

## Why It Feels Slow

A fluent answer quickly becomes ordinary. Expectations rise, and the remaining failures stand out. An agent can solve a difficult bug, then forget a requirement that matters more to you than its benchmark score.

Keep examples of those failures. As I argue in [How to React to a New Frontier Model](/how-to-react-to-a-new-frontier-model/), testing familiar work and previous failures tells you more than trying to feel impressed by a launch.

## Longer Task Horizons

METR measures the difficulty of a task by how long a skilled human takes to complete it. The *50% task horizon* is the task length at which the AI system is predicted to succeed half the time. It measures human work time, not how long the AI runs.[^metr-paper]

Several 2026 systems reach tasks that take humans hours, up from minutes in earlier results. The trend is roughly exponential: each doubling adds more hours than the last. That is the acceleration I mean, even if the doubling rate stays constant.[^metr-data]

METR tests a model with its *harness*: the tools and software that manage its actions. The tasks are bounded technical work with clear success criteria. The human comparison has little prior context, like a new contractor, rather than a colleague who knows your systems.[^metr-current]

Succeeding half the time is too weak for most unattended work, and METR says estimates above 16 hours are unreliable. The chart marks that boundary. Use the trend as a reason to test longer tasks at the reliability your work requires, not as proof that AI can replace a working day.[^metr-current]

## Better Tools, Checks and Recovery

An agent that can run a test, inspect a failure and repair it has a way to improve its own work. The harness gives it that feedback. Access to the right files, a working application and clear checks can change what the same model finishes.

In [The Harness Is the Bottleneck](/the-harness-is-the-bottleneck/), I describe how stopped runs and missing context distorted my coding experiments. A broken setup can look like a weak model.

Checks also need to reach the result a person sees. My text adventure game passed its mechanical tests whilst leaking internal bookkeeping into the story. [Prompt Evals Alone Are Useless](/prompt-evals-are-useless/) explains how I now test the model, code and what the game remembers together. A good answer in one call does not prove that the application works.

## Cheaper Successful Work

The price of reaching a given benchmark score fell sharply in recent years.[^costs] That makes more uses worth trying, but the bill per answer can mislead. Cheap attempts can leave expensive repairs for a person.

In my August coding comparison, the cheaper model's bill excluded the stronger model that reviewed and fixed its work. Add the costs of all attempts, tools, review, repair, setup and maintenance, then divide by accepted completions.

Lower prices give us more room to check and retry. Better checks can reduce the repairs people must make. The saving is real only when the whole process delivers acceptable work for less.

## Has AI Peaked?

The evidence does not support that claim. Technical task horizons continue to grow, and better harnesses make more of that capability useful. Neither trend guarantees that every new model will improve your workflow, or that progress will continue at the same rate.

If a pilot fails at the quality you need, identify the cause before investing further. Keep the failed examples and retest when a model or tool change addresses them.

## Three Measures for Leaders

Choose a recurring task with a clear standard, such as drafting a monthly supplier report from approved records. Define success before testing: figures match their sources, required sections are present and claims have support. Compare similar work against the current process.

### Successful Task Horizon

Track the longest type of task the system completes at your required success rate. Record attempted and accepted tasks, the model and harness, and any human help. Use human completion time as a rough measure of task size.

### Cost Per Successful Completion

Divide the full cost of all attempts by accepted results. Hold the quality standard steady. Separate extra capacity from cash savings: time saved only reduces spending if expenditure falls.

### Human Review Required

Record time spent checking, correcting and redirecting, including failed attempts. Separate routine approval from substantial repair. You have made progress when the same work meets the same quality standard with less money or human effort.

[^metr-paper]: METR, [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499){:target="_blank"}. Defines the 50% task horizon and analyses its growth.

[^metr-data]: METR's [Time Horizon 1.1 data](https://metr.org/assets/benchmark_results_1_1.yaml){:target="_blank"}, checked 11 September 2026. The dashboard was last updated on 8 May 2026. The supplied chart shows the 50% horizon on a logarithmic scale and marks estimates above 16 hours as unreliable. The [January 2026 update](https://metr.org/blog/2026-1-29-time-horizon-1-1/){:target="_blank"} explains how expanding the task suite changes the fitted trend. Neither the fit nor the chart is a timetable for job automation.

[^metr-current]: METR, [Task-Completion Time Horizons of Frontier AI Models](https://metr.org/time-horizons/){:target="_blank"}, checked 11 September 2026. The methodology explains the model-and-harness setup, low-context human baseline and domain limits. Estimates above 16 hours are unreliable with the current task suite.

[^costs]: Epoch AI, [LLM inference prices have fallen rapidly but unequally across tasks](https://epoch.ai/data-insights/llm-inference-price-trends){:target="_blank"}, 12 March 2025. This measures prices at fixed benchmark scores, not the full cost of completed business tasks.
