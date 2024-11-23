---
layout: post
title: Your tests are lying to you
date: 2011-10-17 19:10:29.000000000 +01:00
categories:
- code
- cucumber
- craftsmanship
- bdd
- rspec
- rails
redirect_from:
- "/2011/10/your-tests-are-lying-to-you"
- "/2011/10/your-tests-are-lying-to-you/"
---
Using mocks within your test suite has gone rather out of fashion. Programmers everywhere have been lamenting the fact that mock-based tests are becoming more and more brittle: they're having to change the test code in multiple places each time there's the slightest code change. In fact, they seem to be changing the test code much much more often than the production code.

Using mocks appear to require a lot of set up code for the object under test. Why not just fire up Factory Girl, create a bunch of objects we need to test this code, and just check the outputs?

This works, and appears to work nicely. For a while.

Eventually your tests will get to the point where they're lying to you: they're telling you your code works whereas actually it only works by coincidence. This post will examine the different techniques we can use to test code, and why some work better than others in the long term.

## The problem

To look at this further, let's try to write a conference simulator for a new website that tries to predict how many people might attend an upcoming event: 

{% highlight ruby %}
describe Conference do
  it "calculates total rating" do
    conference = Conference.new(:total_rating => 9)
    conference.total_rating.should == 9
  end
end
{% endhighlight %}

A simple start, with equally simple production code. Next, we decide to extract our code for calculating the rating into <code>Speaker</code> classes. We decide not to change the test suite much, and make the code work behind the scenes:

{% highlight ruby %}
describe Conference do
  it "calculates total rating" do
    conference = Conference.new(:speakers => [:chris, :paul])
    conference.total_rating.should == 9
  end
end
{% endhighlight %}

A nice simple, easy change? You'll pay for this later. Where is the Speaker coming from? Your Conference class is creating it somewhere, or retrieving it from a factory. You've increased the number of collaborators for this class by at least one (possibly three), yet your test isn't showing the additional complexity. It's deceitfully hiding it, whilst you continue on in blissful ignorance.

Your tests are now sitting around the outside of your system. There are no tests for the Speaker class at all, except that we co-incidentally check the rating it emits. Another developer is likely to miss the connection and remove the implied test whilst changing the code for a different reason later.

This gets worse over time:

{% highlight ruby %}
describe Conference do
  it "calculates total rating" do
    conference = Conference.new(
      :schedule => :nine_to_five,
      :talks => [talk_for(:chris), talk_for(:paul)]
    )
    conference.total_rating.should == 9
  end
end
{% endhighlight %}

Can you see what's going on here? We've created some nice helper methods to make it easy to create the required talk objects we need. This test is fairly easy to read, but it's dressing up the problem. The test code is relying on far too many collaborators to function correctly to return the correct result.

When you extract a class, your purely state based tests don't always require change. If you're not stubbing out or mocking systems, you can end up in a situation where you're relying on the code to work without realising it.

How could it be improved?

{% highlight ruby %}
describe Conference do
  let(:talk1) { double(:talk, :rating => 10) }
  let(:talk2) { double(:talk, :rating => 6) }
  let(:schedule) { double(:schedule, :rating => 10) }
  before(:each) { Schedule.stub(:new => schedule) }
  it "calculates total rating" do
    conference = Conference.new(
      :schedule => :nine_to_five,
      :talks => [talk1, talk2]
    )
    conference.total_rating.should == 9
  end
end

describe Speaker do
end
describe Schedule do
end
{% endhighlight %}

Now we've isolated the method nicely from its collaborators, and ensured that its behaviour is correct: that it aggregates the ratings of the talks and the schedule. We also make sure that we're testing Conference correctly, also in isolation.

The more you use refactoring methods such as Extract Class without cleaning up your tests, the more likely your tests will be lying to you. Little by little, those tests that you trusted are slowly testing more and more code. You add a multitude of edge cases at the edges, never thinking about the complexity within. You've resorted to using end-to-end tests to test basic correctness.

This is a bad thing on many levels: for example, what happens to interface discovery? How will you know how the interface of your lower-level classes needs to behave if you're not mocking or stubbing it? You are resorting to guessing, rather than exercising the interface ahead of time in your tests. If you have tests around the edges, but not in the middle, you're not gaining the design input that tests give you in each layer of your system.

## Your code stinks

If you go the whole hog with testing in isolation, then you might end up here with something like this:

{% highlight ruby %}
describe Conference do
  let(:talk1) { double(:talk, :rating => 10) }
  let(:talk2) { double(:talk, :rating => 6) }
  let(:talk3) { double(:talk, :rating => 2) }
  let(:talk4) { double(:talk, :rating => 8) }
  let(:track1) { double(:track, :talks => [talk1, talk3] }
  let(:track2) { double(:track, :talks => [talk2, talk4] }

  let(:venue1) { double(:venue, :nice_coffee_places => 3) }

  let(:joe) { double(:announcer, :experience => 5) }

  let(:schedule) { double(:schedule, :rating => 10, :accouncer => joe) }
  before(:each) { Schedule.stub(:new => schedule) }

  it "calculates total rating" do
    conference = Conference.new(
      :schedule => :nine_to_five,
      :tracks => [track1, track2],
      :organiser => joe,
      :venues => [venue1, venue1]
    )
    conference.total_rating.should == 6.3945820
  end
end

{% endhighlight %}

I'm not surprised people moan about maintaining this: if any aspect of the Conference class changes, this test will break and need to be fixed. We can see that this test code is hard to write and difficult to read. It would be so much easier just to hide this setup in a few factory methods with some sensible defaults, right?

Maybe it's not the test code that's the problem. Perhaps the code stinks. Perhaps the class simply has way too many collaborators, which is why your test code contains a large amount of set up.

For this test code, we can see there are several objects leaking all over the conference code: to refactor this I'd probably get through a Scheduler, Caterer and perhaps a TrackAggregator before I was done. I'd ensure all these objects were tested in isolation, and ensure that there are acceptance tests all the way through to make sure the customer has what they need.

_Well designed code is easy to test._ As a rule of thumb, anytime I get over about two or three lines of setup code for testing a method, I normally take a step back and ask myself if this method is doing too much.


## Test speed

The other advantage of running tests purely in isolation is that they're fast. Very fast. When I'm coding Rails apps these days, thanks to advice from [Corey Haines](http://twitter.com/coreyhaines) I'm running a <code>spec_no_rails</code> folder which runs independently from the rest of my Rails app. Rails apps by default epitomise this problem: default model tests exercise the whole system from the database up. By running your tests independently you're not having to clean the database or start Rails each time you run your tests, which means that much of your interesting code can be tested in under a second. [Gary Bernhardt](http://twitter.com/garybernhardt) has more information on how to set this up in his excellent [Destroy All Software](http://destroyallsoftware.com) screencast series.

## What I'm not saying

This isn't an argument for or against Mocks or Stubs. Either technique can be used successfully to generate clean code. It's an argument about only exercising the code under test, and leave the rest of the system to take care of itself. The important thing is that you _don't exercise your collaborators:_ whether you check they've received messages or simply stub them to return input doesn't matter.

*Don't forget end-to-end tests.* These are very important for business acceptance and for ensuring basic functionality. The important thing is to ensure that you're being intentional about your end-to-end tests and ensure your unit tests are not end-to-end tests by accident.

Take a good look at the test code for a project you recently worked on. You don't need to look at the production code yet: notice that I've not included any production code in these examples. You shouldn't need to see it to know whether it's of good quality or not: you can tell that by reading the tests.

Which is the most annoying or bulky part of your test code? Are your tests deceiving you about what they're testing? How could you improve the code to make this test code easier to maintain?
