---
layout: post
title: "Why I wrote Sol Trader's GUI code from scratch"
date: 2015-08-01 23:25:02 +0100
categories:
  - sol trader
  - game development
  - code
  - c++

---

<div style='float: right; padding: 0 0 10px 20px; width: 250px'><a href="http://imgur.com/2gwzvYN"><img src="http://i.imgur.com/2gwzvYN.png" title="source: imgur.com"/></a>
<div style='color: #999; padding: 0px 0 0 15px'>The new rewritten GUI in action.</div></div>

A decision to rework a major piece of infrastructure late on in a game's development is pretty significant. It's especially so if we're replacing it with our own code written from scratch.

Yet about a month back, after plenty of profiling, I took the decision to remove the GUI library I was using from Sol Trader's codebase and replaced it with my own.

The library I was using, [libRocket](http://librocket.com), has many useful features and it got me a long way during the game's prototyping stage. It is however written in C++ and extensively uses a large class inheritance tree with lots of virtual methods. I've written before about how this can [potentially be a speed problem](/2015/04/how-i-doubled-the-speed-of-my-game-by-giving-up-on-c-plus-plus/), and it turns out through profiling that this was indeed the case for my game. Because parts of the game are very GUI heavy, these performance problems surfaced quite quickly after building the final interface structure for city mode.

So, on 1st July, I set out to write a minimal GUI as quickly as possible, whilst at the same time reskinning the prototype GUI I had with the new look and feel. It took about 60 hours to both write the GUI infrastructure and reskin the interface. In that time I also implemented live code editing, revamped the asset system and vastly improved the efficiency of the renderer.

Here are a few reasons I went with the "from scratch" route rather than using different library:

## Compilation speed is faster

I've been [heavily influenced by Casey Muratori's no-libraries approach](/2015/01/seven-things-i-ve-learnt-in-3-years-coding-my-first-indie-game/) to writing video games. Avoiding libraries really does shorten the debug loop. By pulling out the last major library and its dependencies, I doubled the build speed of the game.

The new Sol Trader coder is leaner and meaner that it has ever been: all 12,000 lines of code now compiles in under a second and updates the running game live.

## I can write the minimum code I need

The current GUI that my game needs is around 1,000 lines of C code. I don't need anything fancy and it doesn't need to be made general purpose: it only has to work for what I need. By cutting out extraneous code I can keep complexity and code size right down to the minimum.

## I gain architectural homogeneity

This is a fancy way of saying "the game code fits together well." Now I'm writing my own GUI code I can create exactly the interfaces that the rest of the game wants to use. I can also build it with my own game's constraints in mind: because of the way space travel looks on screen, a good frame rate is essential.

## Summary: Is the "Not Invented Here" principle overrated?

In hindsight, I definitely made the right decision. Build speed is so important because the shorter our debug loop the faster we can [iterate towards fun](/2015/04/how-to-choose-between-realism-and-fun/). Writing my own tiny GUI library within my game has meant that now there are no external barriers to a smooth frame rate.

I can now understand why there aren't that many well established game GUI libraries out there. It's relatively easy to write just enough GUI for what we need, and relatively difficult to write enough GUI so that everyone can use it.

I think "Not Invented Here" is overrated. As developers we're often tempted to reinvent the wheel, and often that's unnecessary. However, as long as we understand the concepts, sometimes it's ok to rewrite the code without resolving the problem. Perhaps we need to focus more on not reinventing concepts and less on not rewriting code.
