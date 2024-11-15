---
layout: post
title: Sol Trader combat preview
date: 2015-11-11 17:03:57.000000000 +00:00
categories:
- indie games
- game design
- game development
- sol trader
- code
redirect_from:
- "/2015/11/sol-trader-combat"
---
Since the [Kickstarter was successfully funded last month](https://www.kickstarter.com/projects/chrismdp/sol-trader), I've been working hard the next major feature: combat!

Here's a short video showing progress so far. If you're on the beta of the game, head over to the [forums](http://forums.soltrader.net) - you can grab a new copy of the game today and start shooting things for yourself! (There's [still time to jump on the beta](http://soltrader.net/back-us) if you aren't already...)

<div class='embed-responsive embed-responsive-16by9'>
  <iframe allowfullscreen src="http://www.youtube.com/embed/236qzaAvgCk"></iframe>
</div>
<br/>

Since the Kickstarter finished, I've added sound effects and explosions, and I've done a lot of work under the hood on the [entity component system](/2015/06/the-huge-difference-a-good-entity-system-could-make-to-your-game/) to allow the to removal of components from entities.

This was fiddly as I had to change the implementation of some of my fundamental low level data structures in order to support fast removal. It's worth it, though. Now when a ship blows up, I simply remove the components that made it a physical thing (Spatial, PhysicalObject, Renderable, Enterable, etc) and leave the components for its logical existence (Ownable, Nameable, etc) so that characters don't forget about it.

I've also added the basics of 'bad' events when combat takes place. When a ship is destroyed, the game kills everyone who happened to be on the ship, and adds 'killed' events for them, blaming the pilot of the attacking ship. These events will come back to haunt the attackers in future, as word gets around about who is responsible...

Lastly, I've added the first draft of the inevitable "game over" screen, with a Rogue-like throwback style :) This one is a work in progress and will get more interesting later on:

![Game over](http://i.imgur.com/EpKO2aN.png)

If you're the kind of person who likes to get the up-to-the-minute news on development, and doesn't mind lots of detail, you can see the latest development notes on [our Trello board](https://trello.com/b/kApDLQ8t/sol-trader-dev). You can even comment and vote on cards - I welcome any feedback!
