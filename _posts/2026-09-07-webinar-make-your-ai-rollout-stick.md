---
layout: post
title: "Webinar: Make Your AI Rollout Stick"
date: 2026-09-10 14:30:00 +0100
categories:
- ai
- webinar
- leadership
- strategy
image: /assets/img/make-your-ai-rollout-stick-webinar.jpg
image_portrait: true
series: "AI In Action Webinars"
excerpt: "AI rollouts fail by default. The licences land, the training happens, and everyone builds their own version of their own work. Six months later the demos are impressive and the business runs at the same speed. Who owns the AI workflows people have already built, and who fixes them when the model changes or the person who made them leaves?"
description: "Why AI rollouts stall after the demos, the forward deployed engineers nobody budgets for, how to size that team for your company, and a real purchase order checker taken from prototype to engineered workflow."
---

On 10 September 2026, I gave a webinar about the part of an AI rollout that never gets budgeted. The licences land, some training happens, and everyone builds their own version of their own work. Six months later the demos are impressive and the business runs at the same speed. Who owns the tools people have already built, and who fixes them when the AI changes or the person who made them leaves? If the answer is nobody, the rollout has not stuck yet.

<!--more-->

## Let people try things

A support worker builds a tool to spot repeat requests and tells nobody. Finance uses AI to read invoices and saves a few minutes a week. These trials are how people learn what AI can do for their work, but colleagues often know nothing about them, so teams end up solving the same problem several times.

Peter Seibel called this letting a thousand flowers bloom at Twitter.[^seibel] The next step was to choose which tools to support. Trying things is a useful start, but a shared tool needs care beyond its first version. [A Thousand Flowers Is Not Enough](/a-thousand-flowers-is-not-enough/) explores that next step.

## Finish the work

Little's law says the time to finish anything equals the unfinished work divided by the rate work gets finished. AI has raised the unfinished work. A pile of prototypes, meaning early working versions only one person can use, makes teams feel busy without finishing more. The business only speeds up when work leaves the building as a result people can use and trust.

![Little's law: lead time equals work in progress divided by throughput. A conveyor piled with half-built boxes labelled prototype, and one small door labelled shared workflow.](/assets/img/littles-law-prototype-inventory.jpg)

A tool can also seem to work while hiding a serious fault. One executive built a tool in Claude to view client work. When they asked to use it from home, the AI put the data behind a public link. That exposed the company's data, even though the tool appeared to do its job.

## Where work waits

Writing code faster does not help if it then waits longer for someone to check it. A study of ten thousand developers found that heavy AI use produced 98% more pieces of work for review.[^faros] Reviews took 91% longer, while the pace of delivery stayed the same. [Feedback Is the New Bottleneck](/feedback-is-the-new-bottleneck/) brings together the sources on these delays.

Those figures describe software teams, but the same problem can arise elsewhere. A finance worker can use AI to compare a hundred sets of accounts, but someone still has to check them. The slowest step has moved from doing the work to reviewing it.

## Tools need support

Codex, ChatGPT and Claude are good at helping one person on one machine get work done, and they are still rough at the edges themselves. Changing a whole process takes someone who understands its steps and can connect the tools it uses. Buying licences does not assign that job to anyone.

AI companies have committed nearly $10bn to engineers who work inside their customers' businesses.[^tunguz] The name for the role is forward deployed engineer, or FDE, and you will hear it a lot this year. They map how the work happens, connect the AI to your systems and data, decide what it can see and when a person reviews its work, and stay until it runs on its own. The labs send them to customers with thousands of staff, so everyone else has to find their own.

## Who does the work?

At a few hundred staff, a small team of engineers you already have can start part time. At around fifty, it is one engineer, or a couple, with a clear job to do and a name against it. If you are on your own, the same discipline applies: decide what starts the tool, who checks it, and what it can reach before you build. The people who suit this work like mess. They will sit with finance for an afternoon or chase a missing login for a week, and that matters more than being your strongest software designer.

The people doing the work are best placed to choose what to improve, so point the engineers at the tools people have already built. Their job is to sit with the person who made it, understand what they wanted, and make it safe for others to use. Start with real data and aim for a working process in five days. Long rollouts stall while teams wait on each other.

## Is it worth maintaining?

XKCD's chart asks how much time a task can save over five years.[^xkcd] Saving one minute a day allows four hours to build the tool. Saving an hour a week allows ten days. But the chart leaves out the time spent keeping the tool working.

![XKCD 1205, Is It Worth the Time, with a hand-drawn extra column headed maintenance in which every cell is a question mark.](/assets/img/xkcd-is-it-worth-it-maintenance-column.jpg)

AI can cut the time it takes to build something, but the systems it connects to will still change. The AI itself will change, and the person who built the tool will leave. Count the work of keeping it running when deciding whether it saves time.

## One real process

One finance team needed to check sales orders against customer purchase orders. Each sales order arrived in the finance system, but someone still had to find the matching purchase order. The purchase order arrived as a PDF or email, sometimes in another language. Someone compared the amounts, codes and terms, then chased anything that did not match. This took one or two people several hours a week.

The first version ran in one person's AI tool. It showed that AI could do the job and helped define the checks. Nobody else could use it or knew it existed. Turning it into a shared process meant deciding how it would run and who would review it.

![The engineered purchase order checker: new sales order, find the purchase order, read the details, compare, then weekly summary or exceptions to a finance person. Annotated with defined trigger, limited access, a record of what it did, and explicit human review.](/assets/img/purchase-order-checker-engineered-version.jpg)

The shared version starts when a new sales order arrives. It can read the finance system but cannot change it. It records what it checked and any details that did not match. A finance person gets an email alert to review those differences. A weekly email lists what matched, using the format the team found easiest.

## Keep ownership

When outside engineers do this work, whether a vendor, a consultancy or me, the knowledge of how your work happens can end up in their team, and that is how help becomes lock-in. Before anyone starts, ask four questions. Who owns the process maps? Who owns the checks and the records? Can we run it without them? Are they teaching our people, or becoming our AI department? [Escape the Great AI Lock-In](/webinar-escape-the-great-ai-lock-in/) covers this risk in more depth.

## Questions from attendees

One attendee asked how to let people try AI while keeping data safe. My answer was to use company accounts and let tools read data without changing it. Turn on features as people learn to use them, and explain which tools are allowed. Banning AI can push people towards personal accounts. Technical staff can make the same mistakes as anyone else.

They also asked about a single view of all the AI processes staff had built. I did not know of a platform that offered one. Usage counts do not explain what people are doing. Seeing the content of their work also raises questions about privacy. Talk to frequent users to find useful ideas, and to those who avoid AI to understand why.

Another attendee asked how to test AI when its answers can vary. Use evals, which are checks that show whether the AI still does its job after changes. The checks must cover the whole process, as [why prompt evals alone are useless](/prompt-evals-are-useless/) explains. The code and instructions around the AI are the subject of [The Harness Is The Bottleneck](/the-harness-is-the-bottleneck/).

## Key takeaway to remember

Name who owns each AI process, and give engineers time to turn the useful early versions into tools the whole team can rely on. Letting everyone try things is the right start, but it is not a rollout until somebody owns the result and the work of keeping it running is in the plan.

## One thing to try this week

Draw the steps of a process that takes a day a week. Note what starts it, where work waits, and who checks the result. Mark who fixes it when it breaks. Find any version someone already built, then ask whether the time saved covers its upkeep.

[^seibel]: Peter Seibel, [Let a 1,000 flowers bloom. Then rip 999 of them out by the roots.](https://gigamonkeys.com/flowers/){:target="_blank"}, written while he led the Engineering Effectiveness group at Twitter.

[^faros]: Faros.ai study of 10,000+ developers across 1,255 teams. Reported in Ankit Jain, [How to Kill the Code Review](https://www.latent.space/p/reviews-dead){:target="_blank"}, Latent Space, March 2026.

[^tunguz]: Tomasz Tunguz, [The $10B FDE Boom](https://tomtunguz.com/the-10b-fde-boom/){:target="_blank"}.

[^xkcd]: Randall Munroe, [xkcd 1205, Is It Worth the Time?](https://xkcd.com/1205/){:target="_blank"}, CC BY-NC 2.5. The maintenance column is my addition.
