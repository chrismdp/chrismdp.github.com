---
layout: post
title: "Stop Prompting, Start Briefing"
date: 2026-03-20 12:00:00 +0000
image: /images/2026/stop-prompting-start-briefing-motif.jpg
infographic: /images/2026/stop-prompting-start-briefing-infographic.jpg
categories:
  - ai
  - engineering
  - productivity
---

For the past year I have been teaching technical teams a five-step system for getting better results from AI. I call it the Prompt Cycle. Teams that adopt it see immediate improvement because they stop expecting perfection on the first attempt and start treating AI use as a compounding skill.

The Prompt Cycle has one assumption baked in: you are in the room.

<!--more-->

## The Prompt Cycle

The Prompt Cycle has five steps. First, set up **project context**: persistent information about your codebase, architecture, and constraints that the AI reads every session. Do not overthink this at the start. Begin with the basics and let it grow. In Claude Code this is your [CLAUDE.md file](/skills-are-claude-codes-secret-weapon/) and your [skills](/skills-are-claude-codes-secret-weapon/). In ChatGPT it is a Project or Custom Instructions.

Second, write a **meta-prompt**: instructions for how to approach a specific type of task. Role, process, constraints, output format. Third, give it the **specific task**. Because context and instructions are already loaded, the task itself can be short.

Fourth, **reset and refine**. The AI will produce imperfect output first time, and that is expected. Throw away anything below 90% and start fresh with what you learned rather than polishing bad output. Fifth, **update your rules**: ask "what should I have told you at the start?" and fold the answer back into your project context so every session makes the next one better.

<figure class="my-8">
<img src="/images/2026/prompt-cycle.jpg" alt="The Prompt Cycle: a five-step kaizen wheel showing Project Context, Meta Prompting, Specific Task, Reset and Refine, Update Your Rules" />
<figcaption class="text-sm text-brand-black/60 mt-2 text-center italic">A slide direct from my training course showing the Prompt Cycle as I teach it.</figcaption>
</figure>

The Japanese call this continuous improvement *kaizen*. Applied to AI, it means your prompting system compounds over time. I have [taught this cycle](/training) to engineers and knowledge workers across many industries. It works for coding, for strategy documents, for incident postmortems. But every step depends on a human in the loop.

## Your Prompt Cycle breaks when you leave the room

Six months ago that was fine. [AI meant a chat window](/ai-is-still-searching-for-a-home/): open a conversation, work through a problem together, close the session.

AI agents now run independently. Claude Code on a cron job processing your inbox every fifteen minutes, Devin picking tickets off a backlog overnight, [OpenClaw](/dont-let-your-ceo-install-openclaw/) building features while you sleep. The [orchestration problem](/your-agent-orchestrator-is-too-clever/) has shifted from "how do I coordinate agents?" to "how do I trust them when I am not watching?"

I left the country for three days last week. My agents triaged 200 emails, processed 20 meeting transcripts, drafted scheduling emails, published a blog post, reconciled a month of bank transactions, and sent me pre-meeting briefings before every call. They also drafted a scheduling email with the wrong client name, which I caught in the morning debrief. The decision logs from those three days contain 390 lines of timestamped actions and choices. I wrote about the [review burden](/feedback-is-the-new-bottleneck/) separately, but the deeper problem is that the Prompt Cycle assumes you are present at all.

When the agent runs at 3am, there is nobody to reset and refine, nobody to judge the output, nobody to ask what context was missing. Step 4 requires a human, and the human is asleep.

## Nobody knows how to instruct agents

This is an unsolved problem everywhere. When BBC Radio 4's PM programme ran a segment on AI agents in March 2026, their tech editor Zoe Kleinman described trying to build one and giving up: "it was taking longer to explain to it what I wanted it to do."[^4] The gap between that experience and a system that runs autonomously through an entire working day is the question most people are stuck on.

The practical concerns are real. Only 6% of companies fully trust AI agents to run core business processes autonomously.[^1] 89% of UK organisations deploy AI agents, but only 54% have centralised governance with formal oversight.[^2] Nobody knows how to secure them properly: [your bot is your responsibility](/your-bot-is-your-responsibility/), but most teams have no framework for what that means in practice. 98% of organisations with 500+ employees deploy agentic AI, yet 79% lack formal security policies.[^3]

These are delegation problems, not prompting problems. The difference matters, because delegation has been studied extensively in a field that has been running autonomous agents in high-stakes environments for two centuries.

## The Prussian army solved this problem in 1806

Stephen Bungay's [*The Art of Action*](https://www.goodreads.com/book/show/9973202-the-art-of-action) describes how the Prussian military rebuilt itself after being destroyed by Napoleon at Jena. Their core insight: orders get garbled across long chains of command. The further the decision-maker is from the action, the worse the outcome. Micromanagement does not scale.

Their solution was *Auftragstaktik*: mission command. Set the intent, not the method. Tell your subordinates what you want to achieve and why, then let them figure out how. The critical mechanism that makes this work is back-briefing: after receiving orders, the subordinate restates the plan in their own words. The commander listens for misunderstanding and corrects before anyone moves.

<img src="/images/2026/prussian-army-back-briefing.jpg" alt="Comic: The Prussian Army Solved Your AI Reliability Problem 200 Years Ago" />

Bungay identifies three gaps that plague every organisation:

The **knowledge gap** between what you know and what you would need to know to make a perfect plan. You can never have complete information, so you must communicate intent clearly enough that people can adapt when reality diverges from the plan.

The **alignment gap** between what you intended and what your subordinate understood. Back-briefing closes this gap before any work begins.

The **effects gap** between what you expected to happen and what happened. Debriefs close this gap after the work is done, feeding lessons back into the next cycle.

Every failed AI agent I have seen can be traced to one of these three gaps. The agent did not understand the intent. The agent understood the intent but interpreted it differently. Or the agent did something unexpected and nobody found out until the damage was done.

## The Briefing Cycle

The Prompt Cycle is five steps for interactive AI use. The Briefing Cycle adapts those principles for autonomous agents in four steps.

<img src="/images/2026/briefing-cycle.jpg" alt="The Briefing Cycle: a four-step cycle showing Intent, Back-brief, Bound, Debrief with a feedback arrow showing rules improve each cycle" />

**Intent.** In the Prompt Cycle, you set context and instructions conversationally. For autonomous agents, intent lives in rules files, [skill definitions](/skills-are-claude-codes-secret-weapon/), and project notes that the agent reads cold at the start of every run. You can and should still have a conversation before giving instructions. Use plan mode in Claude Code, or chat through the task in your editor or via voice before committing to a brief. The more complex the ask, the more time this conversation deserves. But the stakes are higher than interactive prompting because there is no mid-task course correction. The accumulated context you have built across previous sessions matters even more here. The brief must be clear enough that a fresh agent with no memory can pick it up and act correctly.

**Back-brief.** In the Prompt Cycle, you reset and refine interactively: see the bad output, adjust, try again. For autonomous agents, the back-brief happens before the agent acts. It restates its understanding of the task, its planned approach, and the constraints it will respect, even when nobody is watching. Most agent builders skip this step entirely. Plan mode in Claude Code already does this well for interactive sessions: you talk through the approach before committing to action. We need something similar for autonomous agents before they start a task. Try adding "always restate the task before starting" to your agent instructions and see what changes. Forcing an agent to articulate its plan surfaces misunderstandings that would otherwise become silent failures. Firing off a task to an agent without a back-brief is like sending a WhatsApp to [OpenClaw](/dont-let-your-ceo-install-openclaw/) and hoping for the best.

If the back-brief reveals a misunderstanding, the agent should stop and flag it for your next review rather than pressing ahead with a flawed plan.

**Bound.** Define what the agent can do alone and what requires human approval. Not everything needs review. This is [Ship/Show/Ask](https://martinfowler.com/articles/ship-show-ask.html) applied to agent output. My system uses a simple classification: reversible actions (archiving emails, updating notes, gathering research) ship without asking. Irreversible actions (sending emails, publishing content, deleting data) require sign-off. In my system, about 70% of agent work is routine enough to ship autonomously, 20% is worth a quick glance, and 10% genuinely needs a decision.

Do not just review everything. That is less safe. The 85th correct approval trains you to blindly approve the 86th, which is the one that [deletes the database](/code-review-is-dying/). Explicit boundaries are safer than blanket oversight because they force you to think about where the real risks are. I am working on [Lockbox](/lockbox-constrain-your-bots-to-set-them-free/), which enforces these boundaries for interactive agent sessions, and thinking about how to apply the same constraints to fully autonomous runs.

**Debrief.** In the Prompt Cycle, step 5 is "update your rules." For autonomous agents, the debrief is the mechanism that makes rule updates possible. Every run, the agent reports exactly what it changed, what decisions it made, and why. Not things like "done" or "processed your inbox." Instead: "Archived 14 newsletters. Created project note for inbound sales lead. Drafted reply to training enquiry, saved as Gmail draft for your approval. Flagged calendar clash between Thursday client call and school pickup."

That level of detail is the raw material for improving the system, but the debrief is also a learning mechanism. The agent should review how the run went, draw its own conclusions about what worked and what did not, and present those conclusions for your review. This is another back-brief: the agent states what it thinks it learned, and you correct before the lesson gets baked in. Only then does it update its own rules and [skills](/skills-are-claude-codes-secret-weapon/). "You always archive newsletters from this sender" becomes an auto-archive rule. "You always draft replies to training enquiries in this format" becomes a skill template. The correction rate drops with every cycle because each debrief makes the next run's intent clearer.

## The loop closes

{% include shareable-quote.html text="The best time to start building your agent factory was four months ago. The second best time is now." %}

The Briefing Cycle is the Prompt Cycle adapted for a world where agents work without you. Intent replaces the conversational setup, back-briefing replaces interactive refinement, bounding defines the autonomy envelope, and debriefing feeds the same compounding loop that step 5 always did.

If you are building or managing autonomous agents, start with one change: add two lines to your agent instructions.

Before starting any task, restate the task, constraints, and planned approach.

After completing any task, list exactly what you changed and why.

That is back-briefing and debriefing. The two steps that turn an unreliable agent into one you can trust to run while you sleep.

None of this is rocket science. Intent, back-brief, bound, debrief. It is repeatable, it is consistent, and it compounds. The best time to start building your agent factory was 24th November 2025, when Claude Opus 4.5 came out[^5] and made this whole thing possible. I have been building mine since then and it took months of iteration to get right. The second best time to start is now.

&nbsp;

[^1]: [The Enterprise AI Trust Gap](https://fortune.com/2025/12/09/harvard-business-review-survey-only-6-percent-companies-trust-ai-agents/), Fortune / HBR Analytic Services / Workato, December 2025, n=603 business and technology leaders.
[^2]: [Governance lags agentic AI adoption in the UK](https://www.computerweekly.com/news/366638841/Governance-lags-agentic-AI-adoption-in-the-UK-says-Salesforce), Computer Weekly / Salesforce MuleSoft 2026 Connectivity Benchmark, n=1,050 IT professionals.
[^3]: [Agentic AI Governance Gap: 98% Deploy, 79% Lack Policy](https://www.pixee.ai/blog/agentic-ai-governance-gap-strategic-framework-2026), Pixee / Enterprise Management Associates, December 2025.
[^4]: [BBC Radio 4 PM, 16 March 2026](https://www.bbc.co.uk/sounds/play/m002sn94) (AI agents segment starts at 51 minutes). I was name-checked on the same programme describing a system that runs autonomously through my entire working day.
[^5]: [Introducing Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5), Anthropic, 24 November 2025. The model that made sustained autonomous agent work practical.
