---
layout: post
title: "How tone of voice works in Sol Trader's dialogue system"
date: 2015-05-27 11:45:08 +0100
categories:
  - game design
  - sol trader
  - game development
  - code

---

Hot on the heels of the [main dialogue system](/2015/05/how-dialogue-works-in-sol-trader/) in [Sol Trader](http://soltrader.net), I've been working on adding tone of voice to the system. I think this will add a lot to the way that the dialogue system works. It will allow for some interesting and thematic interactions, like the one below: 

![tone of voice](/files/sol-trader-tone-of-voice.png)

Perhaps I should have chosen a better subject :) Read on for more about how it works. 

## How tone of voice works

Each tone of voice that can be used has two character attributes attached to it, which are opposed against the other. For example, if you attempt to flirt with someone, your "charm" (basic flirting ability) is pitched against their "wisdom" (how easily they can see through you.)

You select a tone of voice and a conversation subject. We then roll a dice for each person and add their relevant attribute. If your score is greatest, any test that is conducted on the selected conversation subject is that much easier to succeed on. For example, if you're trying to borrow a ship, or get a bargain, attempting to impress (or flirt with) the person you are speaking to might make the chance of getting what you want that much greater.

However if you fail the tone of voice test, it makes it much harder to succeed in what you're trying to do. So you have to be careful which tones of voice you select. It pays to use tones for attributes that you are particularly strong in. It also pays to avoid tones where the person you're talking has a high resistance, if you know them well enough to know what these are. For example, if your conversation partner has high wisdom, flirting with them is unlikely to lead to a successful outcome unless your charm is also very high.

## Under the hood: how to mod it

The tone of voice data is completely customisable via a simple CSV file format. Here are some example tones:

{% highlight text %}

       String, you,   them,    effect success string,   effect failure string
   TONE_FLIRT, CHARM,  WISDOM, TONE_FLIRT_SUCCESS,      TONE_FLIRT_FAILURE
 TONE_IMPRESS, MIND,   CHARM,  TONE_IMPRESSIVE_SUCCESS, TONE_IMPRESSIVE_FAILURE
TONE_OBLIGING, WISDOM, MIND,   TONE_OBLIGING_SUCCESS,   TONE_OBLIGING_FAILURE

{% endhighlight %}

The idea is that people can mod both the different tones of voice that characters are able to use, but also the attributes that are checked when running the tests. It's easy to add any tone you want: there's a [lively Facebook discussion on Indie Game Developers](https://www.facebook.com/groups/8117041572/permalink/10152769863491573/) with lots of ideas for tones that could be added:

Can you think of any others we might add?
