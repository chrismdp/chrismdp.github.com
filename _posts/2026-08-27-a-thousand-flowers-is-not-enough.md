---
layout: post
title: "A Thousand Flowers Is Not Enough"
date: 2026-08-27 07:00:00 +0000
categories:
- ai
- leadership
- strategy
image: /assets/img/let-a-thousand-flowers-bloom-engineers.jpg
image_portrait: true
---

AI companies have committed nearly $10bn in the last year to Forward Deployed Engineering teams. OpenAI has bought Tomoro and Northslope outright.[^openai] Anthropic launched a services firm with Blackstone, Goldman Sachs and Hellman & Friedman behind it, explicitly aimed at mid-size companies.[^anthropic] AWS is standing up its own unit.[^aws] Google Cloud compressed its FDE interview process from weeks down to two days, which tells you how badly they want the people.[^pulse]

For something that was supposed to replace human work, that is a lot of humans to hire. It tells us where the hard part of an AI rollout really is, and it is extra cost that is not yet in that many AI budgets.

<!--more-->

## The Gap Has A Price

A Forward Deployed Engineer ("FDE") is a vendor's engineer who works inside your company rather than behind a support desk[^fde]. They map how your work happens, wire the model into your systems and data, decide what the agent can see and when a human reviews it, and stay until it runs in production.

Jason Lemkin puts it well: the single biggest variable in whether an agent works is not the model, the prompt or even the vendor, it is whether you get a real human from the vendor helping you deploy it.[^lemkin] The number he cites is Zendesk data showing enterprise customers with proper deployment support reaching 60 to 80% automation rates, while self-serve customers land around 20%.

The reason is not mysterious:

- To automate a task you need someone expert in that task to work out how AI helps.
- To automate a workflow properly you need engineers to build a secure and compliant version of it.

Neither works without the other. An expert without engineers produces a prototype nobody can safely run, and engineers without the expert produce a beautifully built version of the wrong process that no one uses.


A two-tier world for workflow replacement is currently forming. Below roughly 5,000 employees, most vendors hand you documentation and an onboarding flow and wish you well. The huge companies get deployment support from that $10bn splurge, and everyone else has to make do.

This post is about the second group - how do we build proper repeatable workflows that save us time if we are not 5,000 people?

## 1. Let A Thousand Flowers Bloom...

Start by rolling out a decent AI tool to everyone, and provide kickstart training and coaching alongside it. (I went through the whole sequence, and the ways it goes wrong, in [my webinar on how not to screw up your AI rollout](/webinar-how-not-to-screw-up-your-ai-rollout/).) Encourage early automations and artefacts, while being clear with everyone that these are prototypes. Build a culture of sharing wins, and note that this means considerably more than a Slack channel nobody reads after week three. Measure and observe usage, and learn from the key users who are automating their own workflows.

There is a famous article about engineering at Twitter that describes exactly this process, and calls it letting a thousand flowers bloom.[^seibel] The phrase is itself a slight variation on a speech by Mao Zedong in the 1950s. One team uses Copilot as autocomplete and calls it a day. Another runs agents in tight loops with tests and reviews. A product owner starts prototyping real software instead of mocking screens. A support team turns recurring tickets into automation without telling anyone, because they know exactly where the work hurts and nobody in the centre of excellence ever asked them. A marketing team starts producing content. Everyone starts producing emails that look suspiciously like AI.

It feels productive, and it is genuinely useful as discovery and communication artefacts, but the organisation often still moves at the same speed, because none of it has become anything anyone else can use.

Two things stop the flowers growing wild becoming a well maintained garden:

1. Everyone builds the same workflow slightly differently, so there is no shared process and nothing stable to improve. Each version is tied to the person who made it, sharing is rudimentary, and nobody can manage the sprawl. Ten people solve the same problem ten times, because none of the previous solutions are findable or trustworthy enough to reuse.

2. Prototypes are built by people who do not know where or how they can fail. An executive at one company I spoke to built a tool to visualise their client work and asked to see it from home. The AI obliged and put it behind a _public link_, and the company then had a data exposure on its hands. A non-specialist can now build the feature before they understand the failure modes - it appears to work, but the failures are hidden from them.

{% include inline-image.html src="/assets/img/personal-ai-coworker-prototype-market.jpg" alt="Market stalls selling rival personal AI coworker products, each one a stack of cardboard boxes labelled Gmail, Word, Excel and Teams gaffer-taped to a laptop, with a book of SKILLS propped against the table. The products on sale are themselves prototypes." align="right" width="45%" caption="Est. 2024, and still held together with gaffer tape." %}

The AI tools we currently have are designed for this first stage. They are still stuck together and brilliant for simple prototypes, but they are still prototypes themselves. They are not ready to allow anyone to build real software with them. We're still very early!

You still need this first stage, because it is the best way to find out how AI might influence people's work. Keep the prototypes fast and loose, and then move on to the part that rarely gets budgeted.

## 2. ...Then Bring In Proper Engineers

Build AI-in-product capability inside engineering, and build a platform team, your own internal "FDE" function, to take on use cases across the business. This is the platform team shape I set out in [why AI-fast teams still ship slowly](/why-ai-fast-teams-still-ship-slowly/), pointed inwards at your own tooling rather than outwards at a product. Point that team at the prototypes people have already built. Second the key prototype owners into the platform team, so the knowledge travels with the person rather than being written up and lost. Then rebuild the winners in a stable and secure way and deploy them across teams.

The platform team industrialises the prototypes that already proved themselves and lets the rest die, which is a much better brief than inventing use cases in a room. It also inverts the usual failure of internal platform work, where a team builds what it imagines colleagues need and then spends a year trying to persuade anyone to adopt it. Here the adoption evidence arrives before the build does.

Gergely Orosz's read on the FDE roles being hired right now is roughly a quarter coding, half integration and plumbing, and a quarter customer hand-holding[^pulse] - so we need to staff this team accordingly. People who love messy complexity will do better than your strongest architect.

Palantir's bootcamp model for their FDEs is worth stealing: five days, the customer's own real data, and a working production deployment at the end. Real data and a real deployment are the two bits an internal workshop tends to drop, and they are the two doing the work. A week spent on sample data ending in a demo teaches your team that AI is impressive. A week spent on real data ending in something running teaches them what it takes to ship.

## Retain Ownership Of Your Work

If you are hiring external people for any of this, or you are lucky or large enough to get direct support from a vendor, be careful that you still own your work at the end.

An embedded engineer, whether they arrive from a vendor, a hyperscaler or a consultancy, sees more of your company than almost anyone else. They map your real processes rather than the ones in the handbook, see the formal architecture and the informal workaround, build your evaluations, capture your traces and learn your failure modes.

That is what makes the help valuable, and also how it becomes the lock-in. Tomasz Tunguz points out that FDE investment may itself become the moat.[^tunguz] Switching cost becomes institutional rather than technical, because the knowledge of how your work gets done now lives partly in someone else's team. This is the same trap I described in [my webinar on escaping the great AI lock-in](/webinar-escape-the-great-ai-lock-in/), arriving through the front door with a helpful smile.

So ask these questions before they start (rather than after they leave!)

- Who owns the workflow maps once the engagement ends?
- Who owns the evaluations, traces, exceptions and integration patterns created during deployment?
- Can we run, improve and re-platform this workflow without them?
- Is this transferring capability into our people, or becoming our AI operating layer?

Ensure the artefacts are named as yours in the contract and someone internal alongside anyone external from day one, so that you own a capability rather than renting your own work practices for ever afterward.

## Turn The Flowers Into A Garden

We are still learning how AI can impact work. We need a discovery phase. But in order to embed these learnings into the backbone of our companies we need proper software, and we need engineers to help us get there.

We need to move beyond what Robert Glaser describes as the messy middle: the phase where the licences have landed, AI use is everywhere and uneven, and nothing has changed yet.[^glaser] Who moves discoveries from individuals to teams to organisational capability?

If the answer in your company is nobody, you will get a thousand flowers, but it will never be a garden.

[^fde]: Palantir coined the term, and the role is a recasting of the solutions engineer that enterprise vendors have fielded for decades rather than a new invention. Orosz's read on the roles being hired now is that they are increasingly indistinguishable from consultants and solutions architects.

[^openai]: OpenAI's deployment arm took on 150 forward deployed engineers with Tomoro, an applied AI consultancy in Edinburgh, and then bought Northslope. See [Anthropic and OpenAI are both launching joint ventures for enterprise AI services](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/){:target="_blank"}, TechCrunch, and [OpenAI buys Northslope to sell AI adoption, not models](https://thenextweb.com/news/openai-northslope-acquisition-enterprise-ai-deployment){:target="_blank"}.

[^anthropic]: [Building a new enterprise AI services company with Blackstone, Hellman & Friedman, and Goldman Sachs](https://www.anthropic.com/news/enterprise-ai-services-company){:target="_blank"}, Anthropic.

[^aws]: Ashley Capoot, [AWS puts $1 billion into new AI unit to embed engineers with customers, joining growing wave](https://www.cnbc.com/2026/06/30/aws-amazon-ai-forward-deployed-engineers.html){:target="_blank"}, CNBC, June 2026.

[^pulse]: Gergely Orosz, [The Pulse: Forward Deployed Engineering heats up again](https://blog.pragmaticengineer.com/the-pulse-forward-deployed-engineering-heats-up-again/){:target="_blank"}, Pragmatic Engineer, May 2026. Source for both the Google Cloud interview compression and the split of FDE work.

[^lemkin]: Jason Lemkin, [Who gets an FDE and who doesn't](https://www.saastr.com/who-gets-an-fde-and-who-doesnt-the-great-b2b-ai-debate-right-now/){:target="_blank"}, SaaStr. The 60-80% versus 20% figures are Zendesk's own, so treat them as a vendor's account of its own product rather than an independent measurement.

[^tunguz]: Tomasz Tunguz, [The $10B FDE Boom](https://tomtunguz.com/the-10b-fde-boom/){:target="_blank"}. Also the source for the spending figure at the top of this post.

[^seibel]: Peter Seibel, [Let a 1,000 flowers bloom. Then rip 999 of them out by the roots.](https://gigamonkeys.com/flowers/){:target="_blank"}, written while he led the Engineering Effectiveness group at Twitter. His second stage is the same one this post argues for: once the sprawl is doing more harm than good, pick the tools you will support and support the heck out of them. Mao's original was a hundred flowers, in 1956.

[^glaser]: Robert Glaser, [When everyone has AI and the company still learns nothing](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/){:target="_blank"}.
