---
layout: post
title: "Software Factories Can Handle UX"
date: 2026-08-19 07:00:00 +0000
image: /assets/img/taste-in-the-factory-flow.jpg
image_portrait: true
image_caption: "Spend the taste once, at the top."
series: "Software Factory"
categories:
- ai
- product
- design
---

The hardest thing about running an arm's length software factory has been anything that touches UX. If your quality bar is high, a human still has to look at a screen and use it, and what comes back mostly sort of works while needing small corrections. So I would check a dozen UX changes at once, send them all back for tweaks, and get a dozen slightly wrong things back again.

This feels like a quality problem, but it is actually a batch size problem. Every round trip made the batch bigger rather than smaller - the batch size is effectively the entire group of tickets. I was thrashing between a dozen half-right screens, and the QA step never ended. When I wrote up [52 agent runs last week](/the-harness-is-the-bottleneck/) I had to leave the UX tickets out of the count as I was not sure how to handle them.

This is partly the way I make things. I want to try something, look at it, and work out what I actually want as I go. That is a reasonable way to design, but a terrible way to feed a dark factory, which needs to know what it is aiming at before it starts.

Luckily I think I have found a way around this problem.

<!--more-->

## Galleries Beat Descriptions

The fix came from Gojko Adzic.[^gojko] Build the visual specification before anyone implements anything, in three layers. The first is a **design language gallery**: every component in every state that matters (hover, focus, interaction, light/dark mode, etc). The second is a **design pattern gallery**, holding the rules for combining those components, such as where the primary action sits relative to the secondary one, how much space goes between them, and where the label belongs. The third is a **demo page gallery**, which is static HTML of the main user flows with realistic data and the states the application actually reaches.

The first two layers turn a decent chunk of visual quality into something a machine can check. Gojko runs an SCSS test pipeline over the galleries that checks contrast against WCAG, that elements are visible, that the primary action is more prominent than the secondary ones and so on. It runs in about a minute, starting at the component gallery before the demo pages.

Those checks verify properties you can state and inspect; they cannot tell you that a real person understood the screen or finished the task. Gojko measures that separately, with production completion rates and time to complete key tasks. The gallery moves human judgement earlier rather than removing it: you get to complain about a flow before agent-written code makes the wrong choice expensive to unwind.

## Twelve Screens First

I have not yet built this whole system, but I have tried it on two projects, and it is working very well.

The first was a cohort survey platform I am having built for the training programmes I run. The skeleton app was already up: real routes, real copy, real states, and no visual identity at all. I spent an hour in a prototype redrawing it in the vocabulary of my own website, with a white header and a light blue rule, a turquoise gradient hero, DM Sans headings, and exactly one orange action per page. Claude Design did a fantastic version of this that I have barely had to modify. This is the third layer of Gojko's design setup - I have not got to building the first two layers yet.

{% include inline-image.html src="/assets/img/academy-design-pass.jpg" alt="A design canvas showing twelve app screens laid out in a grid, each redrawn with a white header, turquoise gradient hero and a single orange button, annotated with the route each one serves." align="center" width="100%" caption="Twelve screens in the site's own visual vocabulary. Ten of these can be reached today, plus two the app does not have yet." %}

I did spend a bunch of time eyeballing the screens and the copy, but the difference is that I did it before anything was built, on a surface that costs nothing to change, instead of doing it a dozen screens at a time against a queue of half-finished pull requests. Two of those screens do not exist yet, and laying them out side by side made gaps very obvious: there was no grouped view for somebody enrolled on more than one programme, and the live session playground had no screen at all.

## The Four Step Loop

Here is the process I am going through for UX / design tickets now:

You **iterate on a prototype** until you get the feel of the product you want. There is nothing to stop this happening in Figma over MCP, but honestly Claude Design is doing the job for me. A designer's input would be invaluable here if your project has one. It is meant to be fast paced - I am doing this in Claude Code with the new `/design` skill.

You **freeze what you chose into a gallery**: the components in their states, the rules for combining them, and static pages for the flows that matter. This lives in version control next to the code.

You **write tickets that point at it**. The ticket carries the behaviour as it always did, and adds a reference: build this screen, match this layout, hold this state, and here is the page that shows you what it looks like.

You **delegate, then polish in one deliberate pass** against the prototype rather than against your memory of what you wanted.[^delegate] This is the part that kills the batch problem: instead of a rolling QA queue where a dozen screens are perpetually almost right, there is one implementation and one polish session, and corrections go back into the gallery as well as the code. Otherwise you are straight back to a factory that learns your indecision.

The failure mode is doing step one over and over inside the loop, which is exactly what I had been doing for months without noticing that it had a name.

## Not A Design Phase But A System

The obvious objection is that this is waterfall with a new name, a design phase bolted onto the front of an agile process. It would be, if the gallery were a sign-off gate, but it is a living artefact that the same loop corrects, sitting in the repository alongside the tests, wrong until it is not, and cheap to change because nothing has been built on it yet. Keeping it up to date with the latest code is trivial (just ask Claude to do it) - much easier than managing Figma.

Designers will note that we have had such systems for twenty years. That is largely true, but now we can really take advantage of this practice. A design system would often be a document that humans were meant to honour and frequently did not, and it was eventually left decaying in a folder nobody opened. The consumer is now a machine that will honour it literally, every time, without getting bored, and it is cheap to maintain which makes it useful (simply ask the AI to "make sure the design artboard matches the live code").

I have run this process across two separate repositories now: one where I picked the tickets up myself, and one where I handed them to another developer as GitHub issues. Early days, but feels like it has legs.

It is the same lesson as the [harness post from last week](/the-harness-is-the-bottleneck/), where cheap models became useful the moment the harness could tell them what done looked like, and again the same as [my argument that work becomes delegable once the slice has a clear boundary](/slice-your-job-into-skills/). Design is one of the things you feed the factory, not a phase that happens before it starts. Make sure the AI can tell what good looks like.

If you run product or engineering, give your designers a surface where they can settle layouts, interactions and states cheaply, and make the output of that work a synchronised input to delivery (rather than a picture that delivery is loosely inspired by).

And get designers into the code. Perhaps it is time to abandon Figma for Claude Design and HTML prototypes.

[^gojko]: [Gojko Adzic](https://www.linkedin.com/in/gojko/){:target="_blank"} described this three layer pattern to me directly in August 2026, and I have not seen a published write up of it, so treat it as a practitioner's account of one application rather than evidence that it improves outcomes in general.

[^delegate]: Which worker picks the ticket up, and on which model, is decided by the routing rules in my [delegate skill](https://airskills.ai/chrismdp/delegate){:target="_blank"}, which matches a ticket to a model by cost and difficulty. Install it with `airskills add chrismdp/delegate`.
