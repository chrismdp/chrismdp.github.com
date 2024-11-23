---
layout: post
title: How not to check in temporary code
date: 2014-07-08 16:53:34.000000000 +01:00
categories:
- code
- refactoring
- bdd
redirect_from:
- "/2014/07/how-not-to-check-in-temporary-code"
- "/2014/07/how-not-to-check-in-temporary-code/"
---
[![facepalm](http://chrismdp.com/files/facepalm.jpg)](https://www.flickr.com/photos/brandongrasley/8227882239)

We've all done it.

We were skimming through a set of changes before checking in our code, trying to get the branch pushed up to the build server just before lunch. We'd forgotten that before we went home last night, we added a couple of lines of code to a method which sets up a debug state for testing. Easy to miss; and miss it we did. The change goes up, the build breaks, and we're left feeling embarrassed.

How do we ensure we don't check in temporary code? One way to do so is to utilise that old refactoring staple, *Extract Method*, along with the [power of good naming](/2012/09/the-power-of-good-naming).

# Pull out temporary code into a method

Here's some temporary code currently nestled inside the [Card Pirates](http://cardpirates.com) method for starting a new game. It fixes the position and the cards for the first two players, so I can easily jump to and test the combat user interface.

{% highlight ruby %}

    def start_new_game
      @state = GameState.new_game(@queue)

      attacker = state.players.current_player
      defender = state.players.next_player

      attacker.x = 3
      attacker.y = 3
      attacker.hand = Card.hydrate ["10_of_england", "4_of_spain", "3_of_france"]

      defender.x = 4
      defender.y = 3
      defender.hand = Card.hydrate ["8_of_england", "3_of_spain"]
      state.map.square(4, 3).face_down_cards = []

      init_services(@state.current_player.name)

      @queue << Command.new(:start_game)
      @queue << Command.new(:start_new_player_turn, @state.current_player.name)
      show_board(@state.current_player.name)
    end

{% endhighlight %}

Can you spot where the temporary code stops, and the 'real code' starts? It's difficult, isn't it? I thought so too, so I extracted the temporary code into a method, and gave it a *very* obvious name:

{% highlight ruby %}

    def test_the_combat_dont_check_in(state)
      attacker = state.players.current_player
      defender = state.players.next_player

      attacker.x = 3
      attacker.y = 3
      attacker.hand = Card.hydrate ["10_of_england", "4_of_spain", "3_of_france"]

      defender.x = 4
      defender.y = 3
      defender.hand = Card.hydrate ["8_of_england", "3_of_spain"]
      state.map.square(4, 3).face_down_cards = []
    end

    def start_new_game
      @state = GameState.new_game(@queue)

      test_the_combat_dont_check_in(@state)

      init_services(@state.current_player.name)

      @queue << Command.new(:start_game)
      @queue << Command.new(:start_new_player_turn, @state.current_player.name)
      show_board(@state.current_player.name)
    end

{% endhighlight %}

This has a number of advantages:

* *It's quick to do.* It only takes a minute to make a change like this, and saves you a lot of headaches later.
* *It's easy to spot in a diff.* It's much harder to get out all the code unless it's clearly encapsulated like this.
* *It's easy to spot for someone else.* If instead of going on a lunch break you were cycling home for the day, a co-worker would probably be able to spot and fix this before you got back online.
* *It might be further refactored later.* These kind of 'put the system in a certain state' methods can actually be useful later - we might be able to use this for a tutorial mode, for example. Temporary code often ends up being much less temporary that we originally envisage.

I've found that small refactorings like this often save me lots of time later. How do you stop yourself checking in the wrong code?
