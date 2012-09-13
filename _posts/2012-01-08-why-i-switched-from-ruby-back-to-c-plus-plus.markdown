---
layout: post
title: "Why I switched from Ruby back to C++"
date: 2012-01-08 20:21:41 +0000
categories:
  - products
  - ruby
  - c++
  - code
  - sol trader
  - game development

---
<div class='notice'>
  <b>UPDATE:</b> This post was pretty popular. I've posted a followup <a href="/2012/01/switching-sol-trader-from-ruby-to-c-plus-plus-one-week-on/">here</a>.
</div>

After two months of Sol Trader development in Ruby, I took a difficult decision last Wednesday morning: I've decided to rewrite the game code from scratch in C++. Let me explain my reasons.

<div class='notice'>
  If you'd like to purchase Sol Trader you can now do so at <a href='http://soltrader.net'>soltrader.net</a>!
</div>

## Why I did it

* *Slow frames:* When working with Ruby, I use the excellent [Gosu](https://github.com/jlnr/gosu) library to do all my game specific coding. This initially worked great, but occasionally I'd just get slow frames coming up. My game is timed to run at 60 frames per second, which means that each frame should take no more than 16.67ms to run. Yet every so often my profiling would come up with a frame that would take 25ms or 45ms for no discernible reason. I just couldn't find the issue here: I turned every sub system in the game off. I disabled garbage collection. I hacked my slow frame detection code into the simplest gosu sample I could find, and they still existed. I didn't feel like I could quite trust the stack to deliver the framerate I needed, and I hadn't yet put in half the features I wanted to.

* *Object explosion when bridging to C:* A lot of the libraries I was using were written in C, and therefore there was several thousand objects (mostly floats) being created each frame to act as a bridge between Ruby and C code. It feels like that that CPU time should be better spent in the AI improving the quality of the simulation, or on better effects, rather than loading the garbage collection with an unnecessary burden.

* *Ease of packaging and distribution:* I feel like packaging is going to be a lot easier. I'm not too bothered about hiding the source code: I may well do that anyway to purchasers of the game. It's the running on Windows I'm worried about: from my research it feels like it's going to take some effort to push the game out on a non-Unix platform. And with a video game, releasing on Windows is a must.

* *Manual memory management for performance:* The garbage collection is still too stuttery under MRI (even with Ruby 1.9.3, which is a huge improvement on what's gone before) - it still stops the world each time. I looked at other implementations, and even considered learning all about garbage collection to help improve Ruby myself, but then realised that getting royally distracted wouldn't help me ship a working game.

## What do I miss about Ruby?

* *I miss using RSpec hugely:* There are ways of doing [testing of C programs using RSpec](http://benmabey.com/2007/09/09/bdd-your-c.html) but it doesn't feel like I want to wrap each of my C++ classes with a SWIG interface just to check they're working. I may still do this for some form of Cucumber testing, I'm not sure. I'm using [UnitTest++](http://unittest-cpp.sourceforge.net/) for my testing at the moment, which is very lightweight and good enough for my purposes.

* *Duck-typing:* defining interfaces for everything is a pain in the backside, although it does force you to think more clearly about the roles of your classes.


* *Easy mockist testing:* There's no built in reflection in C++ so it also makes you have to code to interfaces if you want to do any mockist testing. I'm mostly returning to a classist style of testing with small well defined groups of classes being tested at once. It's not a perfect system and I still have much learning to do here.

* *Terseness of syntax:* There's just a lot more characters to type, and a lot more ceremony for each class. This tempts you to larger classes and methods, which I'm resisting at the moment. I need to take the time to set up [c.vim](http://www.vim.org/scripts/script.php?script_id=213) exactly how I want it.

Funnily enough, I don't miss the automatic memory management: I like having that level of control. Old habits die hard.

## So how far have I got?

Thankfully, it's not a complete rewrite as I'd already done a lot of thinking about the architecture and a lot of the basic classes translate directly over.  I worked really hard at the end of last week and got a lot done:

* I put in [SDL](http://www.libsdl.org) to build the basic game framework: hopefully building on Windows will be a snap. I plan to have a working Windows build as soon as I can lay my hands on a cheap Windows 7 PC.
* Basic testing using UnitTest++, with tests that are compiled and run as part of the build process.
* Decoupled gameplay/physics updates from the graphical framerate using the techniques [here](http://gafferongames.com/game-physics/fix-your-timestep/). I have zero [temporal aliasing](http://en.wikipedia.org/wiki/Temporal_anti-aliasing) bugs right now, which makes for a super smooth 300+ FPS graphic loop with a fixed 60FPS physics loop.
* Re-implemented physics using [Chipmunk](http://chipmunk-physics.net/), the same library I used in Ruby, which made it very easy to switch over.
* Put in a brand new and much improved parallax-scrolled starfield.
* Added a basic controllable spacecraft, planets and jumpgates back in: the player can fly around as before and collide successfully with other objects.
* A simple particle system so the spacecraft give off exhaust smoke, and the jumpgates emit spooky purple mist.

Even with using OpenGL [immediate mode](http://en.wikibooks.org/wiki/OpenGL_Programming/GLStart/Tut3#Immediate_Mode) (this is a bad thing) and rendering 10000 stars each frame (very inefficient), and a throwing bunch of particles onscreen, I'm still getting 300+ FPS on my 2009 MacbookPro and only using 30MB of memory. That's satisfying.

*UPDATE:* By (very) popular demand, here's a screenshot. Be aware this is *three days work only*, and obviously not final artwork:

<a href='/files/sol-trader-1.png'><img src='/files/sol-trader-1.png' width='500'/></a>

Next I plan to add back in jumping between different planetary orbits, and then work on a very basic 'person-level view', so that you can get out of your ship and walk around.

## Was it the right decision?

I'll know at the end of the project :) My feeling is though that it was the correct thing to do. Being really close to the metal will make it much easier to implement some of the really complex AI stuff I'd like to do later on. I already know C++ very well, and estimate it'll only delay me a week or two if I work hard. If I like, I can always bundle my project as a C++ library and control it from Ruby later on, but it's harder to go in the other direction.

What do you think? Did I make the right call?

<div class='notice'>
  If you'd like to purchase Sol Trader you can now do so at <a href='http://soltrader.net'>soltrader.net</a>!
</div>
