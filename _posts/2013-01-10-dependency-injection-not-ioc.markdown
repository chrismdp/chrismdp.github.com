---
layout: post
title: "Dependency injection != Inversion of Control"
date: 2013-01-10 13:25:44 +0000
categories:
  - ruby
  - code
  - java
  - cucumber
  - bdd

---

[David Heinemeier Hansson](http://david.heinemeierhansson.com), the creator of [Rails](http://rubyonrails.org), recently posted his [thoughts on dependency injection](http://david.heinemeierhansson.com/2012/dependency-injection-is-not-a-virtue.html). The post is written in an unhelpful inflammatory style, and it's inaccurate in its use of the terms involved.

In particular, there is a confusing conflation of the ideas of dependency injection, a simple programming pattern I use every day, and Inversion of Control (IoC) containers, which are sometimes called "Dependency Injection containers". These are a heavyweight implementation of dependency injection wrapped around the whole application. IoC containers aren't normally needed in a language like Ruby (and many argue they [aren't needed in Java either](http://www.natpryce.com/articles/000783.html)) whereas dependency injection is a useful technique in any language to ensure our classes are properly isolated from each other, which leads to better seperation of concerns.

The purpose of this post is to correct the misunderstandings which may have been created about the differences between the concepts, and try and illustrate where we might use them.

## Dependency injection

Dependency injection is the practice of passing in the our object's collaborators (the code objects that our object depends on) into it, rather than creating them inside the object.

Here's an example of a class which uses a collaborator directly:

{% highlight ruby %}

    class Waffle
      def cook(time)
        @burnt = true if (time > CookingTime.for(self))
      end
    end

    waffle = Waffle.new
    waffle.cook(10.minutes)

{% endhighlight %}

Insead of using `CookingTime` directly in the class, we might choose to "inject" the collaborators into the object:

{% highlight ruby %}

    class Waffle
      def cook(time, times)
        @burnt = true if (time > times.for(self))
      end
    end

    waffle = Waffle.new
    waffle.cook(10.minutes, CookingTime)

{% endhighlight %}

It seems a trivial change, and perhaps even a backwards step. However, now our `Waffle` object is isolated from our `CookingTime` code in a way that it wasn't before - we can now vary the `Waffle` and the list of `CookingTime` objects independently. (They're still reasonably closely coupled by implication: the `Waffle` still expects an object to be passed in which responds to the `for` method and returns a time. Another step to isolate this object further would be to pass in a `CookingTime` value object to the `Waffle` object directly.)

This independence allows the objects to be exercised with mock collaborators in a test in a strongly typed language such as Java. This is less of an advantage when we have mocking libraries that allow us to avoid that need, or when we are preferring value objects over mocks to isolate our code. Making dependencies explicit is useful concept in any case, as it limits unintended side effects and isolates our objects from the details of other objects.

## Inversion of Control (IoC) containers

Taking the idea of dependency injection to the max, a few years ago various application frameworks popped up with the idea of having system objects created using configuration files, and have their dependencies explicitly wired together with XML code. The idea was to "invert the control" of the system by pulling the organisational control out of the objects and keeping it entirely seperate: hence the name Inversion of Control container. Most notable amongst these frameworks was the [Spring framework](http://www.springsource.org/spring-framework) for Java.

This was a desirable alternative to some of the other frameworks out there at the time, and I jumped on the bandwagon too (this very blog contains [a long experience report](/2006/01/spring-rc-introduction) on using [Spring Richclient](http://www.springsource.org/spring-rcp) from about seven years ago). XML was easier to write than Java code, so I got some value from using it.

However, it quickly got very unwieldy to specific all my object wiring in XML and it became rather difficult to follow what was going on. Whilst I still like the concept of writing up objects with explicit dependencies in a place external to the classes involved, these days I prefer to do this in code, or to use something like Rails, which for the most part does this automatically and by convention. For another similar take on this, read Jamis' [great article on DI from 2008](http://weblog.jamisbuck.org/2008/11/9/legos-play-doh-and-programming).

## When coding in Ruby

I don't think the concept of Inversion of Control containers translates to Ruby - in fact many people working across different languages consider it to be rather too big a hammer. XML is not easier to write than Ruby: defining the interface to all our objects using XML and then using more XML to wire them together just doesn't appeal. I'd prefer to write a few lines of Ruby code to wire them up. In practice, when doing [BDD](/tag/bdd), I find that this sort of wiring tends to come out naturally as you look to find easy ways to set up a small part of your application for integration testing.

However, the concept of dependency injection as described above is very useful. A dependency of an object is still a dependency, whether it's explicit or implied. Burying the dependency in the model doesn't make the model any less dependent on the collaborator.

For example, consider this short class:

{% highlight ruby %}

    class Waffle
      def time_since_cooked
        Time.now - cooked_at
      end
    end

{% endhighlight %}

Even though we can refer to a Time.now class in Ruby from within an object, and stub it externally for testing, the object above still has an explicit dependency on the `Time` class: specifically on the `now` factory method which creates the `Time` object. When we bury these references in our code, it becomes hard to see what our collaborators are. It could then be beneficial to inject them into the class via the constructor, rather than referring to them directly.

Additionally, *to stub global methods like `Time` means to reach down in to the guts of all our objects and tweak their behaviour, all at once.* Fixing the date and time of an object across a system might be reasonably well understood, but it's a poor example: with more complex behaviour there may well be unintended side effects to stubbing objects right across the system.

I would never say it was *bad* to have dependent objects fixed in our code: everything depends on context. We just need to be aware of the potentially undesirable consequences of what we're doing.

## Summary

Use dependency injection liberally, based on your judgement as to whether it improves the quality of your system. This applies whatever language you're using.

Use Inversion of Control containers if you find them helpful, but consider the cost. It's often better to simply wire up your objects in code.

Study other language communities and reason carefully about whether their paradigms and patterns are useful. After all, if Ruby programmers hadn't done that, we wouldn't have [Rack](http://rack.github.com/) (which came from Python) or [Cucumber](/tag/cucumber) (which came originally from JBehave, written in Java.)

Do you use dependency injection, or Inversion of Control containers? What trade-offs do you find apply when using them?
