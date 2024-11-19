---
layout: post
title: Why video game coders don't use TDD, and why it matters
date: 2015-03-11 10:37:37.000000000 +00:00
categories:
- sol trader
- tdd
- indie games
- game development
- testing
- code
- functional programming
redirect_from:
- "/2015/03/why-games-coders-dont-use-tdd-and-why-it-matters"
---
![NES test station](/assets/img/nes-test-station.jpg)

Whilst working on [Sol Trader](http://soltrader.net), I've written many unit tests for my code. Many of these tests have been written before the code itself, using a practice called Test-driven Development (TDD).

Test-driven development is the practice of writing a failing test in order to specify the behaviour of a piece of code, then writing the code to satisfy the tests afterwards. We then refactor and improve our code from there.

In most programming environments, people are talking about TDD and trying to practice it. It's even become an essential bullet point on job adverts, as if not practicing TDD makes us fundamentally worse programmers (which isn't true, by the way.) TDD seems to be everywhere.

Everywhere, that is, except the games industry.

Why is this? Is it because TDD is flawed in some way, or simply not applicable here, or that practices have grown up to counter the need for TDD?

## The benefits of TDD

Let's begin to answer this by looking at the specific advantages TDD gives us:

* **It forces usage-first coding.** TDD represents another client for our code, independent from our production code. It asks specific questions of the codebase to ensure that it's correct. It forces us to think about our code from the point of view of 'what it does' first, rather than 'how it works'. This can often lead to surprising realisations about the code we actually need, and prevents us from writing spurious code we might think we need, but actually represents wasted effort.

* **It helps us minimise code size and complexity.** If we adhere strictly to the principle of only writing enough code to satisfy the test, then our tests should capture every possible path through our code. Additionally we only have enough code to satisfy the exact problem we've used tests to define - this is important because [code is a liability, not an asset](/2012/09/code-is-a-liability/). The same is true of code complexity. If we find ourselves writing reams of tests to satisfy a particular piece of code, that code is too complicated or very risky and a prime source of bugs.

* **It provides design feedback.** Well designed code is easy to test. Therefore, when initial tests become harder to write, that might be because our code isn't well designed, or well understood. Typically, pure functions are easier to test and reason about as they have no side effects: testing these functions is very easy and therefore our code tends to gravitate towards them.

* **It allows for verification over time.** I've listed this last, as I don't see it as the most important benefit of TDD. As I refactor my code, tests become simple enough to be self evident and the tests can be safely deleted. At the system level, ensuring that a complicated system continues to work after significant change is useful, but considerable effort is required to write tests that check an entire system safely. Poorly written tests give a sense of false confidence to those new to the practice, which can be highly dangerous - our [tests can start lying to us](/2011/10/your-tests-are-lying-to-you/). In practice, a few end-to-end tests to verify basic functionality of a module are worth the effort, but many more can slow development and provide false confidence.

## How games industry experts verify their code

Let's look at expert coders in the games industry and discover what they do to gain these advantages. Here are some observations:

* **They write the production usage code first.** Casey Muratori on [Handmade Hero](http://handmadehero.org) writes his code from the point of view of the usage of the code first, by writing exactly the calling code before defining structures and basic methods. This gains many of the advantages of TDD, using production code rather like tests to discover what the code should do. By implementing a client for the code first, we discover what the code should look like before we write it.

* **They fail fast using assertions.** Assertions are conditions in the code that are often only present in developmental builds, causing an artificial exception or crash when the condition is not true. They ensure that the running program is in a good set of known states: code running in the wrong state is a hugely common cause of bugs. As unit tests only check a certain set of known states from the outside, assertions are useful in catching unexpected behaviour that wasn't initially thought of. As the code tends toward purer functions with less possible states, the usefulness of assertions within that section of code diminishes. They also do not provide design feedback on the code in the way that TDD does.

* **They rely on static compilation to catch type errors.** Static compilation is a form of testing. If we are thinking carefully about the distinct types we are using, avoiding [Primitive Obsession](http://c2.com/cgi/wiki?PrimitiveObsession), then this distinction between types will help ensure that we aren't passing the wrong things to the wrong functions, or confusing distinct concepts in our code.

* **They use automated testing where the code is risky.** John Carmack recently wrote about the value of testing in his [essay on functional code](http://gamasutra.com/view/news/169296/Indepth_Functional_programming_in_C.php): 

{% include callout.html color="#d9edf7" text="\"Whenever I come across a finicky looking bit of code now, I split it out into a separate pure function and write tests for it. Frighteningly, I often find something wrong in these cases, which means I'm probably not casting a wide enough net.\"-- John Carmack" %}

## What are games developers missing?

Games developers have a number of techniques that give them similar benefits to TDD. We see that by writing usage code first, developers get good feedback on their design as they go. Code verification over time is taken care of through judicious use of assertions and using automated tests with risky code.

The area that games developers miss out by not using TDD is in the reduction of code size and complexity. However, in high performance computing, the size of the compiled system and the branching complexity are constant concerns. There's a real performance penalty through having too much code, breaking branch prediction and accessing memory too often by jumping the execution path all over the place. The fastest and most efficient code boils down to data transformation as functionally as is possible within the obvious constraints of the gaming environment.

If all of this is taken into account, games developers have side-stepped the need for TDD.

However, there are bad reasons to dismiss TDD in games. There's a perception that games are too 'emergent' and complex to apply TDD to. This is false. Games are more deterministic than people think, especially in the inner workings of the code. Moving to a more functional programming style makes this explicit, although often enough so much risk is removed from the code that TDD's design feedback is less useful.

There are clearly areas in games development where TDD is the wrong approach - games are about 'feel' and the 'experience', and we can't test-drive 'fun', or test the output of complex interactions of hundreds of entities. Sometimes however TDD is dismissed because we cannot imagine how we might begin to test our code: this says more about the quality of our code than the merits of TDD as a practice.

## Summary

Video games devs don't do TDD for two reasons:

* **The good reason:** the best practices in the industry deliver many of the same benefits as TDD.

* **The bad reason:** an insufficient knowledge of TDD and good code design can lead people to believe it's just not relevant to games. The smokescreen of "we cannot TDD fun" can mask a poor understanding of good coding architecture.

In practice, I attempt to TDD much of my low level code, especially my functional core code which is simply transforming data from one type to another. I use TDD where I'm weakest as a programmer: reasoning about pointer and bitfield arithmetic aren't my strong points and therefore I like to test-drive it!

I don't use TDD at all for UI testing and where the 'feel' of something is important, and for self-evident code.

TDD has helped to teach me about good code design, side effects, the perils of state, architecture, programming in a functional style and the evils of prevalent inheritance-based object-oriented approaches. Perhaps the real value is not in the continued practice, but in the lessons that it teaches?
