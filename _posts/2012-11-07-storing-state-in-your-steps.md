---
layout: post
title: Should we store state in our steps?
date: 2012-11-07 23:50:39.000000000 +00:00
categories:
- cucumber
- bdd
- ruby
- state
redirect_from:
- "/2012/11/storing-state-in-your-steps"
- "/2012/11/storing-state-in-your-steps/"
---
It's quite common to store state inside our cucumber steps in member variables, like so:

{% highlight ruby %}

    Given /^a person called "(.*)"$/ do |person_name|
      @person = Person.create!(person_name)
    end

    When /^they order a waffle$/ do
      @person.order!(:waffle)
    end

{% endhighlight %}

What are the consequences of making this design choice?

## It leads to more readable steps

Shorter, more readable steps are always helpful, as long as sensible names are used. This allows people to get up to speed more quickly to the project. In addition, more readable code is more likely to be modified confidently by others, rather than feared, ignored and ultimately deleted.

## We lose referential transparency for our steps

[Referential transparency](http://en.wikipedia.org/wiki/Referential_transparency_%28computer_science%29) is the property of a piece of code that describes whether it only changes its behaviour when its arguments change. It's important because if a piece of code can react in lots of different ways depending on how the program state is set up, it becomes very hard to tell if the code is correct or not.

Therefore, if we're tracking state inside our steps, the other steps which preceed our step are more important. In the example above, the `@person` variable has to be set to what we expect. This decreases our ability to reuse these steps again in other files.

## Is it worth it?

I try to work towards referential transparency when I can: I'm planning on posting more about the dangers of overreliance on state in a future blog post series. However, I think this is less important in this context, for the following reasons:

* *We're relying on state anyway.* Normally our `Given` steps are setting up some state that we rely on in our later steps. Whether it is stored in member variables is immaterial - referential transparency at a step level normally doesn't exist practically.

* *I'm not a big fan of step reuse.* I prefer lots of very descriptive steps related directly to one feature, only a little reuse between steps, and short step definitions that in turn call other methods in module code. Therefore I generally treat a series of steps as one 'unit', to be treated as a whole, which means I can normally rely on what comes before and after a particular step.

In the end, as with most things in programming, it comes down to a trade off. Is it worth trading tighter dependencies between our steps to get a more little readability and useability? I think that in many cases it is.

## Use member variables with care

If we decide to use member variables, I suggest we use them with care. Let's make sure we use names that are [as meaningful as possible](/2012/09/the-power-of-good-naming) for all our instance variables in our steps.

Commonality is important too: in a large project I recently worked on, we had only used about three different instance variable names throughout several hundred steps, which referred to key domain objects: e.g. `@person`, `@project`, `@customer`.

If we use too many names, then we're tightening up depedencies between specific steps, and we're making them harder to read.
