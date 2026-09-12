---
layout: post
title: "(I Am No Longer) Coding With AI"
date: 2026-09-11 07:00:00.000000000 +00:00
permalink: "/coding-with-ai/"
replaces: "/coding-with-ai-april-2026/"
categories:
- development
- ai
- code
- craftsmanship
image: "/assets/img/ai-coding-superbikes-motif.jpg"
excerpt: AI writes the code. I direct the work through Fable High and Astra High,
  rapid design feedback and tests of the whole system. This is how my coding workflow changed.
---

Coding with AI feels like the wrong title for these articles now. I am not coding with AI any longer. The AI is doing the coding, and I am doing the direction.

This is a bigger change than getting faster at writing software. I spend my time talking about what I want, trying what comes back and helping the AI find better ways to judge its own work. For my own projects, I am not reading the code at all. I am making sure good code gets written and good decisions get made.

<!--more-->

## A Conversation With the Codebase

Fable High and Astra High thinking are now my default workhorses for code: Fable High in Claude Code, Astra High in Codex. It is expensive: I am running the top-end subscription plans for both. But switching between them and asking them to review each other's work has been the biggest unlock I have experienced so far. I can keep building with one, then have the other investigate what it has done and challenge its decisions.

With these models, I need far fewer tokens and review steps to get the work finished. That saves me time and attention, which is valuable enough to justify the cost.

I can now keep a stream of consciousness running with the codebase. I talk about what I want to build, notice something else, change my mind about a detail and keep going. I can mention 5-6 things whilst the agent is still coordinating the first one. It can handle that now, turning that conversation into work without requiring me to finish specifying everything before anything happens.

I used to obsess about tracking the AI's work: first in Beads, then in notes on disk, then in GitHub Issues. I would put a whole bunch of work into issues and send agents away to do it, then become the bottleneck when lots of slightly wrong results came back. I described that cycle in [Software Factories Can Handle UX](/software-factories-can-handle-ux/): a dozen half-right screens, another round of corrections, then another dozen things to check.

Now I can keep multiple streams of work going by telling Astra what I want. It makes its own notes. I have barely read them, because it remembers the things I wanted to recall without me managing how it does that. I do not ask my assistant how she keeps her notes, so why would I ask Astra?

The conversation stays with one coordinating agent. I use a delegation skill to send pieces of work to other agents in the background, so the main conversation stays available. I can talk through the next change whilst something else is being built. The coordinator brings that work back, reviews it and fits it into the project.

I ask Astra to make sure it is creating a test / eval harness around the work: the tools, context and checks that let it act and see the result. That can mean starting the application, opening it in a browser or creating a way to inspect what it stored. I want to see the result quickly, work out where the friction is and go round again. Astra builds what it needs to make that possible. Evaluations are tests: they are all part of the feedback loop Astra needs to tell whether its work is correct.

My sessions mostly run on a remote computer I can reach from my phone, with a vault of Markdown files alongside the code. I have not had to arrange a special handoff between Fable and Astra. They save notes in files, so the next agent can pick up where the work has got to without making me explain it all again.

## A Tighter Loop for Design

I have a slightly different loop for design. I use Claude Design and talk to Fable about what I want to see. It changes the designs quickly, I try them, and we iterate. Sometimes I make tiny copy tweaks or move something myself. I can work out how I want the product to feel before the coding agent commits that decision to an implementation.

Once I like it, I hand the design to an agent and go away for a bit. When I come back, it's normally finished and has a fairly perfect version ready for me to review. The prototype gives it the screens, the copy and the behaviour to aim at. I do not need to turn every visual choice into a paragraph in a ticket.

The gallery below is Claude Design's output for a training application I was working on with another developer. I could work through the screens and copy in the prototype, then hand over a visual reference for the implementation.

{% include inline-image.html src="/assets/img/academy-design-pass.jpg" alt="Claude Design's output for a training application Chris was building with another developer, showing the screens and their different states." align="center" width="100%" caption="Claude Design's app for the training application was used as a reference for the developer implementing it. He did a great job of this first time." %}

The gallery stays alongside the code, and we update it when the product changes. This used to be a real pain, but now is a super quick job for AI. I can then tweak these designs with confidence, and the agent can build them.

## Finding Better Ways to Review

I am attempting to run 2-3 projects at once in this way, returning to them through the day. I have to intervene much less to keep the implementation moving when I am working in Astra. It just cracks on. Its agency is extraordinary: I can leave it with something substantial and it keeps moving through the work. (That is, until it hits a usage limit. I'm using banked resets with Codex about _once per day_ right now, on a x20 max plan!) No wonder Tibo announced they have paused new subscriptions to the $200 Pro plan.[^pro-pause]

I am much more directly involved in reviewing the result, and in giving the AI ways to review its own work. I also ask it to come up with creative ways for me to judge what it is building. I do not need to design every one of those tools myself.

One example is the text adventure RPG I have been building. You type what your character does, and the game tells the story through a traveller's diary, with illustrations and a map of the world. The map has to fit the world the game describes. A convincing picture is not enough if its geography contradicts the story.

Astra built me a review form with the whole map and enlarged regions. It let me describe what I could see, then reveal the required geography and the earlier AI judgements. That gave me a way to help it work out whether it was judging another AI correctly. I could point to a particular mismatch and draw on my game-development experience without inspecting the code that generated the map.

{% include inline-image.html src="/assets/img/prompt-evals-map-review.jpg" alt="Astra's map review form, with the whole map, enlarged regions and space for observations." align="center" width="75%" caption="Astra made the form so I could help it judge whether the map fitted the world." %}

I wrote about that in [Prompt Evals Alone Are Useless](/prompt-evals-are-useless/). What struck me was how much of the review process the AI had built for me. I was giving it direction about what good meant, and it was finding ways to make that judgement possible. I am editing this blog post in the same way: filling in a form with comments for the AI on each paragraph.

{% include inline-image.html src="/assets/img/coding-with-ai-blog-review.jpg" alt="The review form for this post, showing its title, feedback fields and an Edit or comment control beneath the opening paragraph." align="center" width="100%" link="/assets/img/coding-with-ai-blog-review.jpg" caption="The form I used to review the post you are reading." %}

## Ensuring Good Code Gets Written

Years ago, I remember [Jeffrey Fredrick](https://www.linkedin.com/in/jfredrick/){:target="_blank"} telling me that my job as a CTO was not to make good decisions, but to ensure that good decisions were made. That is how I now feel about coding. My job is not to write good code. It is to ensure that good code is written.

For my own projects, that does not require me to read or see the code. I ask the AI to create a framework where it uses good engineering practices: refactoring as it works, keeping the codebase from growing unnecessarily and testing whether the overall system behaves properly.

A massively underrated part of coding now is getting the AI to make it easy for you to know whether what it has done is correct. That is work I can ask it to do, just as I ask it to build a feature. The map review form gives me something I can judge without first having to reconstruct the investigation myself.

Tests are part of that codebase too. I ask the agents to find duplicate tests and explain what failure each new test catches. A larger test suite can make every build slower without telling us anything useful. The same is true of instructions: I want the current decisions stated clearly, rather than a growing history of contradictory rules that the next agent has to untangle.

In July, testing my Slack agents from a phone kept turning me into the person who had to check every interaction. So I asked for a fake Slack that the coding agent could use to exercise the real application and inspect the replies. It cut out a lot of the boring early feedback I would otherwise have had to give: things that were obvious as soon as I tried to use it. By the time I reviewed the result in the real Slack client, my attention could go into more targeted, higher-level feedback.

Astra and Fable are now very good at using a browser, checking the interface and finding things that make it awkward to use. They can inspect screenshots, follow a journey and make corrections before I try it. I still come back and use the product, but the agent can do a great deal of the investigation first. Sometimes I just ask: "Please use the screens. Minimize the number of clicks I need to get between sessions. Come up with creative ways to improve this." I might ask for a design mockup first, or ask it to change the flow on the page. Then I review what it has done.

Once the AI has built that environment, I can let it run. I want the system to contain the engineering judgement that helps anyone write good code, and to give the agents enough feedback to apply it.

## AI Acting On Feedback Without Me

I am beginning to run AI automatically in response to user feedback. When a request or complaint comes in, an agent picks it up, checks it and works out what needs attention. It can investigate the problem and suggest improvements before I look at it. In my own applications, a background agent checks for that feedback on a timer.

That work comes back to my coordinating AI. It can show me what the feedback means, what it found and what it proposes to change. If I like the proposed changes, the coordinator can have them implemented. I do not have to start by reading the original request and working out what it means myself. The checks need to cover the whole system, including what the user sees, so the agent can tell whether a change actually improves the experience.

I have one conversation about what we are building, with investigation and implementation happening in the background. I use the system, come back, try it a bit, tweak the copy or ask for a change in behaviour, and repeat.

In [The Harness Is the Bottleneck](/the-harness-is-the-bottleneck/), I explored how much cheaper workers could do, and found that their bills left out expensive review and repair. Right now I am spending more on the models that let this whole conversation move with less intervention. I care about the cost of the finished work and the attention it needs from me, rather than the price of generating the code alone.

I am involved in what gets built, how we decide whether it is good and what happens when it falls short. The coding happens around that conversation.

I am no longer "Coding With AI". I am no longer a coder at all. I am a director of systems, and a delegator of creation. I am moving higher and higher up the stack, and I'm not sure where this ends.

[^pro-pause]: [Tibo Sottiaux’s announcement, 10 September 2026](https://x.com/thsottiaux/status/2098113585683808624){:target="_blank"}. The pause applies to new $200 Pro subscriptions. Existing accounts are unaffected; other plans and the API remain available.
