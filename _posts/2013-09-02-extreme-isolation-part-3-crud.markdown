---
layout: post
title: "Extreme isolation part 3: coding a CRUD app (with full example)"
date: 2013-09-02 11:22:27 +0100
categories:
  - ruby
  - state
  - craftsmanship
  - crud
  - code
  - cucumber
  - testing
  - extreme isolation

---

<a href="http://www.flickr.com/photos/9790232@N05/1298814620/" title="Street Crud by Jeremy Doucette, on Flickr"><img src="http://farm2.staticflickr.com/1086/1298814620_5c902c6fef_z.jpg" width="640" height="427" alt="Street Crud"></a>

*CRUD apps start simple, yet often get messy and nasty really fast. They are a great test bed for Extreme Isolation.*

I started a few months ago looking at a [fresh new way of architecting web applications](http://chrismdp.com/tag/extreme%20isolation). I suggest you read parts [one](http://chrismdp.com/2013/05/extreme-isolation-in-web-apps-part-1) and [two](http://chrismdp.com/2013/07/extreme-isolation-part-2) first.

The app I've been mainly working on using this new method is an online version of [Sol Trader](http://soltrader.net), which isn't really a typical web application most people write. I've since applied this paradigm to a directory application called "Discover" I've been working on for the [Trust Thamesmead](http://trust-thamesmead.co.uk) charity, and I thought I'd share the results.

Discover is a much more traditional "CRUD style" application. The administrators define audiences for a local area (people who go to school, or want to find a job) and add places to a site, grouped into topics for that audience. For example, if you're into music (the "music" audience) you might want to see places in the "music shops", "gig venues" and "music video shoot locations" for a particular area.

The source code is fully open source. Trust Thamesmead have a great ethos: they would love other local areas to pick up the application and run with it. This also means that I can use the codebase as a demonstration of extreme isolation.

[Get the source code](http://github.com/thinkcodelearn/discover)

Let me take you through how it works.

## The basic models: Audience, Topic, Place

Let's have a look at the data representation for models first. Check out [audience.rb:](https://github.com/thinkcodelearn/discover/blob/blog-post/lib/discover/audience.rb)

{% highlight ruby %}

    module Discover
      class Audience < Struct.new(:description, :slug, :topics)
        def initialize(*)
          super
          self.description ||= ''
          self.slug ||= sluggify(description)
          self.topics ||= []
        end

        def sluggify(string)
          string.downcase.gsub(/\W/,'-')
        end

        def with_description(new_description)
          self.class.new(new_description, slug, topics)
        end

        def with_topics(new_topics)
          self.class.new(description, slug, new_topics)
        end
      end
    end

{% endhighlight %}

These objects are immutable. They are created from an `AudienceRepository`, which handles all the persistence of the objects for you. They know nothing about loading, saving or disk representations, which is exactly as it should be.

Audiences themselves are very simple containers of a description and a list of associated topics. They have a method to generate a slug, and two generator methods to create new audiences based on this topic: that's how we handle updating audiences.

## A web request to retrieve an object

The web logic is wrapped up in two files: a Sinatra application in [app/audiences.rb](https://github.com/thinkcodelearn/discover/blob/blog-post/lib/discover/app/admin/audiences.rb) which acts like a controller would in Rails, and a shared module in [app/crud.rb](https://github.com/thinkcodelearn/discover/blob/blog-post/lib/discover/app/admin/crud.rb) which contains logic used by all the other Sinatra apps.

A web request comes in to the application and runs this code in the shared logic:

{% highlight ruby %}

    host.get '/:slug/?' do |slug|
      @object = find(slug)
      haml :edit
    end

{% endhighlight %}

This find method is defined in the Audience-specific class:

{% highlight ruby %}

    def find(slug)
      repository.audience_from_slug(slug)
    end

    def repository
      @audience_repository ||= Discover::AudienceRepository.new
    end

{% endhighlight %}

The `AudienceRepository` takes care of the persistence end of things (you can see how in [persisted/audiences.rb](https://github.com/thinkcodelearn/discover/blob/blog-post/lib/discover/persisted/audience.rb)), and returns back a plain ruby `Audience` object as shown above. This object is then passed to the [edit.haml](https://github.com/thinkcodelearn/discover/blob/blog-post/views/admin/audiences/edit.haml) view file as `@object` and we're done.

## A web request to update the object

Updating the object is more interesting. The following action is called first, which then calls a series of other methods:

{% highlight ruby %}

    host.post '/:slug/?' do |slug|
      candidate = find(slug)
      queue = validator(candidate).
        validate(update_from_params(candidate, params))
      queue += editor(slug).apply(queue)
      downstream(queue)
    end

    ...

    def update_from_params(object, params)
      object.
        with_description(params[:object][:description]).
        with_topics([params[:object][:topics]].flatten.compact)
    end

    def validator(candidate)
      AudienceValidator.new((repository.active_audiences - [candidate]).map(&:slug))
    end

{% endhighlight %}

The first line retrieves a plain immutable `Audience` object as before. The `update_from_params` method is called next: this returns a new `Audience` object with the updated information, using the factory methods we defined on the model earlier.

### Validation

The new `Audience` object is passed to an `AudienceValidator` object ([defined here](https://github.com/thinkcodelearn/discover/blob/blog-post/lib/discover/audience_validator.rb)) which takes a list of existing slugs in the database, and returns one of two things:

* A `ValidAudience` change if the new `Audience` object is valid
* An `InvalidAudience` change if it is not valid

We appear to be reinventing the wheel with the Validator object here: but the great advantage with doing things this way is that the object has no dependency on the database at all. This means it can be tested in isolation, it's fast, and we can chain them together and reuse them in more situations.

### Applying the changes

The queue of changes is then pipelined through various other services in true Extreme Isolation fashion. Firstly we apply the queue to an object we receive from the `editor` method call in the Sinatra application:

{% highlight ruby %}

    class Editor < Struct.new(:slug)
      include Reactor

      def valid_audience(change)
        Changes::AudienceEdited.new(slug, change.audience)
      end
    end

    def editor(slug)
      Editor.new(slug)
    end

{% endhighlight %}

This processes the `ValidAudience` change and returns an `AudienceEdited` change, which is tacked on to the end of the queue of changes. (See [reactor.rb](https://github.com/thinkcodelearn/discover/blob/blog-post/lib/discover/reactor.rb) for exactly how the plumbing works.) An `InvalidAudience` change is ignored - we don't want to edit the audience in this case.

The resulting change queue is then passed to `downstream` which is the set of services that process all web requests:

{% highlight ruby %}

    def downstream(queue)
      repository.apply(queue)
      AudienceHandler.new(self, '/').apply(queue).first
    end

{% endhighlight %}

The `AudienceRepository` picks up the `AudienceEdited` change and does the correct thing to the persisted record. The `AudienceHandler` works out how to return the right message to the web interface. It handles `InvalidAudience` and `AudienceEdited` messages, as well as `AudienceCreated` and `AudienceDeleted` messages for the other CRUD operations.

## Creation and deletion

The other CRUD operations work very similarly. The creation simply constructs a brand new `Audience` object, checks validity and passes the resulting set of changes to the `AudienceRepository` and the web handler. Deletion is even simpler: it just passes an `AudienceDeleted` message to the `downstream` method.


## Extending the set of services

This way of doing web applications is extremely extendable. Here's a much more complex `downstream` method for Sol Trader Online, which is run for every single player action web request in the game:

{% highlight ruby %}

    def downstream(queue)
      queue = Solweb::OrderQueuer.new(@position).pipe(queue)
      queue = Solweb::PositionPermissionChecker.new(@position, @game).pipe(queue)
      queue = @position.pipe(queue, @game.turn_count)
      queue += Solweb::GoalChecker.new.check(queue)
      queue += Solweb::OrderChecker.new(@game.positions).check(queue)
      queue += Solweb::MissionDealer.new(Solweb::MissionGenerator).apply(queue, @game)
      queue += Solweb::Notifier.new(@game).apply(queue)
      GameRepository.apply(@game.identifier, queue)
      Handler.new(self).apply(queue).first
    end

{% endhighlight %}

Each piece is totally isolated and therefore easily testable. When one service gets too complex, it's easy to split up what it's doing into two services: `PositionPermissionChecker` is a recent extraction from the code inside the `Position` object.

## Conclusions

This is still an experiment. It's more involved that a typical CRUD app, and harder to get going, but the individual pieces (the validators, the `Editor` class, the `Handler` classes) are all very testable as they only do one thing in isolation.

There are also many ways that I could improve the web logic, but at the moment those classes are fine for my purposes. Likewise, all the javascript is still inline in the views, and has yet to be pulled out and refactored.

What do you think of the approach? Can you see yourself using it on your next project?

