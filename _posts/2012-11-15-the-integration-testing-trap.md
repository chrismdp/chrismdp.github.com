---
layout: post
title: 'Cucumber: the integration testing trap'
date: 2012-11-15 17:04:26.000000000 +00:00
categories:
- cucumber
- bdd
- testing
- tdd
redirect_from:
- "/2012/11/the-integration-testing-trap"
---
"Why don't people read my Cucumber features?"

It's an often heard refrain, and it can feel frustrating for developers. We carefully craft features that make sense to us, and are reasonably easy for us to understand. We post them over to our product manager hopefully, but a glazed look comes over their face as they read them, and they seem only to read the first half before becomes distracted, and mumble that they "look fine", before moving on to something else. As developers, what can we do about this?

There can be many reasons this might happen, but one of them is that we could be writing our features to ensure our code is correct, rather than ensuring that it's suitable. Perhaps we're using Cucumber to writing integration tests, not acceptance tests.

## Acceptance tests != Integration tests

What's the difference between the two? Both types of test sometimes look similar in code, but they are written from completely different points of view.

Integration tests test the objects in our system work correctly together. Where unit tests check the the messages objects are sending and receiving are correct, integration tests check that the messages match up and the objects are playing nicely together.

It's useful to have a few integration tests at points in our codebases where the object interactions are critical. A little too much testing at this level will lead to slow test code, and we'll never be able to cover every eventuality - see [my post](http://chrismdp.com/2011/10/your-tests-are-lying-to-you) and particularly J.B. Rainsberger's [excellent posts](http://www.jbrains.ca/permalink/integrated-tests-are-a-scam-part-1) on integration testing.

Some people use the terms for integration and acceptance tests interchangeably. They may be written similarly, but _integration tests are not the same thing as acceptance tests._ They are still written for the developer's benefit. They are still ensuring that we're building the thing right, not ensuring that we're building the right thing.

Acceptance tests are a whole different ball game. When writing them, our tests are focused on the customer and on what they want built, rather than ensuring our own code fits together well. They're oriented entirely around what the customer sees, not what we see. As developers, they're not actually for us at all.

We probably need both types of test in our system. Many developers, however, though diligently writing integration tests, have never written an acceptance test in their life. By conflating the two ideas, we're missing the point: in order to do BDD properly _there has to be a level of testing that isn't about us, but is about our customer._

Cucumber works best when the step code is oriented around the acceptance of the feature, rather than whether a feature's code is correct. The difference is subtle but important. If we're thinking of integration tests during our feature writing, then we'll write our features in that fashion. Our steps will constantly need to be modified to fit our notion of what needs to be tested, which is why our customers tend to glaze over when they read them. The features will tend toward greater detail, as we're testing correctness not suitability, and there will probably be lots of them. It's difficult for a customer to keep up with these types of tests, and it's not surprising they lose interest.

## Sit down with your customer

I'm generally happy with developers drafting features and then bringing them to a discussion with their team to refine them and nail down exactly what's needed. I don't recommend this when you're starting out, though, and if you're finding that your customer isn't even reading your features properly, then something is seriously wrong.

If this is happening, I suggest you take the ideas back to first principles and sit down with your customer to write a few feature files out before you start on the next piece of work. You could try and get them to suggest the wording for the first feature. They might attempt to suggest wording that would be more in keeping with a developer mindset, and struggle in the process. That's exactly what Cucumber was created to avoid.

Ask them to describe the feature in their own words, and work together to get something down on paper which makes sense to both of you. If we remember that this feature isn't for us to test our system's correctness, but a blueprint to guide our development direction, then there should be no conflict. Try to adopt their words for the different concepts in your system, rather than defaulting to your own pat terms (perhaps shoppers, not users, for example.) If in doubt, defer to the customer's wording: don't try and impose you're own structure except for ensuring the bare minimum to get the feature to run.

I've often said before that if no one is reading our features, we're better off using RSpec. My thinking has evolved: perhaps many people miss the point of the outer part of the BDD cycle entirely - the tests are about the customer, not us. If we're only using Cucumber for integration testing, we are better off using RSpec. Whatever tool we use, we need to make sure it's giving value to customers, not layering on integration tests for our own benefit.


<div class='alert alert-info'>
  <p>If you like what you read, and you'd like to learn more, a quick reminder that Matt Wynne and I are running <a href='http://bddkickstart.com'>BDD Kickstart</a> in London <a href='http://bddkickstart.com/dates#london'>this coming December</a>.
  </p>
  </div>
