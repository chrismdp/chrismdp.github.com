---
layout: post
title: How dialogue works in Sol Trader
date: 2015-05-13 16:29:47.000000000 +01:00
series: "Building Sol Trader"
categories:
- game design
- sol trader
- game development
- code
redirect_from:
- "/2015/05/how-dialogue-works-in-sol-trader"
- "/2015/05/how-dialogue-works-in-sol-trader/"
---
I've recently designed a dialogue system for [Sol Trader](http://soltrader.net). When deciding how to support dialogue, I researched all the different ways that these systems are normally done in video games: I wanted to ensure that our system is as flexible and as immersive as possible. I've gone for a hybrid of all the methods I discovered and I explain how it works at the bottom of the post.

## Dialogue research

<div style='float: right; padding: 0 0 10px 20px; width: 350px'><img src='/files/sol-trader-conversation-preview.png' alt='new conversation preview'/>
<div style='color: #999; padding-top: 5px'>A basic preview of the new dialogue interface</div>
</div>

There are a number of different methods of doing conversations in games, summarised informatively in [these](http://www.gamasutra.com/view/feature/3719/defining_dialogue_systems.php) [two](http://www.gamasutra.com/view/news/114503/Analysis_Conversation_Design_In_Games.php) excellent Gamasutra articles. I've summarised the most relevant ones here:

* *Non branching dialogue.* Players walk up to the character and they deliver their message, which is often the same each time.

* *Branching dialogue.* The classic 'conversation tree' approach. A preset piece of dialogue is delivered and a player has an option to choose from a range of options in reply. This then delivers another response, and the process is repeated. This is better than the non-branching approach, but can lead to linear and frustrating conversations where the player feels they've missed out on a vital piece of information.

* *Hub-and-Spokes dialogue.* This is similar to Branching Dialogue above, but in this version the player chooses from a range of options on a 'hub' of the conversation. After hearing the response, the player is normally returned back to the main hub, or sent to a deeper hub with more options to choose from. Players can therefore exhaust the conversation options with a particular character, which can lead to rather unreal conversations if the character has infinite patience.

* *Parser driven dialogue.* The game attempts to understand the natural language typed in by the player and responds in turn. This is relatively rare in modern games, [Façade](http://www.interactivestory.net) being a notable exception. The number of responses required to keep the conversation feeling natural is very time consuming to produce, and the potential for the game to misunderstand the player's intentions is very high.

* *Time limited dialogue.* In this version a player only has a certain number of interactions they can conduct during any particular time period, and much choose who they spend time with and what they choose to find out. This creates some interesting and potentially agonising choices for the player, although with a fully scripted game the player won't get to explore all the options available.

## Under the hood: Sol Trader's conversation system

Conversations are something that Sol Trader has to get right. I decided as far as possible that the gameplay should be [based around the character interactions](/2015/04/how-to-choose-between-realism-and-fun/), so the player must enjoy the process and not get frustrated with it.

I have gone for a variation on the Hub-and-Spokes method: a rules based system for choosing options, the addition of tone of voice, and two time limiting factors: patience and time of day.

#### Patience

When you start a conversation with a character, they have a certain amount of patience for you. This is based on their Wisdom attribute (which is generally used for emotional intelligence and maturity). It's also modified depending on what they're doing: if they're languishing in prison they'll have a lot more time for you, but if they're on guard duty they won't be able to stand around talking all day. If you're a good friend they will put up with you for longer, but if they can't stand you, you'll get hardly any time at all.

You 'spend' this patience with every conversation statement you choose. Some statements require a test which will affect how much patience the statement ended up taking. Once you're out of patience, the conversation is over. Patience regenerates slowly: you won't be able to immediately start a new conversation with someone if you've just finished talking their ear off.

#### Tone of voice

You'll be able to select a particular way that you say something, allowing you to flirt, to be extra obliging, try to impress the character, and so on. This will affect both the amount of patience you use up, and any tests the selected conversation statement requires.

I'll talk more about tone of voice and how it's implemented in a future post.

#### Time of day

Character go to work in the morning, and go home or out socialising in the evening. The conversation options available to you will vary depending on what they're doing, so you'll have a limited amount of time to interact with them.

## Example: a basic greeting

Two typical conversation statements might have the following data:

{% highlight text %}

Required Character Activity: At reception
Minimum Closeness: Personal friend
What to say: "Hey $firstname! Such a pleasure to see you! Anything I can do for you?"

{% endhighlight %}

{% highlight text %}

Required Character Activity: At reception
Minimum Closeness: Unknown
What to say: "Hello. How can I help?"

{% endhighlight %}

Each of these two statements is checked whenever either the player needs to choose an option, or the character needs to make a response. In this case, this is the initial greeting. If you are a personal friend of the character, they'll greet you in a warm and friendly manner. If they don't know who you are, they'll be much more business-like.

(You can watch me implementing this basic set of statements [on this livestream archive video.](https://www.youtube.com/watch?v=vA0eMnuFq6E))

## Example: making small talk

Here are a set of conversation statements for small talk:

{% highlight text %}

Required Character Activity: Socialising
What to say: Make small talk
Attribute to test against: Charm
Difficulty: Normal
Patience cost: 1
Tag on test success: SMALL_TALK_SUCCESS
Tag on test failure: SMALL_TALK_FAILURE

{% endhighlight %}

{% highlight text %}

Required Character Activity: Socialising
Required tag: SMALL_TALK_SUCCESS
Patience modifier: -1
What to say: You have a long discussion about sports with $firstname.

{% endhighlight %}

{% highlight text %}

Required Character Activity: At front desk
Required tag: SMALL_TALK_SUCCESS
Patience modifier: 0
What to say: You chat briefly about the traffic jam outside on the street, agreeing that the local council should ban cars from the area.

{% endhighlight %}

{% highlight text %}

Required Character Activity: Socialising
Required tag: SMALL_TALK_FAILURE
Patience modifier: +1
What to say: You attempt to engage $firstname on a discussion about weather vanes geometry with little success.

{% endhighlight %}

The player has the option to choose the first statement, which is making small talk. Note that the other options aren't available as the `SMALL_TALK_SUCCESS` and `SMALL_TALK_FAILURE` tags aren't set. If the player selects this option, then a test on your charm is conducted: if works then the `SMALL_TALK_SUCCESS` tag is set.

There are two statements that become available once that tag is set, and the choice will depend on whether you are socialising or chatting at a reception desk. If you're at reception, the cost of the discussion remains 1 for the initial small talk statement, but if you were socialising, this response will give back your patience point to reuse on another statement. People have a tendency to rattle on when at the local bar!

What do you think? Can you think of anything this system doesn't cover?

Next time I hope to have a short video showing off the basics of the system.
