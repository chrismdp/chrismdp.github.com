---
layout: post
title: "Rack::Usermanual: Cucumber features as in-app user manual"
date: 2013-06-17 15:28:34 +0100
categories:
  - cucumber
  - bdd
  - code
  - sol trader

---

<style>
  img { border: 5px solid #eee; }
</style>

I blogged recently about taking our cucumber features [one step further](http://chrismdp.com/2013/04/features-are-documentation-not-tests/) and allowing them to become true documentation rather than tests.

Last week, I spent a little time working on getting the cucumber features in the [online version of Sol Trader](http://online.soltrader.net) working as true user manual style documentation, available from `/help`. I've also packaged this up into a [ruby gem](http://rubygems.org/gems/rack-usermanual) - more info on that below.

Here's an example of what the format looks like:

![example shot](/files/rack-usermanual-1.png)

There are lots more live examples [on the Sol Trader help section](http://online.soltrader.net/help).

# How it works

Here's a little more on how Rack::Usermanual transforms your features:

### Converting scenarios to prosaic examples

I've tried to format the features so that the scenarios are displayed in a sentence-style structure, as you might find in a user manual. This means that the following scenario:

    Scenario: You can't move with a fleet when you're carrying too much stuff
    Given you are playing Eddie
    And you are on Earth
    And Terry is travelling to Earth Orbit
    When you choose to join Terry's fleet
    And you buy 4 water at the market
    Then you are not transported to Earth Orbit with Terry
    And you are no longer a member of Terry's fleet

Renders as this example of play:

<div class='well'>
<p><strong>Example: you can't move with a fleet when you're carrying too much stuff</strong></p>

<p><em>Assume you are playing Eddie, and you are on Earth, and Terry is travelling to Earth Orbit. When you choose to join Terry's fleet, and you buy 4 water at the market, then you are not transported to Earth Orbit with Terry, and you are no longer a member of Terry's fleet.</em></p>
</div>

Although the conversion to sentences needs some more work, I think the second version shown here is much more readable in this context.

### 'Pending' tags convert to alerts

If a feature or scenario has the `@pending` tag, then we warn the reader the feature might not be available. Empty scenarios are also shown with a explanatory message:

![example shot](/files/rack-usermanual-2.png)

### Backgrounds convert to a note

If there's a Background attached to the feature, then we show a note above the list of the examples:

![example shot](/files/rack-usermanual-3.png)

## Available as a Ruby gem!

I've released the code as the [Rack::Usermanual](http://github.com/chrismdp/rack-usermanual) gem, so everyone can benefit from using it.

It's one line in your Gemfile, and another line in your `config/routes.rb` (for rails) or your Rack configuration code, and you can start serving your features straight away. There's lots more information in the [README](http://github.com/chrismdp/rack-usermanual): let me know how you get on using it.

## In conclusion

It's been an interesting exercise converting my features to more of a 'user manual' style. Reading them through again in the new format has helped me think further about just how important precision of language is when putting features together. We can usually be more precise that we think we can, and breaking out of the standard 'Given, When, Then' style can help us rethink the quality of the documentation we're leaving behind us.

I'd be grateful for feedback and more ways in which I can improve the readability of the features in this style. Let me know what you think.
