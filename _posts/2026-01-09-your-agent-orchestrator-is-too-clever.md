---
layout: post
title: "Your Agent Orchestrator Is Too Clever"
date: 2026-01-09 10:00:00 +0000
image: /assets/img/ralph-loops-main.jpg
categories:
- ai
- engineering
---

The most sophisticated agent orchestration system I have seen this year is Gas Town[^1], Steve Yegge's multi-agent factory for coordinating dozens of Claude Code instances. It has seven worker roles, patrol agents, molecular workflows, a two-tier Beads system, and enough Mad Max theming to fill a feature film. Yegge describes it as "Kubernetes mated with Temporal and they had a very ugly baby together."

It's also way too complicated. Gas Town is just a series of Ralph loops with extra steps.

<!--more-->

## The Bitter Lesson Strikes Again

Richard Sutton's bitter lesson in AI is simple: general methods that leverage computation beat specialised approaches that encode human knowledge. The history of AI is littered with clever systems that were eventually surpassed by dumber methods running on better hardware. Chess engines, image recognition, language models: scale and simplicity win every time.

This lesson keeps playing out in agent orchestration. Teams build elaborate multi-agent systems with specialised roles, complex handoffs, and sophisticated state machines. I [tried this myself last year](/ai-swarms-failed-toyota-vs-ford-development/), running four Claude instances in parallel with a detailed PRD. The result was duplicated code, impossible coordination overhead, and a completely unusable codebase. Meanwhile, a technique called Ralph loops achieves better outcomes with a bash for loop. Feed an agent the same prompt repeatedly, let it see its previous work in the files, and watch it iterate until done. That is the entire architecture.

Matt Pocock [released a video](https://www.youtube.com/watch?v=_IK18goX4X8){:target="_blank"} explaining why this works so well now. The answer is model capability. Opus 4.5 and GPT 5.2 crossed a threshold where simpler orchestration approaches became viable. The models are good enough to handle reasonable tasks without elaborate guardrails. You do not need complex state machines when the agent can reliably remember what it was doing and figure out what to do next.

## What Ralph Actually Is

Geoffrey Huntley [created the technique](https://ghuntley.com/ralph/){:target="_blank"} in July 2025. The core is embarrassingly simple:

{% highlight bash %}
while :; do
  cat PROMPT.md | claude-code --continue
done
{% endhighlight %}

Feed the agent a prompt describing what you want built. Let it work. When it finishes or gets stuck, the loop restarts with the same prompt. The agent reads the files, sees its previous work, and continues from there. The "self-referential" aspect comes from the agent seeing its own modifications, not from some clever output routing.

Pocock's implementation adds a JSON file tracking which tasks are complete, a progress log for agent memory, and git commits after each completed task. When all tasks are done, the agent outputs a completion promise and the loop exits. Simple feedback loops through tests and type checking ensure the code actually works.

The technique is described as "deterministically bad in an undeterministic world." Failures are predictable because the prompt never changes. When something breaks, you know exactly what to tune. This turns debugging into prompt refinement rather than architectural archaeology.

The loop also creates relentless focus, bluntly presenting the same goal until the agent completes it. No drift into tangential work. No getting distracted by interesting problems that are not the current priority. The repetition creates a forcing function that sophisticated orchestrators lack.

## Beads: Simple Task Management in Git

Separate from the orchestration complexity, Yegge also released [Beads](https://github.com/steveyegge/beads){:target="_blank"}: a lightweight task management layer that lives in Git. It stores tasks as a dependency-aware graph using hash-based IDs like `bd-a1b2` to prevent collisions. The agent can query for ready work, claim tasks, and mark them complete. Nothing fancy, just tasks in your repo.

I combine Beads with a `RALPH.md` file that treats the agent as one engineer in a relay team:

{% highlight markdown %}
# Ralph Loop Instructions

You are one engineer in a relay team building this project.
Each engineer picks up where the last one left off.
Your job is to complete ONE task and then stop.

## On Start

1. Read `progress.txt` to see what the previous engineer accomplished
2. Run `bd ready` to see available tasks
3. Run `bd list --status in_progress` to check for any work left mid-flight
4. Run `go test ./...` to ensure the codebase is green before starting

## Pick a Task

1. Choose the next logical task based on dependencies and project state
2. Run `bd show <id>` to read the full task and acceptance criteria
3. Run `bd update <id> --status in_progress` to claim it

## On Finishing ONE Task

1. Run `go test ./...` to confirm all tests pass
2. Close completed tasks: `bd close <id>`
3. Append to `progress.txt` with what you accomplished
4. Commit all changes including progress.txt
5. Stop work
{% endhighlight %}

The critical constraint is ONE task per context window. Without this, agents try to be helpful and keep going, eventually losing coherence or drifting off course. One task, commit, stop. Let the loop handle continuity.

The `progress.txt` file becomes the handoff document between iterations. Each "engineer" reads what the previous one did, picks up the next task, and leaves notes for whoever comes next.

There is a Ralph Wiggum plugin in the Claude Code marketplace that automates the loop, but it does not clear context between iterations. Stale conversation history accumulates instead of letting files and commits carry the state forward cleanly. The approach has room to improve.

## The Double Loop

Two nested loops now operate at different abstraction levels.

The inner loop is the agent itself. Claude Code, Codex, whatever you prefer. It takes a task, attempts implementation, hits errors, self-corrects, and iterates until the task is complete. This inner loop already beats structured workflows because the agent can adapt to unexpected situations rather than failing on edge cases the workflow designer did not anticipate.

The outer loop is Ralph. It selects which task to work on next, feeds it to the inner loop, and moves on when done. This outer loop is also pretty basic, which is exactly why it works. The agent decides priorities based on the current state of the codebase, not a predetermined sequence that might be wrong by the time execution reaches it.

This double loop structure is why [multi-phase plans feel unnatural](/coding-with-ai/) compared to working through a backlog. Real engineers do not follow elaborate sequential plans. They look at what needs doing, pick the highest priority item, complete it, and repeat. The Ralph loop mirrors actual engineering workflow in a way that complex orchestrators do not.

## Sprint Prioritisation Falls Next

An agent that can intelligently select which coding task to tackle next can also handle sprint prioritisation. Feed the agent your backlog, your product requirements, your customer feedback. Let it decide what matters most right now based on current context. An agent with access to your codebase, your analytics, and your customer conversations can make better real-time priority decisions than a human working from two-week-old sprint planning notes.

Daniel Jones put it bluntly: one product engineer can look after an entire product now, because human communication is several orders of magnitude too slow. The bottleneck is coordination overhead between humans trying to agree on what to build next.

## The Speed Problem

Yegge's follow-up post tells a story about two developers, Ajit and Ryan, pushing coding agents as hard as anyone on the planet. They have unlimited tokens, multiple accounts, maximum possible throughput. Team coordination breaks down completely at these speeds.

Two hours ago is ancient history. Information from earlier today is so stale it might as well be from two weeks back. They have developed new rules for working together: everything must be 100% transparent and announced immediately, all the time. If your work is not visible the moment you do it, nobody will ever see it because the context has already moved on.

This does not scale to big companies. One company Yegge spoke with was getting so disrupted by merge conflicts that they decided "one engineer per repo" was the only viable approach. They gave up on coordination entirely and let individual velocity dominate. The coordination tax had become more expensive than redundant work.

## From Coding to Business

Simple loops beat complex orchestration for coding, and coding is just one type of knowledge work. The same principle applies to running a business.

Marketing, sales, product decisions, customer support: each of these is amenable to the same double-loop structure. An inner loop of an agent doing the task with self-correction. An outer loop selecting which task matters most right now. Human oversight at the strategic level, but execution flowing through automated loops that never tire and never lose context.

The models still need more capability, the integrations need more work, and the feedback loops for business outcomes are slower than test suites. But the trajectory is clear. [Consistent mediocrity scales better than occasional brilliance](/ai-is-consistently-mediocre/), and loops are how you get consistency.

## What This Means

If you are building elaborate agent orchestration systems, ask yourself what assumptions those systems encode. Are you building complexity because the models need it, or because you do not trust them? Gas Town has seven worker roles and elaborate patrol systems, and Yegge admits the models still need "a lot of elbow grease" to keep running. Better models plus simpler architecture might be the actual answer.

If you are an engineering leader planning AI adoption, reconsider your coordination overhead. The teams that win will be the ones moving fast enough to take advantage of what simple loops already enable. That means smaller teams, radical transparency, and a willingness to let agents make decisions humans used to make.

If you are an individual developer, Ralph loops work today. You do not need Gas Town or any other elaborate system. A bash loop, a prompt file, and a good model will let you ship code while you sleep. Start there. The complexity can come later, if it ever needs to come at all.

The bitter lesson keeps teaching the same thing. Simpler methods plus more compute beat clever engineering. In 2026, the agents are good enough that a for loop is a legitimate orchestration strategy. Your agent orchestrator is probably too clever. Mine certainly was.

<img src="/assets/img/ralph-loops-orchestrator.jpg" alt="Ralph loops: simple beats clever" style="width: 50%; display: block; margin: 2rem auto;" />

[^1]: [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04){:target="_blank"} is extremely long. For a shorter follow-up, see [The Future of Coding Agents](https://steve-yegge.medium.com/the-future-of-coding-agents-e9451a84207c){:target="_blank"}.
