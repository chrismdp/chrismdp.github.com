---
layout: post
title: "Switching Sol Trader from Ruby to C++: one week on"
date: 2012-01-16 09:38:25 +0000
categories:
  - products
  - ruby
  - c++
  - code
  - sol trader
  - game development

---
Well, I didn't quite expect that. My [previous post](/2012/01/why-i-switched-from-ruby-back-to-c-plus-plus/) about switching [Sol Trader](http://soltrader.net) development from Ruby back to C++ caused [quite a storm](http://news.ycombinator.com/item?id=3440596).

Not being used to making waves on the mainstream Internet, I naively attempted to dive in and read and respond to every comment. It appears that feedback from the Internet at large tends towards the negative, so after a few hours I was feeling pretty discouraged, and only continued replying to some of the constructive feedback. Sorry if you didn't get a response.

I have a few more comparisons between Ruby and C++ which I'd like to share.

* *I'm finding myself reinventing the wheel more.* In Ruby-land I found third-party code easier to read, easier to install and easier to use. Trying to use someone else's library is C++ is harder. Often people don't seem to write automated tests, which strongly recommends me against using them. I'm also concerned that new libraries might introduce hidden memory leaks which will waste me time massively when I come to hunt them down. I appreciate people don't release their code just for me, so I'm not complaining: I've just found it more difficult to trust third-party code. I hope to try and fix this tendency by releasing large extractions from my project as libraries in the future.

* *Boost is awesome.* One notable exception to the above concern is the wonderful [Boost](http://boost.org) library suite. There is a library for almost everything you might need there, and the quality is very high. I'm already using the [Signals2](http://www.boost.org/libs/signals2) library for notifications (following the [Observer pattern](http://en.wikipedia.org/wiki/Observer_pattern)) and I plan to use the [Serialization](http://www.boost.org/libs/serialization) library for saving and loading games.

* *What to test?* The testing profile of my C++ code is different to my Ruby code. Thanks to strong typing, my tests fail for longer during the 'red' stage, so I find I have to write fewer edge cases. There are only so many ways C++ types can fit together, whereas Ruby objects can be combined in any way you like. I'm not sure I've hit on the right level of coverage yet: I'm not writing any tests for the more visual parts of Sol Trader yet and I'd like to consider how to.

* *I'm using a classist approach to testing.* In C++ I've tended to favour a [classical approach to TDD](http://martinfowler.com/articles/mocksArentStubs.html): that of testing a few small classes together from the outside using the public interface. Where I'm [coding to interfaces](http://stackoverflow.com/a/384067/1073735) I'm able to stub out that interface by inheriting from it in my test, but I'm not doing that often. Mostly I'm following my nose and attempting to keep my classes small and my collaborations few. I don't get all the design signals from my tests that I would like, but in my view that's better than exposing the internals of my class to the tests: that just complicates it unnecessarily. C++ is already difficult to read.

* *Prototyping complex class structures in Ruby first is really useful.* I've often benefited from having an existing Ruby class structure to take as my lead when writing C++. Those subsystems that I'd already written in Ruby were at least twice as fast to write. Rather than typing, or getting past the syntax, I've found [learning to be the constraint](http://dannorth.net/2010/08/30/introducing-deliberate-discovery/) in a number of coding situations. I'm not sure I'd always write in Ruby first, but in a case where I was really stuck and wanted to explore possible options, I might consider a rapid Ruby prototype over [CRC card design](http://en.wikipedia.org/wiki/Class-responsibility-collaboration_card), for example.

I'll continue to post my learnings as I collect them.

<div class='notice'>
  If you'd like to purchase Sol Trader you can now do so at <a href='http://soltrader.net'>soltrader.net</a>!
</div>
