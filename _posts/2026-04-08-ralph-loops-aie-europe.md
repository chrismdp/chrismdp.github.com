---
layout: post
title: "Ralph Loops Live at AI Engineer Europe 2026"
date: 2026-04-08 07:00:00 +0000
permalink: /ralph-loops-aie-europe/
categories:
- ai
- engineering
image: /assets/img/ralph-loops-aie-europe.jpg
series: "Building Ralph"
---

Last week I ran a two-hour Ralph loops workshop at AI Engineer Europe in Amsterdam, with about a hundred engineers, live coding, and a Q&A that went harder than the talk itself. Video below.

<div class="video-container mb-8">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/2TLXsxkz0zI" title="Ralph Loops Workshop at AI Engineer Europe 2026" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<!--more-->

I opened with a show of hands: who is no longer writing any code themselves? Most of the room put their hands up. Six months ago that would have drawn two or three. We looked at each other for a moment and the implication hung in the air.

## What Ralph Loops Are

[Ralph loops](/your-agent-orchestrator-is-too-clever/) came from Jeffrey Huntley around June last year. The name is from Ralph Wiggum, the Simpsons character who just tries the same thing over and over. The core idea: after an AI finishes a task, point it at the task again. When models were weaker, this caught things they had missed. Now that models are stronger, the real value comes from pointing a loop at a whole pile of work and letting it run.

I used to orchestrate AI the hard way. I built an n8n workflow for my newsletter that took weeks to write and broke at 2pm every Monday. Building a workflow that complex was exactly the kind of work AI should be doing for me, not the kind of work I should be doing to manage AI. I eventually copied the n8n JSON into Claude Code and asked it to write a skill based on the flow. It now runs as a simple loop and produces better first drafts than the complex workflow ever did.

## Building a Pomodoro Timer Live

The workshop was practical. I had a simple Python Pomodoro timer with one command, one test, and a folder of tickets. We spent the first hour building it up with Ralph loops, audience following along on their own machines.

The naive loop first: take a ticket, build it, then tell the AI to build it again and see if it catches anything missed. It often does. The deeper move is to skip the dependency graph. I tried building one once, had six parallel agents fighting over the same tickets, and wrote a fairly depressing blog post about it.[^1] The answer is to tell the AI to pick the next most important ticket. It reads what has been done, figures dependencies on the fly, and chooses. What AI handles poorly is managing dependencies in parallel, and it turns out you probably do not need to start there.

The second stage is running the loop from a shell script: `while true; claude; done`. The audience watched it chew through the Pomodoro feature list while we talked about other things. Claude Code also has a built-in `/loop` command that schedules this internally, so you do not even need the shell wrapper.

## The Question I Could Not Answer

Someone in the Q&A had set up adversarial reviews: a dev agent writes code, a reviewer agent critiques it, feedback loops back. It works well. But they were still the bottleneck in review. The rate at which the system generates specs and code outpaces the ability to review it.

I do not have a clean answer. I find myself in that situation constantly. I wake up to fifteen or twenty draft emails, project updates, content pieces for me to check. A lot of that is work any human could do. The only reason it lands with me is that I have not figured out how to get the AI to do it unsupervised. So the question becomes: do you hire humans to do the review work? Is that an apprenticeship, or is it a treadmill?

Juniors used to learn by doing small, bounded work under senior oversight. AI has eaten that rung. If the only human role left in a workflow is checking AI output, you are hiring for the judgement the apprenticeship used to build, without the apprenticeship.

What I have done is make a conscious decision about which parts of my work I want to do. I want to be the strategist, not the email reviewer. My system drafts, schedules, and gathers, but the strategic thinking stays with me. Drawing that line requires real reflection, because everything is starting to look like a loop.

## Q&A Highlights

**Context rot.** Does a Ralph loop run in the same Claude Code session or spawn fresh ones? Both work. I tend to prefer fresh contexts per iteration. If you are not typing into the session you are not adding context, and the AI can pull files as it goes. With Opus, long context retrieval is good enough that it matters less than it used to.

**Sandboxing.** My setup keeps the AI on a VPS away from my main machine, with specific keys, limited file access, and fine-grained Claude permissions. I will never let it send an email, only draft. I am building [Lockbox](https://github.com/chrismdp/lockbox){:target="_blank"} to make that easier. For a simple start, Docker sandbox isolates the agent inside a container. The concept to read about is the lethal trifecta[^2].

**Tokens.** Should you optimise loops or let them run? Burn the tokens: the right optimisation is freeing your own time, not saving compute. One caveat: at team or enterprise scale the binding constraint is usually the review queue rather than compute, and if procurement cannot absorb the cost, the maths change. For an individual working alone, burning tokens is the right default.

**Theory of constraints.** Teams that adopt AI tools and go slower almost always do so because AI has exposed a bottleneck that was already there: review, release cadence, coordination between services. AI does not create those bottlenecks, it just makes them visible faster. Fix the constraint first, then figure out where the bottleneck moves in the system, and do not work on anything else until that is clear. Read [Goldratt's The Goal](https://en.wikipedia.org/wiki/The_Goal_(novel)){:target="_blank"} if you have not already.

## What I Am Working On Next

The apprenticeship question is the one I keep coming back to. AI has eaten the rung juniors used to learn on, and I do not think the industry has a replacement yet. That is what I am working on.

Workshop code is [on GitHub](https://github.com/chrismdp/pomodoro-workshop){:target="_blank"}. My Ralph skill is on [Airskills](https://airskills.ai){:target="_blank"}. The [video](https://www.youtube.com/watch?v=2TLXsxkz0zI){:target="_blank"} is the best place to start. The live coding gets going quickly and the Q&A from about an hour in is where the hard problems surface.

[^1]: That post is [Your Agent Orchestrator Is Too Clever](/your-agent-orchestrator-is-too-clever/), a record of spectacular failure trying to manage too much parallelism up front.

[^2]: Simon Willison coined the lethal trifecta: untrusted content, internet access, and access to important or secret data in the same agent context. Any two of those three together is a risk. All three is a serious incident waiting to happen.
