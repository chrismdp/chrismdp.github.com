---
layout: post
title: "How I Use AI to Code"
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

One distinction has hardened over the last year, and it matters for what follows: vibe coding and agentic engineering are different practices. Vibe coding, where you do not really check the results and just look at the output, is fine unless you are shipping. Agentic engineering is the other thing. It does not mean reading every diff. It means making a measured call about which diffs need your eyes and which do not. I tend to skim UI diffs. I read security and database diffs carefully.

That judgement, about where to spend your attention, is itself a senior skill and one worth getting good at. Every diff still gets checked; not always by you. Tests, type checkers, and automated gates pick up the rest, and you are training the agent so the diffs that do reach your eyes are the ones worth the attention. Conflating the two is how people end up shipping vibe-coded output into production and getting burned.

<!--more-->

## Coding Turned Out to be AI's Home Territory

{% include inline-image.html src="/assets/img/things-ill-get-to-eventually.jpg" alt="Comic titled 'Things I'll get to eventually' showing a board covered in sticky notes, all crossed off. A developer looks at an AI robot holding a pen and says 'Wait... you did ALL of them?!' The robot smiles." %}

The a16z analysis of Fortune 500 and Global 2000 contracts in April 2026 confirmed what most of us suspected from inside the work: coding is the dominant enterprise AI use case by nearly an order of magnitude[^a16z]. Cursor's growth, Claude Code's ramp, Codex's adoption numbers, all of it has outstripped the most optimistic 2024 predictions.

The growth numbers confirm that coding is where adoption has landed, but not that end-to-end throughput has. [Plenty of organisations are finding their coding teams get faster without the business getting faster]({{ site.baseurl }}/why-ai-fast-teams-still-ship-slowly/), which is Goldratt's Theory of Constraints in action: speed up something that was not the bottleneck, and queues pile up everywhere else. Adoption data proves the shift. It does not prove the productivity.

The lived version, for anyone doing it seriously, is that the backlog you had been dragging around for years suddenly becomes tractable. Things I had been telling myself I would get to eventually are now done. The capability has genuinely stepped up, and it is worth sitting with how much more you can build in a week than you could a year ago, before any of the caveats land.

The reason is mechanical, not cultural. Code is data-dense, precise, text-based, and above all verifiable. You can run it and know if it works, which gives models a tight feedback loop to improve on and gives humans a tight feedback loop to trust. Andrej Karpathy implores us to keep agents on a tight leash: many small generation-and-verification cycles, where the developer reads and accepts each diff before the next one builds on it[^karpathy]. Everything downstream, the harnesses, the agent loops, the skills ecosystem, compounds off the verifiability property.

## The Toolchain In 2026

The honest recommendation for a competent developer starting today is: install [Claude Code](https://claude.com/claude-code){:target="_blank"}, not Copilot. Cursor was the right answer in March 2025 and I recommended it then. By May 2025 I had moved to Claude Code and never looked back. The reason is the harness, not the model. GitHub Copilot with Opus underneath does not produce Claude Code's results, because the wrapper around every request matters at least as much as the model itself. How files are chunked, how context is selected, how the agent loop is structured, how CLAUDE.md is privileged over arbitrary docs, these are harness decisions and they compound.

That recommendation does not survive contact with every procurement department. Plenty of organisations are locked into Copilot seats they bought last year, compliance posture that makes new vendor onboarding a six-month exercise, or hosting requirements that rule out commercial CLIs entirely. If that is you, read what follows as "what to aim for", not "install this by Friday". The principles transfer: the harness matters more than the model, CLAUDE.md and skill files work with any agent CLI, and the reset discipline is tool-agnostic. Getting anything through procurement is its own senior skill in 2026!

On top of that harness sit three practical pieces.

**CLAUDE.md files.** These are the standing instructions Claude reads at the start of every session in a given folder. I keep them short, specific, and continuously refined. After every meaningful change, I ask Claude to update the CLAUDE.md based on what it wished it had known at the start. A year in, this compounding effect is the single biggest lever I have for code quality.

**Skill files.** A [skill file](/skills-are-claude-codes-secret-weapon/) in `.claude/skills/` sits between a strict rule and a background doc. Rules in CLAUDE.md are always loaded and always followed, which forces them to stay short. Docs under `docs/` can hold as much as you like but rarely get read when it matters. Skills get pulled in when the work calls them, and they can hold much more detail than a rule would. That sweet spot is where your coding conventions, API rules, and test standards belong, and Claude can update them when it learns something new. I am running nearly 70 of these now across my projects. A handful are public; you can see them at [airskills.ai/chrismdp](https://airskills.ai/chrismdp) if you want a starting shape to copy from.

**A portable vault.** All of this lives in Markdown, [in its own repository](/build-an-ai-knowledge-base-from-scratch/), separate from any single project. It holds the context that would otherwise fragment across a dozen project repos: concept notes, decision trails, people, prior thinking, running project state. Skills can invoke it directly, so the agent working on one codebase can pull from everything I have written or captured about the problem space without that knowledge having to live inside the code repo. Tool-agnostic markdown is the hedge against a world where tools churn faster than workflows. Crystallised knowledge about context windows, about how to frame a brief, about when to reset, will hold up for years. Fluid knowledge about a specific tool's keyboard shortcuts will not. Invest in the first, not the second.

## From Approver to Trainer

The single shift I would most like engineering leaders to take away is this: your most senior engineers should be training the AI to write better code, rather than writing it themselves or reviewing every diff by hand.

{% include inline-image.html src="/assets/img/code-review-is-dying-comic.jpg" alt="Comic: a cheerful robot hoses a torrent of PR papers at an exhausted developer at a desk labelled 'CODE REVIEW', saying 'I can go faster if you like.' PRs cover the floor." %}

We were heading towards a future where humans sit at the end of a ten-agent pipeline, rubber-stamping diffs they did not write and barely understand. That is not a career, it is what Cory Doctorow calls a reverse centaur: the human as an organic appendage to a machine that is generating the real work[^doctorow]. I have sat with too many teams where the senior engineer is quietly becoming the slowest, most exhausted person in the room, [buried in PRs generated faster than they can read](/code-review-is-dying/).

Separate the senior agentic engineer from the basic AI prompter:

1. **Noticing when the agent has gone wrong**, often three prompts before it becomes obvious in the diff. Pattern recognition built up from real work, not something you can teach in an afternoon.
2. **Extracting the lesson into the right place.** Project-specific rules belong in the CLAUDE.md for this repo. Generic rules should be refactored into a skill file and reused everywhere.
3. **Codifying the rules and patterns** your future agents will need, as skill files. Today's spot-fix becomes tomorrow's skill file, and from there it is a standing instruction for every future session. The harness gets smarter because you put the lesson somewhere durable.
4. **Teaching others how to work with AI.** The discipline does not transmit by osmosis. If you have found the groove, the best use of your time is sitting with colleagues who have not.

Training the harness around your codebase is now as important as creating a good architecture for the codebase itself. Both compound every future decision; both get harder to change the longer you leave them; both are the quiet reason one team ships cleanly while another is stuck in rework.

In the old days I expected senior coders to remove more code than they wrote. Now I expect senior coders to add more skills and rule files than code.

We used to call this taste. It still is taste, and it now compounds into the harness instead of staying locked in one person's head. The test of a good senior engineer now is whether their team's AI writes better code next week than it did this week, because of what they left behind in markdown.

## Harness Beats Prompts

{% include inline-image.html src="/assets/img/treat-agent-blocks-as-context-failures.jpg" alt="Three-panel comic. Day 1: a manager tells an agent 'just use PostgreSQL' and relaxes. Six months later the same manager is drowning in a queue of agents asking 'tabs or spaces?'. Meanwhile another team has given their agents a 'How We Make Decisions' book and is working happily." %}

Teams starting out usually ask me some version of "how do I get started with prompting the AI?" Many of them turn up already half-convinced they need spec-driven development first, because that is what they have heard is the proper way in. I am not keen on it, at least in the form it usually shows up, and I will come back to why in a moment.

When an agent gets stuck on something that should be trivial, treat it as a context failure, not a prompt failure. The answer sits in the harness around the request, not in rewording what you asked. Teams that realise this early stop fighting their prompts and start investing in CLAUDE.md, skill files, and the small ontology of decisions their agent needs to make unassisted.

A good harness has four things. A clear set of **standing instructions** in CLAUDE.md. A set of **skill files** that both enforce rules and pull in extra context when the agent needs it. A **verification loop** the agent can run against itself, whether that is tests, a type checker, a linter, or a headless browser clicking through the app. And a **feedback loop** that feeds lessons back into the first three when the agent gets something wrong. Without the feedback loop the scaffolding rots, as Rahul Garg described well in his feedback flywheel piece on Martin Fowler's site[^garg].

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

Do not use a Ralph loop or an agent pipeline blindly. [I went into this at my AI Engineer Europe workshop earlier this month](/ralph-loops-aie-europe/). Work out the right thing to build together, or give the agent enough context to make good decisions on its own. Those are the two modes that work. The trap is doing neither: writing too much detail too early, handing it to the machine, and assuming the detail will carry the thinking. It will not.

## The Context Sweet Spot

<img src="/assets/img/context-sweet-spot.png" alt="Graph showing output quality as a curve against amount of context. With too little context (none, key details) you get generic slop. Full spec hits the sweet spot at the top of the curve. With everything you have, quality drops sharply as the model drowns in noise." style="max-width: 100%; display: block; margin: 1.5rem auto;" />

Knowing when to reset is actually an early and important skill to learn, a specific balance that sits underneath the four skills above. Output quality is a curve against context. Too little, and you get generic slop. Too much, and the model drowns in what it has been fed and the output gets vaguer and more confident at the same time. Full spec, with the right key details and nothing beyond that, is the sweet spot.

Claude Code and the current generation of harnesses need reset less often than they did a year ago. The discipline still matters, though, and it matters more the moment you move to cheaper or open-source harnesses where the model forgives you less. Learning the feel of the curve is transferable even if today's specific harness absorbs most of the work for you.

Engineers who have been at this for a while know the signs you have drifted off the peak: the third useless refactor of a function that worked fine twenty minutes ago, the agent cheerfully restating the same wrong assumption in different words, the creeping sense that you are the one being led round in circles. The move is to stop, throw the conversation away, and restart with a cleaner brief and a smaller chunk. The agent does not get tired or embarrassed, so neither should you. Resetting is cheaper than correcting, almost every time.

Research has confirmed what practitioners feel daily: LLMs perform significantly worse in multi-turn conversations than single-turn ones, and when they take a wrong turn they tend to stay lost[^llm-lost]. That structural property holds more strongly for cheaper and open-source models, which is where a growing share of coding will run over the next year. Knowing the feel of the curve is transferable in a way that the specific behaviour of any given harness is not.

## Feedback Is The New Bottleneck

Once the loops are running and the agent is producing, the constraint moves. A year ago the bottleneck was code generation. Now it is [verification](/feedback-is-the-new-bottleneck/). How fast can you tell whether what was generated is right?

A team that can generate five approaches and verify all five in an afternoon will outpace a team that generates one and waits a week for feedback. The game is not "how fast can we build" any more. It is "how fast can we tell whether this is right". That shifts where to invest. Build better review surfaces, not better prompts. Make feedback unnecessary where you can by having the agent verify against a realistic environment before it asks a human, and make feedback instant where you cannot. MIT's measurement that developers believed they were 20% faster with AI while delivery was measured at 20% slower[^mit] is the feedback bottleneck showing up in the numbers. The coding itself is undoubtedly faster. Everything around the coding, review, verification, integration, rework when the agent got it wrong, is measurably slower, and developers do not count that part as "the slow bit" because the coding felt so quick. The slow work ended up eclipsing the fast work.

I have written [more on this elsewhere](/feedback-is-the-new-bottleneck/), but the short version for coding is: if verifying an AI-generated change takes almost as long as writing it yourself, either the agent's output needs to present differently, or the verification needs to move to an automated gate, or that particular task should not have been delegated.

## What Still Goes Wrong

{% include inline-image.html src="/assets/img/your-engineers-think-theyve-survived-ai.jpg" alt="Comic showing four engineers in a small wooden boat floating in debris, a giant wave labelled 'CLOUD AGENTS' curling behind them. One engineer says 'Glad that's over.' while the wave looms." %}

**Accidental vibe coding** is still the dominant failure mode for teams getting started. Install Claude Code, give it broad instructions, let it run, ship whatever comes out. It looks fast until it meets production. If your codebase is spaghetti without tests, AI generates more spaghetti, faster. Your guardrails matter more now, not less.

The second failure mode is **review fatigue**. Teams with strong quality instincts burn out their most conscientious reviewers first, because they are the ones reading everything rather than skimming. If your senior engineers spend their days approving diffs, you have structurally built the review-approval-monkey job and you should expect people to quit it. The fix is almost always upstream: write skill files for the issues that keep surfacing in review, and most of those diffs stop needing human eyes at all.

The third is **invisible dependencies**. Your AI is quietly doing things you did not ask it to, noticing anomalies, proofreading numbers, second-guessing vague framings. When the next model ships, some of those hidden dependencies break without warning, and nothing in your playbook warns you that they existed. Before upgrading, audit what your AI does beyond what you asked it to, not just the things you explicitly requested.

The fourth is **premature relief**. If you have got through the first wave of IDE-based AI coding and your team is working in Claude Code or Codex, do not assume the adjustment is over. Cloud agents and autonomous orchestration are the next wave, and the survival strategy for each wave is different. The teams that thought "glad that's over" a year ago are often the ones struggling most now.

## Training The Next Generation

{% include inline-image.html src="/assets/img/practice-with-your-team-not-just-licences.jpg" alt="Comic showing a nervous software engineer on stage holding a guitar labelled Claude Code with a $1,999.99 price tag. A stagehand whispers from the wings: Just play it! The audience waits in darkness." %}

The question I have been asked most often this year, and still have not fully answered, is how we develop the next generation of senior engineers when the traditional ladder of handwriting ever-more-complex code is disappearing.

A year on, I am clearer on one part of the answer. Pairing with juniors and showing them how you work with AI is the single best use of your time. Sit with them while they drive Claude Code and teach them when to reset, what to put in CLAUDE.md, when to promote a lesson into a skill file, how to spec the problem rather than the solution, how to feel the context sweet spot. The specific code they produce matters less than the instincts they build about when the agent is about to go wrong and what to do when it does.

Buying licences is not the same as practising together. An expensive tool shoved into an untrained engineer's hands, under the spotlight of a real deadline, produces exactly the stage fright you would expect. Teams that invest in pairing, internal training, and explicit drills in the safe setting pull ahead of teams that buy seats and hope. Licences are cheap. The practice is where the value sits.

The second part is that the skills that matter most are now the ones that used to come latest in a traditional career: architectural taste, knowing when to throw work away, recognising when a requirement is underspecified, spotting the part of the problem that does the real work. If juniors can develop those earlier, they become senior faster. If they cannot, the AI will out-produce them indefinitely on the bits they used to be paid for.

This is what I teach in my [AI training for engineering teams](/training/): the pairing shape, the instincts, and the skill-file discipline done deliberately rather than discovered through trial.

## What To Do Next

If you are starting from cold in April 2026:

**Install Claude Code** and run it in a repo you already know. Write a short CLAUDE.md with the conventions of that repo, the things a new engineer would want to know on their first day. Ship one small change through Claude Code, read the diff, and note where it surprised you. That is your first skill file.

**Ship a skill file every week.** Pick one recurring annoyance, a convention the agent keeps missing, a gotcha in your codebase, a review comment you have made three times, and write it up in `.claude/skills/`. Iterate on it as the agent uses it. You should have ten by month end and the harness will be visibly smarter for it.

**Start pairing** with a colleague who is a couple of steps ahead. Watch them reset. Watch them catch drift. Watch what they choose not to delegate. Most of what is worth learning is in the small judgement calls that do not show up in blog posts.

**Automate one weekly loop**. Pick something you run by hand every week, the weekly release notes, the backlog grooming, the repetitive code review pass, and write it as a skill plus a Ralph-style loop. It does not have to be fully autonomous on the first attempt. The goal is to get a feedback loop running so you can refine it next week.

**Write in markdown**, not in a tool. Tools churn. Your notes should outlive them.

And if you are a senior engineer worried that your job is quietly turning into approving diffs: it is. The way out is to train the AI so the diffs are right the first time, to make yourself the person on the team who shapes the harness, and to make that work the visible thing you are measured on. That role compounds in a way that reviewing never will.

## Conclusion

The core argument from March 2025 has not changed. Using AI to write production code amplifies human judgement rather than replacing it. What has changed is where that judgement gets applied. The work that pays off is shaping the harness, training the agent, and building the feedback loops that make the next hundred diffs better than the last, rather than reviewing individual diffs one by one.

Coding with AI is now the default. The question is whether you are doing it as a reviewer, a prompter, or a trainer. The trainer role compounds. You leave behind markdown, a CLAUDE.md, a bank of skill files, tests the agent can run against itself, that makes every future diff better. The other two roles shrink. Pick accordingly.

[^a16z]: Kimberly Tan, [Where Enterprise AI is Actually Working](https://www.a16z.news/p/ai-adoption-by-the-numbers){:target="_blank"}, a16z, April 2026. 29% of the Fortune 500 and ~19% of the Global 2000 are live, paying customers of leading AI startups. Coding dominates by nearly an order of magnitude because it is verifiable, text-dense, and has tight feedback loops.

[^karpathy]: Andrej Karpathy, [Software in the Era of AI](https://www.youtube.com/watch?v=LCEmiRjPEtQ){:target="_blank"}, YC AI Startup School, 2025. "I'm always scared to get way too big diffs. I always go in small incremental chunks. I want to make sure that everything is good. I want to spin this loop very, very fast." The loop frequency matters more than the loop size.

[^doctorow]: Cory Doctorow, [Revenge of the Chef](https://pluralistic.net/2022/04/17/revenge-of-the-chef/#boss-babbage){:target="_blank"}, Pluralistic, April 2022. The "reverse centaur" framing: a human chained to a machine's pace, acting as an organic appendage instead of the machine acting as the human's amplifier.

[^garg]: Rahul Garg, [The Feedback Flywheel](https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html){:target="_blank"}, martinfowler.com. Argues that the durable leverage in AI-assisted engineering comes from feeding lessons learned back into the scaffolding (CLAUDE.md, skill files, tests) rather than fixing each failure in the conversation.

[^llm-lost]: Laban, P., Hayashi, H., Zhou, Y., & Neville, J. (2025). [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120){:target="_blank"}. arXiv:2505.06120. Models perform significantly worse in multi-turn conversations than single-turn ones, and when they take a wrong turn they tend to stay lost.

[^mit]: The 20%-slower finding is attributed to an MIT study from 2024/2025, corroborated independently at CTO Craft Con in March 2026 by two presentations that measured end-to-end delivery rather than self-reported speed: [Will Lytle (Plandek)](https://plandek.com/){:target="_blank"} and [Yigit Darcin (Trendyol)](https://trendyol.com/){:target="_blank"}. Both saw teams delivering roughly 20% slower despite engineers reporting they felt faster, with the overhead landing in code review queues, test coverage gaps, requirement ambiguity, and deployment pipelines. Ryan Greenblatt at Redwood Research offers a complementary framing: instead of measuring perceived speed-up, measure "serial speed-up", the factor you would have to work faster to be indifferent to losing AI tools. He estimates roughly 1.6x at Anthropic/OpenAI in April 2026, versus the 3x to 20x that people commonly perceive. The gap is the feedback bottleneck.

