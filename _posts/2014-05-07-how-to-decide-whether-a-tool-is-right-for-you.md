---
layout: post
title: How to decide whether a tool is right for you
date: 2014-05-07 13:10:47.000000000 +01:00
categories:
- tools
- anti-pattern
- process
- craftsmanship
- bdd
redirect_from:
- "/2014/05/how-to-decide-whether-a-tool-is-right-for-you"
---
[![tools](http://chrismdp.com/files/tools.jpg)](https://flic.kr/p/5YWuWk)

We are only at the beginning of our journey in building software. Our discipline is barely a few decades old. We have only a very little experience in how to correctly write code and a limited range of tools and skills to do it with. We should be actively looking for new tools, not wasting our time either promoting our toolset exclusively or disparaging the toolsets of others.

## Tools are tools

Test-driven development has been one of those tools that has proved useful for many people over a number of years. Do I use it? Yes, much of the time.

Using a refactoring IDE has also proved useful to many people over a number of years, especially in certain languages. Do I use one? No. Does that mean it's not a useful tool to others? No, of course not.

The ability to decouple code to promote changeability is also a great tool to have in your toolbox. Do I try and do this? Yes, wherever I can, and I'm always trying to get better at it.

There are many more. The insight as to *when* to refactor, not just how, is an incredibly valuable skill to have. The understanding that all code is built for someone and we should ensure we talk to them about what they want is powerful. Being able to check into source control without touching the network is a real speed boost, and gives me a detailed history of progress.

## The recent TDD storm

So why do we get so hung up on one particular tool? When something works for us, we're compelled to proclaim it's the One True Way and that it'll work for every problem and solve every headache. This is a grevious error, but in avoiding it, we can make the opposite one: when we find a tool's limitations, we discard it completely and move on, proclaiming it useless for all.

[DHH](http://david.heinemeierhansson.com/2014/test-induced-design-damage.html) has a point. Don't listen to the people who say there's only one way to do a job, and that we should use any tool for everything.

[Gary Bernhardt](https://www.destroyallsoftware.com/blog/2014/tdd-straw-men-and-rhetoric) has a point. Test speeds do matter - the faster the better. Fast tests are a powerful tool.

[Uncle Bob](http://blog.8thlight.com/uncle-bob/2014/05/01/Design-Damage.html) has a point. It's not just about fast tests: separating concerns in order to promote changeability in code is a useful skill to learn.

[Tom Stuart](http://codon.com/how-testability-can-help) has a point. TDD is a useful tool because it gives you another client for your code, encouraging us to think harder about what it's doing.

[Seb Rose](http://claysnow.co.uk/to-tdd-or-not-to-tdd/) has a point. We need to learn how to use TDD (or indeed any tool) well before giving up on it.

[Cory House](http://www.bitnative.com/2014/05/01/the-tdd-divide/) has a point. People display their own biases in their opinions and we should learn from them all.

## How to decide whether a software tool is right for you

It doesn't matter whether it's TDD, Vim, Git, Refactoring, OO, Functional programming, JavaScript, RubyMotion, etc. Follow the following advice repeatedly, substituting your own values:

> If you haven't tried tool X, give it a go. Many have found it helpful in areas Y and Z. Some have also found it applicable in areas A and B, but your mileage may vary. Some don't get on with it, and a few hate it and say no-one should use it. Learn it properly before making any final decision about its usefulness to yourself and others. This will take &lt;an amount of days/months/years&gt; to do. Continue using it as long as it's helpful to you.

There are as yet very few absolutes with software tools - we're still way too primitive in our discipline for many of those.  Let's learn how to use as many tools and skills as possible, and use the right ones for the job. Let's not decry the tools, skills and techniques of others if they are useful to them: let's instead spend our energy actively seeking new skills and tools to further our discipline.
