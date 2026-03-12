---
layout: post
title: "Feedback Is the New Bottleneck"
date: 2026-03-13 07:00:00 +0000
series: "Where AI Lives"
categories:
  - ai
  - engineering
  - productivity
---

AI compressed the build cycle from weeks to hours. It did nothing for the feedback cycle.

A developer can generate a working feature in an afternoon, while getting feedback on whether it was the right feature still takes a week. We have all heard about the productivity gains from AI coding tools, but a recent study from MIT tells a different story. Researchers found that engineers who reported being 20% faster with AI were part of teams delivering 20% slower overall.[^mit] The individual feels faster, but the organisation ships slower.

<!--more-->

This happens because coding was rarely the actual bottleneck in a software delivery system. When a developer generates code faster, they push more work into the next stage: code review, testing, deployment, requirements clarification. If those stages are not also getting faster, the queue grows. I wrote about how this is already playing out in [Code Review Is Dying](/code-review-is-dying/), where pull requests now take seconds to create and hours to evaluate. The review side of the conversation is still almost entirely manual.

But the problem runs deeper than code review. There are at least four feedback loops in an AI-assisted build cycle, and most teams are only closing the first one.

## Four Loops

**Loop 1: Code checks itself.** The AI reviews its own output. Tests pass, linter is clean, type checker is happy. This is what everyone has. It is table stakes, and it runs at machine speed.

**Loop 2: Does it look right?** This is the visual and behavioural check. Cursor recently launched computer use and video output, so agents can now run the software they build and send you a recording rather than just a diff.[^cursor] Devin added autofix for review comments, closing the loop between reviewer feedback and code changes. These tools are immature but improving fast, and they take a meaningful chunk of verification work off human shoulders.

**Loop 3: Would anyone use this?** Load a customer persona into the AI, show it the prototype, ask what it thinks. Synthetic customers are not a replacement for real ones, but they are an excellent filter. If the AI persona spots obvious usability problems or missing features, you fix them before burning a real user's time. The concept extends further: StrongDM's Software Factory creates behavioural clones of third-party services like Okta, Jira, and Slack, letting agents validate against realistic simulated environments without hitting real APIs.[^strongdm] They call these "Digital Twin Universes." It is loops 2 and 3 combined, agents testing their own work against realistic simulations at scale.

**Loop 4: Real customers.** The one that matters most. Nothing replaces a real person using your software in their own context, with their own data, for their own reasons. But it is the slowest loop by far, and it always will be.

The teams that are winning are deliberately closing all four loops. The ones struggling have loop 1 running at machine speed and loop 4 running at human speed, with nothing in between.

## The Exhaustion Gap

When code production speeds up but feedback stays slow, the human becomes the bottleneck in every loop. The AI approaches its hundredth prompt with the same energy as its first, while the human reviewing, approving, and validating is running out of steam by mid-afternoon.

This creates what I think of as the exhaustion asymmetry. With human colleagues, natural rhythms emerge. You both get tired, take breaks, and have energy that ebbs and flows in patterns you understand. With AI, the human is the only one who needs rest while the machine keeps generating work that needs evaluating. Permission fatigue, review fatigue, the endless "just need a human to press approve" requests. Cory Doctorow calls this the reverse centaur: humans whose entire purpose is to support the machine's needs.[^doctorow]

The answer is to build the intermediate feedback loops so fewer things need human review. Synthetic customers, digital twin environments, and proper automated evaluation all reduce the supervision burden. Without those intermediate loops, you will burn your people out. The reviewers who care most about quality will be the first to go, because they are the ones who read the code instead of skimming it.

## Where the Surplus Goes

When AI compresses weeks of work into days, the surplus has to go somewhere. The developer absorbs it as slack, or the company extracts it as more output, or the team spends it on code quality. The most productive option is experimentation: trying ten things instead of one, running spikes and prototypes that were previously too expensive to attempt.

Spikes are particularly well-suited to AI because the code does not need to be production-grade. You are just learning. But you can only invest the surplus in experimentation if you have the feedback loops to tell you which experiments worked. Otherwise you are just generating more code that nobody evaluates.

## Close the Loop

The constraint has shifted from "how fast can we build?" to "how fast can we learn whether we built the right thing?"

If you lead a team, map your feedback loops. Identify which ones run at machine speed and which ones still depend on a human who was already busy before AI arrived. Build the intermediate loops. Invest in synthetic validation, automated evaluation, and proper quality gates that run before a human is notified. Every week you leave those gaps open, the bottleneck gets worse, the queue grows, and your best people absorb the cost.

Teams that solve the feedback bottleneck will build faster and in the right direction. Teams that do not will build faster into a wall.

[^mit]: Presented by Will Lytle (Plandek) and independently corroborated by Yigit Darcin (Trendyol) at CTO Craft Con, March 2026. Trendyol found that 90% of developers believed they were faster with AI, but measured delivery showed teams were 20% slower due to downstream overhead.

[^cursor]: Cursor launched agent computer use and video output in February 2026, allowing agents to run the software they build and send video demonstrations of their work. Devin's autofix feature closes the loop between review comments and code changes autonomously.

[^strongdm]: StrongDM's [Software Factory](https://factory.strongdm.ai){:target="_blank"} creates synthetic replicas of services like Okta, Jira, Slack, and Google Workspace, allowing AI agents to validate against realistic environments at scale without hitting real APIs or incurring rate limits.

[^doctorow]: Cory Doctorow, [Pluralistic](https://pluralistic.net/2025/12/05/pop-that-bubble/#u-washington){:target="_blank"}, December 2025. The reverse centaur pattern: "the van uses the driver up."

Thanks to Mick Davison for conversations that shaped this post.
