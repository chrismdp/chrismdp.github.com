---
layout: post
title: "7 things I've learnt in 3 years coding my first indie game"
date: 2015-01-07 14:26:40 +0000
categories:
  - sol trader
  - code
  - business
  - kickstarter
  - game development

---

[![header](/files/sol-press-header.png)](http://kck.st/1Ap3Wf8)

Sol Trader is at the end of Alpha and is [now on Kickstarter](http://kck.st/1Ap3Wf8) to raise funds for completion. Here are the seven biggest lessons I've learnt in the three years of coding my first indie title.

## 1. Pick the right platform

When I started back in late 2011, I thought I'd try and make the game in Ruby. Unfortunately, despite it being my language of choice for development up until then, I discovered that's one of the worst platforms to build a game in.

My main reason wasn't lack of support for games libraries, or the lack of a community: it's that the garbage collector in Ruby can sometimes take an entire frame's worth of time to run. This leads to horribly stuttery framerates. I feel like garbage collection in general doesn't belong in games at all.

In Jan 2012, I decided to take control. I moved back to working in C/C++, which is where I started my career in 2000. I wrote a post about it that [caused rather a stir](http://chrismdp.com/2012/01/why-i-switched-from-ruby-back-to-c-plus-plus). I have never regretted the decision.

## 2. Pick the right architecture

As a former AAA games developer, I thought I knew how to write and structure C++ games. I ploughed in with a big entity inheritance hierarchy and lots of classes. In doing so, I immediately and unknowingly gave up control of my memory layout and the frequency I accessed it. Memory is much slower than you might realised, so this made inner loops much harder to optimise and causes 'general slowness' in the engine which is hard to get rid of.

Unfortunately my ideas for how to do game development were a decade out of date - I should have paid clearer attention to current trends and things like data-oriented design. I should have either stuck to using someone else's engine such as Unity, where a lot of the optimisations and porting comes for free, or thought and read a lot more carefully about architecture up front.

Having a well organised memory layout also leads to another advantage: serialisation comes pretty much for free. All you do is save a chunk of memory to disk, rather than writing thousands of lines of code walking through your entire object hierarchy and saving them all carefully, which is what I'm doing now.

If I was to do it again, I think I'd still write my own engine but stick to C almost entirely, coding in a very functional way where possible, without much C++ at all. In short, I'd take the approach exemplified by [Casey from Handmade Hero](http://handmadehero.org). If you haven't seen his video series, I'd strongly recommend you check it out - he's writing an entire professional quality game from scratch in C without libraries and with full explanations. Very impressive and highly worth a watch.

## 3. Don't go overboard on libraries

When you write your own game in C/C++, you want to be in control. I ended up using lots of libraries (around 15 or so) to get all the various things like GUI, physics, sound, network access, TrueType fonts, serialisation, ZIP compression and PNG support... oh, and Boost for signals, pathfinding... The list goes on.

Libraries do often save you time, but every library you use is something else that you have to learn how to use, compile on all your platforms and deal with all the platform specific bugs that come up. There's quite a lot of overhead in keeping them all working.

Libraries also slow down your compilation, especially highly clever templating/C++ style libraries such as Boost. I think Boost is a monumental achievement, but I won't be using it on my next game project. I've learnt that compilation speed is everything.

There are some libraries you want to use. I'm pleased I went with SDL and OpenGL, although in hindsight I'd have done the architecture differently to make porting easier. I'd use well supported libraries like FreeType and Curl again, but I'd avoid libraries that aren't kept up to date or don't have a strong userbase.

In short, I should have written a lot more of the code myself. The amount of time I've had to work around annoying bugs in libraries, or the weird way they choose to use memory, I'd have been better writing the small amount of functionality I needed myself.

## 4. Port late, not early

I used Mac as my primary development environment for most of Sol Trader's development, but I ported Sol Trader to Windows really early - around 2.5 years ago. Most people who bought Alpha access downloaded and played the game on Windows, but the Windows version was always inferior to the Mac version and still requires a lot of work to get all the libraries compiled and the platform-specific bugs out.

Porting to multiple platforms is like Internationalisation. You plan for it, but do it as late as possible. As soon as you introduce another platform, the maintenance requirements for your app jump - depending on how you've architected it, they can jump by a huge amount.

In hindsight, I should have coded the game exclusively on one platform first, architecting it in such a way as to keep all the platform specific code together as much as possible, and aggressively reducing my dependence on lots of little libraries. Again, engines like Unity make a lot of this legwork go away - either use one, or aggressively code to make this part of your project as painless as possible.

## 5. Use a simple build system, with live code editing

My build system is impressive. I'm pleased with myself for still being able to understand it. This is a bad sign. It is also hilariously complex (hilarious for you, not for me.) There are a huge number of asset generation steps and scripts to mangle names and handle dependencies. It's tricky to worth with, to say the least.

If approaching it again, I'd become a *lot* more careful with build steps and cut out any need for dependency management. It's not that hard to build a unity build system using a simple script file that can compile the game code and relink it using DyLibs or DLLs, *whilst the rest of your code is running.* This does away for the need for a scripting library for fast code editing: if building and reloading your C code takes less than a second, and the only person needing to write script code is you, why bother?

## 6. Make it fun to play, not fun to code!

It sounds obvious, but when you're coding on your own the design decisions you make can be unduly influenced by how fun your game is to *make*, rather than to *play*. It doesn't matter if your game doesn't have the latest features or that they aren't completely real-world accurate. What matter is that it's fun to play and experience.

I learnt this the hard way on Sol Trader. I coded a lot of systems that were 'accurate simulations', but simply not fun. I was effectively simulating the environment, but not honing great player experiences.

The big example in Sol Trader was the market code. I spend a good long time at the beginning of the project making a fully simulated market, with buy and sell orders, and realistically fluctuating prices. When I released it, all pleased with myself, I got lots of complaints from early players about how difficult it was to trade at planets. I kept tweaking it, but the results were the same.

In the end, I realised that this was because I was writing something that was fun to code, not fun to play. The code looked impressive but it was a chore to interact with. In the end I ripped it out, replacing 5,000 lines of carefully crafted boring experience with a couple of evenings worth of code that plays fluidly and isn't a frustrating chore.

A game is meant to be played, not admired. There's a big difference.

## 7. Keep going

I took six months off Sol Trader in 2013, telling almost no-one. I took the time to build a web prototype to test some ideas, but really it was because I was burnt out working on it after 18 months. Games are hard, and finishing them feels almost impossible.

I picked it up again in November after some encouragement from friends, and am so glad that I did and got it this far. The code looks awful to me now, especially the early code, but if you don't look at your old code with disdain you've stopped learning and growing as a developer. I'm resisting the urge to rewrite everything and focusing on doing what I need to do to get it out the door and into your hands!

## Summary

There's a common theme here:

**Write the game so others will enjoy playing it, not so you'll enjoy making it. This is harder, but ultimately the satisfaction payoff is much, much bigger.**

<div class='alert alert-info'>

Don't forget: Sol Trader is <a href='http://kck.st/1Ap3Wf8'>now on Kickstarter</a> - back it and join the adventure!

</div>
