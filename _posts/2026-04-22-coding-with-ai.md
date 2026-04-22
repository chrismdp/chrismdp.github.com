---
layout: post
title: "Coding with AI"
date: 2026-04-22 12:00:00 +00:00
permalink: /coding-with-ai/
replaces: /coding-with-ai-march-2025/
categories:
- development
- ai
- code
- craftsmanship
image: /assets/img/ai-coding-superbikes-motif.jpg
infographic: /assets/img/ai-coding-superbikes-infographic.jpg
---

If you are still tied to your IDE, whether Cursor or Copilot, you are working a year behind. Coding turned out to be AI's home territory. The best tooling has moved out of the editor and onto the command line, and the senior engineer's job is to train the AI, not review its output.

I wrote the [previous version of this post](/coding-with-ai-march-2025/) in March 2025, updated it once in August, and it has been linked from almost everything I have written about AI engineering since. The fundamentals from that post still hold: keep changes small, build guardrails, document ruthlessly, and make sure every change gets verified before it ships. One thing has had to move with the volume. "Verified" used to mean "read by you". With modern agent throughput, it has to mean "checked by tests, by type checkers, by automated gates, or by you where your judgement matters". The check still happens; it just does not always happen in your head.

One distinction has hardened over the last year, and it matters for what follows: vibe coding and agentic engineering are different practices. Vibe coding, where you do not really check the results and just look at the output, is fine unless you are shipping. Agentic engineering is the other thing. It does not mean reading every diff. It means making a measured call about which diffs need your eyes and which do not. I tend to skim UI diffs. I read security and database diffs carefully. That judgement, about where to spend your attention, is itself a senior skill and one worth getting good at. Every diff still gets checked; not always by you. Tests, type checkers, and automated gates pick up the rest, and you are training the agent so the diffs that do reach your eyes are the ones worth the attention. Conflating the two is how people end up shipping vibe-coded output into production and getting burned.

<!--more-->

## Coding Turned Out to be AI's Home Territory

{% include inline-image.html src="/assets/img/things-ill-get-to-eventually.jpg" alt="Comic titled 'Things I'll get to eventually' showing a board covered in sticky notes, all crossed off. A developer looks at an AI robot holding a pen and says 'Wait... you did ALL of them?!' The robot smiles." %}

The a16z analysis of Fortune 500 and Global 2000 contracts in April 2026 confirmed what most of us suspected from inside the work: coding is the dominant enterprise AI use case by nearly an order of magnitude[^a16z]. Cursor's growth, Claude Code's ramp, Codex's adoption numbers, all of it has outstripped the most optimistic 2024 predictions.

The growth numbers confirm that coding is where adoption has landed, but not that end-to-end throughput has. [Plenty of organisations are finding their coding teams get faster without the business getting faster]({{ site.baseurl }}/why-ai-fast-teams-still-ship-slowly/), which is Goldratt's Theory of Constraints in action: speed up something that was not the bottleneck, and queues pile up everywhere else. Adoption data proves the shift. It does not prove the productivity.

The lived version, for anyone doing it seriously, is that the backlog you had been dragging around for years suddenly becomes tractable. Things I had been telling myself I would get to eventually are now done. The capability has genuinely stepped up, and it is worth sitting with how much more you can build in a week than you could a year ago, before any of the caveats land.

The reason is mechanical, not cultural. Code is data-dense, precise, text-based, and above all verifiable. You can run it and know if it works, which gives models a tight feedback loop to improve on and gives humans a tight feedback loop to trust. Andrej Karpathy implores us to keep agents on a tight leash: many small generation-and-verification cycles, where the developer reads and accepts each diff before the next one builds on it[^karpathy]. Everything downstream, the harnesses, the agent loops, the skills ecosystem, compounds off the verifiability property.

## The Toolchain In 2026

The honest recommendation for a competent developer starting today is: install [Claude Code](https://claude.com/claude-code){:target="_blank"}, not Copilot. Cursor was the right answer in March 2025 and I recommended it then. By May 2025 I had moved to Claude Code and never looked back. The reason is the harness, not the model. GitHub Copilot with Opus underneath does not produce Claude Code's results, because the wrapper around every request matters at least as much as the model itself. How files are chunked, how context is selected, how the agent loop is structured, how CLAUDE.md is privileged over arbitrary docs, these are harness decisions and they compound.

That recommendation does not survive contact with every procurement department. Plenty of organisations are locked into Copilot seats they bought last year, compliance posture that makes new vendor onboarding a six-month exercise, or hosting requirements that rule out commercial CLIs entirely. If that is you, read what follows as "what to aim for", not "install this by Friday". The principles transfer: the harness matters more than the model, CLAUDE.md and skill files work with any agent CLI, and the reset discipline is tool-agnostic. Getting through procurement is its own senior skill in 2026.

On top of that harness sit three practical pieces.

**CLAUDE.md files.** These are the standing instructions Claude reads at the start of every session in a given folder. I keep them short, specific, and continuously refined. After every meaningful change, I ask Claude to update the CLAUDE.md based on what it wished it had known at the start. A year in, this compounding effect is the single biggest lever I have for code quality.

**Skill files.** A [skill file](/skills-are-claude-codes-secret-weapon/) in `.claude/skills/` is treated as a rule Claude actively enforces, not background reading it may or may not consult. A testing standards document sitting in `docs/` drifts out of use. The same file moved into `.claude/skills/` gets followed. Put your coding conventions, API rules, and test standards in skill files, and let Claude update them when it learns something new. I am running nearly 70 of these now across my projects. A handful are public; you can see them at [airskills.ai/chrismdp](https://airskills.ai/chrismdp) if you want a starting shape to copy from.

**[A portable vault](/build-an-ai-knowledge-base-from-scratch/).** All of this lives in Markdown, in its own repository, separate from any single project. It holds the context that would otherwise fragment across a dozen project repos: concept notes, decision trails, people, prior thinking, running project state. Skills can invoke it directly, so the agent working on one codebase can pull from everything I have written or captured about the problem space without that knowledge having to live inside the code repo. Tool-agnostic markdown is the hedge against a world where tools churn faster than workflows. Crystallised knowledge about context windows, about how to frame a brief, about when to reset, will hold up for years. Fluid knowledge about a specific tool's keyboard shortcuts will not. Invest in the first, not the second.

## From Approver to Trainer

The single shift I would most like engineering leaders to take away is this: your most senior engineers should be training the AI to write better code, rather than writing it themselves or reviewing every diff by hand.

We were heading towards a future where humans sit at the end of a ten-agent pipeline, rubber-stamping diffs they did not write and barely understand. That is not a career, it is what [Cory Doctorow](https://pluralistic.net/2022/04/17/revenge-of-the-chef/#boss-babbage) calls a reverse centaur: the human as an organic appendage to a machine that is generating the real work. I have sat with too many teams where the senior engineer is quietly becoming the slowest, most exhausted person in the room, buried in PRs generated faster than they can read.

Four skills separate the senior engineer from the prompter:

1. **Noticing when the agent has gone wrong**, often three prompts before it becomes obvious in the diff. Pattern recognition built up from real work, not something you can teach in an afternoon.
2. **Extracting the lesson into the right place.** Project-specific rules belong in the CLAUDE.md for this repo. Generic rules should be refactored into a skill file and reused everywhere.
3. **Codifying the rules and patterns** your future agents will need. Today's spot-fix becomes next week's standing instruction, which becomes next month's enforced rule. The harness gets smarter because you made it.
4. **Teaching others how to work with AI.** The discipline does not transmit by osmosis. If you have found the groove, the best use of your time is sitting with colleagues who have not.

Training the harness around your codebase is now as important as creating a good architecture for the codebase itself. Both compound every future decision; both get harder to change the longer you leave them; both are the quiet reason one team ships cleanly while another is stuck in rework.

In the old days I expected senior coders to remove more code than they wrote. Now I expect senior coders to add more skills and rule files than code.

We used to call this taste. It still is taste, and it now compounds into the harness instead of staying locked in one person's head. The test of a good senior engineer now is whether their team's AI writes better code next week than it did this week, because of what they left behind in markdown.

## Harness Beats Prompts

{% include inline-image.html src="/assets/img/treat-agent-blocks-as-context-failures.jpg" alt="Three-panel comic. Day 1: a manager tells an agent 'just use PostgreSQL' and relaxes. Six months later the same manager is drowning in a queue of agents asking 'tabs or spaces?'. Meanwhile another team has given their agents a 'How We Make Decisions' book and is working happily." %}

Teams starting out usually ask me some version of "how do I get started with prompting the AI?" Many of them turn up already half-convinced they need spec-driven development first, because that is what they have heard is the proper way in. I am not keen on it, at least in the form it usually shows up, and I will come back to why in a moment. The prompt is not where the problem lives. The harness is.

When an agent gets stuck on something that should be trivial, treat it as a context failure, not a prompt failure. The answer sits in the harness around the request, not in rewording what you asked. Teams that realise this early stop fighting their prompts and start investing in CLAUDE.md, skill files, and the small ontology of decisions their agent needs to make unassisted.

A good harness has four things. A clear set of standing instructions in CLAUDE.md. A set of skill files for rules you want actively enforced. A verification loop the agent can run against itself, whether that is tests, a type checker, a linter, or a headless browser clicking through the app. And a way to feed lessons back into the first three when the agent gets something wrong. Without the feedback loop the scaffolding rots, as Rahul Garg described well in his [feedback flywheel](https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html){:target="_blank"} piece on Martin Fowler's site.

Once the harness is in place, the prompts themselves can be almost boring. Most of the time I just need to say something like "here are a few files to look at, this is roughly what I want, figure out the rest." The agent knows the conventions, reaches for the right tools, and verifies its own work. This is the point at which AI coding starts to feel like the apprentice you wanted, rather than the confidently wrong intern you keep having to undo.

One specific pattern that changed my reliability overnight: before asking for anything new, ask the codebase whether the thing already exists. AI has made the cost of that question effectively zero. I had a developer in a recent training session save three weeks of estimation in thirty seconds on exactly this, because the feature he thought he had to build was already in the codebase, commented out during an old refactor. Discovery before generation.

## Specify The Problem, Not The Solution

{% include inline-image.html src="/assets/img/spec-the-problem-not-the-solution.jpg" alt="Two robot builders standing on a cliff edge, one saying 'Sorry, where's the other end again?' next to a half-finished suspension bridge. Comic: Spec the problem, not the solution." %}

This is where I come back to spec-driven development. It is the pattern I most often see teams reach for, and the one I most often push back on. The idea is that you specify everything upfront, every endpoint, every schema, every flow, before the AI writes a line. In March 2025 I was nudging people towards more upfront spec myself. I want to walk that back.

Several months of running [Ralph loops](/ralph-loops-aie-europe/) changed my view. If you specify the solution upfront, you are front-loading all the thinking so the machine can run unsupervised. That was called waterfall in 1986, and it did not work then either. The more you nail down in advance, the more places the plan breaks when reality shifts, which reality always does.

{% include inline-image.html src="/assets/img/dark-factories-specify-everything-upfront.jpg" alt="Two-panel comic. 1986: managers pile a tall stack of REQUIREMENTS onto stressed software developers. 2026: the same managers pile a tall stack of AGENT SPECIFICATIONS onto robots in a DARK FACTORY. The mistake repeats." align="left" %}

What is new is that the waterfall mistake has a fresh cover story. "Dark factory" software development promises autonomous agents running in parallel on a queue of specifications you wrote once, perfectly, in advance. Every team making the leap to more autonomous agents runs into this. Once you learn to see the shape, you spot it everywhere: in the correction loops people type when the agent gets something wrong, in the vague questions people ask when they never told the model how to think about the problem. The failure is always earlier than people think. It is rarely a model problem, and almost always an input one.

The move is to spec the problem, not the solution. The problem is stable and needs to be understood properly. The solution is unknown at the start and should evolve as the agent learns. Specify the problem clearly enough that the agent can iterate on the solution without losing sight of what it is solving for, then give it a feedback loop so it can tell whether it has solved the problem.

In practice this means the brief names the constraints, the users, the existing shape of the system, and the criteria that would make a change good, and leaves the implementation decisions open. "We need an audit log for every write, searchable by user, retained for seven years, and it has to work without slowing the hot path" gives an agent everything it needs to propose a design, argue against your obvious first idea, and come back with two or three options it can defend. "Add a Postgres table called audit_log with these eight columns and this index" does not. The first version lets the machine do the thinking. The second makes it your stenographer.

Do not use a Ralph loop or an agent pipeline blindly. Work out the right thing to build together, or give the agent enough context to make good decisions on its own. Those are the two modes that work. The trap is doing neither: writing too much detail too early, handing it to the machine, and assuming the detail will carry the thinking. It will not.

