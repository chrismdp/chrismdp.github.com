---
layout: post
title: "Ralph In One Line, No Setup"
date: 2026-05-10 12:00:00 +00:00
permalink: /running-ralph-loops-is-easy/
replaces: /running-ralph-loops-is-easy-january-2026/
image: /assets/img/ralph-lessons-motif.jpg
infographic: /assets/img/ralph-lessons-infographic.jpg
series: "Building Ralph"
categories:
- ai
- engineering
---

I've made it easier than ever to get started with Ralph: `npx airskills add chrismdp/ralph` and you are running.

Ralph is an autonomous engineering loop. A bash script spawns a fresh Claude Code session, hands it the next markdown ticket from your repo's queue, lets the agent do the work and flip the ticket from `todo` to `done`, then spawns the next session. [Geoffrey Huntley](https://ghuntley.com/ralph/){:target="_blank"} wrote the original in two lines of bash and named it after Ralph Wiggum, the Simpsons character who keeps trying the same thing until it works. [Airskills](https://airskills.ai) is the registry that ships the skill: one command installs it into Claude Code, Cursor, or any other agent setup it detects on your machine, and the [incorporation](https://airskills.ai/docs/concepts/incorporation) protocol keeps upstream changes from clobbering your local edits.

Four months of running Ralph in production taught me which moving parts to cut. Even when you have decided [the agent orchestrator is too clever](/your-agent-orchestrator-is-too-clever/), the setup around the loop wants to grow: a ticket database, a separate skill for managing it, a copy of `RALPH.md` per project. None of that is Ralph. The version I run now keeps the primitive, which is a loop, a prompt, a queue, and an agent that knows when it is done, and drops everything else.

<!--more-->

## What The Skill Does

The install drops two files into `~/.claude/skills/ralph/` (and Cursor, Pi, or whatever else you have configured). `SKILL.md` is the instructions every engineer in the relay reads at the start of its turn: how to pick the next ticket, claim it, do the work, mark it done, and exit. `ralph.sh` is the bash loop that spawns those engineers and streams their output.

Edit `~/.claude/skills/ralph/SKILL.md` however you want and your changes stay local. When I push an update upstream, [incorporation](https://airskills.ai/docs/concepts/incorporation) handles the merge: your agent reads the new version, explains what changed, and you decide in a sentence what to pull in. You do not have to choose between forking and staying current.

## Files Beat Beads

The original Ralph used [Beads](https://github.com/steveyegge/beads){:target="_blank"} to store tickets. Beads is a lovely little issue tracker and it solved the obvious problems: a queue, status fields, comments for handoffs between sessions, and sync to git.

Four months in, the same friction kept showing up: every new repo needed `bd init`, cross-machine sync needed a `beads-sync` branch and a config file committed to main, comments on beads were rarely better than git commit messages, and the PM layer for managing beads needed its own skill. It was all extra weight on a primitive that did not need it.

So I switched to markdown files. A ticket lives in `docs/tickets/<slug>.md` (or `docs/changes/`, the skill accepts both) and looks like this:

{% highlight markdown %}
---
status: todo
title: Add login form to homepage
created: 2026-05-10
---

# What

A user lands on the homepage and sees a login form with email and password fields.

# Acceptance

- Form submits to `/api/login`
- Invalid credentials show an inline error
- Successful login redirects to `/dashboard`
{% endhighlight %}

Status flips through `todo` to `doing` to `done`, with `blocked` for human-only work. The current engineer reads frontmatter to find the next file, edits it to claim the ticket, commits the implementation alongside the status flip, and exits, and the next engineer picks the next file after that. There is no database, no separate branch, and no sync step.

Beads still works as a fallback: if the loop finds no ticket directory but spots an initialised `.beads/` and a `bd` binary, it falls back to the old workflow. I have not removed beads support, only demoted it.

## Try It

In your project:

{% highlight bash %}
npx airskills add chrismdp/ralph
mkdir -p docs/tickets
{% endhighlight %}

Write a ticket using the example above as a template, then:

{% highlight bash %}
~/.claude/skills/ralph/ralph.sh        # up to 10 iterations
~/.claude/skills/ralph/ralph.sh 100    # up to 100 iterations
{% endhighlight %}

The loop reads the next ticket, hands it to a Claude Code session running the `/ralph` skill, watches the session work the ticket through `doing` to `done`, and then spawns the next engineer. Ctrl-C stops it cleanly; if you run out of tickets it waits for new ones, and if you exhaust the iteration budget it exits with a summary of what is left.

## What I Cut

The bundled `ralph-pm` skill is gone. Its job was managing beads through conversation, which was useful when beads was the queue but redundant when the queue is just markdown files. In a planning terminal, invoke `/ralph` and ask it to draft the tickets you want: the same skill that runs the loop also knows how to author the tickets that go into it. The PM side of Ralph is just `/ralph` running in a different window.

`RALPH.md` is gone too. The instructions used to live in a 167-line file you copied into every project and customised to your stack; the skill carries them now, and project-specific overrides go in `CLAUDE.md` or `AGENTS.md`. Those load at session start regardless of which agent is reading them, and the `/ralph` skill yields to them when they conflict.

The two-layer setup with a separate Ralph PM terminal is still useful, just lighter: on longer sessions you still want a planning terminal alongside the build loop, and now it is plain `claude` open in a window editing ticket files directly, with no skill required and no beads commands to remember.

## What Still Goes Wrong

A clean install does not save you from the patterns that sink Ralph loops in production. Most of what I learned in the last four months, and most of what came up in the Q&A at the [AI Engineer Europe workshop](/ralph-loops-aie-europe/), comes back to four failure modes.

**No feedback turns the loop into a slot machine.** Without something the agent can use to tell when it is done, whether tests, a type checker, an AI judge looking at output, or screenshots compared against criteria, the loop will mark broken work as finished and march on. AI giving feedback on AI works well, so lean into it.

**Vague prompts are silent failure.** "Build the next ticket" is too thin. The agent will build something, declare it done, and move on. The prompt has to encode the role and the exit conditions. Mine starts with "you are one engineer in a relay team, do exactly one change, then drop the context and stop". That framing is what makes the loop know what "done" means. Tickets need the same discipline: describe the problem so the engineer is not wasting context replaying decisions you already made. Dave Rensin's goldfish protocol is the right test. Read the ticket back to a fresh Claude session and ask it to tell you everything it would need to implement the feature. If it asks questions, the ticket is broken. Answer the questions in the ticket itself and try again until the fresh session says it has what it needs.

**Over-specking the context kills the loop.** A 2,000-line `CLAUDE.md` on day one is its own kind of failure. The document has to grow with use. Every time the loop does something wrong in a way that matters, write that lesson into the context. The document earns its length. The same rule applies to the Ralph skill: when the loop blocks on something, the answer is almost always a missing piece of documentation rather than a sharper prompt.

**Reaching for an orchestrator.** When a loop gets stuck, the temptation is to add multi-agent coordination, a planner, a task graph. I have done this and [written about how it failed](/your-agent-orchestrator-is-too-clever/), so resist the urge. The two real paths are upgrading the ticket format, with better dependencies and clearer acceptance criteria, and upgrading the loop body, so it runs the test suite before marking done or stops on a repeat error. Most of my productivity gains in the last month came from sharper tickets, not from anything resembling orchestration.

Two practical caveats sit alongside those. Manual testing for things that cannot be automated still needs a human in the loop, marked `status: blocked` with a note. And token cost matters: running Ralph continuously eats through quota, a Max20 plan is the realistic floor for sustained autonomous work, and the value has exceeded the cost on every project I have run it against, but go in eyes open.

The bottleneck that has not gone away, and the one I [could not answer cleanly at AIE Europe](/ralph-loops-aie-europe/), is review. The loop produces work faster than I can read it, and the apprenticeship rung that used to teach junior engineers how to read code well is the same rung Ralph has eaten. I do not have a clean answer yet, and I am working on it.

## Distribution Was The Friction

The Ralph primitive is small enough to write in an afternoon, and Geoffrey Huntley's [original was two lines of bash](https://ghuntley.com/ralph/){:target="_blank"}. Getting it to other people without three steps of setup that they would not all complete is what took the time. [Airskills](https://airskills.ai/chrismdp/ralph) moved that to one command, the file-based queue removed the database dependency, and the skill took the instructions out of every project repo and into one published place that I can update from anywhere.

The install is one command. Everything that makes the loop reliable, namely sharp tickets, real feedback, and a `CLAUDE.md` that grew with use, still happens in the codebase, where it always has.
