---
layout: post
title: 'BDD: How to deal stories into features'
date: 2013-08-29 16:18:44.000000000 +01:00
categories:
- stories
- cucumber
- bdd
redirect_from:
- "/2013/08/dealing-stories-into-features"
---
<img style='float: right; padding: 0 0 20px 20px; width: 250px' src='http://ak1.ostkcdn.com/img/mxc/100706_card_shuffle.jpg' alt='Dealing cards'/>

It's comparatively easy to learn a methodology such as BDD when it's static and unmoving - to learn *about* it rather than to *learn it*. At that point it's all information, which we're used to consuming and processing. It's much harder to learn how to do it moving: how to handle the process over time as the project grows and changes. When it moves, it's not about information any longer, but about cadence, rhythm, and technique.

Here's an example: recently I was on site doing some [BDD Kickstart in-house training](http://kickstartacademy.io/in-house-courses) with a client, and they asked how do you best modify a feature file over time as new stories are added to it?

The answer is worth writing up properly, as there are two common ways of doing it which I think are unhelpful:

* Simply dump new story text into the feature preamble and keep on adding scenarios without much thought.

* Create a new feature file for every new story.

I think the reason people fall into these patterns is down to a lack of clarity about what features and stories actually are, and how they differ. Let's clear that up first, and then we can discuss how to keep our feature files neat and tidy.

## What's a feature?

A feature in the BDD context describe an functional area of your product. In BDD, a feature is written up as a text file which forms part of your project's source code and seeks to document the feature you're describing. It contains a few thoughtful paragraphs of descriptive text about the area of the product your feature covers. After this, Acceptance Criteria for the feature are listed in bullet form. Then there are a series of scenarios which describe concrete examples the functionality in a (hopefully) unambiguous way.

Features can cover a larger area of your project, and can cut across several sections of your application if that makes sense. I've previously [written a lot](/tags#cucumber) about features and how to write them well.

## What's a story?

Stories are much smaller pieces of work that we complete atomically as part of a backlog of some kind. One definition of a story in a product development context is "a narrative describing the smallest possible unit of work that can deliver value to someone."

Often stories are written in this form:

    "As a <role> I want <feature> so that <benefit>"

Or:

    "In order to <realise benefit> <role> should be able to <do something>"

(It's important not to be constrained by this style, though. I've seen plenty of stories written something like this: "As a well-wrtten application module, I want to ensure that all my inputs are checked for string validity, So that I won't crash when given bad input". It would be better to simply write "String input values for Parser module should always be valid" rather than force the reader to process tortuous English. Stories are read many more times than they are written: it's worth taking the time to ensure they're clear!)

The smaller your stories are, the better: you'll be able to work in smaller batches, which has a [tremendous number of benefits](http://www.startuplessonslearned.com/2009/02/work-in-small-batches.html).

## Dealing cards

So what's the relationship between these two things? And how do they relate over time on a project?

A very useful metaphor is a pack of cards. Stories are like individual cards in a deck. Features are more like a hand of cards in a card game. As a game progresses, we deal more and more cards into our hand. We re-organise them, shuffle them about, and perhaps discard some cards so that the hand is useful.

In the same way, when we have a new story 'dealt' into our feature, we reorganise it like a hand of cards. We tweak the preamble text and expand it. We switch around the acceptance criteria, and add the ones from our story underneath. We add a couple more concrete examples, and remove one that's out of date.

## Starting out

When you only have one card in your hand, there's no need to organise it. Similarly, when starting a story with a brand new feature, I would normally paste the contents of the story into the preamble, along with the acceptance criteria and any concrete examples as scenario headings. As soon as I receive another story that logically belongs in the feature, I would take a step back and consider them both. How can I add to the preamble in a way that makes sense? How best do these acceptance criteria work together? Should I add a brand new example or slightly modify an existing one? At the end of the process, the feature file should concisely express both the stories well.

Then you add a third story, then a fourth, then a fifth. Depending on the stories, at some point your feature file will become unmaneagable, at which point it makes sense to find a logical place to split the feature into two. Normally this happens for me when my scenarios no longer fit on a screen or two, although clearly this varies depending on the feature.

How do you organise your features as they grow over time?
