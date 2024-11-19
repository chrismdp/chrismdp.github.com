---
layout: post
title: Gossip as a game mechanic
date: 2015-09-03 06:21:40.000000000 +01:00
categories:
- game design
- sol trader
- game development
- kickstarter
redirect_from:
- "/2015/09/gossip-as-a-game-mechanic"
---
I'm now in the final stages of getting a playable demo out to beta testers (if you'd like to join the waiting list, you can [sign up on the forums](http://forums.soltrader.net)). I'm busy cramming in the final few things to make the demo as complete and as fun as possible.

I've done all my development on OSX for the last few months, so last week I put together a Windows version: thankfully it only took about four hours, due to both using SDL2 and to [splitting the game code from the platform layer](/2015/08/how-to-add-live-code-reload-to-your-game/). I've also just implemented the code that allows players to talk about another person in the game, and I want to briefly discuss how it works.

## The power of gossip

I wrote in June about how [Sol Trader](http://soltrader.net) uses [information as a form of currency](/2015/06/how-sol-trader-uses-information-as-currency/) in order to help the player advance. The power of gossip to spread rumour and information is known to us all, and it seemed to me the best way to allow players to gain information about others.

![Screenshot showing gossip about another](/assets/img/sol-trader-gossip.png)

<p style='color: #999'>When chatting to Amos, he started talking about Orville Averill. We can now press for more information, or try and find out where he is.</p>

As players chat to various characters, other people will come up in conversation. We can either choose to change the subject, or press them for information about that person. The AI tracks when each character was last seen by that person as well, so asking the right questions can help players track down difficult to find characters to complete certain missions.

Each conversation has a certain amount of patience attached to it - that's what the little blue circles are in the screenshot. Asking questions 'spends' patience, which means that after a while we won't get anything else out of a character and will need to come back later. The better we know someone, the more questions we can ask, and the better information we'll get.

## How to gain information effectively

In playtesting this has thrown up some suprising effects. For example, often the best people to get information from are those in prison: they have plenty of time on their hands and often know a lot of different types of characters:

![Screenshot showing chatting to prisoner](/assets/img/sol-trader-chat-prisoner.png)

<p style='color: #999'>Prisoners are often the best source of information about people, and they have plenty of time on their hands to chat.</p>

People in prison usually don't know where characters are though. For that we're best off talking to bar staff, as they might have seen characters come in to socialise. Making friends with hotel receptionists will give us good information about people who travel a lot, and spaceport staff will often have seen characters passing through.

Barring any last minute issues, the demo should be out on the 22nd on the same day as the new Kickstarter launches, so you will soon be able to try it for yourself!
