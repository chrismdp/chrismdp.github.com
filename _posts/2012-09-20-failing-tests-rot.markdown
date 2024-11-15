---
layout: post
title: Never leave a failing test
date: 2012-09-20 15:36:32.000000000 +01:00
categories:
- tdd
- craftsmanship
- code
- testing
redirect_from:
- "/2012/09/failing-tests-rot"
---
<p>Imagine this: you're taking a guided tour of a nuclear power station. Just above the door as you come in there there are five lights marked Key Safety Indicators. One of the lights is flashing red.</p>

"What's that flashing red light?" you nervously ask your host.

"Oh, that light does that from time to time. We're not sure why; we just ignore it."

There's an awkward silence. How confident are you feeling right now?

## Failing tests fester.

Red tests are like code rot. Catch it early and sort them out, and you'll be fine. If you don't, they'll spread through your code like a disease, causing all sorts of damage:

* *Failures cause fear of change.* If we don't understand why a test is failing, we don't understand the code base. If we don't understand our code, we can't change it safely. All bets are off: any change we make will cause us to be that little bit more anxious.

* *Failures breed failures.* If one test continually fails, then other coders are more likely to tolerate failing tests, and the number of failing tests will grow quickly.

* *Failures kill urgency.* There's a scene in a well-known heist movie where a team of thieves has to break into a bank. Their strategy revolves around putting a remote-controlled car under a waste bin: they use this to cause the bin to move at night, setting off all the alarm sensors. The first time the alarm goes off, the place is filled with police in a matter of seconds. The fifth time the alarm goes off, only one squad car with two bored officers turn up, totally unprepared for the waiting thieves who quickly overpower them. The same is true with tests: if they fail all the time, developers will take a cavalier attitude to checking out the cause. This could cause a really serious failure to be missed.

The only point at which failing tests are valid is when you've written them just before the code you plan to add. If the test should be failing, write code to make it work. If the test shouldn't be failing, change it or delete it. Never leave it to fester.
