---
layout: post
title: Driving out feature ambiguity
date: 2010-01-15 06:19:00.000000000 +00:00
categories:
- cucumber
- apprenticeship
- craftsmanship
- ambiguity
- katas
redirect_from:
- "/2010/01/driving-out-feature-ambiguity"
---
[Cucumber](http://cukes.info) features are very useful. The ability to spec out what the customer wants in detail in a format they can read and understand really helps to communicatate what needs to be done. This combined with the ability to execute the feature to ensure that it is completed correctly catches many bugs and incorrect assumptions.

However there is one area of bugs that features don't catch so well, and even cause to some extent. These bugs are built right into the text in the form of ambiguity, sometimes through the constraint of features being executable.

This came up recently in a conversation with [James](http://ohthatjames.github.com) and [Enrique](http://ecomba.github.com/) at [Eden Development](http://edendevelopment.co.uk) about James' apprentice task, the [Snakes and Ladders Kata](/2009/12/snakes-and-ladders-kata). It turns out that the text of one of the features runs against the commonly understood way that Snakes and Ladders works:

{% highlight text %}
Scenario: Win the game
    Given player 1 is on position 97
    And player 1 rolls 3
    Then player 1 has won the game
{% endhighlight %}

Question: is that a valid scenario? Given the commonly understand rules of Snakes and Ladders, you cannot just start on position 97. Implementing it as written complicates the domain model. 

How do you implement the first step? Do you go for a simple:

{% highlight ruby %}
Given /^player (.*?) is on position (.*?)$/ do |player, position|
  @game.set_player_position(player, position)
end
{% endhighlight %}

The potential issue with this is that you are exposing a method that in real life won't get called, just to set up a test. It's also tying your model down to a particular structure, by implying that the game stores an arbitraty position variable for a player. This might not be the best way to model the problem.

The other option is to change the scenario such that the "Win the game" is tested in a similar way to the following:

{% highlight text %}
Scenario: Win the game
    Given a game is started with two players
    And the following dice are rolled:
      |3|
      |4|
      |5|
      |5|
      (etc.)
    Then player 1 has won the game
{% endhighlight %}

That satisfies our understand of Snakes and Ladders, and gives us more freedom in our domain model. In this case, we simply modify the agreed scenario in the code and sidestep the problem.

Right? *Wrong.*

The important thing to remember is that the customer is always right about how the software should behave, even when it violates our commonly understood assumptions about the world. The software they want you to build might require a different implementation of Snakes and Ladders. They might have a 3 year-old daughter they're planning to play the game with, who always wants to be given a headstart. In this case, we've not delivered what they want, simply because it makes life easier for us. We've let our assumptions and our concerns for good design drive out the features, rather than letting the features drive our design.

There's another possibility: when the customer wrote this scenario, they simply used "starts on position X" as a shortcut and don't really care if it's possible to do this in real life. In this case, we can work with them to write the scenario so as not to cheapen our design for the sake of easier feature writing.

*The key insight: there's no way that we can know which it is from reading the scenario. We have to ask the customer and drive out the ambiguity in the feature.*

We mustn't let the necessary constraints of executable features build ambiguity into your conversations about what the customer really wants. And we must be constantly talking to the customer all the way through the iteration, especially if they're not on site.

You might think "It's only Snakes and Ladders, what does it matter?" It matters a great deal: situations like this come up regularly in real life projects. Practising how to deal with these issues and the conversations that result is one of the many powerful things you gain by doing katas.

What's your take on the above problem? Have you come across it in real life?
