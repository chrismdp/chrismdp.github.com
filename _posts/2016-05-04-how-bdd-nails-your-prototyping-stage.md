---
layout: post
title: 'Extreme YAGNI: How BDD nails your prototyping stage'
date: 2016-05-04 09:51:54.000000000 +01:00
categories:
- bdd
- cucumber
- team
- lean startup
redirect_from:
- "/2016/05/how-bdd-nails-your-prototyping-stage"
---
![prototyping](/assets/img/prototyping.jpg)

Sometimes people don't see the value in the [BDD](/tag/bdd) process. They contend that the BDD ceremonies are a waste of time, and get in the way of delivering real features to customers. Others cannot see how to apply BDD to their project, as no-one knowns exactly what the project will look like yet. As they're only in the prototyping stage, by the time a feature file is written and made executable, it's already out of date.

I don't agree with this. If our process is set up right, we can prototype using just as effectively and retain the collaboration benefits that BDD gives us.

## You Ain't Gonna Need It

One of the biggest wins that Test-driven Development ([TDD](/tag/tdd)) gives us is the principle of YAGNI - "You Ain't Gonna Need It". It's very tempting when writing code to go off on a tangent and produce a beautiful structured work of art that has zero practical use. TDD stops us doing this by forcing us only to write code that a test requires. Even some experts who don't practice or encourage TDD often espouse the power of [writing the calling code first](/2015/03/why-games-coders-dont-use-tdd-and-why-it-matters/) in order to achieve much the same effect.

BDD gives us the same YAGNI win: but at a level higher than TDD. With the BDD cycle we're adding thin slices of customer observable behaviour to our systems. If we can only write the code thats directly used by the business, then in theory we should be cutting down on wasteful development time.

However, there's a snag here. if we're prototyping, we don't know whether this feature will make it into the final product. We still need to give feedback to our product team, so we need to build something. If the feature is complex, it might take a while to build it, and the feature might never get used. Why bother going through the process of specifying the feature using BDD and Cucumber features?

Happily, we can take YAGNI a level further to help us out.

## Extreme YAGNI

Often in TDD, and especially when teaching it, I will encourage people to take shortcuts that might seem silly in their production code. For example, when writing a simple supermarket checkout class in Javascript, we might start with a test like this:

{% highlight javascript %}

    var checkout = new Checkout();
    expect(checkout.total()).toEqual(0);

{% endhighlight %}

Our test defines our supermarket checkout to have a total of zero on creation. One simple way to make this work would be to define the following class:

{% highlight javascript %}

    var Checkout = function() {
      this.total = function() {
        return 0;
      };
    }

{% endhighlight %}

You might think that's cheating, and many people define a member variable for `total`, set it to 0 in the constructor, and miss this step out entirely. There is however an important principle at stake here. The code we have does exactly what the test requires it too. We may not *need* a local variable to store `total` at all.

**Here's the secret: we can practice this "extreme YAGNI" at the level of our features, too.** If there's a quick way to make our feature files work, then there's nothing to stop us taking as many shortcuts as we can to get things working quickly.

For example, if we're testing the user interface of our system via Cucumber features, one fast way to ensure things are working is to hard code the values in the user interface and not implement the back end behaviour too early. Why not make key pages static in your application, or hard code a few cases so your business gets the rough idea?

Again, you might think that's cheating, but your features pass, so you've delivered what's been asked for. You've spent the time thrashing out the story in a 3 amigos meeting, so you gain the benefits of deliberately discovering your software. You're giving your colleagues real insight to guide the next set of stories, rather than vague guessing up front. Our UX and design colleagues now have important feedback through a working deployed system very quickly, and quick feedback through working software is a core component of the [agile manifesto](http://agilemanifesto.org).

By putting off implementing the whole feature until later, we can use BDD to help us navigate the ["chaotic" Cynefin space](https://en.wikipedia.org/wiki/Cynefin_Framework) rather than just the "complicated" space. This in theory makes BDD twice as useful to our business.

## Fast, fluid BDD

This all assumes that we have a fast, fluid BDD process, with close collaboration built in. If it takes a week to coordinate everyone for the next feature file, then the temptation is to have a long meeting and go through too many features, without a chance to pause, prototype, deliver and learn from working software. Maybe it's time to re-organise those desks and sit all the members of your team together, or clean up your remote working practices, or block out time each day for 3 amigo sessions. You'll be suprised how much small changes speed your team up.

