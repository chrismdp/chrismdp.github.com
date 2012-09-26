---
layout: post
title: "OStatus: like Twitter, but open"
categories:
  - social
  - ostatus
  - open data
  - open source

---

Recently Twitter decided to make it's terms of service [rather more restrictive](https://dev.twitter.com/blog/changes-coming-to-twitter-api). This has led to a number of web applications, [IFTTT](http://thenextweb.com/apps/2012/09/20/ifttt-removes-twitter-triggers-comply-new-api-policies/) in particular, change the way they interact with twitter.

Recently, [Tom Armitage](http://twitter.com/infovore) described Twitter as "a universal messaging bus". Unfortuantely that bus appears to be getting less and less open by the day.

I don't blame Twitter, they have a business to run and investors to satisfy. However these days I'm looking for more in a platform than what they appear to want to provide. Recently I did some research on alternatives:

## Diaspora\*?

The [Diaspora\* project](http://diasporaproject.org/) is trying to solve a different problem to the one I'm interested in: that of a closed invite-only social network a la Facebook. I'm interested in finding a solution for the public dissemination of status updates.

## App.net?

[App.net](http://app.net) is interesting (I've [signed up](http://alpha.app.net/chrismdp)) but it's still representative of the same problem: it's one company controlling the platform. Despite what they say about how they're going to remain open, it's just the wrong set up for me and exacerbates the problem.

## Enter OStatus

This is more like it. The [OStatus](http://ostatus.org/faq) set of standards describe how a collection of nodes might publish status updates, reply to each other's updates, follow each other and more, all in a distributed fashion. You can implement the protocol in your app [step by step](http://ostatus.org/2010/10/04/how-ostatus-enable-your-application), so that you don't have a huge hurdle to overcome from the outset. There is now a [W3C community group](http://www.w3.org/community/ostatus/) and they're working on version 2.0.

There are a few implementations out there, most notably [Status.net](http://status.net) which offers a paid hosted corporate version and a freely installable version, and the popular [identi.ca](http//identi.ca) service. These are implemented in PHP, but for those of us who are used to Ruby...

## rstat.us

[rstat.us](http://rstat.us) is a great ruby project I've jumped on board with looking to implement a reference standard for OStatus in Ruby. We're at work implementing most of the core OStatus functionality, trying to push it down into shared gems, and provide a UI reference for a Twitter-like experience.

The team is also hard at work implementing a Twitter-like API, which means that any of the disenfranchised Twitter clients out there will very soon simply allow the changing of the URL endpoint, and their app will <i>just work</i> with rstat.us.

So, a call to action: *if you can code, [get involved](http://github.com/hotsh/rstat.us) in the project and make it happen.*

If you own a Twitter client, or know someone who does, *get in touch and offer to beta test the API using your client.*

## The future

Once rstat.us has matured and core OStatus functionality is done, any project will be able to incorporate a status update setup into their website. For example, my game [Sol Trader](http://soltrader.net) has a list of status updates of the site, currently taken from the Twitter feed. Won't it be great when you can subscribe to those updates on your own node, just by subscribing to 'news@soltrader.net'?  And then you reply to the update using your own node, and have your comment appear directly on the site? That's what we're working towards.

## The goal

I'd love to see App.net adopt OStatus. I've love to see Diaspora\* adopt OStatus when it reaches version 2.0, allowing for more private interaction.

I'd love to see <i>Twitter</i> adopt OStatus - if that happens, we've reached a huge milestone.

You might say Twitter is for 'normals' and OStatus is just for us geeks. They said that about the web at first, too. This movement can gain traction: what's it going to take to make it happen?
