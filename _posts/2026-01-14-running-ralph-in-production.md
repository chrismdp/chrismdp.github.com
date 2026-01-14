---
layout: post
title: "Ralph Redux: 6 Lessons from Autonomous Agents"
date: 2026-01-14 12:00:00 +0000
image: /assets/img/ralph-lessons-motif.jpg
infographic: /assets/img/ralph-lessons-infographic.jpg
categories:
- ai
- engineering
---

I wrote about [Ralph loops](/your-agent-orchestrator-is-too-clever/) last week and have since been running them continuously on a real project. Here is what I learned.

The short version: it works. I have shipped more in the past week than I would have in a month of evening coding sessions. The agent runs, commits code, and moves on to the next task while I handle product decisions. But "it works" hides a lot of calibration. The lessons below are about what I had to adjust to make it practical.

<!--more-->

## The Setup

I am building something new using Greg Isenberg's "demo driven development" methodology.[^1] Rather than coding it myself, I thought I'd try using my version of Ralph for this, building it autonomously while I handle product decisions. My setup is [available on GitHub](https://github.com/chrismdp/ralph){:target="_blank"} if you want to follow along. The architecture has two layers: a Ralph loop that builds, and a Ralph PM that feeds it work.

[^1]: Greg's [LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7411084410546049024){:target="_blank"} lays out the approach: ship an MVP the same day, design interactions to fit a 10-second screen recording, treat short-form video as a live feedback channel, and iterate daily until the app explains itself. I remember the same idea being discussed in game developer circles around the [indiepocalypse](/why-i-hope-i-ll-weather-the-indiepocalypse/): record a tiny GIF to test whether a game's hook lands before investing in full development. That practice is now coming to apps. It is the lean startup updated for the age of AI-assisted building.

<img src="/assets/img/ralph-two-layer-setup.png" alt="Two-layer Ralph setup: PM on the left, builder on the right" style="max-width: 100%; margin: 1.5rem 0;" />

On the left is Ralph PM, an interactive Claude Code session where I discuss features and priorities. On the top right is the Ralph loop, autonomously working through beads. On the bottom right is the dev server for visual verification.

The PM creates beads through conversation. The loop picks them up and builds. I can feed work in without stopping the builder. This separation of concerns is the key practical insight from running this setup.

## Lesson 1: Context is Investment

Ralph will just crack on. Unless you are explicit about what decisions require human input, it will make product decisions itself. Sometimes these are fine, sometimes they are not what you wanted.

My first instinct was to add more rules to RALPH.md about when to stop and ask. That does not scale. The better approach is treating every blocked bead as a context failure. When Ralph blocks because it cannot decide something, I do not just unblock it with an answer. I update the project documentation so future sessions can make that decision autonomously.

I symlinked relevant notes from my vault into the repository. Design principles, user personas, product decisions I have already made. Ralph can look these up instead of guessing. This feels like investment because it is. Each hour spent on documentation saves multiple hours of correcting wrong assumptions.

## Lesson 2: Visibility is the Hard Part

Testing itself is fine. TDD works the same whether a human or an agent writes the code. The hard part is giving the agent visibility into what is actually happening.

I wired up browser access using a mixture of Playwright, MCP, and Claude in Chrome so Ralph could visually verify UI changes. It would start the Flutter dev server, navigate to the screen, take a screenshot, and confirm the change worked. This mostly functioned but hit edge cases. Certain interactions required workarounds. Some things could not be automated at all.

For anything that requires interactive testing, microphone input, complex gestures, I created a `manual-testing` label. Ralph skips these beads and I handle them in interactive sessions. Recognising that some verification needs a human in the loop is part of making this work, at least for now.

The principle holds: give Ralph a way to test itself. Automated tests, visual verification, type checking, linting. The more feedback it gets, the better the output. But perfect automation is not required. Knowing what to automate and what to handle manually is part of making this practical.

## Lesson 3: The Two Layer Architecture

Running Ralph PM alongside the build loop solved a coordination problem I did not anticipate.

If you add beads by committing directly to main while Ralph is also committing, the commits bleed into each other. Git handles the merges fine but the history becomes confusing. Worse, Ralph might pull mid-work and get confused about state.

The solution is git worktrees. Beads sync to a separate branch. Ralph PM commits there while the builder commits to main. This eliminates conflicts, keeps history clean, and lets both run simultaneously.

```toml
# In .beads/config.toml
[sync]
branch = "beads-sync"
```

Ralph PM also monitors blocked beads. A background agent checks for beads with `needs-info` labels and alerts me when something is stuck. This means I do not need to watch the builder constantly. I can focus on other work and respond when Ralph actually needs me.

## Lesson 4: Bead Sizing

One thing I have not fully figured out is the optimal size of a bead. They can be tiny (a single function or UI tweak) or larger (an entire feature slice). Both work but the tradeoffs differ.

Smaller beads mean more iterations, more handoffs, more commits. Each iteration has token overhead: reading RALPH.md, checking bead status, running tests. That overhead adds up. Larger beads risk context window exhaustion and require Ralph to break them down itself, which works but adds another iteration.

My current heuristic is that a bead should be completable in one focused session but not trivial. If I would estimate it at under an hour of human work, it is probably right. If it feels like a full day, break it up. This is not scientific and I am still calibrating.

## Lesson 5: Tokens Add Up

Running Ralph continuously burns through tokens fast. I exhausted my Max5 allocation and upgraded to Max20. The value exceeds the cost, but know this before you start: if you are experimenting with a toy project, the free tier will not last long. If you are building something real, budget for a higher tier from the start.

## Lesson 6: The Output Parsing Problem

Most of the complexity in ralph.sh is parsing Claude Code's streaming JSON output, not orchestration logic.

The `-p` flag runs Claude in print mode but does not give verbose output. You cannot see tool calls, reasoning, or intermediate steps. For debugging and monitoring, I needed to construct my own display by parsing the stream-json format. It is not elegant but it works.

```bash
claude --permission-mode acceptEdits --verbose --print "Read @RALPH.md..." --output-format stream-json | while read -r line; do
    type=$(echo "$line" | jq -r '.type // empty' 2>/dev/null)
    # ... parse and display
done
```

Hopefully Anthropic will improve the CLI's verbose output options and make this unnecessary.

## Try It Yourself

I have published [my Ralph setup on GitHub](https://github.com/chrismdp/ralph){:target="_blank"}. Copy the files, customise RALPH.md for your stack, create some beads, and run the loop.

Start with a single terminal running ralph.sh. Add the PM layer once you want to feed work in without stopping the builder. The complexity can grow with your needs.

The agents are good enough now. The orchestration is simple enough to understand. The only thing left is to use it.
