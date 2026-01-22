---
layout: post
title: "AI Is Still Searching for a Home"
date: 2026-01-21 09:00:00 +0000
image: /assets/img/ai-house-hunt-robot.jpg
infographic: /assets/img/ai-house-hunt-comic.jpg
infographic_carousel: false
categories:
- ai
- strategy
- agents
---

The UK government spent months trialling Microsoft 365 Copilot across thousands of civil servants. Users reported 72% satisfaction but no measurable productivity gains.[^copilot] Is Copilot terrible? Perhaps it is not the product that is the problem. Perhaps it is just in the wrong place.

AI is house hunting, and it has not settled yet. Meanwhile, coding agents have quietly become the most transformative tools I use daily, handling everything from [complex refactoring](/your-agent-orchestrator-is-too-clever/) to [writing these blog posts](/today-in-claude-code/).

These two experiences point to fundamentally different places where AI might settle. One embeds intelligence inside existing applications. The other places AI outside applications, orchestrating them from above. But the orchestrating approach is evolving in ways that blur this distinction, and the answer to which wins is not obvious.

<!--more-->

## Location Is Everything

The first approach embeds AI inside existing products as features: autocomplete in your editor, smart suggestions in email, chat assistants within Slack, AI-generated summaries inside documents. This is the Copilot model, and it is easy to deploy incrementally because users do not need to change how they work. The AI enhances existing workflows rather than replacing them, which is why every major software vendor is racing to add these features.

But the UK government trial found that users loved Copilot yet it did not make them measurably more productive. Copilot excelled at mundane tasks like meeting summaries and drafting emails but struggled with complex work. Excel analysis was lower quality. PowerPoint presentations were faster to produce but required more correction afterwards.

This pattern keeps repeating. Embedded AI works brilliantly for routine tasks where [consistent mediocrity is valuable](/ai-is-consistently-mediocre/). AI maintains the same error rate whether processing its first task or its thousandth, and for meeting notes and email drafts that consistency is a feature. For complex analysis, it becomes a problem. Embedded AI only sees what the host application shows it. Your email assistant does not know about your calendar conflicts or the conversation you had in Slack yesterday. Each feature is an island, optimised for a narrow slice of your work. The more your work requires coordinating information across applications, the less embedded AI can help.

The second approach reverses the relationship. Orchestrating AI sits outside applications and controls them. Claude Code manipulates your filesystem, runs tests, checks the build, and iterates until things work. The Model Context Protocol lets agents operate multiple tools through a standard interface. [Browser automation](/who-wants-a-browser/) navigates websites on your behalf.

Coding agents work well because they have full context. When Claude Code refactors my codebase, it has access to everything it needs. The context is complete and the feedback loops are tight. I can use it [for thinking work](/webinar-use-claude-code-for-thinking/) that has nothing to do with code because it is a general-purpose agent that happens to be good at programming. The rise of [Ralph loops](/your-agent-orchestrator-is-too-clever/) demonstrates this power: a bash for loop feeding the same prompt to an agent repeatedly, letting it see its previous work and iterate until done, with no complex orchestration required.

But orchestrating agents have their own limitations. Security is a constant concern. I teach the ["lethal trifecta" rule](/webinar-stop-ai-stealing-from-you/) in my workshops: never give an agent all three of private data access, untrusted data input, and unfettered internet access simultaneously. Integration is another challenge because every tool your agent controls needs a connection and every API needs maintenance. The [glue code explosion](/openai-devday-where-value-lives-in-ai-agent-tooling/) is real. The Model Context Protocol helps standardise this, but we are still early.

## The Hybrid Evolution

The orchestrating approach is not standing still. Claude Code started as an orchestrator but is evolving into something more flexible: an agent that can embed itself anywhere whilst retaining its orchestrating power.

Consider what happens when you embed Claude Code inside another application. It brings its full context and capabilities with it. Unlike a simple embedded feature, it can still reach out to other tools through MCP servers, still coordinate across systems, still see the broader picture. The lodger has the landlord's keys.

Orchestrating agents can also call themselves. [Ralph loops](/your-agent-orchestrator-is-too-clever/) demonstrate this: a bash for loop feeding the same prompt to an agent repeatedly, letting it see its previous work and iterate until done. The agent becomes both the orchestrator and a sub-component of its own workflow. This recursive capability means the boundaries between embedded and orchestrating are dissolving.

Most AI companies face a strategic choice: focus on the API and become infrastructure, risking commoditisation as alternatives emerge, or focus on the interface and become an application, dependent on whatever platform serves your models. Claude Code chose both. It is the interface layer, the thing you talk to directly, but it also has platform characteristics through its extensibility. MCP servers let it connect to arbitrary tools, hooks let it integrate with your workflows, and skills let you customise its behaviour. Other agents can call it, and you can embed it into your own applications.

[I use Claude Code for everything now](/today-in-claude-code/): research, writing, planning, development. The tool has become my primary interface to my computer for knowledge work, not because it does any single thing better than dedicated applications, but because it can coordinate across all of them whilst embedding itself wherever I need it.

## What This Means for Builders

If you are building AI products or adding AI to existing products, this tension matters for your strategy.

Embedded features are becoming table stakes. Every product will have AI features because users expect them, but table stakes do not differentiate. You need to decide whether your AI features are the product or just expected functionality.

Orchestrating systems face the risk of platform absorption. Anthropic, OpenAI, and others are building increasingly capable agent platforms, and anything you build adjacent to agent capabilities might get absorbed into the platforms themselves. The monitoring tools that cloud providers eventually ate are instructive here.[^1]

The durable position is application-specific intelligence: evaluation of whether your specific AI outputs are good for your specific use case, knowledge of your customer workflows, and integration with your existing systems in ways that matter to your users. This is domain knowledge that platforms cannot easily replicate.

Two years from now, most companies will likely have both: a veneer of expected AI features and connections to powerful orchestrating agents. The question for builders is which layer creates value they can capture, and which becomes commodity infrastructure someone else provides.

For senior leaders [making AI investment decisions](/webinar-how-not-to-screw-up-your-ai-rollout/): do not expect embedded AI features to transform productivity. The UK government data shows that user satisfaction does not equal business impact. If your AI strategy is "add Copilot to everything," recalibrate expectations. The real gains come from orchestrating agents with full context, but those require behaviour change and integration investment. Start evaluating where your teams could benefit from agents that coordinate across systems rather than features that enhance single applications.

## An Open Question

I do not know which approach wins. Embedded AI might improve enough that the context problem dissolves. Orchestrating agents might become easy enough that everyone uses them. The distinction between the two might disappear entirely as orchestrators learn to embed themselves anywhere.

The tools I reach for most are agents that see my whole context and coordinate across boundaries. The productivity gains that the UK government could not find in Copilot, I find every day in Claude Code. Whether AI should live inside your applications, outside controlling them, or move fluidly between both, remains the question everyone building or using AI products needs to answer.

[^copilot]: The criticism is mounting. TechRadar declared it ["time to admit that Microsoft Copilot was a mistake"](https://www.techradar.com/computing/windows/almost-3-years-later-its-time-to-admit-that-microsoft-copilot-was-a-mistake){:target="_blank"} in December 2025, and Microsoft's CEO reportedly [admitted Copilot integrations "don't really work"](https://ppc.land/microsoft-ceo-admits-copilot-integrations-dont-really-work-as-adoption-falters/){:target="_blank"} as enterprise adoption stalled.

[^1]: AWS has a history of building competing products after observing what third-party tools are popular on its platform. Amazon X-Ray and CloudWatch compete with New Relic, DocumentDB competes with MongoDB, and OpenSearch was forked from Elasticsearch after Elastic changed its licence specifically to prevent AWS from offering it as a managed service. See [Startups Beware: If You Use AWS, Amazon May Have You in Its Crosshairs](https://www.inc.com/sonya-mann/aws-startups-conflict.html){:target="_blank"} for the pattern.
