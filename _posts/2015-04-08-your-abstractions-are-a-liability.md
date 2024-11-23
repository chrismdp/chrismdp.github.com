---
layout: post
title: Your abstractions are a liability
date: 2015-04-08 14:04:44.000000000 +01:00
categories:
- code
- c++
- object oriented
- game development
- refactoring
- state
- functional programming
- liability
redirect_from:
- "/2015/04/your-abstractions-are-a-liability"
- "/2015/04/your-abstractions-are-a-liability/"
---
{% include callout.html color="#d9edf7" text="\"If a function is only called from a single place, consider inlining it.\"


-- John Carmack, maker of Doom & Quake" %}

Your abstractions are a liability.

Often we jump to an abstraction in our code because it seems 'obvious' or just seems to fit our understanding of our domain. We want to make our code 'clean', so we look hard for ways to remove duplication and 'code smells'.

As our codebase grows, our abstractions often pass their sell-by date, yet they persist as we attempt to work around them. Removing bad or redundant abstractions as our understanding of our codebase grows is essential.

As an example, consider this simplified game loop. This is pretty much how the [Sol Trader](http://soltrader.net) inner loop worked until about a week ago.

{% highlight c++ %}

    class Game {
      bool _running;
      Music music;

      void init() {
        _running = false;
        music.init();
      }

      void run() {
        init();
        while(_running) {
          update();
          draw();
        }
        cleanup();
      }

      void cleanup() {
        music.cleanup();
      }
    };

{% endhighlight %}

(I've placed the methods within the class definition for brevity, but in C++ they would probably be in a different file. This is important.)

The problem is that the scope of `_running` is propagated further than it should be. It's possible to stop the game loop running from both the `update()` and `draw()` methods: in fact, anywhere in the `Game` class at all. It's also not clear what the designer of this class intended the behaviour to be. Where exactly should `_running` be updated?

With a large and complex set of methods (initializing and tearing down a modern
game is no small feat) then the `_running` could potentially be set from a
large number of places - and perhaps set and set again during the same frame!

Just because a variable is private doesn't save you from a large class giving
access to that variable to many code paths.

## Inlining variables

Let's remove the `_running` member variable and use a local variable instead:

{% highlight c++ %}

    class Game {
      Music music;
      void init() {
        music.init();
      }

      void run() {
        init();
        bool running = true;
        while(running) {
          running = update();
          draw();
        }
        cleanup();
      }

      void cleanup() {
        music.cleanup();
      }
    };

{% endhighlight %}

By moving `_running` into a local variable within the `run()` method, we've stopped the state propagating throughout the class instance, and encapsulated the running logic where it belongs. It's also clear now that the `update()` method should decide when the game stops running, and that the we should draw the final frame before we quit.

## Inlining methods

You can take this further and inline the other objects:

{% highlight c++ %}

    class Game {
      void run() {
        Music music;
        music.init();
        bool running = true;
        while(running) {
          running = update();
          draw();
        }
        music.cleanup();
      }
    };

{% endhighlight %}

The real problem has now become evident. It is an insufficient understanding of Object Oriented programming - namely putting everything into noun-based objects such as `Game`. It turns out there's not actually useful game abstraction here - we are better off with a simple `run()` method. Functional programming, anyone?

It seems simple, but the amount of code I've been able to simplify with this two techniques is astonishing. I do end up with longer methods, but by collapsing unnecessary abstractions the code becomes more straightforward and clearer.

## Summary

Removing useless abstractions by inlining methods and variables where appropriate helps us to see where the real seams of our code are. It helps us to pick apart unhelpful or mistakenly classified objects and leads us to a better understanding of OO.

The wrong abstraction is (far) worse than no abstraction at all.
