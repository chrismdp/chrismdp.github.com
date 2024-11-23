---
layout: post
title: 'Extreme isolation in web apps: part 1'
date: 2013-05-09 10:34:52.000000000 +01:00
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
- "/2013/05/extreme-isolation-in-web-apps-part-1"
- "/2013/05/extreme-isolation-in-web-apps-part-1/"
---
I've been hard at work on a web based prototype for Sol Trader recently in order to test some game mechanics ideas.[^soltrader] I've been building the web app in a slight different way to the normal process I use to build web software, and it's high time I started talking about it.

The examples are written using Sinatra as the web layer and MongoDB as the persistence layer, but you could use any web framework, persistence mechanism, or language for that matter, to express the same concepts. In fact, that's really the point.

## Step 1: Classic Ruby web app design

When I originally started up the project. I threw up a few different Mongo persisted objects to get myself going:

{% highlight ruby %}

    post '/join/?' do
      @game = Game.last
      @character = Character.new(:name => params[:name], :account => @account)
      @joining = Joining.new(:character => @character, :game => @game)
      begin
        @character.save!
        @joining.save!

        flash[:notice] = "You have joined the game successfully."
        redirect '/game'
      rescue Mongoid::Errors::Validations
        flash[:error] = "There was a problem creating the character and joining the game."
        haml :join
      end
    end

{% endhighlight %}

This is pretty typically how I've organised my self in the past when writing an app: I'd have a Game model, and a Character model, and I have a Joining model to link the two together. These objects responsible for handling their own persistence. I'm using Mongoid, but this could just as easily be ActiveRecord. Here's the joining model, for example:

{% highlight ruby %}

    class Joining
       include Mongoid::Document
       include Mongoid::Timestamps

       belongs_to :character
       belongs_to :game
     end

{% endhighlight %}

## Step 2: Extracting the behaviour from the action

When thinking this over, I realised that there were entirely different concerns going on here:

* I'm creating a relationship between a new character and the game that they're joining,
* I'm persisting that relationship in a database,
* I'm responding to the result of that process in my web app.

Time to seperate some of those concerns from the web layer. Following Graham Ashton's excellent recent blog post[^graham], I decided to introduce `CharacterCreator` and `GameJoiner`  class to the procedings to improve the join action. Here's the `CharacterCreator` class (the `GameJoiner` is similar):

{% highlight ruby %}

    class CharacterCreator < Struct.new(:name, :owner, :repository)
      def perform(reporter)
        character = repository.new(:name => name, :account => owner)
        if (character.save)
          reporter.character_created(character)
        else
          reporter.character_creation_problem(character.errors)
        end
      end
    end

{% endhighlight %}

Here's the action which uses it:

{% highlight ruby %}

    def character_created(character)
      @character = character
    end

    def character_creation_problem(errors)
      flash[:error] = "There was a problem creating the character: #{errors}"
      haml :join
    end

    post '/join/?' do
      creator = CharacterCreator.new(params[:name], @account, Character)
      creator.perform(self)
      if (@character)
        joiner = GameJoiner.new(Game.last, @character, Joining)
        joiner.perform(self)
      end
    end

{% endhighlight %}

Instead of the logic existing entirely inside the action itself, the logic has been moved into a seperate class, which calls back into the app class to make the changes that are required. This removed most of the logic from the action at the bottom, and allows us to test the `CharacterCreator` in isolation without having to fire up the whole web app.

## Step 3: Extreme isolation: separating arrangement and work

So far, so good: but it's not perfect. The persistence is still very much embedded inside the character class, and it's necessary to use mocks for testing. I wanted to see how far I could push the tests without needing to use mocks at all, as they are sometimes a code smell for tight coupling. This means that you need to completely avoid callbacks, use dependency injection throughout and rely on passing simple structures between your methods. This means I couldn't use a Publish/Subscribe model either: I wanted to see just how far I could take isolation and code decoupling.

So how about disconnecting characters and games from the persistence mechanism entirely, and just using a queue to communicate between them?[^arrange]

{% highlight ruby %}

    Character = Struct.new(:name, :account_id)
    Game = Struct.new(:characters)

    post '/join/?' do
      changes = []
      character = Character.new(params[:name], @account.id)
      game = GameRepository.latest.join(character, changes)
      GameRepository.apply(changes)
      self.apply(changes)
    end

{% endhighlight %}

This is quite a departure. Let's take each line of the new action in turn.

After creating an empty array to store a set of changes, we then create a character, which is defined as a simply ruby `Struct`.[^struct] We then grab the latest game and call `join`, which represents the actual work of the class. `Game#join` is defined as follows:

{% highlight ruby %}

    def join(character, changes)
      if has_character_with_name?(character.name)
        changes << JoiningError.new("A character with that name already exists.")
        self
      else
        self.class.new(characters + [character]).tap do |game|
          changes << CharacterJoined.new(game)
        end
      end
    end

{% endhighlight %}

Note that we're not changing the object here: we are treating the game object as immutable. We instead create a new copy of the object and then return it. We also return a change object and add the new copy of the game object to it. This is all domain logic: there's no mention of any implementation details.

The `apply` method is very simple. it loops through the changes asking them to perform an operation on the current object. Depending on the type of the change, this will call a different method on the object:

{% highlight ruby %}

    def apply(changes)
      changes.each { |change| change.effect(self) }
    end

    ...

    class JoiningError < Struct.new(:message)
      def effect(caller)
        caller.joining_error(self)
      end
    end

    class CharacterJoined < Struct.new(:game)
      def effect(caller)
        caller.character_joined(self)
      end
    end

{% endhighlight %}

We've now built a generic handler for the different things that can happen when a join is performed. As long as we include the `apply` method in our controller object, and define the `joining_error` and `character_joined` methods, we can handle a joining change in any other object. The apply mechanism shown here can easily be abstracted away so we don't have to worry about it.[^apply]

### Handling the changes

There are two subsystems I want to be able to handle a joining change: the game repository (so that it can save the new character to the database), and the web action itself (so that we can show the relevant page to the user). Both these systems are at the 'edges' of the system, whilst the game object sits in the middle. This turns out very similar to the "Ports and Adaptors" or "Hexagonal" approach Matt's been talking about recently.[^hexagonal] It also has similarities to the Actor model of concurrency used in Erlang.[^actor]

The `GameRepository` defines the relevant methods like this:

{% highlight ruby %}

    def character_joined(change)
      save(change.game)
    end

    def joining_error(change)
    end

{% endhighlight %}

Note that the joining_error isn't interesting to the `GameRepository` class, so we don't do anything with that message.

And the web action in our Sinatra class defines them like this:

{% highlight ruby %}

    def character_joined(change)
      flash[:notice] = "You have joined the game."
      redirect_to '/game'
    end

    def joining_error(change)
      flash[:error] = "There was an error when joining: #{change.message}"
      haml :join
    end

{% endhighlight %}

### The result

We have now seperated the arrangement of the operations which need to be performed (the saving, rendering web pages, joining games) from the work itself: they are all completely and totally isolated from each other. This has a number of advantages:

* The web action and repository steps can be performed independently from each other, and neither cares about the implementation of the other.
* The join method in the plain ruby game object cares nothing for its own persistence, and knows exactly zero about web applications, which is just as it should be. It's like putting your systems in solitary confinement, with no access to the outside world.
* It's easy to build in another handler here - perhaps to update a web socket for a JavaScript client side app - by simply applying the changes to a new subsystem object: `WebSocketServer` perhaps.
* Having Cucumber documentation hitting the web app was very useful as I made bigger changes, as I could still verify that everything was working. This gave me courage to proceed with something a little different.[^cukes]
* There's nothing to stop me making the queues proper `Queue` objects, and start running the system in parallel in future, to take advantage of multiple cores.

### The verdict

I love working in this way. It's very freeing not having to think about persistence or web apps when trying to reason about complex domain concepts. It scales well, too: I've now built most of the protoype using a form of this approach. The domain logic is about 1,000 lines of code, my entire persistence layer still sits in one 200 line file, and the main web app is another 200 line file.  These files are manageable because there isn't much going on in them: they're just handling lots of different types of changes by defining a few methods. In fact the real `GameRepository` class has a lot of lines which look like this:

{% highlight ruby %}

    alias_method :character_ordered_to_travel, :save_position
    alias_method :character_ordered_to_mine, :save_position
    alias_method :character_ordered_to_join_fleet, :save_position
    alias_method :character_ordered_to_attack, :save_position

{% endhighlight %}

What do you think of this approach? Is it an improvement, or does it just obfuscate logic? I'd be grateful for feedback.

## More to come

Next time I plan to talk about how I'm performing more complex operations by feeding changes back into the domain to allow reactions to behaviour. Stay tuned!

[^graham]: [Refactoring with Hexagonal Rails](https://www.agileplannerapp.com/blog/building-agile-planner/refactoring-with-hexagonal-rails) is an excellent post by [Graham Ashton](http://twitter.com/agileplanner) on how he cleaned up controller actions whilst working on his Agile Planner software.

[^soltrader]: [Sol Trader](http://soltrader.net) is the space trading and piracy game I've been writing for the last year or so. The online version I'm describing in this post will be available at [http://online.soltrader.net](http://online.soltrader.net) once it's ready.

[^struct]: [Ruby structs](http://ruby-doc.org/core-2.0/Struct.html) are a convenient way to create simple classes to store values.

[^arrange]: I am indebted to Gary Bernhardt's [Separation of Arrangement and Work](https://www.destroyallsoftware.com/screencasts/catalog/separating-arrangement-and-work) screencast at [Destroy All Software](https://www.destroyallsoftware.com/) for the inspiration that led to the final step in this refactoring.

[^hexagonal]: This is probably the most [comprehensive post](http://blog.mattwynne.net/2012/05/31/hexagonal-rails-objects-values-and-hexagons/) on the subject: there are also many links in the [first post in Matt's series](http://blog.mattwynne.net/2012/04/09/hexagonal-rails-introduction/).

[^apply]: In the real system this all exists in Modules. I'm only showing it long-hand here for clarity.

[^cukes]: See my [previous post](http://chrismdp.com/2013/04/features-are-documentation-not-tests/) for some examples of how I'm writing the Cucumber features for this project.

[^actor]: Read more about the [Actor Model](http://en.wikipedia.org/wiki/Actor_model) here.

