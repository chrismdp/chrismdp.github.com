---
layout: post
title: Pomodoros help you refactor
date: 2011-04-01 20:21:15.000000000 +01:00
categories:
- code
- pomodoros
- tdd
- craftsmanship
- pairing
redirect_from:
- "/2011/04/pomodoros-help-you-refactor"
---
<p><i>"If you finish a task while the Pomodoro is still ticking, the following rule applies: If a Pomodoro Begins, It Has to Ring. It’s a good idea to take advantage of the opportunity for overlearning, using the remaining portion of the Pomodoro to review or repeat what you’ve done, make small improvements, and note down what you’ve learned until the Pomodoro rings."</i></p>

-- Francesco Cirillo, [The Pomodoro Technique](http://www.pomodorotechnique.com/)

What's the single most important part of Test Driven Development not to miss? Refactoring. What's the part of TDD that's most often missed? Refactoring.

With refactoring, we work our way toward a great design, clean code, and flexible organic tests. Without refactoring, we have ugly brittle test suites and uglier code. We know this. What I don't always do is take advantage of the moments I have when I can effectively refactor for free.

At the end of a task, when the build is running, I've previously let my mind wander to the next thing, or check email, surf the net, and generally [get out of the zone](http://www.computus.org/journal/?p=982). This bad habit has been highlighted to me in [my use of the pomodoro technique recently](/2011/03/pomodoros-done-hopefully-right).

I was doing the same for the shorter pauses during normal TDD. My pomodoros statistics were telling me that I'm very bad at concentrating whilst coding: the average time spent before I let my mind wander was 11.67 minutes. I was allowing my mind to drift whilst Rails started up to run whatever test I was working on. Not good.

## Time to improve

This week, I've been trying to take the time to look at my code critically for areas of improvement. A pomodoro is indivisible, which means I'm not _allowed_ to think about anything else.

And guess what? I always find something to improve, and I feel that little bit better about my code.

The also helps with the thing I've missed most about not pairing: that other person's critical eye on what you're doing, always thinking about the code being written. During the natural pauses, you can be that other person and ensure the code you write is great. Being two people is [more fun, too](http://www.pixar.com/shorts/gg/index.html).
