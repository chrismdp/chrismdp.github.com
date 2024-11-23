---
layout: post
title: Make Cucumber features more readable with this one weird trick
date: 2014-02-12 10:15:06.000000000 +00:00
categories:
- bdd
- agile
- cucumber
- process
redirect_from:
- "/2014/02/make-cucumber-features-more-readable-with-this-one-weird-trick"
- "/2014/02/make-cucumber-features-more-readable-with-this-one-weird-trick/"
---
*"Sorry I've written such a long letter; I didn't have time to write a short one."*

-- [Blaise Pascal](http://en.wikipedia.org/wiki/Blaise_Pascal)

If you've got an issue with your customers not reading your feature files, then try this: it'll help ensure their eyes stop glazing over.

As I travel around coaching teams doing BDD, a common problem I see with Gherkin features is that they are nigh on unreadable except by the people that wrote them... and even then, the writers often have trouble explaining what they mean.

This often happens when non-technical stakeholders have little to no involvement in writing features, leaving technical people free to be as obscure as they like. It's easy to write an obscure feature: it takes a lot less effort to ramble and choose the first words that come to mind, rather than crafting carefully considered prose. The pain comes later: an obscure feature is imprecise, error-prone and unmaintainable, as the effort required to understand it will stop others from maintaining it.

## How I help people simplify their features

When asked to review the language of a preamble, *I read the feature out loud, and then ask the writer of the feature what it means.*

A deep breath often follows. "Ok, this is the one where..." The writer will explain the feature clearly and concisely using completely different words to what is actually written in the feature. They use great contextual information that's missing from the written preamble, and work to ensure I really understand what's going on.

Once I've got a good response that I can understand, I ask the writer to replace the preamble with exactly what they just said.

It's never *exactly* what they said (natural language is different to spoken language, after all) but it's always better than what they had before.

Sometimes, when asked what the feature means, the writer will give a short hesitant explanation, and then proceed to read out the preamble again. My response is normally: "yes, but what does it mean?" Occasionally I have to ask five or six times until I get a considered, clear response.

This also works for scenarios, scenario descriptions, tag names, etc.

## Why this works

Sometimes it's easy for us to get so wrapped up in the detail of the features that we're writing that we're unable to see the wood for the trees. Our features read much more like computer code than they do plain natural language.

Features are communication tools first and foremost, and leveraging different ways of communicating while writing them will help to ensure they're as carefully considered as possible.

(This works for natural prose, too. if you write a blog, documentation or even just emails to colleagues, taking a moment to read your text out loud will tell you in an instant whether it makes sense.)

## A challenge

Pick a feature on your project, and read it out loud. If it makes no sense, explain what the feature does to a colleague and ask them to write it down for you. If it reads awkwardly and could be improved, take ten minutes to do so. Your future readers will thank you for it.
