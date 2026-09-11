---
layout: post
title: AI Progress Is Accelerating. Here Is Why It Feels Slow
date: 2026-09-11 07:00:00 +0000
image: /assets/img/metr-time-horizons-2026.jpg
image_caption: METR Time Horizon 1.1, updated May 2026. Human task duration at 50% predicted success. Estimates above 16 hours are omitted because METR considers them unreliable.
categories:
- ai
- industry
- analysis
excerpt: AI progress still compounds through longer task horizons, better tools and lower costs. See which measures leaders should track beyond benchmark hype.
permalink: /ai-progress-is-not-slowing-down/
---

AI progress is accelerating in the length of bounded technical tasks that systems can complete, whilst better tools and lower costs make more work worth delegating. It can feel slow because those gains are hard to see in a chat window. A more reliable answer to a familiar question rarely feels like a breakthrough, even when the system behind it can now finish work that defeated it last year.

The useful question is how much work AI can complete to an acceptable standard, at what cost, and with how much human help. A system can improve substantially and still cost your team more in review than it saves.

<!--more-->

## Why It Feels Slow

Fluent conversation quickly becomes ordinary. Once a model can write a plausible email or explain a piece of code, another improvement in either task is easy to miss. Expectations rise too: yesterday's impressive demo becomes today's minimum standard. GPT-5 launched on 7 August 2025, but no release date tells you whether a model makes your work easier.[^gpt5]

Progress also arrives unevenly. An agent can solve a difficult bug and then lose track of a requirement. If that requirement matters to you, the failure is real, even when the benchmark score improves. Disappointment with a particular tool is useful evidence about that tool, but a poor basis for judging the whole field.

The distinction matters when deciding whether to revisit a failed experiment. In [How to React to a New Frontier Model](/how-to-react-to-a-new-frontier-model/), I argue for testing familiar work alongside tasks you previously expected to fail. Keep the old failures: they give you something concrete to compare when a new model or a better setup arrives.

## Longer Task Horizons

METR's task horizon measures difficulty through human completion time. At the 50% horizon, an AI system is predicted to succeed half the time on tasks of that duration. The hours describe how long the human takes, rather than how long the AI runs.[^metr-paper]

METR expanded its task suite in January 2026. Its current data puts several 2026 systems in the range of roughly five to six hours, with Claude Opus 4.6 around twelve hours. The latter estimate has especially wide uncertainty. The revised data fits a doubling roughly every four months for models released since 2023.[^metr-data] Compounding means each doubling adds more hours of task difficulty than the last. That is the acceleration I mean, without claiming that the doubling time keeps shrinking. The fitted rate depends on the period and task selection, so it is a poor timetable for predicting when a particular job becomes automated.[^metr-update]

METR measures a model-plus-scaffold system. The scaffold supplies tools and manages the loop of instructions, actions and results. Tasks are bounded technical work, mainly software engineering, machine learning and cybersecurity, with clear success criteria. The human comparison is a skilled but low-context person, closer to a new contractor than a colleague who knows your systems.[^metr-current]

Fifty per cent reliability is insufficient for unattended deployment in most workflows. METR warns that estimates above 16 hours are unreliable with its current task suite, so the chart excludes those points. These measurements do not establish that agents can replace a working day across arbitrary jobs.[^metr-current]

For your team, a longer reliable task horizon means an agent can carry a useful piece of work further before someone has to redirect it. Establish that horizon at the success rate your work requires. A benchmark measured at 50% gives you a reason to test, not a production acceptance standard.

## Tools That Catch Mistakes

An agent that can run a test, inspect the failure and try a repair has a way to recover. Giving it access to the right files, a working environment and evidence of success can change what it finishes. METR's research links longer task horizons to improvements in reliability, recovery from mistakes, reasoning and tool use.[^metr-paper]

Verification needs more than asking the same model whether it did a good job. In March 2026, Anthropic described a coding setup with a separate evaluator that used the application and reported specific faults. The evaluator still needed tuning because it accepted weak work too readily. The authors also found that stronger models made some checks unnecessary overhead on easier tasks.[^harness]

My own experience in [The Harness Is the Bottleneck](/the-harness-is-the-bottleneck/) shows how much the surrounding software matters. Clear tickets, continuation after a stopped run, and review all affect whether generated code becomes accepted work. A model comparison that ignores those parts can mistake a broken setup for a capability limit.

That is also why [Prompt Evals Alone Are Useless](/prompt-evals-are-useless/) tests the wider system. Evals are repeatable checks of AI behaviour. A good answer in one call cannot prove that an application remembers earlier decisions or works when someone uses its screens. Test through to the outcome, then use the failures to improve the tools and the instructions.

## Cheaper Successful Work

Falling prices let teams try work that previously cost too much. Epoch AI's 2025 analysis found sharp declines in the price of reaching fixed benchmark scores, though the rate varied widely by task.[^costs] It does not establish what a finished piece of work costs your business.

A cheap model can spend the saving on retries, or leave expensive repairs for a person. A stronger model can cost more per call and less per accepted result. In [my August coding comparison](/the-harness-is-the-bottleneck/), the cheaper model's bill left out the premium model used to review and fix its work.

For a batch of comparable tasks, divide the total cost by the number of accepted completions. Include failed attempts, tools, human review and repair. Allocate setup and ongoing maintenance costs across a realistic volume of work. Hold the acceptance standard steady, so a falling bill cannot hide declining quality.

Lower costs and better recovery can reinforce each other. Cheaper attempts leave room for verification and another try, whilst better verification catches faults before they reach a person. This only pays off if the whole process produces useful work for less. A low token price alone cannot tell you that.

## Has AI Peaked?

The evidence does not support a broad claim that AI has peaked. Longer technical task horizons and improving systems give us concrete reasons to keep testing. They do not prove that progress will continue at the same rate, or that every new model improves every workflow.

Some tasks remain poor candidates for delegation because success depends on unstated context, judgement or coordination with people. If the whole process fails to beat your existing approach at the required quality, defer investment. Retest when a relevant model or tool change addresses a recorded failure.

## What Leaders Can Track

Choose a recurring task your team already knows how to judge and name the business outcome it serves. Keep a representative set of examples, including previous failures, and compare results during a pilot and after relevant model or tool changes. Record three measures together.

For example, test drafting a monthly supplier report from approved records. Define success before running it: every figure matches its source, required sections are present, and a reviewer finds no unsupported claims. Compare with the existing manual process. Time saved creates capacity for other work, but only becomes a cash saving if expenditure falls.

### Successful Task Horizon

Track the longest class of task the system completes at your required success rate. Use human completion time as a rough size measure, and record accepted and attempted task counts beside it. Keep the task mix comparable and record the model, tools and allowed human help.

### Cost Per Successful Completion

Divide the full cost of all attempts by accepted results. Include review and repair, and compare against the existing way of doing the work. Keep latency visible too: a cheap result that arrives too late can still be useless.

### Human Review Required

Record the minutes people spend checking, correcting and redirecting each task, including failed attempts. Separate completions that need routine approval from those that need substantial repair. Completing the same valuable work at the same standard with less cost or human effort is progress worth measuring, even before you delegate anything larger.

[^gpt5]: OpenAI, [Introducing GPT-5](https://openai.com/index/introducing-gpt-5/){:target="_blank"}, 7 August 2025.

[^metr-paper]: METR, [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499){:target="_blank"}. The paper defines the 50% horizon and discusses the capabilities associated with its growth.

[^metr-data]: METR's [Time Horizon 1.1 data](https://metr.org/assets/benchmark_results_1_1.yaml){:target="_blank"}, retrieved 11 September 2026. The dashboard's last listed update is 8 May 2026. The chart uses post-2023 estimates at or below 16 hours, with uncertainty intervals clipped at that limit. It does not plot the higher estimate for Claude Mythos Preview (early). The current fit since 2023 gives a doubling time of about 129 days and excludes central estimates above 16 hours.

[^metr-update]: METR, [Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/){:target="_blank"}, 29 January 2026. The update expanded the suite to 228 tasks and explains why changing the task mix changes the fitted trend. Most longer tasks still used estimated human durations.

[^metr-current]: METR, [Task-Completion Time Horizons of Frontier AI Models](https://metr.org/time-horizons/){:target="_blank"}, checked 11 September 2026. The methodology and FAQ explain scaffolds, human baselines, domain limits and the warning above 16 hours.

[^harness]: Anthropic, [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps){:target="_blank"}, 24 March 2026. These are the authors' experiments, rather than an independent estimate of productivity gains.

[^costs]: Epoch AI, [LLM inference prices have fallen rapidly but unequally across tasks](https://epoch.ai/data-insights/llm-inference-price-trends){:target="_blank"}, 12 March 2025. This study tracks prices at fixed benchmark performance levels, rather than total costs of deployed workflows.
