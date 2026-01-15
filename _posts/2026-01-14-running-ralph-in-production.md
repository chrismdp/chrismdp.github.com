---
layout: post
title: "Ralph Redux: 5 Lessons from Autonomous Agents"
date: 2026-01-14 12:00:00 +0000
image: /assets/img/ralph-lessons-motif.jpg
infographic: /assets/img/ralph-lessons-infographic.jpg
excerpt: "Treat documentation as compound investment, give agents visibility through automated tests not browser automation, use git worktrees to separate PM from builder, size tasks for single focused sessions, and parse Claude's JSON output for proper monitoring."
categories:
- ai
- engineering
---

I wrote about [Ralph loops](/your-agent-orchestrator-is-too-clever/) last week. Yesterday I built my own version from scratch and ran it continuously on a real project. Here is what I learned.

The short version: it works. I shipped more in a single day than I would have in hours and hours of evening coding sessions. The agent runs, commits code, and moves on to the next task while I handle product decisions. But "it works" hides a lot of calibration, and the lessons below are about what I had to adjust to make it practical.

<!--more-->

## The Setup

I am building something new using Greg Isenberg's "demo driven development" methodology.[^1] Rather than coding it myself, I thought I'd try using my version of Ralph for this, building autonomously while I handle product decisions. My setup is [available on GitHub](https://github.com/chrismdp/ralph){:target="_blank"} if you want to follow along.

The core idea is treating agents as a relay team. Each engineer picks up where the last one left off, completes one bead of work, commits, and exits. The loop script spawns the next engineer, who reads what was just done and continues. No single agent needs to hold the whole project in context because each one inherits state from the codebase and the bead comments left by previous sessions.

<img src="/assets/img/ralph-two-layer-setup.png" alt="Two-layer Ralph setup: PM on the left, builder on the right" style="max-width: 100%; margin: 1.5rem 0;" />

The architecture has two layers. On the left is Ralph PM, an interactive Claude Code session where I discuss features and priorities. On the top right is the Ralph loop, autonomously working through beads. On the bottom right is the dev server for visual verification. The PM creates beads through conversation and the loop picks them up and builds. I can feed work in without stopping the builder, and this separation of concerns turned out to be the key practical insight from running this setup.

[^1]: Greg's [LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7411084410546049024){:target="_blank"} lays out the approach: ship an MVP the same day, design interactions to fit a 10-second screen recording, treat short-form video as a live feedback channel, and iterate daily until the app explains itself. I remember the same idea being discussed in game developer circles around the [indiepocalypse](/why-i-hope-i-ll-weather-the-indiepocalypse/): record a tiny GIF to test whether a game's hook lands before investing in full development. That practice is now coming to apps. It is the lean startup updated for the age of AI-assisted building.

## Lesson 1: Context is Investment

Ralph will just crack on. Unless you are explicit about what decisions require human input, it will make product decisions itself and some of those decisions will be wrong. I watched it ship UI that did not match my vision and features that did not quite work, all because it was guessing at intent rather than asking.

My first instinct was to add more rules to RALPH.md about when to stop and ask, but that does not scale. The better approach is treating every blocked bead as a context failure. When Ralph blocks because it cannot decide something, I do not just unblock it with an answer. I update the project documentation so future sessions can make that decision autonomously. The documentation becomes a growing body of product knowledge that compounds over time.

I symlinked relevant notes from my vault into the repository: design principles, user personas, product decisions I have already made. Ralph can look these up instead of guessing. This feels like investment because it is. Each hour spent on documentation saves multiple hours of correcting wrong assumptions, and unlike verbal explanations to a human teammate, documentation persists across every future session.

## Lesson 2: Visibility is the Hard Part

Testing itself is fine. TDD works the same whether a human or an agent writes the code. The hard part is giving the agent visibility into what is actually happening, and if you do not solve this problem, the loop breaks down entirely.

I wired up browser access using a mixture of Playwright, MCP, and Claude in Chrome so Ralph could visually verify UI changes: start the Flutter dev server, navigate to the screen, take a screenshot, and confirm the change worked. This mostly functioned but hit edge cases with Flutter Web. The framework intercepts browser events at a different layer than browser automation tools expect, so gestures like long press and tap simply did not work through Playwright or Chrome DevTools. Ralph would attempt to verify something, fail to interact with it, decide it could not test the feature, and move on to the next bead. The work got marked done but was not actually verified.

The solution came from understanding Flutter's testing ecosystem. Widget tests can do what browser automation cannot because they operate directly on the widget tree rather than sending events through the browser. A simple `tester.longPress(find.byType(MicButton))` works perfectly in a widget test but fails completely through browser automation. Once I documented this in a testing strategy file, Ralph stopped trying to verify things through the browser and wrote proper widget tests instead.

For anything that genuinely requires interactive testing (microphone input, complex gestures, platform-specific behaviour) I created a `manual-testing` label. Ralph skips these beads and I handle them in interactive sessions. Recognising that some verification needs a human in the loop is part of making this work, at least for now. The principle holds: give Ralph a way to test itself through automated tests, visual verification, type checking, and linting. The more feedback it gets, the better the output. But perfect automation is not required, and knowing what to automate versus what to handle manually is part of making this practical.

## Lesson 3: The Two Layer Architecture

Running Ralph PM alongside the build loop creates a coordination problem. If you add beads by committing directly to main while Ralph is also committing, the commits bleed into each other. Git handles the merges fine but the history becomes confusing, and worse, Ralph might pull mid-work and get confused about state.

Git worktrees fix this. Beads sync to a separate branch while the builder commits to main, which eliminates conflicts, keeps history clean, and lets both run simultaneously. The config is simple:

```toml
# In .beads/config.toml
[sync]
branch = "beads-sync"
```

There is also the problem of in-progress beads. When one Ralph session gets interrupted or runs out of context, the next session inherits whatever state was left behind: uncommitted changes, failing tests, half-finished work. Early on Ralph would just assume the previous session had succeeded and close the bead, even when the work was incomplete. I added a decision table to RALPH.md that forces each session to assess the situation before proceeding: check the working tree, run the tests, read the comments, and only then decide whether to continue the work, fix what is broken, or block the bead for human attention. This small addition eliminated an entire class of silent failures.

Ralph PM also monitors blocked beads through a background agent that checks for beads with `needs-info` labels and alerts me when something is stuck. This means I do not need to watch the builder constantly. I can focus on other work and respond when Ralph actually needs me.

## Lesson 4: Bead Sizing

One thing I have not fully figured out is the optimal size of a bead. They can be tiny (a single function or UI tweak) or larger (an entire feature slice), and both work but the tradeoffs differ.

Smaller beads mean more iterations, more handoffs, more commits. Each iteration has token overhead from reading RALPH.md, checking bead status, and running tests, and that overhead adds up. Larger beads risk context window exhaustion and require Ralph to break them down itself, which works but adds another iteration. If a bead is too large, RALPH.md instructs the agent to split it into smaller beads and exit without doing any work, letting the next session pick up the now-tractable pieces.

My current heuristic is that a bead should be completable in one focused session but not trivial. If I would estimate it at under an hour of human work, it is probably right. If it feels like a full day, break it up. This is not scientific and I am still calibrating.

## Lesson 5: The Output Parsing Problem

Most of the complexity in ralph.sh is parsing Claude Code's streaming JSON output, not orchestration logic. The `-p` flag runs Claude in print mode but does not give verbose output, so you cannot see tool calls, reasoning, or intermediate steps. For debugging and monitoring, I needed to construct my own display by parsing the stream-json format:

```bash
claude --permission-mode acceptEdits --verbose --print "Read @RALPH.md..." --output-format stream-json | while read -r line; do
    type=$(echo "$line" | jq -r '.type // empty' 2>/dev/null)
    # ... parse and display
done
```

It is not elegant but it works. Hopefully Anthropic will improve the CLI's verbose output options and make this unnecessary.

## Try It Yourself

I have published [my Ralph setup on GitHub](https://github.com/chrismdp/ralph){:target="_blank"}. Copy the files, customise RALPH.md for your stack, create some beads, and run the loop. Fair warning: running Ralph continuously burns through tokens fast, and I exhausted my Max5 allocation within a few hours. The value exceeded the cost, so I upgraded to Max20 without hesitation.

Start with a single terminal running ralph.sh. Add the PM layer once you want to feed work in without stopping the builder. The complexity can grow with your needs.

The agents are good enough now. The orchestration is simple enough to understand. The only thing left is to use it.

---

*Thanks to Sachin Shah for contributions to earlier versions of this article.*
