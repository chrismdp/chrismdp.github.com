---
layout: post
title: "Who wants a browser?"
date: 2025-10-23 09:00:00 +0000
image: /assets/img/wardley-map-browser-wars.png
image_portrait: true
series: "Where AI Lives"
categories:
- ai
- strategy
- business
- agents
- security
---
I watched the Apple keynote live in 2007 with baited breath, not sure what was coming. I clearly remember Steve Jobs' crushing disdain for an entire generation of smartphone products. "Who wants a stylus? You have to get them, put them away, you lose them. Yuck!"[^stylus]

He wrote off the competition with a stroke, and gave us the iPhone and a huge change in the way we experience technology. The stylus represented the old paradigm of adapting desktop interfaces to mobile. Multi-touch represented designing for how humans naturally interact.

Browsers are today's stylus. They represent adapting web navigation to an agent world when we should be designing for how humans want to delegate tasks.

<!--more-->

I have been using [Wardley Maps](https://www.wardleymaps.com/) to try and make sense of the shifts we're seeing in technology due to AI - see my previous maps on [coding](/coding-with-ai/) and [no-code workflow tools](/agentkit-helps-its-competitors/). This week, OpenAI launched Atlas, a browser with ChatGPT integration[^atlas], so time to take a look at the browser landscape.

The tech press framed it as another front in the browser wars. Chrome versus Edge versus Arc versus Atlas. I think this analysis is insufficient.

The real competition is not between browsers. It is between paradigms. Browser-based agent integration represents a transitional phase towards direct agent interfaces that bypass web browsing entirely. The winner will not be determined by rendering speed or extension libraries.

Security remains the critical unsolved blocker. Until we solve how to build secure agent systems, everything else is just expensive theatre.

## The New Browser Wars

Another example: for decades, Coca-Cola and Pepsi obsessed over cola market share whilst the actual competitive dynamics shifted entirely beneath them. Health-conscious consumers moved to bottled water, energy drinks, and specialised beverages. Today their cola rivalry appears quaint compared to the fragmented beverage landscape.[^cola-wars]

Users do not want to browse the web. They want to accomplish tasks. We browse only because tasks live on websites. When agents can book restaurants or process expenses directly, browsers become unnecessary overhead.

Browser-based agent integration is transitional. Valuable now, replaceable later. Atlas positions OpenAI to capture users during this shift whilst building towards what comes next.

The timeline for this transition depends entirely on solving security. As I explored in my analysis of [where value lives in AI agent tooling](/agentkit-helps-its-competitors/), the infrastructure for autonomy is not ready. Browsers provide a constrained environment where agents can act with some guardrails. Pure agent interfaces require solving security problems we currently do not know how to solve.

## Value Shifts to the Integration Layer

As LLMs themselves commoditise, platforms compete by building differentiated user interface layers. OpenAI offers Atlas with integrated agent mode. Others push real-time voice interaction, visual canvas builders, or domain-specific agent templates.[^competing-interfaces] The model underneath matters progressively less. The interface and integration layer concentrates value.

This mirrors exactly what happened in cloud computing. Amazon Web Services did not win by having technically superior virtualisation. They won by making infrastructure dead simple to consume through well-designed APIs and interfaces. The underlying technology became commodity infrastructure. The integration layer captured value.

The economics favour whoever controls the chokepoints. There are only a few integration points worth fighting over: browser extensions, operating system integrations, communication platforms. Everyone building agents must flow through these narrow gates. The gatekeeper taxes the entire ecosystem.

Custom-built agents proliferate endlessly across specific use cases. But they all funnel through the same handful of integration layers to reach users. This asymmetry creates the strategic advantage. Building a better agent is hard work with marginal returns. Controlling the integration layer means every agent pays you rent.

This explains why OpenAI built Atlas rather than focusing exclusively on model improvement. They recognised that model capabilities are commoditising faster than integration layers. Atlas positions them to capture value during the transitional phase when agents still need browsers to accomplish tasks.

**But this integration layer is itself temporary.** Traditional browsers face an existential problem: their business model depends on the web remaining the primary interface for tasks. When agents act directly without web interfaces, Chrome's dominance in rendering engines becomes as relevant as Netscape's innovations once the competitive axis shifted.

The value shifts to whoever solves the security problem that enables direct agent action.

## Security Remains the Killer Blocker

The lethal trifecta creates catastrophic security risks.[^lethal-trifecta] Never give an agent all three of these simultaneously: private data access, untrusted content exposure, and external communication capability. As I demonstrated in my webinar on [how to ship your agent](/is-ai-unshippable/), this combination turns agents into data exfiltration systems.

OpenAI acknowledges this directly in the Atlas announcement. Agent mode carries risk from hidden malicious instructions embedded in web content. Safeguards exist but "will not stop every attack." Users must "weigh the tradeoffs" and monitor agent activities closely.

This is admirably honest. It is also a damning admission. We are shipping agent systems to millions of users whilst openly stating we cannot secure them. The guardrails we build are constructed on sand. We add detection systems that catch known attacks whilst new attack vectors emerge faster than we can defend against them.

Current security approaches are fundamentally inadequate. Prompt injection attacks become more sophisticated daily. Attackers hide malicious instructions in images that agents process as text. They use social engineering techniques adapted from human manipulation to confuse AI systems. They chain together innocuous-seeming requests that combine into malicious actions.

Evaluation and guardrails cannot solve this problem. You cannot evaluate your way to security when attack patterns evolve faster than evaluation datasets. You cannot build guardrails that catch every malicious instruction when the instruction space is infinite and creativity favours attackers.

The only robust approach requires architectural boundaries that make certain attacks impossible rather than merely detectable. As I explored when [building Cherrypick's meal generator](/how-to-build-a-robust-llm-application/), security comes from constraining the possibility space. Do not tell the agent what not to do. Only give it options it can safely choose from. Make failure architecturally impossible.

But this approach limits agent autonomy. An agent that can only choose from pre-approved options cannot handle novel situations. It cannot adapt to changing requirements. It cannot act independently across the full range of tasks users want to delegate. The very architectural constraints that provide security prevent the autonomy users demand.

This creates a fundamental tension. The capability threshold where users will pay for agent services requires autonomy that current security approaches cannot protect. One possibility is that models simply become capable enough to naturally resist prompt injection and security attacks, following the "bitter lesson"[^bitter-lesson] that compute and scale solve problems better than clever engineering. But betting on this requires faith that improving model capabilities will outpace attacker sophistication.

The safer approach combines both paths: build the best architectural boundaries we can whilst models improve. Understanding and eliminating security issues through careful system design remains valuable regardless of whether models eventually become robust enough to handle attacks themselves. Free browser-based agents remain expensive toys that companies subsidise to drive model usage. The step change to paid adoption requires solving security through engineering, scale, or both.

## Monetisation Depends on Crossing the Autonomy Threshold

Atlas launches free for all users. This continues the expectation of free browser use established over decades. But this cannot last without revenue to sustain it.

The willingness to pay emerges only when capability crosses the threshold where agents genuinely replace human assistance rather than merely augment it. Current agents are assistants that help you accomplish tasks faster, suggest responses you can edit, and draft documents you review. These capabilities provide value but do not justify significant ongoing subscription costs for most users.

The threshold for paid adoption requires agents that act more like trusted employees: a housekeeper who maintains your home without detailed instructions, an executive assistant who manages your calendar independently, or a research analyst who investigates questions without supervision. This shift from augmentation to replacement requires handling complex tasks autonomously, making routine decisions without input, and managing edge cases without breaking.

Reaching this threshold depends on solving security. Users will not delegate genuine autonomy to systems that cannot be trusted with sensitive data. Companies will not allow agents access to business-critical information when vendors openly admit security limitations. The honesty in Atlas's documentation is refreshing but disqualifying for serious business adoption.

Open source models accelerate pressure on this model. When the underlying model becomes free, the economic case for subsidising expensive integration layers collapses. The company that solves security first can charge for that capability whilst others continue giving away insecure systems. Security becomes the only differentiated capability worth paying for.

## Where This Leaves Everyone

If you are building agent tooling, the question is not whether Atlas threatens your market. The question is whether you are building towards the post-browser paradigm or investing in transitional technology.

The defensible position is solving security for pure agent interfaces, not optimising browser integration. The company that cracks security-preserving autonomy will make browsers irrelevant.

This is why I built [Kaijo](/i-built-kaijo-to-fix-unreliable-ai/) focused on evaluation frameworks and model-agnostic architectures. Security through systematic evaluation and architectural boundaries is the foundation for what comes next.

The bet is on security becoming solvable in the next two to three years. If not, agents remain expensive toys. If so, whoever solves it first defines the post-browser era entirely.

For users evaluating these tools: current agent systems cannot be trusted with business-critical data. The vendors are telling you this directly. Atlas's honest documentation should be read as a warning, not reassurance. Use agents where failure is acceptable. Do not delegate autonomy you cannot afford to lose.

Security remains the only battle that actually matters.

[^atlas]: For OpenAI's perspective on Atlas, see their [announcement post](https://openai.com/index/introducing-chatgpt-atlas/){:target="_blank"}. The [Atlas documentation](https://help.openai.com/en/articles/10449547-atlas-browser-faq){:target="_blank"} provides technical details and importantly includes their honest assessment of security limitations.
[^stylus]: Watch the [full 2007 iPhone keynote](https://www.youtube.com/watch?v=vN4U5FqrOdQ){:target="_blank"} where Jobs introduces multi-touch as the fundamental interaction paradigm for mobile devices.
[^competing-interfaces]: Examples include OpenAI's [Advanced Voice Mode](https://openai.com/index/navigating-the-challenges-and-opportunities-of-synthetic-voices/){:target="_blank"} for real-time conversation, their [Agent Builder visual canvas](https://openai.com/index/introducing-agentkit/){:target="_blank"} released at DevDay, Anthropic's [Claude Code](https://www.anthropic.com/claude-code){:target="_blank"} for developer workflows, and Google's [NotebookLM](https://notebooklm.google.com){:target="_blank"} for research-focused interactions. Each platform differentiates through interface design whilst underlying model capabilities converge.
[^cola-wars]: The Cola Wars between Coca-Cola and Pepsi dominated beverage industry headlines from the 1970s through 1990s with massive marketing campaigns and taste tests. Yet whilst both companies obsessed over cola market share, the actual competitive dynamics shifted entirely. Health-conscious consumers moved to bottled water, energy drinks, and specialised beverages. Today, both Coca-Cola and PepsiCo derive significant revenue from non-cola products, whilst their cola rivalry appears quaint compared to the fragmented beverage landscape. See this [Decline of Big Soda](https://www.nytimes.com/2015/10/04/upshot/soda-industry-struggles-as-consumer-tastes-change.html){:target="_blank"} article for analysis of how the industry transformed around them.
[^lethal-trifecta]: Simon Willison coined the term "lethal trifecta" in his post [The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/){:target="_blank"}. He explains: "If an agent combines these three features, an attacker can easily trick it into accessing private data and sending it to that attacker." This framework has become essential for thinking about agent security architectures.
[^bitter-lesson]: Rich Sutton's essay [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html){:target="_blank"} argues that the history of AI research shows that general methods leveraging computation ultimately outperform approaches that leverage human knowledge. "The bitter lesson is that building in how we think we think does not work in the long run... breakthrough progress eventually arrives by an opposing approach based on scaling computation."
