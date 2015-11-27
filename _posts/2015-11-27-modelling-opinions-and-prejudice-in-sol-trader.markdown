---
layout: post
title: "Modelling opinions and prejudices in Sol Trader"
date: 2015-11-27 16:51:31 +0000
categories:
  - indie games
  - game design
  - game development
  - sol trader
  - code

---

I've been working hard on the [Sol Trader](http://soltrader.net) core gameplay mechanics in the last two weeks. High up on my list was a way of generating more interesting missions for the characters to complete.

In order to have a reason to gather dirt, find locations or desire an early end for an enemy, our characters need to feel strongly about other people they know. This is where their opinions and prejudices come in.

<div><a href="http://imgur.com/7Zt8unW"><img src="http://i.imgur.com/7Zt8unW.png" title="source: imgur.com"/></a>
<div style='color: #999; padding: 10px 0 20px 0px'>So why is he so interested in where Terrilyn is? What does he know about her?</div></div>

Characters already keep track of the events they know about for each other character in the game. Now they can form an opinion of a character based on the partial set of info they know about someone else's past.

The plan is to use these thoughts about each other to make decisions about who they're friends with, deal with relationship breakdown, blame and prejudice.

<div><a href="http://imgur.com/Px17oXw"><img src="http://i.imgur.com/Px17oXw.png" title="source: imgur.com"/></a>
<div style='color: #999; padding: 10px 0 20px 0px'>Characters can hold a wide variety of opinions about each other</div></div>

Here's an example of how we configure this under the hood for an occasion where a character is caught and reported for taking bribes:

{% highlight text %}

    event,         opinion,    impact, I caught them, I was caught
    PRISON_BRIBES, PITIABLE,    -0.4,   0,             0
    PRISON_BRIBES, MORAL,       -0.4,   0,             0
    PRISON_BRIBES, INFLUENTIAL, -0.4,   1,             0
    PRISON_BRIBES, MY_FRIEND,   -1.0,   0,             1

{% endhighlight %}

Anyone knowing about this event will think the character is less deserving of sympathy and assume the character is less moral. If we're the one catching them take the bribes, then the briber becomes much less influential over us. If we're the one being caught, then the one catching us is definitely no longer our friend. Depending on our profession, we will brief against them or possibly try to take them out.

Now characters have opinions about others, we can use these to guide their conversation choices, who they're likely to target, give us gossip on, etc. It's all game design fuel for other behaviours in the game, and will combine to form interesting unexpected effects and tell original stories each time.

Next time I'll discuss about the new events that get created in the history generation because of these new opinions. Our stylised formulaic view of history is about to become, well, a lot more messed up. Rather like real history...
