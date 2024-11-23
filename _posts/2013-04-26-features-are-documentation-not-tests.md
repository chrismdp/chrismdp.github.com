---
layout: post
title: Features are documentation, not tests
date: 2013-04-26 08:50:13.000000000 +01:00
categories:
- bdd
- cucumber
- state
- ruby
- sol trader
redirect_from:
- "/2013/04/features-are-documentation-not-tests"
- "/2013/04/features-are-documentation-not-tests/"
---
Cucumber features are primarily documentation, and only incidentally tests to execute.

However, it's easy to fall into the trap of writing features which don't actually read like documentation at all, but a long, tortuous, and highly repetitive mess of tests.

## The problem

Here's an example of a feature that's difficult to read.

{% highlight cucumber %}

    Feature: User adds a task to a project

    As a user I want to add a task to a project, so that I can track
    what's left to do on the project.

    Scenario: User adds tasks
      Given a user called "User"
      And a project called "Project"
      And the user "User" has permission "Task managment" for the project "Project"
      When I add a task "Task" to the tasks list of the project "Project"
      Then the task "Task" should be listed on the task list of the project "Project"

{% endhighlight %}

I've written many scenarios like this in the past: I'm sure many of us have. What's wrong with it?

## It doesn't read like English

Scenarios like this are easy to code, because all the information you need is right there. However, they don't read well: they are very repetitious in their use of language and are difficult to scan. They don't read like English.

In my experience, those who are the best at coding are often the worst at writing features. They tend to think of steps like code and apply good coding principles to them. For example, they try to reuse steps as much as possible (the DRY principle), and give steps all the information they need to run (the Dependency Injection principle).

This sounds sensible, but it leads to poor scenarios and poor step code in practice. Steps are not method calls, and shouldn't read like them.

The whole point of Cucumber is that we get the ability to use natural language to make our features easier to understand. Writing a feature in this way is akin to writing this blog post in the following style:

*"If I kept mentioning the feature when discussing the feature with my audience, my audience will get bored with the fact that I kept mentioning the feature when discussing the feature with my audience, and my audience as a result of getting bored will lose interest in the feature that I keep mention when discussing the feature with my audience..."*

Nobody speaks or writes like that! The key difference is that we use context when we communicate to people. We use shorthands such as 'it' to refer to someting that we've just discussed, and we constantly assume a huge amount of knowledge on the part of our listeners.

## Using member variables in step definitions helps give context

When I'm tempted to be too repetitous and start writing my features like test code, I start using member variables to capture what the current state is my steps (I've written about the pros and cons of this before: see the article linked at the end of the post.) As long as you are judicious with your member variables and don't let them get out of control, they can make your features much easier to read. Let's restate the previous feature using context:

{% highlight cucumber %}

    Feature: User adds a task to a project

    As a user I want to add a task to a project, so that I can track
    what's left to do on the project.

    Scenario: User adds tasks
      Given a project called "Project"
      And I'm signed in as "User"
      And I have permission to add tasks to the project
      When I add a task to the project
      Then the task should be added to the project

{% endhighlight %}

Much easier to read. Here's what the steps might look like:

{% highlight ruby %}

    Given /^I'm signed in as "(.+?)"$/ do |name|
      @user = User.new(name)
    end

    Given /^a project called "(.+?)"$/ do |name|
      @project = Project.new(name)
    end

    Given /^I have permission to add tasks to the project$/ do
      @project.add_permission_to(@user, "Task management")
    end

{% endhighlight %}

Once you are freed from needing to refer to the domain objects you are using in every step, you are able to write your feature in pretty much the way you want to, and you can make them into true documentation, not matter what your audience.

## Reading like a game manual

If we've now got the tools to make our features more flexible, then how about we try and make them true documentation that's useful to our end users, not just our stakeholders?

For example: currently I'm in the process of working up a web prototype of some of the game mechanics on Sol Trader, a game I've been working on for the last year. The aim is to quickly iterate on the core simulation: it's hard to do anything quickly in raw C++.

In order to document these game mechanics for my beta testers, I could have sat down and written a long markdown file, but instead I decided using the cucumber features themselves to describe the behaviour that I want to capture. I've used the preamble to write my "acceptance criteria" in prosaic format so that someone new to the game will be able to undrstand how to play. The scenarios are written as specific examples of game behaviour that still reads like a manual.

Here's an example feature of a character joining a fleet:

{% highlight cucumber %}

    Feature: Joining other characters' fleets

    A character that is travelling to another location is vulnerable
    to attack from pirates. If you wish, you can choose to join a
    character's fleet as they travel to bolster their defences against
    any attack that they might come under. You will also participate
    in any attacks they might make against pirates.

    You choose to join travelling characters through meeting them in
    the Spaceport Bar, or by contacting them on the Comms Channel
    should you be in open space. Once you are in a character's fleet,
    you will stay with them until they leave the location, and you
    will travel with them to their destination. You can choose to stop
    being in the fleet at any time.

    ...

    Scenario: You can't join a fleet when someone is in the middle of a travel order
      Given you are playing Eddie
      And you are in Earth Orbit
      And Terry travelled to Mars Orbit a turn ago
      Then you won't be allowed to join Terry's fleet

{% endhighlight %}

I've chosen here to reverse the normal "Given I do this" and instead use "Given you do this" - it feels more like a game manual when I write the feature like this.

Hopefully it's clear enough to understand, assuming you had some context about travel orders. Let me know what you think.

## Stories that are specific but not soporific

Using a tool like Relish, which allows you to publish your features to a website, is a great way to ensure that the documentation that your project is producing is actually readable over time. When forced to read your features as documentation on a website, rather than as "code" in your text editor, you immediately start seeing ways that they can be improved.

The more interesting we make our features to read, the more likely people will read and update them.

A challenge for today: pick one scenario on your project and read it out loud to a non-technical co-worker. If they don't get a sense of what the scenario is describe, try and rework it until they do.

## Further reading

* [Should we store state in our steps](http://chrismdp.com/2012/11/storing-state-in-your-steps): a blog article I wrote last year discussing the pros and cons of member variables in steps.

* [Sol Trader](http://soltrader.net): the space trading and piracy game I've been writing for the last year or so. The online version will be available at [http://online.soltrader.net](http://online.soltrader.net) once it's ready.

* [Relish](http://relishapp.com): a great tool for getting your features published in a non-technical format. Full disclosure: I train with the creator of Relish at [BDD Kickstart](http://bddkickstart.com), but although I don't personally benefit from Relish. It's a great tool though, you should use it.
