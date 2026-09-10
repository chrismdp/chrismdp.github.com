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

On 10 September 2026, I gave a webinar about the part of an AI rollout that never gets budgeted. AI rollouts fail by default. The licences land, the training happens, and everyone builds their own version of their own work. Six months later the demos are impressive and the business runs at the same speed. I opened with a question: who in your company owns the AI workflows people have already built, and who fixes them when the model changes or the person who made them leaves? If the answer is nobody, the rollout has not stuck yet.

<!--more-->

I have plenty of drift stories of my own. I built an OpenClaw agent on a Mac Mini and it broke every ten minutes. I wired up smart home workflows that made the smart home worse. I connected Hermes to WhatsApp so the family could talk to it, and it spammed them with useless information until they were all cross with me, and I turned the lot off. That is a trivial home example, and it is exactly what happens inside teams. Somebody builds a workflow that becomes mission critical. Then they move teams, or leave, or the model updates, and it stops doing quite what it did. Nobody notices until the work is not being done any more.

## Let a thousand flowers bloom

The rollout I see most often goes like this. Everyone gets Copilot, or ChatGPT, or Claude. Some training happens. Then a support person builds a little automation that spots recurring tickets and tells nobody, not even the rest of the support team. Finance builds a spreadsheet that reads invoices and saves ten minutes here and there. Marketing produces three times the content and it is all slightly worse. One engineering team ships as fast as Copilot will let it. Everyone starts sending emails that read as if they handed the thinking to a machine.

Peter Seibel described this at Twitter and called it letting a thousand flowers bloom.[^seibel] His second stage matters more than the first: once the sprawl does more harm than good, you pick the tools you will support and support them properly. The first phase is right. It is the best way to find out how AI changes people's work, and you need it. The mistake is thinking the rollout is finished when the flowers are up. I made the longer version of this argument in [A Thousand Flowers Is Not Enough](/a-thousand-flowers-is-not-enough/).

## Work in progress is waste

Little's law explains why the business does not speed up. Lead time equals work in progress divided by throughput, and it holds for any stable system: a factory, a hospital, a finance team. What AI has done is raise work in progress. A hundred half-built prototypes that nobody else can use feel like a lot of work happening, and they are, but the work is incomplete. Throughput is work that leaves the building as a result the business can rely on. Unless finished work rises to match, lead time goes up, and everyone is busier while nothing moves faster.

![Little's law: lead time equals work in progress divided by throughput. A conveyor piled with half-built boxes labelled prototype, and one small door labelled shared workflow.](/assets/img/littles-law-prototype-inventory.jpg)

Three teams can now each build a working solution to the same problem in the time it used to take to write the proposal. Who decides which one is right, and how it gets deployed? Ten people solve the same problem ten times because none of the earlier solutions are findable or trusted enough to reuse. The thousand flowers phase is an inventory problem, and that is good news, because inventory problems have known fixes.

Some of that inventory is worse than useless. An executive at one company built a tool in Claude to visualise their client work, which was useful. They asked to see it from home, which was reasonable. The AI obliged by putting the data behind a public link, and the company had a data breach to deal with. Nobody did anything wrong by their own lights, and the tool appeared to work. A non-specialist can now build the feature before they understand how it fails, and the failures are hidden from them.

## The bottleneck moved

Every process has one bottleneck. Speed up anything else and nothing changes, and it can make the whole system slower. Engineers who said they were 20% faster with AI were on teams measured at 20% slower, with more work to review and reviews that took longer.[^plandek] A separate study of ten thousand developers found teams using AI heavily produced 98% more pieces of work for review, review took 91% longer, and delivery pace did not move.[^faros] I collected the sources in [Feedback Is the New Bottleneck](/feedback-is-the-new-bottleneck/).

Those numbers come from developers because engineering was transformed first and is the part of the company being measured. Treat them as a canary for everywhere else. A finance person can generate a hundred reconciliations that someone still has to check, because AI is doing what it was asked. The bottleneck moved, and nobody moved with it.

## Tools are not a rollout

Codex, ChatGPT and Claude on the desktop, the bots arriving in Slack, and whatever Google does next with Spark are good at what they are for, which is letting one person on one machine get something done well. They also all feel unfinished, like prototypes bodged together and sold at a market stall. None of them change the whole system, with its bottlenecks, its flow and its coordination.

So usage sits at the edges. Google published a post the day before the webinar on how Gemini makes admin chores quick and easy: forms, licences, parking fines.[^google] That is my read of where most AI use sits right now, admin and drafting and summarising around the work, and not Google's statistic. AI can replace whole processes, and that is where the leverage is, but it takes effort, process mapping, and platform work. Buying licences does not assign that work to anyone.

## The $10bn nobody is sending you

If you have five thousand or more employees and a direct contract with a lab, you are probably getting help with this. AI companies have committed nearly $10bn in the last year to forward deployed engineering.[^tunguz] OpenAI bought two consultancies outright, Anthropic launched a services firm with Blackstone, Goldman Sachs and Hellman and Friedman, AWS put a billion dollars into a unit that embeds engineers with customers, and Google Cloud compressed its interview process for these people to two days.[^vendors]

A forward deployed engineer, or FDE, is a vendor's engineer who works inside your company. They map how your work happens, wire the model into your systems and data, decide what the agent can see and when a human reviews it, and stay until it runs in production. For something that was meant to replace human work, that is a lot of humans to hire, and it tells you where the hard part of a rollout is. The rest of us are not getting those people, so we have to find our own.

## Who belongs in it

Gergely Orosz looked at the FDE roles being hired and reckons about a quarter of the work is coding. The rest is integration, plumbing and hand-holding.[^pulse] The role belongs to the person who loves messy complexity, not necessarily your strongest architect: someone who is happy to sit with a finance person for an afternoon, and who will chase a missing system login for a week without losing interest. We used to do this work with business analysts and internal software teams, then we bought it as SaaS. In the AI world we either buy it back in through an ERP vendor or we build those people again ourselves.

The shape depends on your size. At a few hundred people, stand up a small internal team, part time at first, made of engineers you already have, and point them at the prototypes people have already built. Those engineers are not the best people to pick use cases, and the worst outcome is handing a finished system to a team that never wanted it. Their job is to sit with the person who built the prototype, understand what they wanted, and turn it into something safe, reliable and still working after that person leaves. At around fifty people it is one engineer, or a couple, named and given a clear mandate. If you are solo, you can still do this, but you have to be disciplined: think in triggers and integration points, not just prompts. My own Telegram bot reads receipts, works out whether they are personal or business, and files them in Xero. It takes some technical understanding, and it works.

Whatever the size, it is not a hiring spree. When you stand the team up, steal Palantir's bootcamp: five days, real data, a working deployment at the end. Rollouts stretched over months stall on their dependencies.

## Is it worth maintaining?

Before touching a prototype, decide whether it is worth it at all. XKCD 1205 shows how long you can spend automating a task before you spend more than you save over five years. A daily one-minute task earns four hours of automation. A weekly one-hour task earns ten days.[^xkcd] AI collapsed the build time, so almost every cell now says yes. What the chart never showed is the maintenance column, and that is the column that decides whether the savings are real. The model will change, the system it talks to will change, and the person who built it will leave.

![XKCD 1205, Is It Worth the Time, with a hand-drawn extra column headed maintenance in which every cell is a question mark.](/assets/img/xkcd-is-it-worth-it-maintenance-column.jpg)

## One real process

Here is one my company built recently for a finance team. A sales order lands in the finance system. Somewhere there is a customer purchase order that should match it, as a PDF or an email, sometimes not in English. Someone finds it, reads it, and compares amounts, codes and terms. If it matches, fine. If not, it goes on a pile to chase. That took one or two people several hours a week, and a mismatch that slipped through caused headaches downstream for ages.

The first version was one person on one machine, trying it in their own AI tool. That is one of the thousand flowers: nobody else could use it and nobody else knew it existed. It was still valuable, because it proved AI could do the job and told us exactly what the checks were. Do not stop there. That was the one thing I asked people to take away.

![The engineered purchase order checker: new sales order, find the purchase order, read the details, compare, then weekly summary or exceptions to a finance person. Annotated with defined trigger, limited access, a record of what it did, and explicit human review.](/assets/img/purchase-order-checker-engineered-version.jpg)

The engineered version is the same map with four things added: a defined trigger, limited access so it can read the finance system and cannot change it, a record of everything it checked and every exception, and an explicit human review. That review is delivered as email because it was the easiest thing for the team to engage with, a weekly summary of what matched and an alert for anything that did not. It did not take long to build, it costs little to maintain, and it is already saving hours every week.

## Keep ownership

If you are lucky enough to have vendor engineers arriving, do not let them own your process. An FDE, or any embedded engineer or consultant, sees more of your company than almost anyone, and the knowledge of how your work gets done starts to live in their team. That is how help becomes lock-in, and it is why vendors are happy to pay for the engineers. The same thing happens on every ERP rollout that goes wrong. Before anyone starts, ask who owns the workflow maps, who owns the checks and the records, whether you can run it without them, and whether they are teaching your people or becoming your AI department. Get help, but do not outsource your intelligence. I covered the wider version of this in [Escape the Great AI Lock-In](/webinar-escape-the-great-ai-lock-in/).

## What the virtual room asked

One attendee asked where the balance sits between letting the flowers bloom and keeping data safe, given the public link story. Technical people make those mistakes as readily as anyone. My answer is guard rails for the early phase: enterprise accounts, tools attached read only, features switched on gradually as people are trained, and clear communication about which tools are sanctioned and why. Ban AI outright and people use it anyway on personal accounts, which is where the data leaks. They also asked whether any platform gives a compliance lead a dashboard of the workflows people have built, and I do not know of one. You get token usage per person and feature switches, because content visibility runs straight into privacy. There is no substitute for talking to both ends of the usage graph: the people not using it at all, to find out why, and the heavy users, to find the unusual uses everyone should learn.

Another attendee asked how you test something probabilistic that might one day just decide not to do the thing. The short answer is evals, and I wrote about [why prompt evals alone are useless](/prompt-evals-are-useless/) the day before. An eval is closer to a performance review than to an automated test: is the AI still doing what it said it would, and will it still hit its targets after an upgrade? The model is the engine, the harness of code, prompts and skills is the car around it, and the eval system is the mechanics workshop you need to keep the car on the road. Building the car and never visiting the workshop is another way of saying you build the prototype and leave it. I went into the harness side of this in [The Harness Is The Bottleneck](/the-harness-is-the-bottleneck/).

## Key takeaway to remember

Name who owns each AI workflow, and staff for the engineers who turn prototypes into workflows that last. Using AI is easy if you want a little value. Unlocking a lot of it is harder, because the work is process mapping, integration and maintenance rather than prompting, and it is worth it because the leverage is enormous. If you want the rollout to stick, somebody has to do the second phase.

## One thing to try this week

Draw one workflow. Pick the process in your business that eats a day a week, and write down its trigger, its main steps and its outcome. Mark where work waits, who checks it, and who fixes it when it breaks. Circle the missing owner or the longest wait, because that is where your rollout is stuck. Then find the prototype someone has already built for it, and ask the maintenance question before you build anything.

[^seibel]: Peter Seibel, [Let a 1,000 flowers bloom. Then rip 999 of them out by the roots.](https://gigamonkeys.com/flowers/){:target="_blank"}, written while he led the Engineering Effectiveness group at Twitter.

[^plandek]: Presented by Will Lytle (Plandek) and independently corroborated by Yigit Darcin (Trendyol) at CTO Craft Con, March 2026. Trendyol found that 90% of developers believed they were faster with AI, but measured delivery showed teams were 20% slower due to downstream overhead.

[^faros]: Faros.ai study of 10,000+ developers across 1,255 teams. Reported in Ankit Jain, [How to Kill the Code Review](https://www.latent.space/p/reviews-dead){:target="_blank"}, Latent Space, March 2026.

[^google]: [4 ways Gemini makes administrative chores quick and easy](https://blog.google/products-and-platforms/products/gemini/ai-navigate-bureaucracy/){:target="_blank"}, Google, 9 September 2026.

[^tunguz]: Tomasz Tunguz, [The $10B FDE Boom](https://tomtunguz.com/the-10b-fde-boom/){:target="_blank"}. Also the source for the observation that the vendors' investment in FDEs may become their moat.

[^vendors]: [Anthropic and OpenAI are both launching joint ventures for enterprise AI services](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/){:target="_blank"}, TechCrunch, May 2026. Ashley Capoot, [AWS puts $1 billion into new AI unit to embed engineers with customers, joining growing wave](https://www.cnbc.com/2026/06/30/aws-amazon-ai-forward-deployed-engineers.html){:target="_blank"}, CNBC, June 2026. The Google Cloud interview compression is from the Pragmatic Engineer piece in the next note.

[^pulse]: Gergely Orosz, [The Pulse: Forward Deployed Engineering heats up again](https://blog.pragmaticengineer.com/the-pulse-forward-deployed-engineering-heats-up-again/){:target="_blank"}, Pragmatic Engineer, May 2026.

[^xkcd]: Randall Munroe, [xkcd 1205, Is It Worth the Time?](https://xkcd.com/1205/){:target="_blank"}, CC BY-NC 2.5. The maintenance column is my addition.
