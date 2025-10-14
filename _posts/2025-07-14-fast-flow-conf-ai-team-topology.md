---
layout: post
title: "The Tortoise on a Scooter: Why AI-First Teams Need Structure, Not Solo Hares"
date: 2025-10-14 12:00:00 +0000
categories:
- talk
- ai
- team-topology
- platform-engineering
event_name: "Fast Flow Conf UK 2025"
venue: "London"
talk_date: 2025-10-14
talk_url: "https://www.fastflowconf.com"
talk_title: "Vision for an AI-First Team Topology: How AI Fundamentally Transforms How We Organise Technical Teams"
image: /assets/img/tortoise-scooter-hare.png
---

*This post is based on a talk given on 14th October 2025 at [Fast Flow Conf UK](https://www.fastflowconf.com){:target="_blank"}.*

You did everything right. You read Team Topologies. You drew the Miro diagrams. You defined your bounded contexts, briefed new platform and enabling teams. You even hired a consultant or two. You completed the reorganisation. Things were working.

Then AI showed up.

Suddenly prototypes drop into Slack from stakeholders who built them over the weekend. Your developers write and deploy code faster than ever. But your organisation is not getting faster. Revenue is not increasing to match the new pace of coding.

<!--more-->

Your boss is reading McKinsey's latest report on AI productivity, looking at the vendor bills for all those new AI tools, and beginning to ask why the bottom line is getting worse not better.

What is going on?

## The Temptation of Hybridisation

You have heard stories of solos shipping faster. People doing more than ever before. Why not take this to the logical conclusion? Break the structure completely. Unleash teams of one, loaded up with tools, to achieve specific goals.

This is the path of hybridisation. Give design tools to developers. Give developer tools to product managers. Train individuals to wear all hats. Product and developer and designer hybrids, operating independently. This eliminates communication pathway issues. What could be quicker than communicating in your own head?

Or we go down the path of amplification. Keep teams intact, but powered up. Smaller, more aligned. Amplify each function rather than removing it.

The key question is this: will the added communication overhead of having different types of team member neutralise the AI benefit of producing more quickly?

I think the answer is no. Hybridisation is dangerous. Solo teams are deeply flawed. An AI first topology should not be a crowd of individuals. It still needs structure.

## Two Fatal Flaws of Hybridisation

### Ecosystem Collapse

Duncan Brown calls this [ecosystem collapse](https://mechanicalsurvival.com/blog/team-dynamics-after-ai/){:target="_blank"}. Think about the classic design system. Designers use the design system, and they contribute back to it. It is a read and write relationship. They encounter real problems, they learn from actual use, and that learning flows back into the system. The design system gets stronger over time.

However, developers use AI to consume design systems. They generate beautiful interfaces quickly. They ship products. Everything looks great.

But there is a problem: they are not contributing back.

They only consume. It is read only. They ship products, but the learning from real problems does not flow back.

The result? The design system gets weaker over time. It stops receiving feedback from actual use. And eventually, the AI tool itself gets weaker, because its foundation has gone stale.

This is not just about design systems. This same pattern threatens open source libraries, data standards, documentation. All the ecosystems we depend on.

### Loss of Diverse Thought

Your skills are the senses through which you perceive problems. A designer sees interaction problems. A developer sees technical constraints. A product manager sees customer needs. They are looking at the same thing, but they see completely different possibilities. They argue. They fight. They bring their own perspectives.

AI does not fight with you. Even when you ask AI to disagree, it cannot truly challenge your intentions the way a human with a different perspective can. Homogeneous thinking leads to bias reinforcement. And bias reinforcement leads to slower real progress.

You need humans who will actually push back. Not AI that politely suggests alternatives. Humans who will say "No, that is wrong" and mean it.

Most of our teams do not have enough conflict.

Patrick Lencioni, author of "The Five Dysfunctions of a Team", said in his latest book "The Advantage" that unless teams have to occasionally apologise for taking it too far, they are not creating enough conflict.[^lencioni] We need more of the right kind of conflict in our companies, not less. Solo AI people will not cut it.

[^lencioni]: I have written more about Lencioni's framework for [building healthy startup culture](/how-to-avoid-bad-startup-culture/).

### The Hare's Mistake

You have heard the story of the race between the hare and the tortoise, where the hare races to the finish only to become overconfident and unwittingly allow the tortoise to win the race.

Instead of real meaningful progress, with hybridisation you will have a lot of hares running around hitting walls.

In 2015, I built [Sol Trader](/tags/#sol-trader) entirely on my own. Design, engine, code in C. All me. It was a glorious ride, exhilarating, great fun. I was the consummate hare.

Trouble was, I built the wrong product.

I learnt moving fast is exhilarating but not necessarily productive. No one to challenge my assumptions, spot the problems I could not see.

## Amplification: The Tortoise Gets Wheels

So if hybridisation creates hares, how instead do we amplify our stream aligned teams? What do amplified teams look like?

With amplification we keep the stable pace of the tortoise, but they get a whole new set of wheels.

### Coders Become Strategic

Coders can feel like superheroes, where coding itself is no longer the constraint.

Whole systems can be built quickly, as OpenAI demonstrated when they [built AgentKit in six weeks](/openai-devday-where-value-lives-in-ai-agent-tooling/){:target="_blank"} instead of six months.

Coders are able to strategically change whole systems much quicker, and still manage to keep an eye on technical debt. Test coverage becomes so much easier. They can think more about the architecture strategically.

They can move so quickly that prioritisation and tickets become less important. You have a conversation, you build it that afternoon. This means the need to order everything reduces.

For this to work, you must fix the underlying health metrics. Make sure there is good linting, tests and CI. Get AI to help you get there first, to unlock the AI enabled coder.

### Product Managers Become Clairvoyant

Product managers can feel like clairvoyants.

They are freed from the prioritisation work as developers can build whatever is next fast.

They can use AI to hone their customer questions, and process their insights.

They can prototype their own systems to test with customers themselves, and communicate with developers what they want.

This next part is more aspirational, but the direction is clear. They could use Digital Twin ICPs built by the platform team to ask AI what customers need as a quicker validation step. [A recent study](https://arxiv.org/html/2510.08338v1){:target="_blank"} shows this does in fact work.[^digital-twins]

[^digital-twins]: The research demonstrates that AI models can simulate customer personas with surprising accuracy, achieving 85% alignment with real customer responses in product validation tests. This means product managers could run initial validation rounds with AI twins before investing time in actual customer interviews, dramatically accelerating the discovery cycle.

They free up time for true product strategy.

### Designers Become Holistic

Designers can be truly holistic, and really think about their systems.

Many designers that I have worked with love this part the most, but seem pulled constantly back to layout, or fiddling with slides for marketing or executives.

Now AI can take care of the routine, they are freer to work on problem solving and contributing back to the design system based on what they have learned.

Design tools need the most work, but this is the direction of travel. Designers are being freed to be truly strategic.

## Strategy Becomes the Bottleneck

The fundamental thread through these: strategic. I believe strategy and thinking well will be the new constraint with AI. Strategy is not goals or vision statements, it is a path to achieve those goals. Here again diverse perspectives will win.

The bottleneck is no longer "can we build it?" but "should we build it?". And more fundamentally: "what is the actual problem we are solving?"

You must now answer this question faster, but it did not get easier to answer. The challenge of deciding what matters becomes even more critical when [everything can be built quickly](/coding-with-ai/){:target="_blank"}. We will be limited and held back by argument and consensus. Rigorous strategic debate, that is exactly the kind of thing that helps teams build the right thing.

## What Changes About Stream Aligned Teams

So amplification of stream aligned teams rather than replacement with solo hares.

What does change about stream aligned teams?

They get smaller. Artefact production is not the bottleneck, strategic thinking and discussion is, so two to three people is the new size.

They need more independence. They will be blocked more easily. Make sure they are really directed well.

They need support. Just be aware they will wobble and fall off more often. The latest DORA report states that the best AI teams are shipping faster yet stability of releases is dropping.[^dora-stability]

[^dora-stability]: The [2025 DORA Report](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf){:target="_blank"} found that whilst AI-assisted teams show significant improvements in deployment frequency and lead time, they also experience a slight decline in change failure rates. This suggests teams are moving faster but their quality processes have not yet caught up. The solution is not to slow down, but to invest in better testing, CI/CD, and observability infrastructure.

## Platform Teams Evolve

Platform teams are evolving. In the old model, they delivered vendor integrations, maintained cloud infrastructure, provided general purpose tools, oversaw CI and CD workflows.

The best teams were creating amazing internal tools to help stream aligned teams build, deploy and run services on steroids.

AI Agents are a platform team's dream. They can build custom AI agents that encode your company context. They create intelligence layers specific to your organisation. They provide governance and intelligence, not just vendor integrations.

What does this actually look like?

Building some of those agents we talked about product teams using. What about company specific code generation trained on your patterns and standards. Intelligent data analysis tools. Chat agents that understand your business model. Context aware documentation and discovery tools. Digital sovereignty. Keep an eye on open models. This protects against AI vendor lock in.[^open-models] It is super important with this new tech to keep an eye on the vendors and retain control. Custom agents we have not even thought of yet.

[^open-models]: Open source AI models [now cost 150 times less](/doing-real-work-with-ai-just-became-150x-cheaper/){:target="_blank"} than frontier models whilst delivering comparable performance. This economic shift makes digital sovereignty realistic for most organisations. By building on open models, you avoid vendor lock-in, maintain control over your data, and can run models on your own infrastructure. The gap between open and closed models is closing rapidly, making this the right time to prioritise independence.

Any investment in your platform team building custom AI creates massive amplification across all your stream aligned teams. One platform team can multiply the capability of dozens of product teams.

## Enabling Teams Become Critical

Now, enabling and empowering teams become critical in this model.

Remember the concern about read only consumption? Enabling teams solve this. They ensure design systems, the standards and shared knowledge propagate. They ensure the foundations remain strong as more teams consume them.

Enabling teams bridge the AI capability gap. Not everyone needs to be an AI expert. Enabling teams spread patterns and tools across the organisation. They focus on making AI accessible without requiring deep technical knowledge. They help teams understand when to use platform agents versus build their own.

So we have a three layer model:

Stream aligned teams doing the product work with amplified multidisciplinary specialists. Platform teams building custom AI agents and intelligence layers. Enabling teams taking those platform capabilities and helping stream aligned teams adopt them effectively and diffusing knowledge and sharing.

This is standard Team Topologies, but with AI as a major new capability area that needs explicit enabling and platform support. You can use AI as a trojan horse here. Say you are changing for AI and actually bring in good practice.

## What This Looks Like in Practice

Imagine teams of three people. Maybe even two. Developer, product, design. Truly multidisciplinary. They represent genuine diversity of thought. These are quite different people who see things differently. And that diversity pushes hard against status quo and groupthink.

They work differently. They will fall out sometimes, because they have genuinely different perspectives. But they will always be respectful, because psychological safety is the foundation.

That friction generates better decisions, better strategy, better products. And they move from conversation to shipped product in hours, not weeks.

They are supported by the organisation. Enabling teams are there to make them even faster. Training, patterns, custom adaptations, capability bridging. Platform teams endlessly supply them with improved agents. These agents take care of the grunt work quickly. Intelligence layers that understand company context. Custom tools that no vendor could provide.

The result? Small teams with massive impact. Fast flow that is actually sustainable. Thousands of quick experiments.

Strategy becomes the work, not a separate phase. Juniors rotate between these teams to learn strategic thinking from day one. Everyone contributes back to the ecosystems we depend on.

The tortoise on the scooter. Steady coordination plus incredible speed.

## Three Things to Do Right Now

### First: Fix the Underlying Health Metrics

The [2025 DORA Report](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf){:target="_blank"} says it clearly: "AI does not fix a team, it amplifies what is already there."

The best teams get faster with AI. It is a force multiplier.

But AI still has a negative relationship with software delivery stability.

Your job? Help fix the friction first. Improve linting, CI and CD, testing, deployment pipelines. Use AI adoption as the forcing function. Tell your CEO that if you want to go faster with AI, then you need to invest in the platform to make it happen. Send them to me if you need more ammunition.

Refactoring tech debt is a great place to start learning about AI. It is unconstrained by others. It is a reasonable place to experiment whilst improving the fundamentals.[^refactoring-ai]

[^refactoring-ai]: When using AI for refactoring, start with well-tested code that has good coverage. Ask AI to improve code structure whilst keeping tests green. Focus on extracting methods, improving naming, removing duplication, and modernising patterns. The safety net of existing tests means you can move fast whilst learning what AI does well. This builds confidence before tackling more complex greenfield work.

### Second: Amplify Your Teams

Beware the lone wolf success stories. You will hear isolated stories of individuals succeeding on their own. They are either exceptional or got lucky. Survivorship bias is strong.

Many build the wrong thing fast. I know this from experience with [Sol Trader](/tags/#sol-trader). [CB Insights data](https://www.cbinsights.com/research/startup-failure-post-mortem/){:target="_blank"} shows 90% of startups fail, often due to lack of market fit.[^startup-failure] Solo builders suffer from confirmation bias without diverse perspectives to challenge their assumptions.

[^startup-failure]: The 90% failure rate is measured over a 10-year period, with the peak danger zone being years 2-5. Most failures are not sudden collapses but slow deaths from building something nobody wants. Diverse teams become most critical during the discovery and product-market fit phase, when challenging assumptions and exploring alternatives determines success. Solo builders can execute brilliantly on the wrong idea, whilst diverse teams argue their way to the right one.

Speed without direction equals waste.

### Third: Build Agents With an Eye on Model Independence

You are uniquely positioned to enable this future. Build custom AI agents that amplify without homogenising. Create intelligence layers that make specialists superhuman.

But maintain your freedom. Keep one eye on open models. Use frontier models tactically, but do not couple tightly to specific APIs. Be careful buying too many services from model vendors. They have every incentive to lock you into their ecosystem.

Support the enabling teams who will spread this capability. Preserve diversity whilst enabling speed.

## The Vision

Reject hybridisation. Keep your stream aligned teams. Make them smaller, help them think strategically in their area, support them properly.

This is the vision. This is where we are headed. Here is to AI first teams that you have made insanely productive and happy.
