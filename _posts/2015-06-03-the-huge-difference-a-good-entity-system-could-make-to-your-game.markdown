---
layout: post
title: "The huge difference a good Entity System could make to your game"
date: 2015-06-03 11:17:09 +0100
categories:
  - game design
  - sol trader
  - game development
  - code

---

Continuing a general theme of discussing the nuts and bolts of [Sol Trader's](http://soltrader.net) design, this post is about the huge difference the recent decision to move to an decent Entity System with components has made to the flexibility of the underlying engine.

In case you're not familiar with Entity Systems, I'll summarize briefly why they're important and how they work.

## The problem

Most games have multiple things in them that work in similar but varying ways,
such as players, bullets, walls, trees, weapons, and so on.  The Entity
abstraction is a useful one to encode this -- all things in the game share
basic properties (such as position), but have special behaviour in certain
circumstances.

Here's how Entity systems have often been approached in the past:

{% highlight c++ %}
class Entity {
  int x, y;
};

class Player : public Entity {
...
};

class Monster : public Entity {
...
};
{% endhighlight %}

We have general shared behaviour across all entities stored in the `Entity` superclass, and special case behaviour in the classes underneath it.

After a while, we come up against two different entities that need to have the same behaviour. To solve this, we might attempt to insert a class in the middle of the hierarchy:

{% highlight c++ %}
class Destroyable : public Entity {
  int health;
};

class Player : public Destroyable {
...
};

class Monster : public Destroyable {
...
};

{% endhighlight %}

However, this becomes quickly unworkable. Inheritance hierarchies are fairly rigid, and this increases with complexity. It's not easy or desirable to specify in advance all of the different behaviours that our entity might want to have. If for example we wanted to share two different types of behaviour between two other entities, then we might be stuck at that point.

In theory you could use multiple inheritance, but this is a bad idea. See the [deadly diamond of death](http://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem) if you're not familiar with why this could be a problem. Also these designs can rely on virtual functions to override behaviour, which are [fundamentally slower to execute](/2015/04/how-i-doubled-the-speed-of-my-game-by-giving-up-on-c-plus-plus/#virtual-function-calls-are-slow).

# A solution using components

A way around this problem is to ditch the idea of inheritance entirely (I'd done this already by [switching away from C++ at the beginning of the year](/2015/04/how-i-doubled-the-speed-of-my-game-by-giving-up-on-c-plus-plus)) and instead break up all your entity behaviour into separate components, which are then associated with each other via an ID.

Here's a great diagram of an entity system using components from [Cowboy Programming](http://cowboyprogramming.com/2007/01/05/evolve-your-heirachy/):

[![Entity system diagram](http://cowboyprogramming.com/images/eyh/Fig-2.gif)](http://cowboyprogramming.com/2007/01/05/evolve-your-heirachy/)

In order to code this in C, we just have the following code to represent an entity:

{% highlight c++ %}

struct GameState {
  uint32 nextEntity;
};

uint32 pushEntity(GameState* state) {
  return state->nextEntity++;
};

{% endhighlight %}

That's it! An entity is denoted by a simple counter, and has no data attached to it. All the data lives in the components.

Here's a snippet of the initialisation code from [Sol Trader](http://soltrader.net) for `Human` and `Ship`:

{% highlight c++ %}

// Human
uint32 humanId = pushhuman(state);
pushEventful(state->history, arena, humanId);
pushHistoricalFigure(state->history, arena, humanId);
pushNameable(state, humanId)->type = NAMEABLE_HUMAN;
pushEnterer(state, humanId);

// Ship
uint32 shipId = pushEntity(state);
pushNameable(state, shipId)->type = NAMEABLE_SHIP;
pushRenderable(state, arena, shipId);
pushEnterer(state, arena, shipId);

{% endhighlight %}

Here I've listed a few of the components in [Sol Trader's](http://soltrader.net) current system:

* *Eventful:* Attach this component to entities which can have historical events (currently humans and organisations.)
* *HistoricalFigure:* Attach for an entity with a human-like history. Only used for humans.
* *Nameable:* Attach to entities with names. This component has different types depending on how it is being displayed. All `Nameable` entities can can be renamed by the player, allowing them to customise the names of lots of different things in the system. Used for humans, organisations, ships and homes.
* *Enterer:* Attached if an entity is allowed inside an entity with the `Enterable` component.

It's now trivial for several entities to share the same component, which hits on one key advantage: re-usability.

If you're interested in more, then this [blog post series](http://t-machine.org/index.php/2007/09/03/entity-systems-are-the-future-of-mmog-development-part-1/) does a pretty good job of explaining the above in more detail.

## Why this is so important

The cost of development is a huge barrier to quickly prototype new ideas for our games. Anything we can do to bring this down allows us to try more ideas and [get to 'fun' as quickly as we can.](/2015/04/how-to-choose-between-realism-and-fun/) The longer it takes to build a new type of entity, the slower the prototyping of new ideas.

It's so much easier to prototype with entity systems: you can much more easily reuse behaviour between components. Here are some advantages I've discovered in just the last two weeks:

* *Added `Nameable` to ships meant customisation for free.* It's really important to me that the players can rename lots of different things in the game. Previously I would have had to spend ages refactoring the naming code to make it usable across entities. By spending about 45 minutes implementing `Nameable` for ships, I got customisation for free.

* *Adding landed ships to the GUI took less than 20 minutes.* I simply reused the `Enterer` component for ships, and because they were also `Nameable` they simply popped up on the GUI in the list of people. After straightening out a few assumptions in the GUI that all `Enterer` entities also had `HistoricalFigure`, the game was back up and running.

* *Adding homes for humans took about 2 hours.* I wanted to try the idea of humans all having their own homes visible on the planet GUI. Up until now, this was implemented via a simple flag. Adding new entities for homes with a few components on game start caused them to pop up in the GUI immediately. Seeing the human homes on the GUI felt great - but if it hadn't been so easy to add, I might not have attempted it. It also allowed me to delete a stack of special-case movement code. Wonderful.

* *Components save memory.* Previously to create a human in history generation meant you had to store all the data the human could possibly need, even though many humans would die before the game began. With an entity system, I could only add the component I needed for generation, and add the rest of the components to humans that survived to the game start. This also speeds the generation up: the history generator now iterates through less data allowing more efficient use of the memory cache.

I can't imagine building another game without a decent Entity System. It's transformed my prototyping speed and is very extensible. There are a few disadvantages, but they pale in comparison to the benefits.

How do you organise your Entities? Do you use a similar system?
