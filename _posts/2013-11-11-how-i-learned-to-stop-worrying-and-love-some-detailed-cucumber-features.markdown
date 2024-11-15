---
layout: post
title: How I learned to stop worrying and love (some) detailed Cucumber features
date: 2013-11-11 17:55:51.000000000 +00:00
categories:
- ruby
- cucumber
- testing
- training
redirect_from:
- "/2013/11/how-i-learned-to-stop-worrying-and-love-some-detailed-cucumber-features"
---
As the revival of interest in Cucumber continues, I'm finding that a lot more people are using Cucumber for two very different types of testing. When coaching or training, I sometimes come across QAs writing Cucumber tests like this:

{% highlight cucumber %}

    Feature: Menu regression script
      Scenario Outline: Check top menu does not scroll
        Given I click on <link>
        And I scroll down
        Then the menu should still be visible at the top of the screen

      Examples:
        | link     |
        | Home     |
        | About    |
        | Products |
        | Clients  |
        | Services |
        | Company  |
        | Contact  |
        etc.

{% endhighlight %}

I don't use Cucumber like this... but I've changed the way I approach features such as these when I come across them.

## How I use Cucumber

When I use Cucumber, I hold discussions with stakeholders, and I write down the results as Cucumber features, carefully avoiding too much incidental detail to help with maintainability later. These features form the initial acceptance tests for my system. I then use TDD to flesh out the functionality I need. The features end up as very useful documentation and regression testing artefacts (which can even form a [user manual](http://chrismdp.com/2013/06/rack-usermanual/) for the application.)

The example feature above is very different. It is an exhaustive regression test to check that the scroll option is working in all cases on every page. This example is pretty short: in reality I've seen extremely long Cucumber features written in this style. Note this isn't the same as very long boring and overly detailed features: they're running a simple scenario in many slightly different ways.

Because this is not how I use Cucumber, I used to discourage this long form style of feature writing out of hand. I've learnt to stop worrying... as long as it's clear what sort of features these are and how they should be treated.

## Developers: who are we to judge?

Firstly, developers: I don't think we should be saying "you can't write tests like this."

Just because people are not using the tool how we might expect them to, their use of it is not invalid. It's very tempting to say "you're doing it wrong", because these feature look so much like the "bad features" developers are taught to eradicate from their codebases. However, we have to understand that they're simply using the tool for a different set of advantages it provides: it allows them to quickly run through expected functionality on a multitude of different places.

There isn't one way to use Cucumber (or any tool) - there are only ways that give value, and ways that increase or decrease friction. We would be wise not to discount the way that others get value out of the tools we use, just because they use them in a way that we didn't expect.

## A different approach

When I see these sorts of features, rather than dismissing these features as 'too detailed' or 'unmaintainable', I ask questions about who is using these features. Who is writing them, who is reading them, and who is keeping them up to date?

Often it's the QA people on a team who are exclusively writing with these types of tests. These are then handed on to the developers who are getting very frustrated with them. No one is clear who should be maintaining them. The developers don't want to, and inevitably try to refactor them, which annoys the QAs as the detailed regressions they were aiming for are lost. The QAs don't want to maintain them as they usually don't have strong coding skills and therefore they find it hard to maintain the step code. The end result is a void of responsibility which gives rise to a mess of unmaintained code.

A good solution? Be clear about the responsibility. Move these features out of your regular BDD workflow. Create a structure a bit like this:

    features/
      docs/
        account_management.feature
        buying_products.feature
        step_definitions/
          ...
      regression/
        menu_interface_checks.feature
        step_definitions/
          ...

Have the QAs maintain all the features and step definitions under `regression` above, allowing them to manage their own features without conflicting with the needs of the developers. Ensure that they're only run under controlled conditions (perhaps as a nightly build) rather than as a part of the normal BDD workflow, otherwise they'll slow development down to a crawl.

Who should be writing features? When we're using Cucumber from the point of view of development and documenting functionality for customers, then write the features in collaboration with developers, testers and your business people, in '3 amigos' style. However, when you're using Cucumber to effectively construct old fashioned test scripts which perform exhaustive regression testing of the application, then I can see value in this approach.

## From tail end to up front: QAs to Analysts

A word of caution for QAs: the important thing is to discuss this type of test with your developers and your business people. Are we testing where the risk is? What is the likelihood of this test ever failing in practice, catching a real bug that otherwise would not have been caught? What's the impact of such a bug? If there's little to no risk, or little impact, then the test we are writing has very little value, and we are creating work for ourselves for the sake of it. Overtesting is a waste of time: there is a better path for QAs.

I often try to work with QAs to transition them to a role which is much more upfront than at the tail end of the process. Traditionally, QAs are thrown working (but untested) code to see if they can break it, and the more code is sent back the more wasteful the process is.

However, with BDD there's a lot more automated testing going on. Developers are receiving their requirements direct from the stakeholders through proper communication, distilled down to clear Cucumber features. QAs should be involved in this process, working with the stakeholders, teasing out edge cases. If that sounds like a Business Analyst role to you, then you aren't far wrong: the roles can be very similar.

The old fashioned methods of in depth regression testing using scripts can still be useful. However, thanks to the advances of BDD and Specification By Example, there's less need for QAs to take a lead in this area. Instead of writing these tests, or God forbid clicking through them manually, they have the opportunity to take a lead in defining the scope of what's under test and when a requirement is finished.

## In summary

There's nothing wrong with features like these in our codebase as long as we understand who they're for, why they've been created, and who is maintaining them. Let's not be quick to dismiss them, just because we're not used to writing features in this style; but let's also be sure they're necessary before littering the build with brittle tests that have little value.

Do you have features like these in your code? Are you using them to drive business value, or are they clearly separate from your other features? How could they be improved?

