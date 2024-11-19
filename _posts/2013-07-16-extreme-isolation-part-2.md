---
layout: post
title: 'Extreme isolation part 2: separate the domain from the changes'
date: 2013-07-16 09:37:39.000000000 +01:00
categories:
- ruby
- state
- craftsmanship
- refactoring
- sol trader
- code
- cucumber
- testing
- extreme isolation
redirect_from:
- "/2013/07/extreme-isolation-part-2"
---
I started a few months ago looking at a fresh way of architecting web applications. Since writing the first article in this [series](http://chrismdp.com/tag/extreme%20isolation) I've extended the codebase considerably and have a few more thoughts on how to take these ideas further. If you've not read it already, you probably want to go back and read the [previous article](http://chrismdp.com/2013/05/extreme-isolation-in-web-apps-part-1) first.

This time round, I discuss how I reduced the codebase dramatically by separating the full updating of the domain from the generation of change information. This refactor stemmed from two problems I had spotted in my code: an observation that some of my methods were doing too much, and the need for wrapper methods to preserve immutability.

## Problem 1: methods doing too much

In [Sol Trader: Online](https://online.soltrader.net), each player has a `Position` within the game. I'm using the word "position" in the same way you'd talk about a chess position: it's the state of the players involvement in the game.

In the previous article I was doing two things within each method in the domain that performed an action for game `Position`.

1. Returning a new copy of the domain object modified to reflect the change
2. Pushing a new object onto the `changes` array

For example, this particular method on a player's `Position` allowed them to attack a target:

{% highlight ruby %}

    class Position
      def attack(target, changes)
        new_position = with_order(AttackOrder.new(target))
        changes << CharacterOrderedToAttack.new(new_position)
        new_position
      end
    end

{% endhighlight %}

As well as calling `with_order` to create and return a new `Position` with an `AttackOrder`, I'm creating a `CharacterOrderedToAttack` change, adding the new position to it, and adding that to the `changes` array.

## Problem 2: container objects needing wrapper methods

This was problematic enough, but it was exacerbated by the fact that the position was only one of a list of positions within a `Game` object, so in order to keep the `Game` immutable, I had to have a `Game#attack` method to wrap the new position returned within a new game, using code something like this:

{% highlight ruby %}

    class Game
      def attack(position, target, changes)
        self.class.new(positions.map do |current_position|
          if current_position == position
            position.attack(target, changes)
          else
            current_position
          end
        end)
      end
    end

{% endhighlight %}

I abstracted much of this out to helper methods, but I was deeply unhappy about having to have a method on the `Game` object for each action I could apply to `Position`.

## A mistaken assumption: that I actually need this object

The reason for writing all this code to return a new copy of the object with the changes applied rested on the assumption that I was actually going to need this object to finish processing the request.

After a close look at the calling code in the web logic, it turns out that I didn't need it at all - I only ever operated on the changes that were returned in the array. Therefore, why was I bothering to generate it?

{% highlight ruby %}

    post "/attack/:target" do |target|
      changes = []
      new_game = game.attack(current_position, target, changes)
      GameRepository.apply(changes)
      WebResponder.apply(changes)
      # new_game is never used!
    end

{% endhighlight %}

If I don't bother to return the updated game object, I can reduce the code for the `attack` method to a one-liner which simply returns a change. Now my domain logic was back to just doing one thing:

{% highlight ruby %}

    def attack(target, changes)
      CharacterOrderedToAttack.new(with_order(AttackOrder.new(target))
    end

{% endhighlight %}

I didn't then need `Game#attack` at all, so that method could be safely deleted.

This one insight, when propagated through the system for all the existing actions, reduced the size of the codebase by about 10%.

In making this change, I've moved entirely to a version of the [Command Query Reponsibility Segregation (CQRS)](http://martinfowler.com/bliki/CQRS.html) pattern. My regular domain is entirely read only, and only used for querying the data, and my domain for updating the model is based on lightweight change objects, which are passed to services to update persistence and handle web requests.

## Next time

Changes can cause other changes: Next time, I plan to talk about how I'm feeding changes back into other services, to allow reactions to certain behaviour.
