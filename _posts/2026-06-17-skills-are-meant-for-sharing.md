---
layout: post
title: "Skills Are Meant For Sharing"
permalink: /skills-are-meant-for-sharing/
date: 2026-06-17 07:00:00 +0000
series: "Where AI Lives"
image: /assets/img/skills-are-meant-for-sharing-comic.jpg
image_portrait: true
categories:
- ai
- productivity
- leadership
---

One of the engineers on a team I train built something genuinely clever: a tool that turned plain questions into the gnarly database queries his team ran by hand a dozen times a day. It saved hours. For weeks, nobody else knew it existed. Then he showed it off in a sprint review, and within a week half the team was using it.

The gap between a) someone building something useful with AI and b) everybody else getting the benefit is hidden, but very expensive. When economists ran a controlled trial across 66 firms and more than 7,000 knowledge workers, the people given AI each saved around two hours a week, yet the researchers found no measurable change at the level of the firm. The gains stayed personal and never became embedded in the organisation.[^nber]

<!--more-->

## We Don't Share AI

A year ago the problem was getting AI into people's hands at all. Now your best people are brilliant with it, but that brilliance stays locked up with them. Microsoft found that more than three-quarters of people now bring their own AI tools to work, and over half will not admit to using AI on their most important tasks.[^byoai] All the prompting and the hard-won workflows live in one person's head, or buried in their private chat history.

For a leader this is familiar ground. It is the same problem as any other kind of siloing or expertise lock-in. The stakes are simply higher with AI: break the silos and it compounds fast; leave them in place and it never really gets off the ground.

**What makes this suddenly fixable is the skill.** A skill is a set of instructions you write once and your AI loads when it is relevant, and I went into [what a skill is and how to build one](/skills-are-claude-codes-secret-weapon/) in an earlier post. They can also bundle in [scripts that turn a workflow into runnable code](/stop-saving-tokens-start-writing-scripts/), which makes them a powerful symbiosis of AI creativity and repeatable process. Because everything travels together in one file, a skill can in theory move between people, which is exactly what you need to stop the siloing.

## Specific, not generic

Skills are ideal for the intrinsic knowledge that is hard to put into words: how your team actually works, the instincts only experience teaches. They are useless for anything the model could already recite, and that is the part people get wrong. SkillsBench, a benchmark built from 322 tasks contributed by 105 people across academia and industry, found that carefully curated skills lifted an agent's success rate by sixteen percentage points, while skills the model generated for itself gave no benefit on average.[^skillsbench] ([Hermes](https://hermes-agent.nousresearch.com/){:target="_blank"}, take note!) A separate study from Martin Vechev's group at ETH Zürich found that automatically generated context files made coding agents slightly worse and pushed their running cost up by a fifth.[^ethzurich]

It is the same lesson Perplexity's team reached writing skills in production: if something is easy to explain, the model already knows it, so delete it.[^perplexity] A skill that lists the git commands everyone already knows is useless. The ones worth sharing hold what is not on the public internet: your tone of voice, the shape of your internal systems, the way your team reviews code, the judgement calls that make the work yours. Share those.

## Have Context, Won't Travel

**On their own, though, skills do not travel well.** Copies drift: your laptop has version three, a colleague has version one, and nobody is sure which is right. They rot as the underlying tools change underneath them. The off-the-shelf options do not fit either: model vendors like Anthropic have plugin systems that can hold skills, but those are unwieldy and tie you to one vendor, and getting skills in and out of ChatGPT still means passing zip files around.

Even a Git repository, the engineer's instinct, is the wrong shape for this. Skills are not code, and many people who most need to contribute one do not write pull requests. What about the salesperson with a proposal workflow worth copying or the operations lead who has tuned a reconciliation process down to ten minutes?

## Airskills

I have watched this problem at nearly every [training client](/training/) trying to use skills well. So I fixed it.

{% include inline-image.html src="/assets/img/airskills-mark.png" alt="Airskills logo" align="center" width="140px" link="https://airskills.ai" rounded="false" %}

[Airskills](https://airskills.ai){:target="_blank"} keeps your skills in one place, syncs them across every machine and agent you work in, and lets you hand a set to your team so a new joiner gets the right skills on day one rather than hunting for a config file someone shared in Slack last month. It can even serve that skillset over MCP, the open protocol the non-terminal agents already speak, so ChatGPT or Claude Desktop pull the live set from one address instead of passing a stale zip around. People have wired single skills into MCP before, but a hosted, governed library a whole team connects to is, as far as I can tell, new. The command-line tool is open source, because something built to free your skills from vendor lock-in has no business locking them to me.[^oss]

You can install it in about ten seconds and try it on your own skills first:

```
curl -fsSL https://airskills.ai/install.sh | bash
airskills sync
```

You can also pull a single skill without installing anything, with `npx airskills add chrismdp/retro`. The team side is early, and I am running it as a free two-week trial with a handful of companies while I work out what teams actually need from it. If sharing AI across your team is the wall you keep hitting, that is exactly who I want to hear from, and you can reach me straight from the tool with `airskills feedback`.

## Skills Are Meant For Sharing

Remember that AI team productivity requires real coordination between people. You cannot just have one person who is brilliant with AI. Spreading good practice in effective ways needs to be part of the job. AI skills are simply the newest version of it, and right now one of the most valuable.

[^nber]: [*Shifting Work Patterns with Generative AI*](https://www.nber.org/papers/w33795){:target="_blank"} (Dillon, Jaffe, Immorlica and Stanton), a six-month randomised trial across 66 firms and 7,137 knowledge workers, found that giving individuals AI saved each of them about two hours a week but did "not detect shifts in the quantity or composition of workers' tasks". [McKinsey's State of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai){:target="_blank"} echoes the gap at scale: more than 80% of organisations report no material impact on enterprise earnings from generative AI.

[^byoai]: Microsoft and LinkedIn's [2024 Work Trend Index](https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part){:target="_blank"} found that 78% of AI users bring their own tools to work, and 52% are reluctant to admit using AI for their most important tasks.

[^skillsbench]: [SkillsBench](https://arxiv.org/abs/2602.12670){:target="_blank"}, a benchmark from UC Berkeley, Anthropic, Microsoft and Tsinghua, built 322 tasks from 105 contributors across academia and industry and ran more than seven thousand agent trajectories against them. Curated skills lifted task success by 16.2 percentage points; skills the model wrote for itself gave "no benefit on average".

[^ethzurich]: [*Evaluating AGENTS.md*](https://arxiv.org/abs/2602.11988){:target="_blank"}, from Martin Vechev's lab at ETH Zürich, found that automatically generated repository context files decreased coding-agent performance by around 3% on average while increasing inference cost by over 20%. Human-written context files helped only marginally.

[^perplexity]: Perplexity's agents team wrote up [how they design and maintain agent skills](https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity){:target="_blank"}, including a sharp section on when you do not need a skill at all. Their rule of thumb: "If it's easy to explain, the model already knows it. Delete it."

[^oss]: The Airskills command-line tool is open source under the MIT licence at [github.com/chrismdp/airskills](https://github.com/chrismdp/airskills){:target="_blank"}.
