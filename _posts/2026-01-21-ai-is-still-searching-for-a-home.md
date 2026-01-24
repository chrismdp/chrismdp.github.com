---
layout: post
title: "AI Is Still Searching for a Home"
date: 2026-01-21 09:00:00 +0000
image: /assets/img/ai-house-hunt-robot.jpg
infographic: /assets/img/ai-house-hunt-comic.jpg
infographic_carousel: false
series: "Where AI Lives"
categories:
- ai
- strategy
- agents
---

Should AI live inside your tools, or sit outside orchestrating them?

The UK government spent months trialling Microsoft 365 Copilot across thousands of civil servants. Users reported 72% satisfaction but no measurable productivity gains.[^copilot] Meanwhile, coding agents have quietly become the most transformative tools I use daily, handling everything from [complex refactoring](/your-agent-orchestrator-is-too-clever/) to [writing these blog posts](/today-in-claude-code/).

These two experiences point to fundamentally different answers. One embeds intelligence inside existing applications. The other places AI outside applications, orchestrating them from above. AI is house hunting, and it has not settled yet.

<!--more-->

## Location Is Everything

The first approach embeds AI inside existing products as features: autocomplete in your editor, smart suggestions in email, chat assistants within Slack, AI-generated summaries inside documents. This is the Copilot model, and it is easy to deploy incrementally because users do not need to change how they work. The AI enhances existing workflows rather than replacing them, which is why every major software vendor is racing to add these features.

But the UK government trial found that users loved Copilot yet it did not make them measurably more productive. Copilot excelled at mundane tasks like meeting summaries and drafting emails but struggled with complex work. Excel analysis was lower quality. PowerPoint presentations were faster to produce but required more correction afterwards.

Ethan Mollick recently pointed out[^mollick] that Claude in Excel consistently beats Microsoft's own Excel Copilot. Microsoft's agent stays bound to Excel functions like VLOOKUPs. Claude does its own analysis in Python and uses Excel just as a user interface for input and output. As Mollick put it: "The difference between the software being the point (Microsoft's perspective) and the output being the point (Anthropic's perspective)."

Microsoft is not standing still. Copilot is moving towards specialised agents per context with the ability to access data from anywhere in M365, becoming a platform where you can tag different agents into a conversation. But access requires organised data, and most organisations have never had a reason to get their information in order. Claude Code works well for coding precisely because it has access to the whole project including git history. The context is already there.

Copilot is actually good at pulling in context from Teams conversations, emails, meetings and documents. That is its strength. The problem is taking action. It retrieves knowledge but does not coordinate action between applications. Even if there was a Copilot equivalent of Claude Code, productivity gains might not materialise because managers do not yet know how to restructure workflows around AI. Organisations often switch off features like Agentbuilder simply because it is called "agent," when really it is just a custom GPT.

Embedded AI works brilliantly for routine tasks where [consistent mediocrity is valuable](/ai-is-consistently-mediocre/). AI maintains the same error rate whether processing its first task or its thousandth, and for meeting notes and email drafts that consistency is a feature. For complex analysis, it becomes a problem. Embedded AI only sees what the host application shows it. Your email assistant does not know about your calendar conflicts or the conversation you had in Slack yesterday. Each feature is an island, optimised for a narrow slice of your work. The more your work requires coordinating information across applications, the less embedded AI can help.

The second approach reverses the relationship. Orchestrating AI sits outside applications and controls them. Claude Code manipulates your filesystem, runs tests, checks the build, and iterates until things work. The Model Context Protocol lets agents operate multiple tools through a standard interface. [Browser automation](/who-wants-a-browser/) navigates websites on your behalf.

Coding agents work well because they have full context. When Claude Code refactors my codebase, it has access to everything it needs. The context is complete and the feedback loops are tight. I can use it [for thinking work](/webinar-use-claude-code-for-thinking/) that has nothing to do with code because it is a general-purpose agent that happens to be good at programming. The rise of [Ralph loops](/your-agent-orchestrator-is-too-clever/) demonstrates this power: a bash for loop feeding the same prompt to an agent repeatedly, letting it see its previous work and iterate until done, with no complex orchestration required.

But orchestrating agents have their own limitations. Security is a constant concern. I teach the ["lethal trifecta" rule](/webinar-stop-ai-stealing-from-you/) in my workshops: never give an agent all three of private data access, untrusted data input, and unfettered internet access simultaneously. Integration is another challenge because every tool your agent controls needs a connection and every API needs maintenance. The [glue code explosion](/openai-devday-where-value-lives-in-ai-agent-tooling/) adds up fast, and whilst the Model Context Protocol helps standardise connections, we are still early.

## The Hybrid Evolution

The orchestrating approach is not standing still. Claude Code started as an orchestrator but is evolving into something more flexible: an agent that can embed itself anywhere whilst retaining its orchestrating power.

Consider what happens when you embed Claude Code inside another application. It brings its full context and capabilities with it. Unlike a simple embedded feature, it can still reach out to other tools through MCP servers, still coordinate across systems, still see the broader picture. This idea defies a housing metaphor: the AI lives in every house in the village, but also owns the land.

Orchestrating agents can also call themselves. [Ralph loops](/your-agent-orchestrator-is-too-clever/) demonstrate this: a bash for loop feeding the same prompt to an agent repeatedly, letting it see its previous work and iterate until done. The agent becomes both the orchestrator and a sub-component of its own workflow. This recursive capability means the boundaries between embedded and orchestrating are dissolving.

Most AI companies face a strategic choice: focus on the API and become infrastructure, risking commoditisation as alternatives emerge, or focus on the interface and become an application, dependent on whatever platform serves your models. Claude Code chose both. It is the interface layer, the thing you talk to directly, but it also has platform characteristics through its extensibility. MCP servers let it connect to arbitrary tools, hooks let it integrate with your workflows, and skills let you customise its behaviour. Other agents can call it, and you can embed it into your own applications.

[I use Claude Code for everything now](/today-in-claude-code/): research, writing, planning, development. The tool has become my primary interface to my computer for knowledge work because it can coordinate across all my applications whilst embedding itself wherever I need it.

## What This Means for Builders

If you are building AI products or adding AI to existing products, this tension matters for your strategy.

Embedded features are becoming table stakes. Every product will have AI features because users expect them, but table stakes do not differentiate. You need to decide whether your AI features are the product or just expected functionality.

Orchestrating systems face the risk of platform absorption. Anthropic, OpenAI, and others are building increasingly capable agent platforms, and anything you build adjacent to agent capabilities might get absorbed into the platforms themselves. The monitoring tools that cloud providers eventually ate are instructive here.[^1]

The durable position is application-specific intelligence: evaluation of whether your specific AI outputs are good for your specific use case, knowledge of your customer workflows, and integration with your existing systems in ways that matter to your users. This is domain knowledge that platforms cannot easily replicate.

Two years from now, most companies will likely have both: a veneer of expected AI features and connections to powerful orchestrating agents. The question for builders is which layer creates value they can capture, and which becomes commodity infrastructure someone else provides.

For senior leaders [making AI investment decisions](/webinar-how-not-to-screw-up-your-ai-rollout/): do not expect embedded AI features to transform productivity. The UK government data shows that user satisfaction does not equal business impact. If your AI strategy is "add Copilot to everything," recalibrate expectations. The real gains come from orchestrating agents with full context, but those require behaviour change and integration investment. Start evaluating where your teams could benefit from agents that coordinate across systems rather than features that enhance single applications.

## Orchestrating Wins

I think orchestrating AI wins. The tools I reach for most are agents that see my whole context and coordinate across boundaries. The productivity gains that the UK government could not find in Copilot, I find every day in Claude Code. The difference is stark enough that I am willing to call it.

The icing on the cake is hybrid mode: orchestrating agents that can embed themselves anywhere whilst retaining full context. Claude Code already does this. It can drop into any application, bring its capabilities with it, and still reach out to other tools. This is where AI will settle: not inside your tools, not just outside them, but moving fluidly between both whilst maintaining the broader view that makes it useful.

Embedded AI might end up being called "the Computer," personified rather like the scene in The Empire Strikes Back where R2-D2 discovers the hyperdrive has been sabotaged. C-3PO asks how he knows, and R2 indicates that Cloud City's central computer told him. "R2-D2, you know better than to trust a strange computer!" Intelligence is there, but it is located and embedded within the system. Orchestrating AI is more like the droid itself: R2-D2 operates independently, manipulates things, and is often our primary interface with technology. Both have their place, but the droids are more generally useful, and the future might be more Star Wars than we think.

_Thanks to Owen Morris and Eleanor Brown for their contributions to an earlier version of this article._

[^mollick]: See Mollick's [LinkedIn post on Claude in Excel](https://www.linkedin.com/posts/emollick_claude-in-excel-is-really-impressive-so-activity-7420659769209765888-JbyB){:target="_blank"} for the full comparison.

[^copilot]: The [UK government Copilot experiment report](https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report/microsoft-365-copilot-experiment-cross-government-findings-report-html){:target="_blank"} found high user satisfaction but no statistically significant productivity improvements. The criticism is mounting elsewhere too: TechRadar declared it ["time to admit that Microsoft Copilot was a mistake"](https://www.techradar.com/computing/windows/almost-3-years-later-its-time-to-admit-that-microsoft-copilot-was-a-mistake){:target="_blank"} in December 2025, and Microsoft's CEO reportedly [admitted Copilot integrations "don't really work"](https://ppc.land/microsoft-ceo-admits-copilot-integrations-dont-really-work-as-adoption-falters/){:target="_blank"} as enterprise adoption stalled.

[^1]: AWS has a history of building competing products after observing what third-party tools are popular on its platform. Amazon X-Ray and CloudWatch compete with New Relic, DocumentDB competes with MongoDB, and OpenSearch was forked from Elasticsearch after Elastic changed its licence specifically to prevent AWS from offering it as a managed service. See [Startups Beware: If You Use AWS, Amazon May Have You in Its Crosshairs](https://www.inc.com/sonya-mann/aws-startups-conflict.html){:target="_blank"} for the pattern.
