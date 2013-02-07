---
layout: post
title: The perils of curiosity
date: 2013-02-07 07:27:02 +0000
categories:
  - bdd
  - testing
  - craftsmanship
  - products
  - sol trader

---

Identifying behaviour in any system can be a tricky endeavour. As a developer, unless we take clear deliberate steps to discover the desired behaviour of the system, it's very easy to just focus on what our system *does*, forget what our system is *supposed to be for.*

When we build things to satisfy intellectual curiosity, we focus on what the thing *does*. It might have fancy features, or bells and whistles, but it won't necessarily satisfy a need.

## Features just for us

How many times have you used a feature of a product which only seems to exist because the developers thought it might be fun to build? No, I don't use them either. Often features like that exist because of a vague hope that someone might want to use them in the future, not to satisfy a perceived real need, right now.

When someone is using our shiny new product, lovingly fashioned, the proud output of our curiosity and the joy of making something new; and our carefully built features make no difference to their use of the product, *then those features are for us, not them.*

We shouldn't kid ourselves we're making something for others: we're really using our resources to make something for ourselves. This isn't a bad thing in itself, but it's not "building a product for customers", but it's good to be clear about how we are spending our time and money.

## Sol Trader: lesson learned

I learnt this lesson the hard way on [Sol Trader](http://soltrader.net) recently. I've been working on the game on and off for the best part of fourteen months, and on this current codebase for a little over a year. Through this process, I've discovered a lot about what it takes to build a great product: one which customers actually want to purchase, and doesn't just satisfy the intellectual curiosity of the maker.

I'm building Sol Trader as a game that I would like to play. That means focusing on features that make the game more fun. However, for a few weeks, I lost the plot. Based on feedback from customers, I decided that the game needed a stronger focus on AI, rather than combat. I immediately started focusing on building an attribute system for my characters. AI characters in the game needed a greater depth of personality, and therefore I should give them that personality by varying the way characters interact with the game.

## Invisible features

What I'd forgotten is this: at the moment, the only way that players interact with characters is indirectly through the stock market system, with prices going up or down as sales and purchases are made. There isn't a way to easily see the difference more complex personalities will make: at best, prices might fluctuate slightly differently, but that won't easily be perceivable.

I'd forgotten to ask, "Why? What's the reason I need this feature?" A nice system to store actor personality is all very well, and satisfies my curiosity about how to build such a system, but it doesn't directly lead to a change in behaviour my customers can see. Invisible features aren't really features at all.

I've now changed tack. When people say they want more AI interaction, I think they actually want more direct interaction with the AI rather than a more complex yet invisible simulation. I've decided to work on a long cherished cornerstone of the game experience: I want players to be able to get off their ships, walk around space stations and planets and interact directly with AI characters.

This is a lot of work, but the benefits to customers are obvious to me: it's a whole new way of interacting with the game. (If you have [alpha access](http://soltrader.net/buy) then hit TAB in a recent build and you'll see the very early stages of this feature.)

I'll probably get to using my fancy attribute system at some point. Probably. There's a risk that I won't use it and have to implement something else. That's the cost of forgetting the outside-in approach.

## Acceptance tests: antidote to vague product thinking

After thinking further about where I went wrong, I realise the root cause of this was a tool deficiency: *I hadn't written an acceptance test.*

There weren't any automated tests in my game which checked the new AI was working. I had tests around attribute creation, but those were unit tests. I didn't have anything which allowed someone to see the change in behaviour from the outside.

For the attribute system, this acceptance test would have been hard to write from a customer's point of view, which would have helped me realise it was a poor place to start improving the AI. The maxim "well designed code is easy to test (via unit tests)" also applies to at another level: "well throught through product features are easy to test (via acceptance tests)."

As a developer, I've discovered just how hard it is to get my head out of the code and into the product mindset. It's an essential skill to learn, even if we're only building products for other people. The BDD/TDD cycle of acceptance testing and unit testing is very useful in keeping us on the straight and narrow whilst we're learning this skill.

## Product builders should beware intellectual curiosity

At this point, if I was going to fully satisfy my intellectual curiosity, I'd probably throw away the codebase I have, and rebuild it in a much more immutable, functional style, rather than the classic OO, mutable, entity driven design I have right now. I'd also ensure that the build times were significantly better, after talking to [Alex](http://twitter.com/mmalex) about his 100ms build-compile-test cycle he enjoys for his C/C++ projects. That would be great fun for me, but it won't result in fun for customers any time soon, which is the real goal.

Sometimes we need to make sacrifices to get our product out of the door. I don't think this is technical debt: it's the inevitable slide into legacy a result of learning. Unless the code we wrote a few months back looks ugly and poorly implemented to us, we probably haven't learnt anything in the intervening period. Therefore we will most certainly encounter this temptation when building our products, and we need to strive to resist it.

Does the feature you're working on right now lead to a direct change in the behaviour of your system that your customers can appreciate? If not, why not?
