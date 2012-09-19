---
layout: post
title: Cucumber isn't a testing tool
date: 2012-09-19 17:41:22 +0100
categories:
  - cucumber
  - business
  - bdd
  - team
  - testing

---

This is your periodic reminder that [Cucumber](/tag/cucumber) isn't a testing tool.

Here's what it actually is:

* *Cucumber is a great communication tool.* The great thing about collaborating on a cucumber feature is that the whole team get to stand in the same room and take part in the discussion. Everyone gets to argue about what should go in, what to keep out, and to help capture all the edge cases. The forming of the feature file facilitates that communication, with a great side effect of being able to check the finished feature still works at a later time. Cucumber excels as a communication tool, first and foremost: it's only incidentally a testing tool.

* *Cucumber captures conversations.* A feature file is a [bookmark](/2010/02/the-story-card-is-not-the-story) for the real feature: *the shared understanding of what needs to be done* that exists in the minds of the team. When the arm-waving and the arguments are done, a well written feature will expertly capture the essence of the conversation - the [semi-formal nature](http://dannorth.net/whats-in-a-story) of a feature acts as a checklist to ensure that we've talked about everything we need to.

* *Cucumber is for the team, not the developers.* Developers are often the gate-keepers of the feature files: if we're not careful we tend to write them, update them and run them without anyone else ever seeing them. We moan about how much more difficult features are to maintain than regular tests, whilst all the time we're missing the point: the features aren't for us, they're for those who can't read code!

For more on this, [watch this video](http://video2012.scotlandonrails.com/D1_LB_03-Ruby1280_b.mp4) ([slides](https://speakerdeck.com/u/chrismdp/p/cucumber-its-about-talking-not-testing)) from Scottish Ruby Conference where I explore these points in more depth. Remember that at its heart, Cucumber simply translates plain language into executing code. Its power lies in its ability to express code in plain language. Let's not reduce it to a mere testing tool, without letting the stakeholders see the features. If you're doing that, you're better off using RSpec.
