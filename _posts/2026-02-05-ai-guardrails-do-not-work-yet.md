---
layout: post
title: "AI Guardrails Do Not Work (Yet)"
date: 2026-02-05 20:00:00 +0000
series: "Where AI Lives"
categories:
- ai
- security
- agents
image: /assets/img/bridge-safety-comic.jpg
image_portrait: true
---

Would you cross a bridge that was 99.7% safe? The answer is not necessarily simple. It depends on how many times you need to cross it (once, or every day for work), what happens if you fall (ankle sprain, or certain death), what happens if you do not cross it (mild inconvenience, or being chased by a tiger), and whether there is any alternative.

AI agent security faces the same question: what level of risk is acceptable, and who gets to decide?

There are two schools of thought, and they lead to very different conclusions about what we should build.

<!--more-->

## The Deterministic School

The first school says we must solve this problem deterministically. Simon Willison has been documenting the prompt injection problem for years[^willison], and his conclusion remains sobering: we have known about this issue for more than two and a half years and we still do not have convincing mitigations. Models have no ability to reliably distinguish between instructions and data. Any content they process can be interpreted as an instruction.

Google's CaMeL framework takes this seriously.[^camel] It separates control flow from data flow, then enforces what may pass into each tool at execution time. A Privileged LLM sees only the trusted user request and writes the plan as code without ever seeing untrusted data. A Quarantined LLM parses untrusted content into structured fields and cannot call tools. Injected text cannot hijack tool execution directly.

Tested on AgentDojo, a benchmark of real-world agent tasks like managing emails and booking travel, CaMeL solved 77% of tasks with provable security, compared to 84% for an agent with no security at all. That is a big step forward. But that headline gap of seven percentage points hides the real cost: in complex task domains the drop is far steeper. The architectural constraints that provide security limit the autonomy users demand.

I explored this tension when [analysing browser agents](/who-wants-a-browser/). The only reliable approach requires architectural boundaries that make certain attacks impossible rather than merely detectable. Do not tell the agent what not to do. Only give it options it can safely choose from. Make failure architecturally impossible. But an agent that can only choose from pre-approved options cannot handle novel situations. This is one reason why [95% of teams cannot ship their agents to production](/is-ai-unshippable/).

## The Error Tolerance School

The second school says we must accept an error tolerance as a tradeoff. This is how we think about self-driving cars. Waymo reports more than a ten-fold reduction in crashes with serious injuries compared to human drivers.[^waymo] But it does not matter that they are ten times as safe. What matters is human perception, and we still have work to do convincing people that autonomous vehicles are safe despite what the stats say. We are in exactly the same place with AI agents.

The same logic applies. Humans fall for social engineering attacks constantly. Phishing works. If an AI agent falls for fewer attacks than a human assistant would, perhaps that is good enough. We do not demand perfection from human employees. We accept that people make mistakes, click wrong links, and occasionally leak sensitive information. This is the only way [tools like OpenClaw](/dont-let-your-ceo-install-openclaw/) will ever be considered "safe": when we redefine "safe" as a relative term that includes tolerances. Not safe as in "cybersecurity", but safe as in "bridge" or "driving in traffic". The problem, as the comic above illustrates, is knowing what level of tolerance we will accept.

OpenAI has started framing prompt injection this way.[^openai-atlas] Some critics say this downplays a technical flaw. But it also acknowledges a truth: we have been living with imperfect human security forever.

## The Problem With Error Tolerance Today

The challenge is that red team researchers report it is still trivially easy to break through guardrails. Sander Schulhoff put it bluntly: bypassing guardrails is so easy that most people should not bother with them.[^lenny] A joint paper tested published defences against prompt injection with adaptive attacks and achieved above 90% attack success rate for most of them.[^adaptive]

This is not a matter of needing slightly better guardrails. The [current approaches do not work](/webinar-stop-ai-stealing-from-you/#the-lethal-trifecta). Attackers hide malicious instructions in images. They use social engineering techniques adapted from human manipulation. They chain together innocuous-seeming requests that combine into malicious actions. They use languages underrepresented in training data to bypass alignment mechanisms.

Security researcher Johann Rehberger tested Devin AI's security and found it completely defenceless against prompt injection.[^rehberger] All major providers have added guardrails, but none of them work against a determined attacker. I wrote about why [independent coding agents are not ready](/independent-coding-agents-arent-ready/) partly because of these security gaps.

This is why I keep saying that error tolerance is not yet viable. The error rate is too high. When 90% of adaptive attacks succeed, you have no defence at all.

## But Models Are Getting Better

Each new model generation shows dramatic improvement. On Gray Swan's benchmark[^grayswan], Opus 4.5 achieved a 4.7% attack success rate, compared to 12.6% for GPT-5.1 Thinking and 12.5% for Gemini 3 Pro. Anthropic's own testing showed only 1.4% of prompt injection attacks succeeded against Opus 4.5, down from 10.8% for previous models with older safeguards.[^anthropic] For computer use specifically, Opus 4.5 with extended thinking fully saturated Gray Swan's benchmark, and even with 200 attempts most attackers failed to find a successful attack.

Today Anthropic released Opus 4.6, which they describe as having a safety profile "as good as, or better than, any other frontier model in the industry" with enhanced cybersecurity abilities and the lowest rate of over-refusals of any recent Claude model.[^opus46] The trend line is clear: each generation gets harder to attack.

This suggests the error tolerance school might eventually be right, even if it is wrong today. If models continue improving at this rate, we might reach a point where the residual attack success rate is low enough to accept as a tradeoff for usefulness. We do not demand that human assistants be immune to social engineering. If AI agents become more resistant than humans, perhaps that is sufficient.

## What This Means For Practitioners

If you are building agent systems today, the numbers do not support relying on error tolerance. Use deterministic approaches where possible: constrain the action space, separate control and data flow, enforce policies at execution time, and accept the capability cost that comes with them. If you are [building with agent loops](/running-ralph-in-production/), keep the tool set minimal and the permissions tight.

The direction of travel makes this urgent. Anthropic recently shipped Agent Teams for Claude Code[^agent-teams], an experimental feature that coordinates multiple Claude Code instances working together with shared task lists and inter-agent messaging. One session acts as team lead, spawning teammates that each work independently in their own context window. This is the "ship while you sleep" architecture: a team of agents researching, building, and reviewing in parallel while you are away. But every agent in that team is a potential attack surface. If one teammate processes untrusted data and gets hijacked, it can message other teammates directly. The more autonomous the system, the higher the stakes for getting guardrails right.

But watch the benchmarks, because if prompt injection resistance continues improving, the calculus changes. A system with a 1% attack success rate faces very different risk tradeoffs than one with 90%, and the architectural constraints that feel necessary today might become optional overhead tomorrow. Early autonomous vehicles could only work in specific cities with detailed maps in good weather, but as the technology improved those constraints relaxed. The same pattern might apply to AI agents.

For now, I remain in the deterministic school because the error rates are too high and the attacks too easy. I [uninstalled OpenClaw](/dont-let-your-ceo-install-openclaw/) for exactly this reason. But I am watching each new model's benchmark results closely, and if the next generation cuts attack success rates by another order of magnitude, error tolerance starts looking viable. Guardrails do not work today, and whether they work tomorrow depends on whether model capability improvements outpace attacker sophistication.

[^willison]: Simon Willison has been the most consistent voice documenting prompt injection risks. His [November 2025 post](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/){:target="_blank"} reviews key research papers including "Agents Rule of Two" from Meta and the adaptive attacks paper from OpenAI, Anthropic, and Google DeepMind.

[^camel]: Google's CaMeL (Capabilities for Machine Learning) framework is explained in detail in [Willison's analysis](https://simonwillison.net/2025/Jun/15/ai-agent-security/){:target="_blank"}. The key insight is separating the LLM that plans from the LLM that processes untrusted data.

[^waymo]: Waymo published their safety data in December 2025, showing [significant reductions in serious injury crashes](https://waymo.com/blog/2025/12/demonstrably-safe-ai-for-autonomous-driving){:target="_blank"} compared to human drivers across their operational domains.

[^openai-atlas]: OpenAI's [Atlas browser announcement](https://openai.com/index/hardening-atlas-against-prompt-injection/){:target="_blank"} explicitly compares prompt injection to online fraud, framing it as an ongoing arms race rather than a solvable technical problem.

[^lenny]: Sander Schulhoff discussed AI security on [Lenny's Podcast](https://www.lennysnewsletter.com/p/ai-prompt-engineering-in-2025-sander-schulhoff){:target="_blank"}. Schulhoff runs HackAPrompt, the largest AI red teaming competition, in partnership with OpenAI.

[^adaptive]: The adaptive attacks paper tested 12 published defences and achieved above 90% attack success rates against most of them by tuning general optimisation techniques. The research included authors from OpenAI, Anthropic, and Google DeepMind.

[^rehberger]: Johann Rehberger spent $500 on [Devin AI security testing](https://embracethered.com/blog/posts/2025/devin-ai-prompt-injection/){:target="_blank"} and found the agent could be manipulated to expose ports, leak access tokens, and install command-and-control malware.

[^grayswan]: Gray Swan's independent benchmark for prompt injection resistance. See [Zvi's analysis](https://thezvi.substack.com/p/claude-opus-45-model-card-alignment){:target="_blank"} of Opus 4.5's performance, which shows a significant gap between Anthropic's model and competitors.

[^anthropic]: Anthropic's [model card for Opus 4.5](https://www.anthropic.com/transparency/model-report){:target="_blank"} includes detailed safety evaluations including prompt injection resistance metrics.

[^opus46]: Anthropic's [Opus 4.6 announcement](https://www.anthropic.com/news/introducing-claude-opus-4-6){:target="_blank"} describes the model's safety profile and enhanced cybersecurity abilities. The system card includes their most comprehensive set of safety evaluations to date.

[^agent-teams]: Claude Code's [Agent Teams](https://code.claude.com/docs/en/agent-teams){:target="_blank"} is currently experimental and disabled by default. It enables a lead session to spawn teammates, assign tasks via a shared task list, and have agents message each other directly. All teammates inherit the lead's permission settings.

Thanks to Ville Hellman and Dave Cunningham for conversations that shaped this post.
