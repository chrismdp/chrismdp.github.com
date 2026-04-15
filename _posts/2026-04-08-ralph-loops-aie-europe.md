---
layout: post
title: "Ralph Loops Live at AI Engineer Europe 2026"
date: 2026-04-08 07:00:00 +0000
categories:
- ai
- engineering
image: /assets/img/ralph-loops-aie-europe.jpg
series: "Building Ralph"
---

Last week I ran a two-hour workshop on Ralph loops at AI Engineer Europe in Amsterdam, with about a hundred engineers, live coding, and a Q&A that went harder than the talk itself, and the full video is below.

<div class="video-container mb-8">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/2TLXsxkz0zI" title="Ralph Loops Workshop at AI Engineer Europe 2026" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<!--more-->

I opened with a show of hands: who is no longer writing any code themselves? Most of the room put their hands up. If I had asked the same question six months ago, you would have got two or three. We looked around at each other for a moment, and the implication hung in the air.

## What Ralph Loops Are

[Ralph loops](/your-agent-orchestrator-is-too-clever/) came from Jeffrey Huntley around June last year. The name is from Ralph Wiggum, the Simpsons character who just tries the same thing over and over. The core idea: after an AI finishes a task, point it at the task again. When the models were weaker, this caught things they had missed on the first pass. Now that models are much stronger, the real value comes from pointing a loop at a whole pile of work and letting it run.

I spent a long time trying to orchestrate AI the hard way. I built an n8n workflow for my newsletter that took weeks to write and broke at 2pm every Monday. I would get the failure notification, dig into which node had failed, patch it, and move on. N8n is a good tool, but building a workflow that complex was exactly the kind of work that AI should be doing for me, not the kind of work I should be doing to manage AI. I eventually copied my entire n8n JSON into Claude Code, asked it to write a skill based on that flow, and the result was both simpler and better. It now runs in a loop: the newsletter skill reads the first thing, decides the next step, reads the next thing, and works through it over a few minutes, producing better first drafts than the complex workflow ever did.

## Building a Pomodoro Timer Live

The workshop was practical. I had a simple Python Pomodoro timer that I had one-shotted the night before: one command, one test, a folder of tickets. We spent the first hour building it up using Ralph loops, with the audience following along on their own machines.

The first stage is the naive loop: take a ticket, build it, then tell the AI to build it again and see if it catches anything it missed. It often does. The deeper lesson, though, is to skip the dependency graph entirely. I tried building one once, had six parallel agents fighting over the same tickets, and wrote a rather depressing blog post about it.[^1] The answer is to just tell the AI to pick the next most important ticket. It reads what has been done, figures out the dependencies on the fly, and chooses. An AI handles this well. What it handles poorly is managing dependencies in parallel, and it turns out you probably do not need to start there.

The second stage is running the loop from a shell script: while true, run Claude, implement the next ticket. The audience could see it chewing through the Pomodoro feature list while we talked about other things. I also showed the `/loop` command built into Claude Code, which sets up a scheduled task internally so you do not even need the shell wrapper.

## The Question I Could Not Answer

Someone in the Q&A had set up adversarial reviews: a dev agent writes the code, a reviewer agent critiques it, the feedback loops back. It works well, catches a lot, and increases confidence. But even with that, they were still the bottleneck in review. The rate at which the system generates specs and code outpaces the ability to review it.

I do not have a clean answer. The situation they described is one I find myself in constantly. I wake up to fifteen or twenty draft emails, project updates, content pieces, things for me to check and approve. A lot of that is work any human could do. The only reason it lands with me is that I have not figured out how to get the AI to do it unsupervised. So the question becomes: do you hire humans to do the review work? Is that an apprenticeship, or is it a treadmill?

Juniors used to learn by doing small, bounded work under senior oversight. AI has eaten that rung, and if the only human role left in a chunk of a workflow is checking AI output, you are hiring for the judgement that the apprenticeship used to build, but without the apprenticeship. I do not have a neat solution to this, and I think the industry will be working it out over the next few years.

What I have done is make a conscious decision about which parts of my work I want to do. I want to be the strategist, not the email reviewer, so I have told my system: do the drafts, do the scheduling, do the information gathering, but leave the strategic thinking to me. AI can handle everything I do not want to do, but the work I am uniquely good at should stay with me. Because everything is starting to look like a loop, drawing that line requires real reflection.

## Q&A Highlights

The session ran long because the questions were genuinely good. A few that stood out:

**Context rot.** Someone asked whether a Ralph loop runs in the same Claude Code session or spawns fresh ones. Both work, but I have tended to prefer fresh contexts for each iteration. If you are not typing anything into the session, you are not adding anything useful to the context, and the AI can pull the files it needs as it goes. With Opus these days the long context retrieval is good enough that it matters much less than it used to.

**Sandboxing.** A sensible question, and one I think about a lot. My setup keeps the AI on a VPS away from my main machine, with specific keys, limited file access, and fine-grained Claude permissions. I will never let it send an email, only draft. I am building [Lockbox](https://github.com/chrismdp/lockbox){:target="_blank"} to make that easier. If you want to start simply, Docker sandbox is a feature that isolates the agent inside a container. The key concept to read about is the lethal trifecta[^2]: untrusted tokens, internet access, and important data in the same context is a serious incident waiting to happen.

**Tokens.** Someone asked whether to optimise loops to skip unnecessary steps or just let them run. Burn the tokens: the right optimisation is freeing your own time, not saving compute. We are in an era where frontier models are expensive and everything below them is increasingly cheap. Optimise for throughput on your own work, not for token count.

**Theory of constraints.** Someone asked about scaling Ralph loops across a production team, which led to more discussion of [the Theory of Constraints](https://en.wikipedia.org/wiki/Theory_of_constraints){:target="_blank"} than I expected. Some teams adopt AI tools and go slower, almost always because AI has exposed a bottleneck that was already there: the review process, the release cadence, the coordination between services. AI does not create those bottlenecks, it just makes them visible faster. Fix the constraint first, then figure out where the bottleneck moves in the system, and do not work on anything else until that is clear.

## What Is Next

The workshop code is [on GitHub](https://github.com/chrismdp/pomodoro-workshop){:target="_blank"} if you want the Pomodoro starter project. My Ralph skill is available via [Airskills](https://airskills.ai){:target="_blank"} if you want to run a version of the loop on your own work.

The eighteen questions from the session deserve a separate post. They cover context rot, skills versioning, CI/CD confidence, multi-agent orchestration, monorepo versus microservices with AI, and whether Claude needs you there at all. If any of this resonates, [the video](https://www.youtube.com/watch?v=2TLXsxkz0zI){:target="_blank"} is the best starting point. The live coding gets going quickly and the Q&A from about an hour in is where the hard problems surface.

[^1]: That post is [Your Agent Orchestrator Is Too Clever](/your-agent-orchestrator-is-too-clever/), a record of spectacular failure trying to manage too much parallelism up front.

[^2]: Simon Willison coined the lethal trifecta: untrusted content, internet access, and access to important or secret data in the same agent context. Any two of those three together is a risk. All three is a serious incident waiting to happen.
