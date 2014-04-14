---
layout: post
title: How to layer context into your features using Real Narrative
date: 2014-04-14 17:22:12 +0100
categories:
  - bdd
  - stories
  - cucumber
  - craftsmanship

---

Take a look at this Cucumber feature and see what you think:

{% highlight cucumber %}
Feature: Power allocation on ship

  Blaster fire rippled across the rear of Charles's fighter. One of his engines immediately caught fire as the bullets tore through the outer casing, and the core reactor started to overheat.

  "Damn," thought Charles. He flung his ship hard left with one hand on the flight stick, using the other to knock out power to the damaged engine and route it to front shields. The large pirate cruiser loomed into view over his left shoulder. Slamming full power to engines and shields, he drove his ship straight towards the danger. Enemy bolts flashed off his shields like a mini light storm, but they held firm.

  Soon he was within range. With power to short range missiles and rear shields, he fired all three remaining missiles at the last possible moment, right at the belly of the enemy ship. Charles overshot the cruiser, pulling his ship around in a wide arc, keeping an eye out for their next move.

  Scenario: ...
    Given ...
    When ...

{% endhighlight %}

## Preambles don't have to be boring

This preamble uses real fictional narrative to make its point.

The whole point of the preamble is to provide this context for your feature. This allows the business and the customer to get the development of the feature right. Why shouldn't we include some actual fiction to give us a flavour of the feature that's required? 

This might seem easier with a space shooter game, but narrative on any project, even one that is more business focused, will help to get across a sense of *how the feature should feel.*

If we employ our reader's imaginations, it'll help them connect to the intangible reasons for the feature that we can't quite fit in a concise agile story description.

## Proper context drives implementation

The narrative above gives me plenty of context to write stories such as these:

{% highlight cucumber %}
Scenario: Allocating full power to a single component
  When Charles allocates power to engines
  Then engines should be given full power
  And other systems should be dropped to minimal power

Scenario: Knocking out power to a component
  When Charlies knocks out power to a component
  Then the component should no longer receive any power
  And the component cannot be used
  And the reactor stops overheating

{% endhighlight %}

It also raises plenty of questions. What happens if I push full power to two seperate systems? How should that feel to the player? Should that cause overheating? Should it even be possible? The narrative has driven a conversation with more depth and richness that I might not have had otherwise.

## Behaviour-driven development is for everyone

Who says that BDD is just for business web apps? It can work for games, too, any any other kind of software project. We've shown that in any domain where technical and non-technical people have to communicate about a software project, the core tenets of BDD are useful.

Whether it's software for a space shooter or a sugar factory, real people are always involved. There's always a translation process from great concepts to carefully crafted code. We should make that process as painless as possible.

## Let's choose to be interesting

The things we often write down in our stories are often the least interesting part of the conversation. Sometimes, in a drive to be pithy, we miss the point. How about we take a chance and include some actual narrative in our feature preambles and our story writing?

How are you leveraging the power of preambles to add context to your features?

