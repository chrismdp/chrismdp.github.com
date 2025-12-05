---
layout: post
title: "How to Structure Your Teams for AI"
date: 2025-12-04 14:00:00 +0000
categories:
- ai
- webinar
- team-topology
- leadership
image: /assets/img/tortoise-scooter-hare.png
---

On 4th December 2025, I gave a webinar about a question that every technical leader is wrestling with: how should we structure our teams now that AI has arrived? The session opened with contributions from attendees already experimenting with AI team structures. The stories were instructive: agentic teams burning through budgets with nothing to show for it, engineers using AI as advanced autocomplete without rethinking workflows, organisations unsure where to put the human in the loop. We can now do things faster than ever, but faster does not automatically mean better.

The core insight from the session: if coding speeds up but your organisation does not get faster, coding was never the bottleneck. So where has the constraint moved?

<!--more-->

## The Constraint Has Shifted

Since Agile and Cloud arrived, our organisational principles have been fairly static. We drew bounded contexts, built platform teams to support product teams, and used frameworks like [Team Topologies](https://teamtopologies.com/){:target="_blank"} to structure our organisations effectively. Those principles worked well for two decades.

Then AI showed up.

Suddenly prototypes drop into Slack from non-technical CEOs who built them over the weekend using Lovable. Developers write and deploy code faster than ever. But business outcomes are not increasing to match. The vendor invoices pile up whilst revenue stays flat. Your boss is reading McKinsey reports and wondering why the bottom line is getting worse.

Goldratt's Theory of Constraints from the 1980s explains what is happening. When you remove one bottleneck in any system, the constraint does not disappear. It moves randomly to another point within the system. If you focus on something that is not the constraint, things do not get faster. They can actually get slower as queues build up elsewhere.

This leads to a key insight. If we speed up coding and our organisation does not get faster, coding was never the constraint. Worse still, if we speed up something that was not the bottleneck, queues of work build up in other places and the organisation actually slows down.

If coding is no longer the bottleneck, where has it moved? The likely candidates are all human and organisational, not technical:

**Decision making processes.** If every proposal needs approval from a sales director, more proposals just means a longer queue.

**Strategic thinking.** Perhaps we do not know what we want fast enough. We reach the end of the work and realise what we built was not valuable.

**Team structure.** Perhaps the very organisation that helped us before is now hindering us.

The irony of AI is striking. By introducing human-like automation, it brings human work into greater focus. We have to think harder about how we interact, behave, and work with each other.

## The Big Decision: Hybridisation vs Amplification

Before restructuring, make sure structure is actually your biggest constraint. Reorganisations are expensive and cause anxiety. Most problems are not solved by another reorg.

But if structure is the constraint, you face a fundamental choice between two paths.

**Hybridisation** takes the solopreneur success stories to their logical conclusion. Break the structure completely. Give design tools to developers, developer tools to product managers. Train individuals to wear all hats. Create hybrids operating independently with AI, eliminating communication overhead entirely. What could be quicker than communicating in your own head?

**Amplification** keeps teams intact but powers them up. Smaller teams, more aligned, with each function amplified rather than removed.

The key question: will the communication overhead of having different types of team member neutralise the AI benefit of producing more quickly?

I think the answer is no. Hybridisation is dangerous. Here is why.

## Two Fatal Flaws of Hybridisation

### Ecosystem Collapse

Duncan Brown introduced this concept at [Agile Cambridge](https://mechanicalsurvival.com/blog/team-dynamics-after-ai/){:target="_blank"} this year. Consider a design system. Designers use it and contribute back to it. They encounter real problems, learn from actual use, and that learning flows back into the system. The design system gets stronger over time.

Now imagine developers using AI to consume that design system. They generate beautiful interfaces quickly. They ship products. Everything looks great.

But there is no contribution back. They only consume. The design system stops receiving feedback from actual use. It gets weaker over time. And eventually, the AI tools themselves get weaker because their foundation has gone stale.

This same pattern threatens internal libraries, data standards, documentation. All the shared ecosystems we depend on.

### Loss of Diverse Thought

Your skills are the senses through which you perceive problems. Designers see interaction problems. Developers see technical constraints. Product managers see customer needs. They look at the same thing but see completely different possibilities.

AI does not fight with you. Even when you ask it to disagree, it cannot truly challenge your intentions the way a human with a different perspective can. This leads to bias reinforcement.

Patrick Lencioni argues in "The Advantage" that unless teams occasionally apologise for taking disagreement too far, they do not have enough conflict. We need more of the right kind of conflict, not less. [Healthy teams need productive friction](/how-to-avoid-bad-startup-culture/) to build the right things.

I learned this the hard way. In 2015, I built a video game called Sol Trader entirely on my own. Design, engine, all the code. It was exhilarating. The codebase was wonderful. I was the consummate hare racing ahead.

The trouble was I built the wrong product. No one challenged my assumptions or spotted the problems I could not see. Moving fast is exhilarating but not necessarily productive.

## The Tortoise on a Scooter

If hybridisation creates hares running into walls, what does amplification look like?

I want tortoises on scooters. Slow, steady work by small multidisciplinary teams, given a power-up by AI. The steady coordination of the tortoise, with incredible new speed.

### Coders Become True Engineers

Coders can feel like superheroes. OpenAI built [AgentKit in six weeks](/openai-devday-where-value-lives-in-ai-agent-tooling/) instead of six months. Whole systems can be changed quickly. Test coverage becomes easier. Coders can think more strategically about architecture rather than getting lost in implementation details.

The speed means prioritisation and tickets become less important. You have a conversation about what to build and you build it that afternoon. The need to order everything carefully reduces.

For this to work, you must fix the underlying health metrics. Good linting, tests, CI. Minimal reviews to get code live. Feature flags for safe rollouts. If your code is hard for humans to work with, it will be hard for AI too.

### Product Managers Become Clairvoyant

Product managers are freed from card shuffling. If developers can build whatever is next quickly, the low-level prioritisation work that consumes so many product managers becomes less necessary.

They can use AI to hone customer questions and process insights from interviews. They can prototype their own systems using tools like Claude Code with internal components, creating throwaway prototypes to validate ideas before developers build the real thing.

This frees up time for genuine product strategy rather than backlog management.

### Designers Become Holistic

Design tools need the most work, but the direction is clear. Many designers I have worked with love strategic UX thinking but get constantly pulled back to layout work or fiddling with slides for marketing.

AI can take care of the routine, freeing designers to focus on problem solving and contributing back to design systems. Designers become truly strategic about user experience.

## The Common Thread: Strategy

The fundamental thread through all these roles is strategy. I believe strategic thinking will be the new constraint with AI.

Strategy is not goals or vision statements. It is a clear path to achieve those goals. And it is always best done in a group with diverse perspectives.

Imagine a team of two or three people: developer, product, design. Truly multidisciplinary, representing genuine diversity of thought. They push hard against groupthink. They work through friction to generate better decisions, better strategy, better products. Then they use AI to handle everything else.

The bottleneck is no longer "can we build it?" but "should we build it?" And more fundamentally: "what is the actual problem we are solving?"

## What Changes About Teams

Stream aligned teams get smaller. Artefact production is no longer the bottleneck, so two to three people becomes the new size.

They need more independence. They will get blocked more easily by external dependencies. Make sure they are well directed.

They need support. The latest [DORA report](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf){:target="_blank"} shows that the best AI teams ship faster but stability of releases is dropping. Teams will wobble and fall off more often.

Platform teams evolve from providing CI/CD and vendor integrations to building custom AI agents that encode your company context. They create intelligence layers specific to your organisation. Your version of coding assistants with your prompts, your workflows, your components. Custom tools that no external vendor could provide.

Enabling teams become critical. They ensure design systems and shared knowledge propagate. They bridge the AI capability gap, spreading patterns and tools across the organisation. They help teams understand when to use platform agents versus building their own.

## Three Things to Do Right Now

### Fix the Underlying Health Metrics

If your code is hard for humans to understand, assume it will be hard for AI to understand too. Use AI to reduce technical debt as a safe way to learn the technology. It is unconstrained by others, reasonably safe if you have tests, and helps you learn whilst improving the foundations that make AI effective.

As I explored in my [previous webinar on AI rollouts](/webinar-how-not-to-screw-up-your-ai-rollout/), AI amplifies what is already there. Fix the friction first.

### Beware the Lone Wolves

You will hear success stories about people shipping whole products in a week. Survivorship bias is strong. The reason they could move fast is because they did not have the whole business around them that you do.

Speed without direction equals waste. Many build the wrong thing fast. A portfolio approach works better: some people doing incremental improvements, some taking on strategic projects, and a few exploring what is possible at the edges.

### Build Agents With Model Independence in Mind

Build custom AI agents that amplify without homogenising. But maintain your freedom. Keep one eye on open models. [Open source models now cost 150 times less](/doing-real-work-with-ai-just-became-150x-cheaper/) than frontier models whilst delivering comparable performance.

Do not sign anything longer than three months with any vendor. Do not fall into using one ecosystem just because you already pay for it. Create experimentation teams whose job is to try everything.

## Key Takeaway to Remember

The constraint in your organisation has moved. If coding speeds up but your business outcomes stay flat, coding was never the bottleneck. Look for the human and organisational constraints: decision making, strategic thinking, team structure.

Reject hybridisation. Keep your multidisciplinary teams, make them smaller, help them think strategically, and support them properly with platform and enabling teams building custom AI capabilities.

The tortoise on a scooter. Steady coordination plus incredible speed.

## One Thing to Try This Week

Before your next planning session, ask your team: "If we could build anything instantly, what would we build?" The answers reveal whether your constraint is truly coding speed, or whether it is actually knowing what to build in the first place.
