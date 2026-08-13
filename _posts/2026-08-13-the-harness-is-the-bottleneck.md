---
layout: post
title: "The Harness Is The Bottleneck"
date: 2026-08-13 07:00:00 +0000
image: /assets/img/harness-bottleneck-stats.jpg
image_portrait: true
categories:
- ai
- engineering
- agents
---

DeepSeek V4-Flash 0731 is doing better than I expected.

It does not beat the best premium coding models: it is slower, stops early more often, and needs a decent harness built around it. But at about twenty cents a run(!) it is close enough to useful that the model cost is no longer the thing holding the work up. The harness is.

<!--more-->

In May I moved my whole background worker fleet onto DeepSeek V4 Pro and wrote that [open models are ready](/open-models-are-ready/). The open question from that post was how much further the cheaper Flash variant could take the same work, and how far it would pull the daily bill down. The earlier preview versions of Flash were not quite good enough, but the new one definitely is.

I have been running Flash as a challenger model in my own software factory. I give the same bounded software ticket to more than one model in parallel, then review what each one produced, with the premium model as the control.

I completed 52 runs from 1 to 13 August, costing $13.09 in total and a median of $0.19 each. I have graded 48 of them by running the tests myself and getting Opus to read the diff against the ticket. Fully 36 produced work I would merge: 20 shipped clean and 16 shipped with fixes. All for less than the price of three coffees.

## Twice as many runs failed on my harness as on the model

Four of the graded runs were rejected because the work was not good enough, but double that failed for reasons that have nothing to do with the model at all!

Two of those hit a roughly 258k-token context ceiling while the model was still editing, so they were cut off mid-change and never given room to finish (this has since been raised to 1M). Three more were invalid because my coordinator showed the worker an already-landed solution from the control, which contaminated the run before it started. The rest were discarded or inconclusive for similar reasons of my own making.

## Harness changes will fix it

DeepSeek often gets a long way into a ticket, then stops before the work is complete. A one-shot comparison marks that as failure, but a persistent process can treat it as partial progress and carry on.

Ralph loops, which I wrote about in [Ralph In One Line, No Setup](/running-ralph-loops-is-easy/), are probably the answer here. The loop keeps a ticket in the repository, gives one agent turn to the work, records the state, then passes context to the next turn. If we do not get to the end of the ticket, the next job just picks the same ticket up again.

If a premium model finishes most tickets in one pass, that loop is superfluous. But with a cheap model that gets most of the way there for cents, we might as well go back to the techniques that worked well last year.

## It's still cheaper even with rework

Cost per token is a poor guide on its own, because a model that grinds through twice as many turns costs twice as much at the same rate. The number worth tracking is what a completed task costs, counting everything I paid for the runs that finished nothing.

All 52 runs cost $13.09 and 20 of them shipped clean, so a clean change works out at about 65 cents. That price carries every failure alongside it: the contaminated runs, the ones the context ceiling cut off, and the four rejects, and some of those failure modes are already fixed. Counting the 16 that shipped after fixes brings it down to about 36 cents, although that number quietly leaves out Opus's review and fixing time, which is now the most expensive bit!

## What changes now

I have not yet switched over fully. Flash is too slow for some tickets, stops early too often, and needs clear tickets, tests, continuation rules, and review.

But in May I was still asking whether a cheap open model could hold the thread across a multi-step task at all, and it can. I plan to fix the harness failures soon and see if I can run fully on Flash.

If you run engineering teams, you are probably paying per token (I am still on a Max plan, long may those continue), and this could be a much cheaper option. Measure which model, harness and review process gives you accepted work at the best price, then put the effort into the harness rather than the model. Pi is a good place to start: it is a minimal coding harness that works with any model, and I wrote about how I use it in [Coding With AI](/coding-with-ai/).[^pi]

Raw intelligence is coming to everyone, at pennies on the dollar. Is your organisation poised to take advantage?

[^pi]: [Pi](https://pi.dev/){:target="_blank"} is by Mario Zechner. It keeps the moving parts visible instead of hiding them behind a polished CLI, which is what makes the harness something you can measure and improve rather than a black box you either trust or do not.
