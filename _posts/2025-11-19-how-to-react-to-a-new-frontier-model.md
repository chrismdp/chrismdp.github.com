---
layout: post
title: "How to React to a New Frontier Model"
date: 2025-11-19 09:00:00 +0000
image: /assets/img/final_dt_blog_evals_2.gif
categories:
- ai
- strategy
- evaluation
---

Gemini 3 is out. The benchmarks are genuinely incredible. But it's hard to know what to do about it.

41% on HLE. 45% on ARC-AGI-2. These are colossal achievements. But it feels like more of the same. Another week, another frontier model. OpenAI, Anthropic, Google - they're all leapfrogging each other every month.[^gpt51]

[^gpt51]: Case in point: whilst writing this post, OpenAI announced [GPT-5.1-Codex-Max](https://openai.com/index/gpt-5-1-codex-max/){:target="_blank"} on November 19th, the day after Gemini 3. Release blindness intensifies.

We've got release blindness because the pace is relentless. Another week, another set of impressive numbers. Traditional benchmarks measure performance on maths problems, coding challenges, and academic exams. Easy to track, easy to compare. Each generation scores higher than the last. It can feel like the pace of improvement is slowing as benchmarks saturate ([it isn't](/ai-progress-is-not-slowing-down/)).

But benchmarks are not important. Does the new model translate into real-world performance for your organisation? Most people won't know because they're running AI without proper evaluation. They're using vibes and anecdotes. That's not good enough anymore.

Here are two ways to know whether a model is better: not just for the world, but for you.

<!--more-->

## Benchmarks that matter: GDPval and METR

GDPval and METR benchmarks are a much better standard for whether a model is actually useful.

**GDPval** measures performance on actual economic tasks across 44 occupations. These aren't simple text prompts - they come with real files, real context, and expect deliverables spanning documents, slides, diagrams, spreadsheets, and multimedia. The evaluation uses head-to-head comparison with industry professionals who have an average of 14 years of experience.

The findings are striking: frontier models can complete GDPval tasks approximately 100 times faster and 100 times cheaper than human industry experts, with quality approaching professional standards.[^gdpval]

[^gdpval]: See [Measuring the performance of our models on real-world tasks](https://openai.com/index/gdpval/){:target="_blank"}. GDPval evaluation framework showing frontier models approaching expert quality.

**METR** tests autonomous agent capabilities on complex, long-running tasks in machine learning engineering, cybersecurity, and software engineering. These tasks take human professionals between one minute and 8+ hours to complete.

The key metric is time-horizon: the length of tasks that AI agents can complete autonomously with 50% reliability. This has been doubling approximately every seven months for the last six years. AI agents are improving rapidly at autonomous software development and machine learning tasks.[^metr]

[^metr]: See [Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/){:target="_blank"}. Blog post introducing time-horizon measurement showing exponential growth in task completion capability.

GDPval and METR tell you whether AI can actually do the work, not just score well on tests.

But we don't have that data yet for Gemini 3.

## What to Do About Gemini 3 (And The Model After That)

Whilst we wait for proper evaluation data, your response depends on how you're using AI.

### If You Build AI Into Products

**Run your evals.** See how good Gemini 3 is for your use case specifically. If you don't have evals yet, build them now.

Testing AI is not like testing regular code. The outputs are not deterministic. Evaluations score outputs based on criteria rather than checking for exact matches. Did the model understand the task? Was the response useful? Did it avoid common failure modes?

I built [Kaijo](/kaijo/) specifically for this. You need a way to systematically evaluate AI performance on tasks that matter for your business. Bring some examples, or generate them with AI. Let the evaluation system handle the rest - continuously testing and optimising your AI functions against real criteria.

Without evals, you're flying blind. You can't tell if Gemini 3 is actually better for your use case or just better at benchmarks that don't matter to you. [AI's consistent mediocrity](/ai-is-consistently-mediocre/) means you need systematic evaluation, not gut feel.

### If You Use AI for Productivity

**Get your early adopters testing.** Give them access to Gemini 3 and Antigravity.[^antigravity] Have them run typical tasks side by side with current tools. Get them reporting findings in lunch-and-learn sessions.

If you don't have an early adopter group yet, create one now. Set them up for systematic exploration with shared learning.

[^antigravity]: Google's new Antigravity IDE is their fork of Visual Studio Code with agentic capabilities baked in. Agents work across the editor, terminal, and browser. It's available now on Mac, Windows, and Linux, using Gemini 3, Gemini 2.5 Computer Use, and Nano Banana models. You can even use Anthropic's Claude Sonnet 4.5 or OpenAI's models to power the agents. But I suspect we still have a long way to go on interaction paradigms. Typing in files feels out of date, trying to one-shot whole systems allows too much creative freedom, and writing everything down in a spec is a flawed return to waterfall techniques. A creative, iterative process at the architecture level feels like the right direction of travel, and our tools don't natively support this yet, despite early attempts like Antigravity and Kiro.

### If You Have Neither Evals Nor Early Adopters

**Start building your internal AI platform now.** Without proper evaluation infrastructure, you won't know whether Gemini 3, GPT-6, Claude 5, or whatever comes next month actually helps your organisation.

The releases won't stop. The benchmarks will keep climbing. The organisations reacting fast are those that can systematically evaluate whether new capabilities translate to real value for the specific tasks and workflows that matter to them.
