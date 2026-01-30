---
layout: post
title: "Parallel AI Agents Create Unusable Code"
date: 2025-07-31 12:00:00 +0000
permalink: /parallel-ai-agents-create-unusable-code/
redirect_from: /ai-swarms-failed-toyota-vs-ford-development/
image: /assets/img/ai-swarms-failed-toyota-vs-ford.png
categories:
- ai
- engineering
- productivity
- sol trader
---

**AI swarms are not faster.** They create massive cognitive load, produce duplicate code, and optimise for the wrong thing entirely.

I spent a few hours experimenting with running four Claude instances in parallel to build a personal knowledge management system. It was a deliberate test to push PRD-driven development to its logical extreme and see if parallelisation could work. The result? A completely unusable codebase, some valuable lessons, and unexpected insights about the difference between manufacturing cars and building software.

<!--more-->

## The Seductive Promise of AI Swarms

The idea seemed brilliant: take a Product Requirements Document, have AI break it into parallelisable chunks, then unleash multiple Claude instances using Claude Squad to write different parts simultaneously. Maximum throughput, minimum time. What could go wrong? This approach is everywhere right now. Teams across the industry are writing comprehensive PRDs, feeding them to AI systems, and expecting magic to happen. The appeal was undeniable. Instead of waiting for one AI to work through problems sequentially, I could have four working in parallel, each tackling different aspects of the system. It felt like the natural evolution of AI-assisted development.

Everything, as it turns out, could go wrong. Perhaps all these teams using PRD-driven AI development are making the same fundamental mistake.

## The Experiment: Four Claudes, One Learning Experience  

I was building a Python application using the [Graphiti](https://github.com/getzep/graphiti) graph database library. The plan was elegant in its simplicity: feed the PRD to Claude, let it identify parallelisation opportunities, spin up four Claude instances working on different stories, then watch the code flow like a well-oiled assembly line. They would work independently on their domains and I would orchestrate the integration. I wanted to test whether this approach could actually deliver the productivity gains that PRD-driven parallel development promises.

For a few hours, I managed four parallel streams of development, each with full project context and legitimate, separate concerns. On paper, it should have worked. The technical architecture supported this kind of separation. The stories were genuinely independent. Each Claude instance had access to the same requirements and codebase context. The coordination overhead should have been minimal.

## The Cognitive Load Problem

The reality hit me quickly: context switching every few seconds. That is not hyperbole. My brain was burning from the constant task switching required to keep four separate development streams moving forward. I became the bottleneck in my own optimisation attempt, frantically jumping between conversations, trying to make product decisions on the fly while simultaneously managing technical coordination.

While the Claudes churned out code, I found myself constantly making judgement calls: Should this be a REST endpoint or GraphQL? What should the user actually be able to do with this feature? How do these four different approaches fit together? How should the graph relationships work between different node types? These were just the obvious decisions. There were hundreds of smaller choices that emerged during development: error handling approaches, data validation strategies, API response formats, authentication flows, logging patterns. Trying to specify all of these upfront in a PRD would have created an unwieldy document that still missed the contextual nuances that only emerged during implementation. The problem was not technical coordination, which actually worked reasonably well. The problem was that **product decisions cannot be parallelised**.

I was trying to figure out what I wanted the project to do while simultaneously building it. These were not engineering problems to be solved in parallel. They were sequential human judgements about user needs, system design, and product direction. Each decision required context from the others, creating dependencies that destroyed the parallelisation benefits. I spent zero time writing code myself. The entire session was consumed by my own brain trying to keep track of everything and make coherent decisions across four different contexts.

## The Duplication Discovery

When I finally tried to integrate everything, I discovered something fascinating and frustrating. One Claude instance had essentially re-implemented the entire Graphiti library without actually using Graphiti. The code looked professional, compiled cleanly, and even had decent architecture. But it was completely redundant with work that another instance was doing at a higher level, creating an entirely parallel implementation of graph operations that would never be needed.

Because each Claude was optimising for its own slice of the problem, none of them could see the forest for the trees. Each instance interpreted the shared context slightly differently and could not get the boundaries quite right between the stories. They generated sophisticated solutions that overlapped in subtle ways with what other instances were building. The application ended up with multiple approaches to similar problems because I had not been specific enough about the boundaries and independence between stories. But here is the crucial insight: specifying those boundaries with sufficient precision upfront is extraordinarily difficult, perhaps impossible. Something felt off during development, but I was too overwhelmed by context switching to identify what was happening. I am experienced enough at code review to recognise over-duplication, but I was too buried in orchestration to notice it happening in real time. The experiment had taught me exactly what I wanted to know: this approach does not work.

## Toyota vs Ford: The Key That Could Unlock AI Swarms

This experience reminded me of a fundamental shift in manufacturing philosophy that happened over several decades in the automotive industry. Henry Ford revolutionised manufacturing in 1913 with the moving assembly line, creating the first mass production system that could produce standardised products at unprecedented scale and low cost. Ford's system was a push-based approach: make a big plan, forecast demand, break production into standardised pieces, and push work through the assembly line to build inventory based on predicted market needs.

Toyota studied Ford's system intensively but identified a critical flaw: standardised products could not meet all customer demands, and push-based production created massive inventory waste. Starting in the 1950s, Toyota developed what became known as the Toyota Production System, built around a revolutionary pull-based philosophy. Instead of forecasting and pushing production, Toyota's Just-in-Time system only built what was needed, when it was needed, in the amount needed, based on actual customer demand pulling requirements through the system. This "supermarket supply method" meant that subsequent processes would take only what they needed from earlier processes, eliminating overproduction and inventory pile-up.

The parallels to my failed AI swarm experiment were striking. I had implemented push-based development: plan everything upfront in the PRD, parallelise based on technical architecture, push work through multiple AI streams, and optimise for code output. What I should have been doing was pull-based development: start with actual user needs, build only what is required for those needs, let requirements pull implementation decisions through the system, and optimise for problem solving rather than solution building.

**AI swarms optimise for the wrong metric entirely. They maximise code production when what you actually need is problem understanding.** This is the fundamental insight that changed my approach to AI-assisted development. The goal is not to produce more code faster. The goal is to understand and solve problems more effectively.

## The Battle Scars: What I Learned

The most painful lessons are often the most valuable. Here are the hard-won insights from my experiment:

**Parallelisation is not always faster.** Work-in-progress limits exist for good reasons, and having four streams of development created four streams of decisions I had to make simultaneously, destroying any speed gains through cognitive overhead.

**Product work cannot be parallelised.** Understanding what users need and how systems should fit together requires sequential human judgement that builds on previous decisions, creating dependencies that eliminate the benefits of parallel development.

**Context is everything, but context is expensive.** Full project context became a liability rather than an asset because it multiplied the cognitive load of each decision by the number of parallel streams.

**AI optimises for code generation, not problem solving.** AI instances will happily generate sophisticated solutions to problems that do not need to exist or have already been solved elsewhere in the system.

**Integration hell is real and inevitable.** Code that looks excellent in isolation can be completely incompatible when you try to merge it, leading to architectural mismatches and requiring complete rewrites rather than simple merging.

## The New Approach: Pull-Based AI Development

I am restarting the project with a completely different methodology:

1. **Identify three specific use cases** that must work
2. **Work backwards** from those use cases to figure out what needs to be built
3. **Build only what is needed** to satisfy those use cases
4. **Let requirements pull implementation decisions**, not the other way around

No more PRDs. No more parallelisation. No more push-based planning.

Instead: real user scenarios, behaviour-driven development, and just-in-time implementation decisions.

It will be interesting to see if this pull-based approach works better. I remember from my games and high-performance coding days learning from very experienced game developers how they manage complexity, which is quite different to our traditional SDLC. No tests, but they tend to write usage code first, creating only enough to test their use case manually, then move on. Eerily similar to BDD and good TDD workflows, arrived at from a totally different perspective.

I learned this approach from <a href="https://www.youtube.com/@MollyRocket" target="_blank">Casey Muratori</a>'s Handmade Hero (<a href="https://guide.handmadehero.org/" target="_blank">episode guide</a>, <a href="https://www.youtube.com/watch?v=F3ntGDm6hOs" target="_blank">first video</a>), an excellent YouTube series that I watched hundreds of hours of when I was writing <a href="https://store.steampowered.com/app/396680/Sol_Trader/" target="_blank">Sol Trader</a>. Casey demonstrates a pull-based development approach in real time: start with what you need to see on screen, work backwards to implement only what is required, and let the usage drive the architecture. No upfront design documents, no parallel development streams, just methodical problem-solving driven by actual requirements.

I have identified my first use case, but that is a story for another post.

## The Bottom Line

AI swarms feel like productivity, but they are productivity theatre. They optimise for the feeling of progress rather than actual progress. The entire industry seems to have fallen for the same trap: write a comprehensive PRD, break it down, parallelise the work, and expect better results. But if PRDs worked well for AI development, why are so many teams struggling with the same coordination problems, integration nightmares, and duplicated effort that I experienced?

The future of AI-assisted development is not about running more AI instances in parallel or writing better PRDs. It is about using AI more intelligently to understand problems before rushing to implement solutions. Toyota figured this out for manufacturing forty years ago. Perhaps it is time we applied the same principles to software development and questioned whether the PRD-first approach that everyone is using actually works.

**Next time you are tempted to parallelise your AI development, ask yourself: am I optimising for code output, or am I optimising for problem understanding?**

The answer might save you from your own failed experiment. It might also make you question whether the conventional wisdom about AI development that everyone else is following is actually correct.
