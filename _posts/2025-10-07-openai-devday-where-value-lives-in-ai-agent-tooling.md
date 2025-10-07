---
layout: post
title: "Why AgentKit Creates the Market for Production Agent Tools"
date: 2025-10-07 09:00:00 +0000
image: /assets/img/wardley-map-openai-devday.png
image_portrait: true
categories:
- ai
- strategy
- business
- agents
---

OpenAI's DevDay 2025 yesterday released AgentKit, a suite of tools designed to build AI agents in minutes. Many people interpret this as OpenAI "owning" the AI agent market, threatening anyone building agent tooling. The reality is more interesting.

AgentKit creates the market for production agent building tools rather than threatening it. By commoditising prototyping, OpenAI expands the pool of teams who discover they need custom-built agents for production. These are not competing tools. They are sequential stages in a natural progression.

<!--more-->

## What OpenAI Actually Released

[AgentKit](https://openai.com/index/introducing-agentkit/){:target="_blank"} is OpenAI's complete toolkit for agent development. Sam Altman positioned it as "a complete set of building blocks available in the OpenAI platform designed to help you take agents from prototype to production."

The headline feature is Agent Builder, a visual canvas for designing agent workflows. OpenAI describes it as "like Canva for building agents." You drag and drop nodes, connect tools, configure guardrails, and preview your agent before deployment. During the keynote, an OpenAI engineer built an entire AI workflow and two AI agents live on stage in eight minutes.

ChatKit provides embeddable chat interfaces that developers can customise to match their brand. Canva reported they "saved over two weeks of time building a support agent" and integrated it "in less than an hour."

The Connector Registry centralises data management across workspaces, consolidating sources like Dropbox, Google Drive, SharePoint, and third-party integrations into a single admin panel.

Enhanced Evals now includes datasets, trace grading, automated prompt optimisation, and third-party model support. The automated prompt optimisation is particularly interesting - OpenAI confirmed they are using GEPA (Gradient-free Evolution for Prompt Adaptation), which was new to me. This validates the approach I have been building into [Kaijo](/kaijo/) - using evaluation data to automatically improve prompts rather than manual prompt engineering. Carlyle reported that "the evaluation platform cut development time on our multi-agent due diligence framework by over 50%, and increased agent accuracy 30%."

Everything ships at standard API pricing. OpenAI clearly designed this to maximise adoption rather than extract immediate revenue from tooling.

## The Strategic Landscape: A Wardley Map View

Understanding where this positions OpenAI requires mapping the AI agent tooling value chain. I built a Wardley map to analyse how AgentKit reshapes this landscape.[^wardley]

[^wardley]: Wardley mapping is a strategic tool that visualises value chains and component evolution. The vertical axis represents the value chain from user needs at the top to infrastructure at the bottom. The horizontal axis shows evolution from genesis through custom-built and product to commodity.

At the top of the map sit five anchor user needs that drive all agent development:

- **Reliability** - agents must work consistently at scale
- **Security** - protecting data and preventing manipulation
- **Cost** - economical enough to sustain long-term
- **Capability** - solving problems that justify the complexity
- **Quick Iteration** - testing ideas fast before committing resources

These needs connect to two distinct implementation approaches sitting in the middle of the map:

**Workflow tools** (like AgentKit, [n8n](https://n8n.io){:target="_blank"}, and similar platforms) optimise for quick iteration. They provide visual builders, pre-built integrations, and standardised patterns. AgentKit is dragging this entire category further into product space, accelerating commoditisation. The eight-minute live demo signals that workflow tools are becoming expected table stakes rather than competitive advantages.

**Custom-built agents** sit adjacent but serve different needs. These are agents you build from scratch using evaluation frameworks, model-agnostic platforms, and prompt optimisation tools. Custom agents connect to reliability, security, cost, and capability needs that workflow tools struggle to address at production scale.

Supporting both approaches are evolving capabilities:

- **Evaluation frameworks** - systematic testing and quality measurement
- **Model agnosticism** - flexibility across vendors
- **Prompt optimisation** - consistent performance
- **Third-party integrations** - n8n's 400+ connectors create strong network effects

At the infrastructure layer sit LLM APIs and open source LLMs. OpenAI and similar providers have reached market status. Open source LLMs are evolving rapidly toward commodity, becoming cheaper and more powerful whilst ticking both cost and security requirements that once favoured proprietary models.

![Wardley Map: OpenAI DevDay Impact on AI Agent Tooling](/assets/img/wardley-map-openai-devday.png)

Three critical insights emerge from this map that explain market dynamics for the next 12 to 18 months.

## The Natural Customer Progression

The customer journey is not a choice between AgentKit and production tools. It is a progression through sequential stages where different tools serve different needs.

**Stage one: prototype with AgentKit.** You have an idea for an agent. You need to validate it quickly. Does this approach work? Will stakeholders support it? Can we demonstrate value before committing significant resources? AgentKit excels here. Eight minutes to a working demo. Minimal code. Impressive results. Lock-in is acceptable because prototypes are throwaway experiments.

**Stage two: hit limitations.** Your prototype succeeds. Now you need to deploy it to real users handling real requests. You discover AgentKit's constraints. You cannot evaluate systematically across different models. You cannot optimise costs by switching vendors when pricing changes. You cannot implement security boundaries beyond basic guardrails. You cannot customise behaviour for domain-specific requirements. The prototype that worked brilliantly in demos starts failing in ways you never imagined during prototyping.

**Stage three: build custom agents for production.** You recognise you need control that workflow tools cannot provide. You need evaluation frameworks that understand your domain. You need model agnosticism so vendor lock-in does not create business risk. You need prompt optimisation that works across model versions. You need to build agents properly for production rather than scaling prototypes.

These stages are sequential, not competitive. The message for anyone building production agent tools should be: "Prototyped with AgentKit? Now build it properly with our platform."

The larger OpenAI grows the prototype pool, the larger the pool of teams discovering they need custom-built agents for production. AgentKit creates the market by helping teams validate that agents solve their problems. Once validated, those teams need proper tools to deploy reliably.

This is why AgentKit ships at standard API pricing. OpenAI is not monetising prototyping tools. They are expanding the market of teams who need AI agents, knowing that increased adoption at the prototype stage drives consumption at all stages.

## Where Value Concentrates: Building Custom Agents

The strategic battleground is building custom agents for production, not prototyping. This distinction matters for anyone building or buying in this space.

Workflow tools optimise for quick iteration. You want to test an idea fast. You want to show stakeholders something impressive. You want to iterate on prompts and workflows without writing code. AgentKit excels at this, as do platforms like [n8n](https://n8n.io){:target="_blank"} for integration-heavy workflows.

Custom-built agents optimise for the other four user needs: reliability, security, cost, and capability.

**Reliability** requires systematic evaluation that catches degradation before users complain. When I built [Kaijo](/kaijo/), the insight was recognising that developers were spending months wrestling with prompt engineering when they should have been building evaluation systems. You need datasets of good and bad examples. You need automated grading. You need trace-level analysis of why agents fail. AgentKit's enhanced Evals move in this direction, but platform vendors face a structural limitation: their business model depends on you using their models, which constrains how deeply they can support multi-model evaluation.

**Security** goes beyond guardrails and evaluation. During my webinar on [how to ship your agent](/webinar-how-to-ship-your-agent/), I demonstrated the ["lethal trifecta"](/webinar-how-to-ship-your-agent/#the-security-reality) - never give an agent all three of these simultaneously: private data access, untrusted data input, and unfettered internet access. Evaluation and guardrails are insufficient for full protection. You need architectural boundaries that make certain attacks impossible rather than merely detectable. Workflow tools can add guardrails, but custom-built agents let you implement compartmentalisation at the architecture level.

**Cost** requires model agnosticism. You cannot accept 10x price increases when your primary vendor changes economics. You need the ability to switch vendors without rebuilding your entire system. Pricing changes too fast. Model capabilities shift too quickly. Regulatory requirements differ by geography. Platform vendors like OpenAI structurally cannot offer genuine multi-vendor flexibility without cannibalising their revenue. Independent platforms optimising for model agnosticism have a positioning advantage that capital alone cannot overcome.

**Capability** often requires domain-specific customisation that workflow tools do not support. When building [Cherrypick's meal generator](/how-to-build-a-robust-llm-application/), we could not give the AI a full recipe list and trust it to avoid harmful selections for customers with food allergies. We needed architectural constraints that made failure impossible. We only provided recipes the customer could safely eat, then used the AI's creativity for generating compelling explanations. This pattern - constrain the possibility space, use randomness where it adds value - is harder to implement in workflow tools designed for generality.

The economics differ dramatically. A prototyping tool might save you two weeks of development time upfront. A custom agent building platform saves you ongoing costs every month, prevents outages that lose customers, and enables you to switch vendors when economics shift. The total value differs by orders of magnitude.

This explains where customers will actually pay. Prototypes are speculative and often disposable. Production systems represent business risk. Willingness to pay follows business risk, not development speed.

This is why AgentKit does not concern me for [Kaijo](/kaijo/). Kaijo targets developers who are happy building traditional systems and do not want to think about the AI bit. They want to write functions, add tests, and let the platform handle prompt optimisation and model selection. With AgentKit, AI is all you can think about. You are constantly working within their workflow paradigm, their visual builder, their constraints.

The customisation limitation becomes clearer over time. Workflow tools can only offer what their interface exposes. When you need behaviour that sits outside their visual builder's capabilities, you are stuck. Custom-built agents let you implement whatever your domain requires because you control the entire stack.

## Defensive Moats in a Commoditising Market

If workflow tools commoditise, which companies maintain defensible positions? Two different types of moats emerge from this analysis, both resistant to commoditisation but for different reasons.

**There is no longer a build moat.** OpenAI reportedly built AgentKit in six weeks. That development speed signals something important: implementation time is not the constraint. Thinking time is. Six weeks is not enough time for significant product innovation. This is a land grab, not a carefully considered product strategy. That leaves plenty of space for others to innovate on features that require deeper product thinking.

More importantly, you cannot compete on development speed alone. Any company with capital can ship features quickly. Features without defensibility commoditise immediately. The question is not whether you can build workflow tools fast. The question is whether you have a moat that persists after you build them.

**Network effects: the n8n integration moat.** [n8n](https://n8n.io){:target="_blank"} has built 400+ connectors to various services and platforms. Each connector represents weeks of development time to understand APIs, handle edge cases, and maintain compatibility across versions. Building a competitive connector library would require years and significant capital.

The value increases as the network grows. Each new connector makes the platform more valuable to users who need that specific integration. Users contribute connectors back to the ecosystem. The community builds templates and workflows that assume certain connectors exist. This creates a reinforcing cycle that becomes harder to disrupt over time.

AgentKit's Connector Registry attempts to build a similar moat, but starting from scratch. OpenAI has advantages in capital and distribution. But network effects take time to compound regardless of resources. You cannot shortcut the process of building community-contributed templates and workflows. You cannot manufacture the ecosystem effects that make n8n valuable for integration-heavy workflows. Integrations take time regardless of development speed. You can ship a connector registry quickly. You cannot ship 400 well-tested connectors quickly.

For companies building in this space, the lesson is clear: if you compete on workflow tools, you need network effects or you will commoditise. Integrations are one path. Community-contributed templates are another. Platform ecosystems are a third. Features alone will not sustain differentiation as AgentKit and similar tools race to feature parity.

**Positioning advantage: the model agnosticism moat.** The model agnosticism moat exists by removing the moat from the models themselves. Platform vendors like OpenAI build their business on vendor lock-in. An independent platform that truly enables model agnosticism removes that lock-in, which becomes its defensible advantage.

This strengthens as open source LLMs commoditise. The model landscape will look different in 12 months. New providers will emerge. Capabilities will shift. Pricing will change. Companies that built assuming one vendor dominates will face expensive migrations. Companies that built for model agnosticism will switch with configuration changes.

When I designed Kaijo's architecture around multi-vendor evaluation and testing, the insight was recognising that CTOs cannot accept lock-in at the model layer. Platform vendors cannot credibly offer this without cannibalising their revenue. This is positioning, not network effects.

Companies building in this space need one or both of these moats. The question is not whether you can build a better workflow tool than AgentKit. The question is whether you have a defensible position that prevents OpenAI from replicating your core value.

## The Three to Five Year Horizon

Fully AI-written workflows remain three to five years away. Agent Builder assists with implementation but does not make architectural decisions. As I discussed analysing [independent coding agents](/independent-coding-agents-tools-arent-ready/), the infrastructure for autonomy is not ready.

AgentKit accelerates prototyping commoditisation. What took hours now takes minutes. But this creates a multi-year window for custom agent building tools to establish defensible positions. The gap between commoditised prototyping and autonomous workflows is where value concentrates.

The defensible positions are in areas AI cannot easily automate: evaluation frameworks that understand domain-specific correctness, monitoring systems that recognise degradation patterns unique to your business, cost optimisation across vendors where trade-offs change constantly, security architectures that prevent entire classes of attacks.

When AI can generate workflows from natural language, customers will still need to verify they work correctly, monitor them in production, optimise costs across vendors, and maintain security boundaries. Custom agent building remains valuable. Implementation becomes commoditised.

## Strategic Implications

OpenAI's move to commoditise prototyping creates the market for production tools rather than threatening it.

**If you are building in this space**, position as the natural next step after prototyping. Your message: "Prototyped with AgentKit? Now build it properly." Do not compete on prototyping speed. You will lose. Own the production stage. Build for teams that validated their concepts and now need what workflow tools cannot deliver. Establish defensible moats through network effects or positioning advantages.

**If you are buying tools**, understand the progression. Workflow tools for stage one. Custom agent building for stage two. Trying to scale a workflow tool to production creates technical debt.

**For both**, AgentKit expands the market. More prototypes mean more teams discovering they need production tools.

I am grateful for OpenAI bringing workflow tools to the masses. They are validating the market and creating demand. Soon, many will discover they need more than workflows can provide.

The strategic question is not whether OpenAI will dominate AI agent tooling. OpenAI chose to land grab workflow tooling to speed model adoption. The strategic question is who will dominate custom agent building for production. That layer has different requirements, different economics, and different defensibility.

The market just got clearer. AgentKit defined prototyping. Custom agent building tools should focus on everything prototyping cannot deliver: reliability at scale, security through architecture, cost through multi-vendor flexibility, capability through domain-specific customisation.

The next 12 to 18 months will separate companies that recognised this progression from companies that tried to compete on prototyping speed.

For more insights on building production AI systems, join my [monthly webinar](/webinar/) where I explore these topics with technical leaders.
