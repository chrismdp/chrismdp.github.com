---
layout: post
title: "Don't Just Give Everyone an AI"
date: 2026-06-30 07:00:00 +0000
permalink: /ai-first-product-organisation/
categories:
- ai
- talk
- leadership
- team-topology
event_name: "Scott Logic: Adopting Agentic"
venue: "Techspace Shoreditch, London"
talk_date: 2026-06-30
talk_url: "https://www.scottlogic.com/"
talk_title: "Vision for an AI-First Product Organisation"
image: /assets/img/scott-logic-ai-first-product-org.jpg
---

We built our companies to make software, because software used to be expensive to make. The teams, the roles, the handoffs, the sign-offs all exist for that reason. Now AI is making software cheap, and that raises a question nobody at the event was asking. If the thing you built the company to produce has suddenly become cheap, is the company still the right shape?

<!--more-->

That was the one idea I took to Scott Logic's "Adopting Agentic" evening for engineering leaders in Shoreditch. The rest of the night was rightly about tools and models. I wanted to talk about the organisation instead, because this is a design question, not a tooling one.

## The Constraint Moved

An old idea from the 1980s explains what is going on. Goldratt's Theory of Constraints says every system has one slowest part, and only that part sets the speed. A chain is only as strong as its weakest link. Speed up anything else and the whole thing does not get faster, the queue just moves somewhere new.

So think about coding, which we made faster. If you are not shipping faster, then coding was never the slow part. There is data on this: teams using AI agents wrote around eight times more code but shipped only about a third more.[^nber] That gap is the slow part showing up somewhere else. It has moved to the things AI cannot speed up, like deciding what to build, reviewing it, applying judgement, and getting people to agree.

You see it on the ground the moment the AI says "I can go faster if you like", and then does. It floods you with pull requests, and every one of them still has to be understood, reviewed and judged by a human. The new bottleneck is deciding whether the code is any good, not writing it.

## Two Paths

Every engineering org is now on one of two paths, and most have not noticed they are choosing. The two look identical at the start and end up somewhere completely different.

The first path is the easy one. Give everyone an AI, leave the org chart exactly as it was, and let each person get faster at their own bit. It feels like speed, but you have sped up every station except the constraint, so more code, more pull requests and more half-finished tools all pile up in front of the same review-and-decision queue. Over time it hollows you out, because when everyone is heads-down producing, nobody is doing the deciding, and that muscle wastes.

Taken to its logical extreme you get the "one-person team", which is not a strawman. Coinbase's CEO cut around 14 percent of staff and floated a future of one person being the engineer, the designer and the product manager all at once, with AI doing the rest.[^coinbase] It sounds bold, but a one-person team is oxymoronic and moronic. You have not built a team of superhumans, you have thrown away the one thing you now need most, which is people combining their judgement.

## Amplify, Don't Dissolve

The second path takes more thought. You redesign the team around the new slow part rather than bolting AI on. Teams get smaller, four or five people, and one person owns a whole job from problem to deploy rather than passing it down a line. Your platform team stops doing vendor plumbing and starts building your own agents, skills and guardrails, the intelligence layer no vendor can sell you. And you invest in the enabling teams who spread the working patterns, because they are the difference between adoption that compounds and adoption that stalls. I go much deeper on that team structure in my [tortoises not hares](/ai-teams-need-tortoises-not-hares/) write-up from Fast Flow Conf.

The common thread is to put your best people where the constraint actually is now, on direction and judgement. The developer stops being constrained by code, so what took six months takes six weeks, but they still need the designer and the product manager in the room. The product manager gets customer insight on tap and can prototype and validate in days. The designer is freed from fiddling with layout to do real design thinking, and keeps feeding the design system so it gets stronger rather than staler.

None of this asks for mythical people. Amplification asks your specialists to grow into more strategic, more demanding work, and you have to invest in that. The alternative asks for a unicorn who is brilliant at three jobs at once, and almost nobody is. Slow and steady, but amplified, beats fast and frantic every time.

{% include inline-image.html src="/assets/img/scott-logic-speakers.jpg" alt="The Adopting Agentic speaker panel at Scott Logic's Shoreditch event" %}

## Delegation, Not Abdication

Amplification only stays healthy if judgement stays in the loop, and that is easy to lose. The AI does an okay first job, so you let it do more, and more, until it is building everything and you are not even looking. That is abdication, not delegation, and you are still responsible for what the AI does.

For engineering specifically, engineers should happily let go of where the semicolons go and the latest syntax, but never give up architecture, simplicity, security, and being able to tell whether the code is any good. Let the mechanics go, and protect the judgement that made the craft worth doing.

So here are three things to do if you are the CEO of a product business. Find your real constraint rather than assuming it is coding, and measure shipped value, not lines of code. Choose amplification deliberately, because hybridisation is what you get by default when you hand out tools and walk away. And protect judgement as you scale, so that handing work to AI never quietly turns into nobody owning what it ships.

[^nber]: The figures come from the NBER working paper [Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools](https://www.nber.org/papers/w35275){:target="_blank"} (Demirer, Musolff and Yang, 2026), which matched more than 100,000 developers to their real AI usage. Autonomous agents drove a huge jump in code written but only around a 30 percent rise in releases actually shipped. Producing code was never the bottleneck, so making it faster does not make the business faster.

[^coinbase]: Brian Armstrong, Coinbase's CEO, [set out the reasoning publicly](https://www.forbes.com/sites/rachelwells/2026/05/08/coinbase-ceo-announces-ai-layoffs-and-the-end-of-pure-managers/){:target="_blank"} in May 2026 while announcing layoffs of around 14 percent of staff, describing experiments with "one person teams" where a single person plays engineer, designer and product manager with AI support.
