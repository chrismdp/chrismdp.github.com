---
layout: post
title: Your framework is a liability
date: 2012-09-28 20:46:31.000000000 +01:00
series: "Liabilities"
categories:
- code
- ruby
- agile
- liability
- sinatra
- paypal
redirect_from:
- "/2012/09/your-framework-is-a-liability"
- "/2012/09/your-framework-is-a-liability/"
---
Your framework is a liability.

Every library you import before you start the project means more for someone else to digest and understand. Each complex 'clever' library equals another few minutes per team member trying to interpret why you imported it, how to use it, and where the configuration goes. Every framework you decide to use is a early decision about how your project will fundamentally work, which might turn out to be the wrong one. Each library is an opportunity for someone else to introduce a bug into your project.

*The only asset a framework or library gives you is a faster route to your feature.* Anything else will drag you down.

If your framework is heavy and onerous, then your code will have a large net negative liability before you've even begun. You'll be constrained to follow a certain set of patterns, which you might end up fighting against later on. Work on the app first: your <anacronym title="minimum viable product">MVP</anacronym> might not even need the benefits your framework provides.

A few examples of where I've benefited from not blindly installing the "standard stack":

* I've recently started building some new projects wholly in [Sinatra](http://sinatrarb.com), pulling in various gems only when I need to, rather than starting with Rails from the outset. [Sol Trader's website](http://soltrader.net) is pure Sinatra. It was simply much quicker to get started, and I found I could layer on functionality as I needed it. Several months on, I've yet to need to turn to a Rails app.

* When I came to add Paypal integration to the site, I looked at various gems, and decided they were just going to drag me down with extra configuration and hassle. I ended up building Paypal IPN integration [in about 30 lines](https://gist.github.com/2768532) using pure ruby: no libraries. Most of that code was tests.

Don't get me wrong: I still use frameworks for some of my projects, and libraries for all of them, but I'm learning to stop and think before cargo culting the latest stack of 25 different libraries before I can get anything done.

Import a lightweight framework or library when you need to. Consider when you might be chaining yourself to it, which might make a later pivot difficult. It's much easier to add a framework than to remove one from your project: pick the easiest thing to move away from.
