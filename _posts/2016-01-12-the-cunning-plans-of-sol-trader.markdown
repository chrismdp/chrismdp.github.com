---
layout: post
title: The cunning plans of Sol Trader
date: 2016-01-12 05:56:28.000000000 +00:00
categories:
- indie games
- game design
- game development
- sol trader
redirect_from:
- "/2016/01/the-cunning-plans-of-sol-trader"
---
I've just finished reworking the old state-machine based AI system that I threw
in to the game last year just to get something working. Sol Trader now boasts a
full
[STRIPS-based](http://aigamedev.com/open/article/strips-theorem-proving-problem-solving/)
planning AI. This works by starting a character off with some basic needs to
fulfil: the need to socialise, rest, work, self-improve, etc. It then uses
pathfinding techniques to work out a series of steps to get those needs
fulfilled, such as buying a cheap good and selling it for more somewhere else,
hitting the bar after work, or hanging around a jumpgate looking for easy prey. Here's how it works.

<div><a href="http://imgur.com/EeaL2Bp"><img src="http://i.imgur.com/EeaL2Bp.png" title="source: imgur.com"/></a>
<div style='color: #999; padding: 10px 0 20px 0px'>The new planning system at work: a few of your relatives sleep at a tiny motel</div></div>

## Making a plan

Let's say Anthony, an AI character, is tired and has a strong need to rest. To
fulfil that need, the game allows the character to rest at home, but also to
stay a night at a friend's house.  Here are some rules from the actual planner
in the game written in a semi-formalised manner:

* in order to `REST` we can `RELAX_AT_HOME` if we are `IN_LOCATION(MY_HOME)` at cost of 0
* in order to `REST` we can `STAY_A_NIGHT` if we are `AT_HOME_OF(CLOSE FRIEND)` at cost of 50

To stay the night at a friend's house, Anthony would need to move to their house, so we need some more rules to cover this:

* we are `AT_HOME_OF(PERSON)` if we are `IN_LOCATION(PERSON)`
* in order to be `IN_LOCATION(LOCATION)` we can `MOVE_TO(LOCATION)` if we are `IN_CITY(CONTAINING LOCATION)` at cost of 10

Let's assume that we are already in the city in question. The planner starts off at the need (`REST`) and works backwards until it find this `IN_CITY` state. It then forms a chain of actions to complete to get the need fulfilled:

    ANTHONY'S PLAN: MOVE_TO(HOME) -> RELAX_AT_HOME -> FULFIL_NEED(REST)

The game will always chose the lowest cost option. If Anthony is in his home already, or in the same city, then he would just go home to rest, rather than to a friend's house. However, let's assume he is in a different city. It's too far for Anthony to head home to his house, so the lowest cost option would then be to trespass on the hospitality of a friend who lives in that city.

## Planning works extremely well for Sol Trader

There's no one-size-fits-all when it comes to good game AI. The effectiveness
of AI techniques varies dramatically depending on the type of game being
designed. However, planning is a great fit for Sol Trader: it's had
a dramatic effect of the feel of the game.

Now the AI is now intelligently making decision based on relative needs, the
game has the following new features, all of which were easily added:

* Characters now visit friends and colleagues, hiring ships if they don't have their own transport
* Traders buy and sell goods intelligently, by buying cheap, travelling to another planet and selling
high. It's great fun watching the ships take off and land, knowing they have a cargo
full of cheap goods bound for some far-flung planet, which will actually be
more expensive in their destination.

<div><a href="http://imgur.com/uukvQ3t"><img src="http://i.imgur.com/uukvQ3t.png" title="source: imgur.com"/></a>
<div style='color: #999; padding: 10px 0 20px 0px'>Plenty of characters making travel enquiries at a Martian spaceport</div></div>

* Navy ships now take off and escort famous characters.
* Unwise navy characters might take the law into their own hands, destroying ships close to them that contain characters they know to be immoral.
* All ships defend themselves when attacked, depending on their piloting skills and their wisdom
* Characters will run to a planet for repairs should their ship get too damaged.
* I've also got the bare bones of the Pirate AI in, so you need to watch out when travelling around the various systems now: I've already been attacked once whilst trying to test something else. They're not that smart yet, and will attack even in major population centres, but I'll fix that in an upcoming release.

<div><a href="http://imgur.com/Ph1Ml1m"><img src="http://i.imgur.com/Ph1Ml1m.png" title="source: imgur.com"/></a>
<div style='color: #999; padding: 10px 0 20px 0px'>Watch that trigger finger: ships will now attack and defend themselves</div></div>

It was also very easy to put in a conversation option which asks what a
character is thinking about. This returns some text detailing the character's
top need, which shows what they're most likely to do next:

<div><a href="http://imgur.com/cJ367oH"><img src="http://i.imgur.com/cJ367oH.png" title="source: imgur.com"/></a>
<div style='color: #999; padding: 10px 0 20px 0px'>Pretty forward thinking of Alysa to want to improve her life... at the age of 1</div></div>

I've posted the start of a [reference guide](http://forums.soltrader.net/post/modding-planner-data-structures-7884634?pid=1290506069) to the forums for modders.

This new build is now available from the forum if you have purchased insider access (if you haven't [there's still time](http://soltrader.net/back-us)!) If you are already a Kickstarter backer and you haven't received your copy, or you're a member of the press, do [get in touch](mailto:support@soltrader.net).

