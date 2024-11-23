---
layout: post
title: Waxing Lyrical on Pathfinding
date: 2012-05-15 16:02:40.000000000 +01:00
categories:
- code
- conference
- fun
- software craftsmanship
- sc2012
redirect_from:
- "/2012/05/waxing-lyrical-on-pathfinding"
- "/2012/05/waxing-lyrical-on-pathfinding/"
---
I've been attending and giving talks at the [Software Craftmanship](http://www.codemanship.co.uk/softwarecraftsmanship/) conference at Bletchley Park for a couple of years now. I've always found the crowd there engaging and great to hang out with, and I'd encourage you to come along if you're not doing much on June 14th. There are [still a few tickets left](http://www.codemanship.co.uk/softwarecraftsmanship/register.html) if you're quick.

## My talk proposal: Pathfinding Peril

This year my talk proposal is about pathfinding, a subject rather close to my heart since I started [building a game](http://soltrader.net). Finding the shortest path through a connected graph is a complex problem, and one which has a number of very useful applications, not just in the game sector.

Thankfully there are some efficient algorithms out there which solve it well. The aim of my session will be to teach the popular A-Star pathfinding algorithm, along with the factors to consider when choosing appropriate algorithm weights to make the implementation efficient.

A-star can be written in any language, but a simple (untested, probably buggy) version might look like this:

{% highlight ruby %}

    def find(goal)
      closed_set = []
      open_set = [ start_node ]
      came_from = {}
      while(!open_set.empty)
        current = open_set.sort{|node| node.estimated_score }.first
        return reconstruct_path(came_from, goal) if (current == goal)

        open_set -= [current]
        closed_set += [current]
        current.neighbours.each do |neighbour|
          next if closed_set.include?(neighbour)
          possible_score = best_score[current] + current.cost_to(neighbour)
          if !open_set.include?(neighbour) || possible_score < node.running_score
            open_set += [neighbour]
            came_from[neighbour] = current
            neighbour.running_score = possible_score
            neighbour.estimated_score = neighbour.running_score + neighbour.cost_to(goal)
          end
        end
      end
      return 'failed'
    end

{% endhighlight %}

The session will last a couple of hours. I'll take you through the basic A-Star implementation in the first 30 minutes of the session, and we'll spend some time getting that coded up in the second 30 minutes. After a break, we'll be running a tournament for an hour using Matt Wynne's [Robot Tournament engine](https://github.com/mattwynne/robot_tournament). Your robot will be one of two characters in a maze, and the idea is to find the exit as soon as possible without being eaten by the minotaur that roams randomly around it.

You'll get points for exiting the maze within a certain timeframe, exiting first, and simply avoiding being eaten! If I get time, I'll write a basic ruby gem which allows you to parse the maze presented on stdin into nodes with connections.

We'll run around 20 minute iterations, but probably reset the score every time so that the final score is the one that matters. It should be lots of fun!

What do you think of the session idea? How could I improve it?
