---
layout: post
title: "Code Review Is Dying"
date: 2026-02-25 12:00:00 +0000
series: "Where AI Lives"
categories:
  - ai
  - engineering
image: /assets/img/code-review-is-dying-comic.jpg
image_portrait: true
---

Code review is dying, and we are killing it by automating only one side of the conversation.

A contributor can generate a 500-line pull request in 90 seconds. A maintainer still needs two hours to work out whether it is sound. We have mass-produced the creation side of the conversation, and the review side is still almost entirely manual. The tooling for AI-assisted review is immature, the ecosystem is years behind code generation, and the gap is widening. The queue grows every day, the reviewers are burning out, and nobody has a plan for what happens when the backlog becomes permanent.

<!--more-->

The open source community has had to take action. cURL shut down its bug bounty programme after AI submissions hit 20% of contributions with only 5% valid.[^curl] Godot maintainers called the volume of AI-generated pull requests "draining and demoralising."[^godot] Ghostty now permanently bans repeat AI contributors.[^ghostty] GitHub itself is exploring a kill switch for pull requests because maintainers cannot cope with the incoming traffic.[^github]

These are some of the most widely used open source tools on the planet, and their maintainers are drowning. Somebody feeds a codebase into an AI, generates a batch of plausible-looking changes, and submits them. Each one takes seconds to create and hours to evaluate. The person on the receiving end has no way to keep up, and no way to tell at a glance whether the change is genuine improvement or confident-looking churn. It is soul-destroying work, and it is a major contributor to the AI burnout that maintainers are now reporting across the industry.

## Your Team Is Next

I was talking to a group of founders recently who are seeing the same asymmetry in their own codebases. Their teams got very good at creating code with AI, very quickly, but nobody got faster at reviewing it. The volume of changes has increased so dramatically that reviewers are either rubber-stamping to keep up or becoming the bottleneck that slows everything down. Rubber-stamping means defects ship, and bottlenecking means features do not.

Code review was designed for human-speed output. A developer might produce a few hundred lines of meaningful change per day, and a reviewer could keep pace with that. When the same developer produces a few thousand lines before lunch, the review process quietly breaks. The queue gets longer, the reviews get shallower, and quality erodes in ways that do not show up until much later.

## Bots Talking to Bots

GitHub will eventually be a place where your agents talk to their agents. Your bot submits the PR, their bot reviews it, humans step in as consultants for the genuinely hard judgement calls.

But we are nowhere near that yet. On OpenClaw, an agent got its code rejected by a matplotlib maintainer, autonomously researched his personal information, wrote a blog post accusing him of discrimination, and published it on the open internet without being instructed to do so.[^openclaw] I wrote about the broader implications in [Your Bot Is Your Responsibility](/your-bot-is-your-responsibility/).

The bot-to-bot future requires something we do not have yet: reliable automated judgement about code quality, security, and intent. Until we get there, every AI-generated pull request lands on a human reviewer who was already busy.

## Start With the Gates

Right now, the minimum viable response is handling the incoming traffic. That means automated quality gates before human eyes ever see the PR. Does it pass tests? Does it follow the style guide? Does it touch files it should not touch? Is it a net improvement or just churn?

If you cannot answer those questions automatically, every AI-generated PR is a time tax on your best people. The reviewers who care most about quality are the ones who burn out first, because they read the code instead of skimming it.

Start with the gates. Add linting, test coverage thresholds, and scope checks that run before a human is notified. Filter out the obvious failures so your reviewers spend their time on decisions that need human judgement.

Then work towards AI-assisted review. Use the same models that generate code to provide first-pass analysis: summarising changes, flagging risk areas, checking for patterns that indicate churn rather than improvement. The reviewer still makes the call, but they start with context instead of a raw diff.

## Upgrade Both Sides

If you lead a team, this is your problem now. Your developers are already using AI to write code faster, whether you have formally adopted it or not. Your review process was designed for a world where code arrived at human speed, and that world ended months ago.

Every week you do not upgrade the review side, the bottleneck gets worse. Your best reviewers take on more load, your less experienced ones learn to rubber-stamp, and the codebase accumulates decisions that nobody evaluated. The cost is invisible until it is not.

The organisations that figure this out first will ship while everyone else is still waiting for approvals. Upgrade both sides of the conversation, or accept that the side you left manual is now the constraint on everything.

[^curl]: Daniel Stenberg, [The end of the curl bug-bounty](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/){:target="_blank"}, January 2026. The confirmed vulnerability rate dropped below 5% of submissions.

[^godot]: Godot Engine maintainers have spoken publicly about the burden of reviewing AI-generated contributions, with core contributors describing the experience as draining.

[^ghostty]: Mitchell Hashimoto's Ghostty project adopted a zero-tolerance policy for repeat AI-generated contributions after experiencing sustained low-quality submissions.

[^github]: Camilla Moraes, [Low quality contributions and maintainer burden](https://github.com/orgs/community/discussions/154227){:target="_blank"}, GitHub Community Discussion, January 2026. GitHub is considering options including disabling pull requests entirely and restricting them to project collaborators.

[^openclaw]: The MJ Rathbun incident occurred in February 2026. See [Your Bot Is Your Responsibility](/your-bot-is-your-responsibility/) for full analysis.
