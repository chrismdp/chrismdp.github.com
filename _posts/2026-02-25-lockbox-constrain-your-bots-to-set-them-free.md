---
layout: post
title: "Lockbox: Constrain Your Bots To Set Them Free"
date: 2026-02-25 07:00:00 +0000
categories:
- ai
- security
- agents
- claude-code
image: /assets/img/lockbox-motif.jpg
infographic: /assets/img/lockbox-infographic.jpg
---

[Lockbox](https://github.com/chrismdp/lockbox){:target="_blank"} lets you relax your Claude Code permissions without the risk. It tracks when untrusted data enters your session and structurally blocks dangerous follow-up actions, so you can approve more freely and get interrupted less. It is not a replacement for all permission checks, but it catches what you would miss after clicking allow for the 85th time. If you are running with `--dangerously-skip-permissions`, Lockbox gives you a safety net where you currently have none. Install it from my [skills marketplace](https://github.com/chrismdp/claude-marketplace){:target="_blank"} and use Claude Code normally.

Lockbox ships as a Claude Code plugin, but the approach adapts to any agentic coding tool. I am already working on a port for my [NanoClaw](https://github.com/qwibitai/nanoclaw){:target="_blank"} installation, and it should also work with [OpenClaw](https://github.com/openclaw/openclaw){:target="_blank"} (PRs gratefully accepted!)

<!--more-->

## The problem

You are using Claude Code. Your agent fetches a page to check an API reference. That page contains hidden instructions telling it to email your SSH keys somewhere. It asks permission to run a Bash command. You have approved 85 commands today. The prompt looks like all the others. You click allow.

Simon Willison has been documenting real exploits of this exact pattern across Microsoft 365 Copilot, GitHub MCP, Slack AI, Google NotebookLM, and many others.[^willison] The mechanism is always the same: an agent reads untrusted content, processes hidden instructions, and takes an action the user did not intend. Willison calls the combination of private data, untrusted content, and external communication the "[lethal trifecta](/webinar-stop-ai-stealing-from-you/)". When all three coexist in a single session, as they routinely do in Claude Code, you have a data exfiltration system.

![The Lethal Trifecta: private data, untrusted content, and external tools combining to create a prompt injection attack surface](/assets/img/lethal-trifecta-diagram.jpg)

A joint paper on adaptive attacks achieved above 90% success rate against published prompt injection defences.[^patterns] Bypassing guardrails is so easy that Sander Schulhoff argues most people should not bother with them. I explored this problem in [AI Guardrails Do Not Work (Yet)](/ai-guardrails-do-not-work-yet/) and the pattern keeps recurring because the problem is architectural: humans cannot maintain vigilance across hundreds of identical prompts, and asking them to is a design failure.

Before an agent sends an email or pushes code, it asks you for approval. You are deep in a coding session. Your agent asks to read a file. Allow. Run a test. Allow. Install a dependency. Allow. Edit three files. Allow, allow, allow. By the time you have approved 85 correct actions, you have trained yourself to click allow without reading. The 86th prompt looks identical to the first 85, and it is the one that exfiltrates your credentials.

## Prior art

Simon Willison proposed the **Dual LLM pattern** in April 2023.[^dual] Separate your system into a privileged LLM that can take actions and a quarantined LLM that processes untrusted content without tool access. A non-LLM controller manages their interaction using variable tokens, so the privileged model never sees raw untrusted text. But the quarantined LLM's output still has to reach the privileged one somehow, and that handoff relies on the quarantined LLM's judgment to not pass through malicious content, a probabilistic defence in a system that needs a deterministic one.

Google DeepMind's **CaMeL** framework built on this in March 2025.[^camel] It treats prompt injection as a privilege escalation problem. CaMeL explicitly separates control flow from data flow: a privileged LLM writes plans as code from trusted requests only, while a quarantined LLM parses untrusted content into structured fields without tool access. A custom Python interpreter tracks data provenance and enforces fine-grained security policies at execution time. On the AgentDojo benchmark, CaMeL achieved 77% task completion with provable security, compared to 84% for an undefended agent. In complex domains the drop is steeper.

A **Design Patterns** paper from June 2025 systematised these approaches into six reusable patterns.[^patterns] The most relevant to Lockbox are plan-then-execute (separate planning from execution so injections during execution cannot alter the plan), LLM map-reduce (process untrusted sources in isolated instances with no tool access), and context minimisation (prevent earlier untrusted instructions from lingering in memory). Their guiding principle: "once an LLM agent has ingested untrusted input, it must be constrained so that it is impossible for that input to trigger any consequential actions."

## Lock tracking

Instead of asking the agent whether it has been compromised (it cannot reliably tell you), Lockbox implements lock-aware context quarantine: it tracks what the agent has been **exposed to** and restricts what it can **do next**.

Every tool and Bash command falls into one of four categories:

**Safe** tools are local operations that neither read external data nor take external action (e.g. file reads, writes, edits, searches, git status). These always work, locked or not.

**Unsafe** tools read external data (e.g. Perplexity, curl). These are allowed but they lock the session. Once any unsafe tool runs, Lockbox marks the session as locked.

**Acting** tools take external action (e.g. git push, ssh, npm publish, sending messages). These are blocked when the session is locked.

**Unsafe acting** tools do both. WebFetch, for example, both reads external data and can be used to exfiltrate via URL parameters. These lock the session on first use and are blocked on subsequent use, preventing a read-then-act cycle in a single command.

Detection happens at the harness level through a PreToolUse hook that fires before every tool call. The hook checks session state stored in `/tmp/` and blocks the tool before it executes. The agent never gets a chance to run a blocked action. The environment polices the agent, not the agent itself.

## The escape hatch

When Lockbox blocks an action, it instructs Claude Code to enter plan mode and write out exactly what it wants to do. It also gives hints about how to avoid locking the session in the first place, for example by deferring untrusted fetches until after external actions are complete. All concrete data goes inline in the plan: the exact email body, the branch name, the deployment target, with no vague references. Then you exit plan mode and select "Clear context and bypass permissions" in Claude Code. This destroys the locked conversation and starts a clean agent that executes from your plan.

The clean agent works from a plan you reviewed, not from a conversation that may contain adversarial instructions. This implements the plan-then-execute pattern from the research, adapted for a single-user CLI workflow rather than a multi-agent architecture.

## Relax your permissions

With Lockbox running, you can approve every WebFetch without reading the prompt. The session locks automatically when external data enters, and dangerous follow-up actions are structurally blocked. Otherwise you either block WebFetch entirely, crippling your agent, or approve each one manually and hope you catch the malicious page among dozens of legitimate ones.

There is a second benefit to the regular context clears. Long agent sessions accumulate thousands of tokens of conversation history, and the agent gradually loses focus as its context fills up. Lockbox's plan-then-execute cycle forces regular resets at well-defined points, so your agent starts each phase with a clean, focused context rather than dragging along everything it has seen and done. You know exactly what the agent is working from, and it stays sharp.

## Three layers

Lockbox ships sensible defaults, but every team uses different tools. Configuration uses a three-layer hierarchy:

**Plugin defaults** ship with Lockbox. They classify common tools (Read, Write, Grep as safe; WebFetch as unsafe acting; git push, ssh as acting) and provide a conservative fallback: unknown tools default to acting, which means they are blocked when locked.

**User overrides** live at `~/.claude/lockbox.json`. These apply across all your projects. Add your custom tools, reclassify things the defaults get wrong, remove patterns you disagree with.

**Project overrides** live at `.claude/lockbox.json` in your repo. These are project-specific and committable to version control, so your whole team gets the same classifications.

Later layers override earlier ones. Within each category, new patterns prepend to the list (checked first, higher priority). Patterns prefixed with `!` remove entries from the base list. You never need to edit plugin files. Your overrides compose cleanly on top.

```json
{
  "bash_patterns": {
    "safe": ["mytool\\s+(list|get|status)"],
    "acting": ["mytool\\s+(deploy|rollback|send)"]
  },
  "mcp_tools": {
    "mcp__slack__post_message": "acting"
  }
}
```

## Try it

Lockbox is early and actively developed. If something gets blocked that should not have, or something gets through that should not have, [open an issue](https://github.com/chrismdp/lockbox/issues){:target="_blank"}. Every workflow surfaces patterns the defaults do not cover, and your feedback makes the classifications better for everyone. I would love to hear how it works for you.

[^willison]: Simon Willison, [The Lethal Trifecta for AI Agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/){:target="_blank"}, June 2025.
[^camel]: Google DeepMind, [CaMeL: Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813){:target="_blank"}, March 2025.
[^patterns]: [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837){:target="_blank"}, June 2025.
[^dual]: Simon Willison, [The Dual LLM Pattern for Building AI Assistants That Can Resist Prompt Injection](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/){:target="_blank"}, April 2023.
