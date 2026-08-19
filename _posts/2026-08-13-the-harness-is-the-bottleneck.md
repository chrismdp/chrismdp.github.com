---
layout: post
title: "The Harness Is The Bottleneck"
date: 2026-08-13 07:00:00 +0000
image: /assets/img/harness-bottleneck-stats.jpg
image_portrait: true
series: "Software Factory"
categories:
- ai
- engineering
- agents
---

DeepSeek V4-Flash 0731 is doing better than I expected.

It does not beat the best premium coding models: it is slower, stops early more often, and needs a decent harness built around it. But at about twenty cents a run(!) it is close enough to useful that the model cost is no longer the thing holding the work up. The harness is.

<!--more-->

By harness I mean everything around the model that turns a nearly finished attempt into work I will merge: the ticket that says what done looks like, the tests that prove it, the loop that lets a stopped run carry on, the isolation that keeps one attempt from standing on top of another, and the review at the end. The model writes the code, but the harness decides whether that code ever lands.

Over the past few months I have learned a lot about running [Ralph loops](/running-ralph-loops-is-easy/), and got more proactive at breaking work into tickets a worker can pick up and finish without me. I am currently using GitHub issues for this and running loops with Opus as the orchestrator, fanning out to models of varying strength depending on task complexity.[^delegate]

Throughput is the obvious gain, but any ticket written to be delegated also doubles as an A/B test. The same piece of work can go to several models at once, run in parallel, and be judged on what comes back.

In May I moved my whole background worker fleet onto DeepSeek V4 Pro and wrote that [open models are ready](/open-models-are-ready/). The open question from that post was how much further the cheaper Flash variant could take the same work, and how far it would pull the daily bill down. The earlier preview versions of Flash were not quite good enough, but the new one is.

So Flash has been running in my software factory as the challenger, taking the same bounded tickets as the premium model that serves as my control, and I review what each one produces.

I completed 52 runs from 1 to 13 August, costing $13.09 in total and a median of $0.19 each. Grading only works when a ticket has an objective definition of done, so this covers the work a test can settle and leaves out the UX tickets, where my own taste would be doing most of the deciding. I have graded 48 of the 52 by running the tests myself and getting Opus to read the diff against the ticket, and four are still pending. Of those 48, 36 produced work I would merge: 20 shipped clean and 16 shipped with fixes, all for less than the price of three coffees.

## My Harness Failed Twice As Often

Four of the graded runs were rejected because the work was not good enough, but double that failed for reasons that have nothing to do with the model at all!

Two of those ran out of context while the model was still editing and were cut off mid-change. That was my own doing: I had capped the context at 256k in my harness config, when Flash will happily take a million tokens. Three more were invalid because my coordinator showed the worker an already-landed solution from the control, which contaminated the run before it started. The rest were discarded or inconclusive for similar reasons of my own making.

## The Control Still Wins

Every ticket also went to a premium model as a control, whichever one my routing rules picked for that difficulty. On twenty of them I graded both arms, and the control produced something I would merge on all twenty, against fifteen for Flash.

That gap is the entire argument for the harness. Across the eighteen of those pairs where I have the control's cost recorded, Flash cost $3.40 and the controls cost $500.07. The median control run was $7.47 against fifteen cents, and one control run alone came to $215.[^control]

So the trade is five tickets out of twenty against roughly a hundred and fifty times the price. Three of those five were rejected on quality and the other two failed for reasons of my own making, which is the same pattern as the wider set. Close the harness gap and the trade gets better.

## Loops Beat One Shots

DeepSeek often gets a long way into a ticket, then stops before the work is complete. A one-shot comparison marks that as failure, but a persistent process can treat it as partial progress and carry on.

Ralph loops are probably the answer here. The loop keeps a ticket in the repository, gives one agent turn to the work, records the state, then passes context to the next turn. If we do not get to the end of the ticket, the next job picks the same ticket up again.

If a premium model finishes most tickets in one pass, that loop is superfluous. But with a cheap model that gets most of the way there for cents, we might as well go back to the techniques that worked well last year.

## Cheaper Even With Rework

Cost per token is a poor guide on its own, because a model that grinds through twice as many turns costs twice as much at the same rate. The number worth tracking is what a completed task costs, counting everything I paid for the runs that finished nothing.

All 52 runs cost $13.09 and 20 of them shipped clean, so a clean change works out at about 65 cents. That price carries every failure alongside it: the contaminated runs, the ones my context cap cut off, and the four rejects, and some of those failure modes are already fixed. Counting the 16 that shipped after fixes brings it down to about 36 cents, although that number leaves out Opus's review and fixing time, which is now the most expensive bit!

## What Changes Now

I have not yet switched over fully: Flash is too slow for some tickets, stops early too often, and needs clear tickets, tests, continuation rules, and review.

But in May I was still asking whether a cheap open model could hold the thread across a multi-step task at all, and it can. I plan to fix the harness failures soon and see if I can run fully on Flash.

If you run engineering teams, you are probably paying per token (I am still on a Max plan, long may those continue), and this could be a much cheaper option. Measure which model, harness and review process gives you accepted work at the best price, then put the effort into the harness rather than the model. Pi is a good place to start: it is a minimal coding harness that works with any model, and I wrote about how I use it in [Coding With AI](/coding-with-ai/).[^pi]

Raw intelligence is arriving at pennies on the dollar, and the price is only half of it. These runs currently take a median of 24 minutes at about 28 tokens a second. When that same work lands in under a minute, a cheap model that needs three attempts becomes the obvious way to work, because the harness can absorb the failures faster than a premium model can avoid them. The teams that spend this year building the harness will be ready to use it when it arrives.

[^control]: The controls were a mix of Opus 5, Fable 5, Sonnet 5 and GPT-5.6-sol, depending on how my routing rules scored each ticket, so this compares Flash against premium models in general rather than against any single one. Two of the twenty paired control runs had no cost recorded, so they count towards the merge tallies but not the cost figures.

[^delegate]: The routing rules live in my [delegate skill](https://airskills.ai/chrismdp/delegate){:target="_blank"}, which covers how a ticket gets matched to a model by cost and difficulty, and how a challenger is benched against a control on the same work. Install it with `airskills add chrismdp/delegate`.

[^pi]: [Pi](https://pi.dev/){:target="_blank"} is by Mario Zechner. It keeps the moving parts visible instead of hiding them behind a polished CLI, which is what makes the harness something you can measure and improve rather than a black box you either trust or do not.
