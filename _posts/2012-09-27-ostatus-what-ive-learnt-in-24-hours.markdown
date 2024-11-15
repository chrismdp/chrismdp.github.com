---
layout: post
title: 'OStatus: what I''ve learnt in 24 hours'
date: 2012-09-27 20:24:54.000000000 +01:00
categories:
- social
- ostatus
- open data
- open source
redirect_from:
- "/2012/09/ostatus-what-ive-learnt-in-24-hours"
---
[Yesterday's post](/2012/09/ostatus-like-twitter-but-open/) was rather [popular.](http://news.ycombinator.com/item?id=4574858)

Here are a few things I've learnt since, from various commments, Hacker News posts and further reading:

* *WordPress might be a tipping point for OStatus.* There's a [WordPress plugin](http://wordpress.org/extend/plugins/ostatus-for-wordpress/) which gives a fairly straightforward path to link any WordPress blog to the OStatus network. That would allow people to follow any blog through [rstat.us](http://rstat.us) (for example) and to reply directly on their own node and have the conversations appear on the original blog. There are [apparently 60 <i>million</i>](http://news.ycombinator.com/item?id=4575016) WordPress installs out there: this could be a huge gateway for the federated social web. Here are [some great ideas to market it](http://news.ycombinator.com/item?id=4575054): anyone able to help [pfefferle](http://profiles.wordpress.org/pfefferle/) out?

* *Tent.io exists.* OStatus is a couple of years old, but someone else has attempted to solve the same problem recently: there's an [open source platform](http://tent.io) and a first class [implementation](http://tent.is), just launched. Apparently there are [scaling problems with the architecture](http://chrismdp.com/2012/09/ostatus-like-twitter-but-open/#comment-663156881), but it's good to see any sort of movement. Hopefully we can all learn from each other and move forward the conversation.

* *The Developer Experience movement exists.* The [developer experience movement](http://blog.oshineye.com/2011/05/what-is-devexp.html) seeks to apply user experience techniques to design software other developers love to integrate with. This is very relevant to the OStatus movement: if the protocol is too complex, then it won't propagate as people won't be able to implement it. Arguably the hardest piece of OStatus to implement is the signed updates via Salmon, and it has a wealth of buggy half-done implementation out on the net. This means nodes are constantly tripping over each others bugs when trying to talk to each other. The antidote to these sick implementations? We need simple-to-use libraries for every language under the sun. Time to get to work!

* *User acquisition isn't the only problem to consider.* It's obviously a big problem, but it's only one piece of the puzzle. My friend [Adewale Oshineye](https://plus.google.com/+AdeOshineye) has been thinking about this problem a lot, and lists a number of different problems on an [insightful Google+ thread.](https://plus.google.com/105037104815911535953/posts/RZY3SPcCndz) None of these problems are insurmountable though, and clever people are working on getting them solved, which is very encouraging.

What can we do individually to push things forward? And how can we keep the conversation going?

