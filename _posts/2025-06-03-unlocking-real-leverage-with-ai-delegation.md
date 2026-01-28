---
layout: post
title: "Unlocking Real Leverage with AI Delegation"
date: 2026-01-27 09:00:00 +0000
categories:
- ai
- engineering
- automation
image: /assets/img/replace-work-ai-infographic.jpg
image_portrait: true
infographic: /assets/img/replace-work-ai-infographic.jpg
---

I used to just code. Then I managed teams. Now I find myself needing management skills again, even when I am not managing people.

The first time I tried delegating to an AI agent, it felt exactly like onboarding a new team member. I was not sure what to hand over or how to check the work. It took a lot longer than doing it myself. But there is real leverage on the other side. This is how I found it.

<!--more-->

## A New Mental Model

AI agents are not people to manage and they are not programs to command. They are something new entirely, and that requires a new mental model. I wrote previously about [how engineering managers are often well-suited for AI work](/webinar-how-not-to-screw-up-your-ai-rollout/) because they already think in terms of delegation and non-determinism. But even they have to unlearn old habits.

## Chat vs Agents

Before going further, a distinction matters here. Chat interfaces like ChatGPT or Claude.ai are for quick questions. Agents have agency: they can plan, execute, and adapt.

Agents work with multi-file context, multi-step reasoning, and persistent context across sessions. Chat just responds to what you type. The shift is from "AI assistant" to "AI thought partner." For delegation to work, [you need the repository approach, not chatbots](/writing-and-thinking-with-ai-why-repositories-beat-chatbots/).

Tools like Claude Code and Cursor are platforms, not just interfaces. Through MCP (Model Context Protocol) and tool chaining, you can build an extensible delegation infrastructure. Your CLAUDE.md file becomes a training document for your AI staff. You are building a system that compounds, not just delegating individual tasks.

I have written more about [how to use Claude Code skills](/how-to-use-claude-code-skills/) to encode your work patterns into reusable prompts. This turns one-off delegation into repeatable systems.

## When and How to Delegate

Not every task should go to AI. [AI reaches consistency quickly through prompting, but competence slowly through model improvements](/ai-is-consistently-mediocre/). Humans reach competence quickly but consistency slowly.

Deploy AI where uniform mediocrity beats variable excellence: expense categorisation, first-pass code reviews, interview scoring against rubrics. These are tasks where consistency matters more than occasional brilliance, and where human variability causes problems. This reframes the "80% as well as you" concern. It is a strategic advantage, not a compromise.

Once you decide to delegate, the next question is how hands-on to be. Shreyas Doshi's radical delegation framework offers a useful lens: consider both the stakes of the outcome and the capability of the person (or in our case, the AI) handling it.[^1]

Two questions determine your delegation level. How much does outcome quality matter? A draft email to a colleague has different stakes than a client proposal. And how capable is AI at this task? Some tasks AI handles well today, others require significant human judgment. This changes as models improve, so revisit your assumptions regularly.

<img src="/assets/img/delegation-levels-table.jpg" alt="Choosing Your Delegation Level for AI - table showing five levels from Fire and Forget to Human-Led with AI Boost" class="float-right w-1/2 ml-4 mb-4 rounded-lg" />

These two factors create a spectrum of involvement:

**Fire and forget.** Low stakes, AI is capable. You set it up once and let it run. Email triage rules, calendar scheduling, routine data formatting. Check occasionally to make sure nothing has drifted.

**Spot check.** Medium stakes, AI is mostly capable. You review outputs periodically but do not approve each one. Internal summaries, first-draft documentation, research compilation.

**Approve before action.** Higher stakes or lower AI capability. AI drafts, you review and approve before anything goes out. Client communications, code merges, published content.

**Collaborative.** High stakes, complex judgment required. You work together in real-time, AI assists your thinking rather than replacing it. Strategy documents, architectural decisions, sensitive communications.

**Human-led with AI boost.** Critical outcomes, novel situations, high judgment. You lead the work entirely, AI helps with research, drafting, or analysis. Contract negotiations, hiring decisions, crisis response.

One factor people forget: [AI can be phished](/webinar-stop-ai-stealing-from-you/#the-lethal-trifecta). Prompt injection attacks can manipulate agents into leaking data or taking unintended actions. The more autonomous the delegation level, the more you need guardrails and monitoring in place.

This matters more as always-on agents become common. Anthropic recently launched Clawdbot (since renamed Moltbot) which can work autonomously on tasks over hours or days. When AI can act without you in the loop, being intentional about what you delegate becomes critical. Choose your delegation level deliberately, not by default.

Where you draw the line depends on task-relevant maturity. As AI improves at a task (or as you build better prompts and guardrails), you can move down the spectrum. What starts as "approve before action" might become "spot check" after a few months of reliable performance.

## How to Delegate a Workflow

The flowchart above walks through my decision process for whether to automate a task at all. Once you have decided to delegate, here is how to actually do it.

### Pick Something That Fits

Find a task that passes the flowchart test: takes meaningful time, drains your energy or you hate doing it, and would not require endless tweaking to get right. Start there.

The bitter lesson applies here: try the simplest approach first. What once required elaborate automation pipelines in n8n or Zapier now often works with a simple prompt and a CLAUDE.md file that knows your preferences. Ask Claude Code to do it directly before reaching for workflow tools.

### Find the Decision Point

Look for the moment in the task where judgment happens. Where you would not normally give the job to a computer. Try to find a really simple decision that you make all the time.

If you are not sure what an AI might be able to do, ask an AI agent to brainstorm where an agent could help within your workflow. This kind of meta-thinking about strategy is a really important skill to develop.

### Automate and Iterate

Pick that decision point and automate it. Test, iterate, and refine.

Each experiment will teach you something new about what AI can do, slowly increasing your leverage over time. If something does not work, revisit when a new model comes out. The tech is moving so fast that what did not work three months ago might just work now.

### Real Examples

I started with email triage. Imagine you receive inbound emails asking for advice. You probably already automate parts of this process using rules, marking particular emails as important based on who they are from. Try first to move this process to a workflow tool.

Once that is done, how do you process the rest? Normally, you might read each one and decide: should you reply personally, refer the person to a resource, or have AI draft a first response? Set up a workflow where AI reviews the email and drafts a reply for you to approve, or marks the email as important for your attention. You can start by automating the triage step, then gradually hand over more of the process as you gain confidence.

But that was just the beginning. I now run workflows for meeting scheduling from Slack, natural language analytics queries against BigQuery, Slack summarisation to docs, daily check-outs that pull from Linear and GitHub, and pre-meeting briefings from CRM data. Each one started as a single decision point, and each one now runs without my involvement.

## Surviving the 80% Trap

Most people hit 70-80% quality on their first delegation attempt, realise that is not good enough, and have to reverse-engineer everything to start over. This is the process, not failure. The 80% trap catches almost everyone. Knowing it is coming makes it easier to push through.

The journey to effective AI delegation is not linear. Each round improves your ability to specify requirements and spot problems. Big Design Up Front does not work here. You cannot write a detailed spec and parallelise the work like a traditional software project. Instead, start from use cases and pull through functionality. Let the agent reveal what is needed through iteration.

Approach AI delegation like hiring contractors: experiment quickly and move on if something is not working. Do not get stuck trying to make a suboptimal approach work. The goal is to find what works for you.

The path to effective AI delegation is not smooth. It is fiddly and sometimes frustrating. But every experiment brings you closer to real leverage. The mess is part of the process.

## Build Infrastructure, Not Tasks

The contractor metaphor has limits. You are building a delegation system, not just hiring a contractor.

Your CLAUDE.md file and your [skills](/how-to-use-claude-code-skills/) are your operations manual for the AI team. They encode how you work, what you expect, and how decisions should be made. Every time you refine them, you are training your infrastructure to work better without you. Share them with others. Unlike tribal knowledge locked in someone's head, these are portable, forkable, improvable. I have written about [how simple orchestration patterns beat clever engineering](/your-agent-orchestrator-is-too-clever/). A bash loop calling an agent repeatedly outperforms elaborate multi-agent architectures.

One pattern I am exploring: using task managers like Reclaim as a queue, with Claude Code as the executor. When you start a Reclaim task, the agent spins up with context. You are delegating your task system, not individual tasks.

## The Payoff

The awkwardness is a sign you are learning and making progress. If we learn to delegate and let go of our perfectionism, real leverage opens up for us. The beauty of the AI age is that this leverage is beginning to be available to all, not just high-performing leaders. We need to learn the skills they use to realise the same benefits.

Every experiment brings you closer to the kind of leverage that transforms your workflow. You do not need a perfect system. You just need to start.

[^1]: Shreyas Doshi's radical delegation framework considers both impact to the business and the person's confidence level to determine how hands-on a leader should be. The higher the stakes and lower the confidence, the more closely you need to be involved. See his [original thread](https://x.com/shreyas/status/1401598910792011776){:target="_blank"} for more.
