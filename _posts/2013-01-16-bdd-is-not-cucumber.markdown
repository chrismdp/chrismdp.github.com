---
layout: post
title: "That's not BDD, that's just Cucumber"
date: 2013-01-16 20:57:57 +0000
categories:
  - bdd
  - cucumber
  - tdd
  - craftsmanship

---

Continuing in the vein of "concept and values vs concrete tools" ([see my previous post about dependency injection](http://chrismdp.com/2013/01/dependency-injection-not-ioc)), I'd like to highlight a common fallacy about Behaviour-driven Development (BDD) and Cucumber, and BDD and story-writing; namely, that they're all the same thing.

BDD is a set of concepts and values, and Cucumber is one of many tools which we can use to work with those values. Using a tool such as Cucumber, or following a practice such as feature-writing does not mean that you've internalised the values of BDD yet or understand what it really means.

Before I get into that, let me clearly explain the distinctions in my mind between the different terms.

## Concepts, practices and tools

A concept or value is the higher level idea or principle we are attempting to espouse or instil. For example:

"Code only behaviour that has value the customer can see."

"Write software that matters; avoid software that doesn't."

A practice is a way of expressing that concept: for example, they may take the form of guidelines about how to write features in a certain way, or the exhortation to use acceptance tests alongside other automated tests.

The tools are the different software programs we use to execute these practices. They are many and varied: popular BDD tools include [Cucumber](http://chrismdp.com/tag/cucumber), [RSpec](http://relishapp.com/rspec), [SpecFlow](http://www.specflow.org) and others.

These distinctions are essential to prevent useless arguments about the relevant importance of practices, and even more useless arguments about tools.

## The concept should outlive the practice and tools

Test-driven development (TDD) is a good example of a series of concepts that has outgrown the tool and the practices that were originally associated with it. Most people don't think of [JUnit](http://en.wikipedia.org/wiki/JUnit) when they think of TDD, but the first TDD implementations used it extensively. The concept (test-driven coding) has transcended the tool (JUnit + Java).

TDD is also universally introduced using a form of practice called the "TDD cycle." We are encouraged to write tests, then write code, then refactor. However, as the coder becomes more familar with this cycle and follows it instinctively, TDD becomes much more about design than about "Red, Green, Refactor." The coder outgrows the practice (although they may never abandon it entirely) and becomes intimately associated with the concept. This concept in TDD's case can be quite difficult to describe, but might be partially summarised as *clean, reliable code.*

Scrum is a series of practices and tools used to illustrate agile concepts. Unfortunately, unlike with TDD, many who practice Scrum have never got past these practices to the principles behind them. Some people view Scrum as the Standup, or the Sprint, or perhaps the Backlog. The important concepts of team synchronisation, regular cadence, and progressive iteration can be lost in the noise.

If the concepts cannot outgrow the tools and practices we use to express them, then the concepts are weak, or the tools and practices are weak (or weakly understood.) Further, if we cannot envisage discarding a practice or tool, perhaps we haven't fully grasped the concepts behind it yet.

## We still need the practices

That's not to say we can internalise concepts without good practices. We can't just bleat "write clean, reliable code!" at someone and expect them to know what clean, reliable code truly is, and how to continue to write it when it's difficult to do so. Without the understanding that comes from diligently applying "Red, Green, Refactor" over a long period, we will never gain full insight into the values behind TDD. I've been applying TDD practices for several years now, and I am still learning about the relationships between objects and how they can be improved.

In the same way, good tools more suited to the practices we are trying to use will help us internalise concepts and values more quickly. A good example is the way that RSpec changed the language we use when writing unit tests, to help us to focus on behaviour rather than just correctness.

## BDD is a series of values and concepts, not practices or tools

Given the above, let's consider the fundamental difference between BDD (the set of concepts) and Cucumber (the tool) or feature-writing (the practice).

BDD is the formalisation of the best of the underlying values and concepts discovered and propagated by TDD. It further formalises and extends the basic TDD practices and fuses them with other practices to help team communication. This spawned a number of new tools to aid in this approach. Particularly, new tools were needed to help non-technical people read and understand acceptance tests, although the old tools could still be used and many still continue to do so.

Tools and practices are the most visible side effect of a series of concepts, and bandwagon jumping is always a danger. Due to the popularity of the tools, BDD can be unfortunately conflated with the principal tools used to drive it. We should work hard to explain that this is not the case.

For example, I've heard some people talk about "writing the BDD, then writing the code" - reducing "BDD" to the tool (Cucumber) and the practice (feature-writing) rather than the fundamental concepts which give rise to the practice. To do so is to make the mistake that many do when learning Scrum, to miss the values by blindly using the tools and following the practices by rote.

A similar problem is the idea that BDD is simply the "Given When Then" approach to writing stories. That approach is a practice we use to clearly express the concept of communicating requirements, and valuing that communication process highly. The approach is not the value in itself.

I think part of the reason we have a tendency to do this is because internalisation of concepts is desirable, but hard to do, and we're seeking a quick road to success. We think "if we're using Cucumber, we're doing BDD," or "if we're writing stories, we're being agile." Sadly, this isn't true, and although I can understand the motivation there are no shortcuts to internalising the concepts. *We need to carry out the practice, using the best available tools, whilst considering the values carefully* - that is the long road to mastery.

## In summary

When [training BDD](http://bddkickstart.com) we communicate the values and concepts to our trainees, demonstrate the practices and tools, and help them to try them out. We teach the usage of the tools, and the correct way to complete the practices, referring back to the concepts as appropriate. This way, when trainees are on their own they're able to head in the right direction, and will internalise the values in such a way as to be able to shed the initial tools (and even some of the practices) as they improve.

When learning something new, try to seperate the values and concepts you are trying to internalise from the practices and tools that you are using to do this. Carry out the practices whilst considering the concepts, and always inquire of yourself "why am I doing this now?" and "what am I learning?" For myself, I'm currently attempting to apply the practice of immutability to my code, in an attempt to internalise more functional programming concepts. It's early days, but it's leading to interesting results.

## We're teaching this stuff

In case you hadn't noticed, a few of us are starting to [teach BDD in person](http://bddkickstart.com/) at the moment. Our next courses are in [Brussels](http://bddkickstart.com/dates#brussels) and [Edinburgh](http://bddkickstart.com/dates#edinburgh); instead of flailing about with the tools or hesitantly attempting the odd practice, come and learn what BDD is really all about.
