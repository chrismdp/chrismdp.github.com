---
layout: post
title: "The Sol Trader Christmas Eve update: moddable missions"
date: 2015-12-24 07:43:19 +0000
categories:
  - indie games
  - game design
  - game development
  - sol trader
  - code

---

The relative radio silence from Sol Trader Towers is for a reason: I've been working hard on a flexible and moddable mission structure, that allows players to take a variety of interesting quests in-game.

This build is now available [on the forums](http://forums.soltrader.net) should you have access ([there's still time if you don't](http://soltrader.net/back-us).)

![kill mission](http://i.imgur.com/x08Gprc.png)

I've built a few missions to start with, including delivering parcels for business or personal reasons, taking characters to on business trips and making other characters disappear. It's great fun to have a variety of things to do for characters now and adds yet more colour to the game. Because it's completely moddable, I'm also excited to see what storylines other people come up with!

## Under the hood

The full details of how to create your own missions are [available as a lengthy forum post](http://forums.soltrader.net/post/modding-mission-data-structures-7846221?pid=1290228731#post1290228731), which will be kept up to date with changes and clarifications. Here's an overview:

The missions are organised into packs, which exists under the `data/missions` subfolder. If you have access to the beta builds, you'll see there's one pack there already: these are the missions that are built in to the game.

There are several csv files in each mission folder:

* `requirements.csv`: This file details the cases in which this mission might be triggered. Each character in the game has a chance of picking this mission (and becoming the 'giver' of the mission), based on the conditions imposed by this file.
* `conversation_player.csv`: The extra conversation options available to the player because of this mission.
* `conversation_ai_response.csv`: The extra options the AI can choose from as conversation responses.
* `opinions.csv`: The extra opinion triggers, used for reactions to the generation and completion of these missions.
* `strings.csv`: The new strings needed for the previous CSV files.

The possibilities for you to build your own missions are expanding all the time, as I add new missions triggers and possible goals for the AI.

![business trip](http://i.imgur.com/G4WjgFP.png)

# What's next?

At the moment it's possible to take on any mission from any person, which isn't very realistic. I need to allow players to gain other character's trust, so that they will only give you sensitive missions in certain cases. Additionally [it will soon be possible to start a career with an organisation](https://trello.com/c/Kvjzaeqb/196-organisation-rank-careers), which will give you a rank, a certain amount of built in trust, and access to more senior characters.

I'm also [going to be working on the in-space AI](https://trello.com/c/LgVsT5xN/227-space-ai) very soon. At the moment only freelance traders fly around between planets: it's time we had passenger ships, military guards and pirates thrown into the mix.

Have a fantastic Christmas and I'll see you all in the new year with some more updates.
