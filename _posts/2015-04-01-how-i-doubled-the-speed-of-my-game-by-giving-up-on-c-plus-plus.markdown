---
layout: post
title: "How I doubled the speed of my game by giving up on C++"
date: 2015-04-01 12:49:53 +0100
categories:
  - sol trader
  - code
  - game development
  - c++
  - object oriented

---

C++ is fast. It's a good fit for games. It's certainly [faster than Ruby](/2012/01/why-i-switched-from-ruby-back-to-c-plus-plus/). However, there's a better fit for game development. It's called C.

This isn't an April Fool's joke. Look at what happened to the [Sol Trader](http://soltrader.net) history system when I ditched the slow C++ version and rewrote it in optimised C. The line count is also about 20% reduced.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BPbWcsmS1lA" frameborder="0" allowfullscreen></iframe>

C++ code can be fast, but the way C++ is commonly used and the language
features that it promotes can get in the way of this goal. Here are a few
things I've learnt about C++ that are essential for anyone to know who wants to
write modern performant code.

## Memory access is slow

In case you hadn't realised: compared to your CPU, your memory is slow. Very
slow. It's probably the thing that's most holding your CPU back right now.

Memory has been gradually increasing in speed over the last few decades, but at
10% of the rate of CPU speed:

![memory vs. CPU speed incrase](/files/memory-cpu-speed-increase.png)

Memory cache misses cause the CPU to stall, losing several hundred cycles each
time it happens. Every year, cache misses become a more and more significant
cause of CPU slowdown.

With the previous version of the history generation, using classic object
oriented patterns, my data was all over the place. I had hundreds of little
objects all encapsulating their own data, using virtual method calls to access
tiny pieces of it.

I moved to arrays of values, storing references to other objects via indexes
everywhere. I moved all the string processing right out of the generation
engine, so that the engine was only dealing with small data structures of
perhaps 20-30 bytes at a time.

## Virtual function calls are slow

A virtual function is one that changes it's behaviour depending on the type of
the object. For example, if we use an interface in C++, we create an abstract
class with some virtual functions attached to it. We then derive our class
from this interface, passing pointers of the interface type around our
program. When our program calls the interface function, the program is able to
work out which method to call on the derived object, based on extra information
that's kept in our object.

So far, so good. Except virtual functions are slow for the same reason that the
memory is slow. With virtual methods, the right method to call can only be
decided at run time, and there's normally one or two cache misses for these
method calls. The compiler is constrained about what it can do to make this
quicker. It might not seem like much, but it stacks up for inner loops.

Back in 2002, when I was working in the games industry, I lambasted the PS2 to
my fellow AAA games developers for not even supporting virtual pointer tables,
meaning that virtual functions were impossible. In deriding the platform I
showed my ignorance about the speed trade offs that smarter people than me were
making. It turns out that the constraints of the PS2's architecture changed the
face of games development for the better.

A few virtual calls aren't going to massively slow down a codebase. However, my
code was a mass of tiny virtual calls for trivial operations. Parts of my code
were iterating over every entity in the game with at least three or four
chained virtual function calls each time!

In the new version of the code, I cut out all the virtual methods completely,
sticking to bare C++ method calls. I inlined a lot of these, leaving the game
with fewer longer methods but without the need for the CPU to constantly be
jumping around to figure out what to do.

## Templates are slow (to build)

Templates were introduced to C++ in order to help make parts of the code
generic with respect to type. For example, the supplied vector type in C++ is
a template type, meaning that we can store multiple different types of objects in
the same data structure. This allows us to seperate two concerns: the way the
object is stored and how it works, which partitions complexity for our minds.

Templates reduce the number of lines of code in our programs. They are harder
to understand when reading them later, but the bigger disadvantage is that *they
slow down build time.* The compiler has to effectively copy all the code each
time for each template and do a lot of processing in order to produce efficient
executables out of them.

By cutting out all the templates from my code (including all uses of the C++
Standard Template Library), I've cut down the full build time of the entire game
to about 4 seconds. With a debug loop as short as this, I barely have time to
sip my tea before I'm testing the code I just wrote, and I can change headers
without having to wait 10 minutes for a new build to compile.

## Encapsulation can be unhelpful

Encapsultation is the packing of functions and data into one component. It is
one of the fundamental concepts behing Object Oriented programming.

Much of encapsulation in C++ (and other OO languages) is promoted through the
use of classes with private members to hide data from outside code.

Promoting encapsulation is held up as a pillar of good code design. However, I
think we might be doing encapsulation wrong. I don't think encapsulation should
be at the class or method boundary, but at the data boundary.

Essentially I'm advocating a switch from this style of coding:

![Traditional OO](/files/c-oo.png)

To this style:

![Data transformation](/files/c-data-transformation.png)

It's important to get our architecture right. We encapsulate concepts in the
correct sections of our program and ensure data flows well through the various
pieces. If we use simple value objects (perhaps arrays of data) as the handoff
between different sections of our program, calling methods that transform data
between different types, then our code becomes more isolated and easier to
reason about. It's also far easier to parallelise.

Incorrect encapsulation is worse than no encapsulation at all. Hiding data
behind code limits what the calling code can do. Those constraints can be
helpful, but they can also hinder us. If we get the architecture right and use
data structures to provide bounded contexts to our code, rather than layers of
method abstraction, then we have less need to hide our data from others.

By rearchitecting my application to not require callbacks at all, I've made it
simpler to test and debug. There's less code reuse, but inevitably the concepts
I thought were duplicated were actually subtly different. I'm also treating the
data in batches, looping through arrays of small amounts of data rather than
arrays of objects. Rather than one big loop bouncing up and down the layers of
abstraction for each object (exacerbating the method call overhead, which is
further increased if we are using virtual methods), I have multiple loops doing
one small stage of data transformation each time.

There are no methods in classes: it's all public structs and functions.  I
still have encapsulation, because each stage of data transformation is distinct
from the others, but I've no need to hide my data behind code. 

## Summary

There are some bits of C++ I find useful. Operator overloading is helpful to
clean up verbose code, for example. I still compile my 'mostly C' code using a
modern C++ compiler.

It's the paradigms that C++ promotes and supports through its language features
that aren't for me, and I've doubled the speed of my code as a result.
