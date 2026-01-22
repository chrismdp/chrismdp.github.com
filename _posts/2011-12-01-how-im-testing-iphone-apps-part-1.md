---
layout: post
title: 'How I''m testing iPhone apps: part 1'
date: 2011-12-01 22:45:35.000000000 +00:00
series: "Testing iPhone Apps"
categories:
- code
- ios
- tdd
- bdd
redirect_from:
- "/2011/12/how-im-testing-iphone-apps-part-1"
- "/2011/12/how-im-testing-iphone-apps-part-1/"
---
<p><i>This week I've been working with <a href='http://shilling.co.uk'>Shilling</a> helping them get starting with iOS application development. Part of the deal was for me to learn it myself as we went: I've done hardly any iOS work and we've been learning how to do it together.</i></p>

<p><i>As part of this process, working out the best way to test-drive the development of iOS apps was high on my priority list. I know that the automated testing of iOS applications is still not widely practiced and isn't well documented, so I decided to write a series of posts to start to rectify that.</i></p>

## Our goal

There are two main parts to working out how to test-drive applications on a new platform. One is to figure out the testing libraries and write simple `1 + 1 = 2` style tests to prove it can be done. The other half is working out how to apply common testing techniques such as stubbing external systems, isolating tests correctly and optionally driving the interface.

The first of these steps is quite easy on iOS, but the second part is harder. In our case, we have some code which makes use of CoreLocation and the [Geonames](http://geonames.org) service to get an iPhone's location and look up the county name from a latitude and longitude. This means that our code relies on two external services to run, which we want to stub out: we don't want these services to be called each time our tests run. How were we to set this up correctly?


## Apple's documentation

To kick off our testing adventure on iOS, we started with [Apple's own public documentation](http://developer.apple.com/library/ios/#documentation/Xcode/Conceptual/ios_development_workflow/135-Unit_Testing_Applications/unit_testing_applications.html) on how to test iOS. This is a fairly comprehensive guide on how to set up a project with built in testing, allowing you to write basic SenTest tests quite quickly.

Apple divides its definition of unit testing into two categories:

* Logic tests: these are what I would normally call unit tests. They rely on very few external APIs and are run standalone without the use of a simulator.
* Application tests: these are executed in the context of a running application on a simulator or iOS device.

The document details how to set up both types in your project. There's a few things missing though:

* They have good ideas about [how to write decent tests](http://developer.apple.com/library/ios/#documentation/Xcode/Conceptual/ios_development_workflow/135-Unit_Testing_Applications/unit_testing_applications.html#//apple_ref/doc/uid/TP40007959-CH20-SW12), but lack information on how to correctly mock system endpoints. I want to do this so that I don't have to rely on iOS location simulation, or HTTP response data, to make my tests work.
* There was also nothing on how to test asynchronously, which is a real problem as iOS applications are mostly written in this way.
* Application tests are executed in the context of your application, but without extra work it's not possible to support native UI testing, [Capybara](https://github.com/jnicklas/capybara) style. We are reduced to manipulating controllers directly, which is good enough for now. This assumes you have your user interface wired up correctly. As the app always has to be tested manually anyway then this isn't too much of a risk, but if you want to take a step further you could use [KIF](https://github.com/square/KIF), [Frank](https://github.com/moredip/Frank) or Apple's own [UIAutomation](http://developer.apple.com/library/ios/#documentation/DeveloperTools/Reference/UIAutomationRef/Introduction/Introduction.html). There's a good post comparing them [here](http://sgleadow.github.com/blog/2011/10/26/which-automated-ios-testing-tool-to-use/).

So we followed through the basic set up instructions, and got a simple test running which added two numbers together. A good start, but useless for real work.

Time to go in search of an asynchronous testing framework: and we found a great one. Next time, I'll talk about the wonderful [Kiwi](https://github.com/allending/Kiwi).

<i>How are you testing iPhone apps? Do chime in throughout the series with suggestions and comments, and I'll edit the posts as appropriate.</i>
