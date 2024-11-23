---
layout: post
title: The power of good naming
date: 2012-09-18 20:43:02.000000000 +01:00
redirect_to: https://deliverydoubled.com/name-as-if-your-life-depends-on-it-a-guide-to-cleaner-code/
categories:
- code
- craftsmanship
- refactoring
redirect_from:
- "/2012/09/the-power-of-good-naming"
- "/2012/09/the-power-of-good-naming/"
---
<p><i>"There are two hard problems in computer science: Cache invaliation, naming things, and off by one errors."</i></p>

-- Source: [Martin Fowler](http://martinfowler.com/bliki/TwoHardThings.html)

Naming things is hard. Why do we expend so much effort to get them right? Because naming programming concepts well gives us a big insight into how they fit into the system we're designing. Continually renaming things records our insights as we go: the right names for our objects, methods and variables will yield fresh insight and in turn shape the design of the system.

J.B. Rainsberger [talks about](http://www.jbrains.ca/permalink/the-four-elements-of-simple-design) names of classes, methods and variables going through four stages:

* *Nonsense:* For example, we might extract a method from a larger one and quickly rename it `foo()` to get the refactor done and the tests passing.

* *Accurate:* We rename the nonsense method to what it actually does, such as `processPayroll()`.

* *Precise:* Once we realise what the method really does, we might refine the accurate name and give it more precision, such as `loopThroughEmployeesAndPayThem()`.

* *Meaningful:* At this point, we've revealed the complexity of the method, and can look to split it up into two methods: `forEachEmployee()` and perhaps a `pay()` method on a seperate interface.

Some simple rules of thumb to follow when naming things:

* *Don't be afraid of nonesense names.* We shouldn't shy away from the early stages of naming. If we're not sure what something is yet, give it a nonsense name. The name `foo()` is fine, as long as it's only going to last fifteen minutes. Best not to commit it though :)

* *If you don't like the code you're writing, use really long names.* If in doubt as to what or where something fits, use a really (really) long name: the longer and more precise the better. I will call a variable something like `computed_unsorted_project_task_matrix` especially if I don't like it and want to refactor it at some point. This is much better than `result` (or `res` or even `r`). I reveal the complexity of the object through the name, which helps reveal complexity in the code.

* *Characters are cheap, confusion is costly.* Let's not make things harder for the programmers who come after us. Remember, this is just as likely to be ourselves in a few months. Let's avoid using a name like `prj` when `project` is only four characters more typing. Anything that reduces reading friction in our code is a good thing.

How often do you rename your methods, objects, and classes? How does naming help you understand your code?
