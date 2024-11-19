---
layout: post
title: How I'm using Proxemics in Sol Trader's game design
date: 2015-04-28 21:01:22.000000000 +01:00
categories:
- game design
- sol trader
- game development
- code
- psychology
redirect_from:
- "/2015/04/how-i-m-using-proxemics-in-sol-trader-s-game-design"
---
<div style='float: right; padding: 0 0 10px 20px; width: 250px'><img src='/files/new-relationships.gif' alt='new relationships'/>
<div style='color: #999; padding-top: 5px'>Your relationships, shown closest first. Your relationship with your father has cooled lately...</div>
</div>

I've been trying to get to the heart of [Sol Trader](http://soltrader.net)'s gameplay in recent months. I've been working on [rewriting the history generation system in pure C](/2015/04/how-i-doubled-the-speed-of-my-game-by-giving-up-on-c-plus-plus), and concentrating on the interactions between the player and the characters in the game.

This week I completely replaced all the relationships code to make it [more manageable and more fun](/2015/04/how-to-choose-between-realism-and-fun). Read on for a comparison of the old relationship system and the new one, and why the new code  is better and more fun for the player.

## The old system: numerical levels

Previously a relationship between two people consisted of a status field which described the type of relationship (parent, child, sibling, spouse, etc) and a numerical value from -10 to 15 which described the strength of the relationship. Negative values meant that the characters were enemies, and high positive values signified close friendships.

Each year the history simulation would go through the list of relationships for each character, do some tests on them and work out whether the level should drop or rise. If the level went through a threshold, the relationship might change (people married, divorced, fell out etc).

This worked well enough, but it had some problems. For one thing there was no limit on the number of people a character could befriend. High charm characters had hundreds of extremely close friends, which is hardly realistic. Also, the generation was slowing significantly as a few highly networked characters shared every last detail of their lives with all their friends and relations.

## The new system: Proxemics for relationships

[![Personal space diagram](/files/Personal_Space.png)](http://en.wikipedia.org/wiki/Proxemics#/media/File:Personal_Space.svg)

To counter this, I've moved to a simpler system based on the social psychology concept of [Proxemics](http://en.wikipedia.org/wiki/Proxemics). Proxemics is the study of personal space between people: I've used the idea to limit the levels of relationships that each character can have. The idea is that each person is allowed a number of relationships at each of four levels:

* Intimate: sharing highly personal information with 1-2 very close people
* Personal: for 4-6 good friends
* Social: another 5-10 friends and acquaintances who share more public information and gossip
* Public: other acquaintances, co-workers and random people the character comes across

Each year during history generation, all these relationships are tested for each character and can move up and down the list. New people can be suddenly introduced at a high level: get a new boyfriend or girlfriend and the character's older family relationships can be pushed down to a lower level, as there's only room for a few people that close to us. When a type of relationship breaks into a new more intimate space, certain events can be trigged (marriage, for example.)

There's a hard limit to the number of relationships a character can have in total. This means relationships which bubble downwards can vanish over time as the character loses touch with friends and distant relatives.

# The benefits of the new system

There's both a realism and a fun boost with the new code. It's much easier for the player to manage and keep track of the number of people a character knows, so that they can use that network to their own advantage. It's also feels more realistic: low charm characters have many fewer relationships, and even characters with high charm don't have an overwhelming number. It's great fun to scroll through a character's known relationships and see who they've chosen to be close to.

The history generation is also faster now, as I'm storing fewer relationships and less information for each, which means more info is being fetched each cache miss (see [this article](/2015/04/how-i-doubled-the-speed-of-my-game-by-giving-up-on-c-plus-plus/) for why this matters). Overall it's a win for realism, fun, speed and code simplicity and I'm pretty happy with it so far.

Do you think this model works well for modelling relationships? Anything I can improve?
