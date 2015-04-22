---
layout: post
title: "Why I ditched all the build tools in favour of a simple script"
date: 2015-04-22 11:42:46 +0100
categories:
  - code
  - tools
  - game development
  - continuous integration
  - sol trader

---

[![white elephant](/files/white-elephant.jpg)](https://www.flickr.com/photos/pattoise/10667319965/)

Build tools are wonderful and impressive constructions. We developers invest colossal amounts of time, effort and code into their creation and maintenance.

Perhaps a lot of this work is unnecessary.

On [Sol Trader](http://soltrader.net), by ditching the complex dependency checking compilation system I was doing in favour of a simple homegrown script, I cut my build time from several minutes down to 5 seconds.

I'm not talking about continuous integration tools such as [Jenkins](http://jenkins-ci.org), but tools such as [CMake](http://cmake.org), [Boost.Build](http://www.boost.org/build/doc/html/) and [autotools](http://en.wikipedia.org/wiki/GNU_build_system). Perhaps these build tools are white elephants? They require endless maintenance and tinkering: does this outweigh their actual usefulness?

## Incremental compilation: the end of the rainbow

One of the main aims of a compilation tool is to allow us to divide all the pieces of a system up into component parts to be built individually (another main aim is portability, which I'll address below). This allows us to only build the part of the code which changed each time, and link all the compiled pieces together at the end.

However every time we build a source file, we have to grab a piece of code, grab *all the dependencies of that code* from disk. The disk is probably the slowest thing in our machines, and we have to grab everything from desk every time, for each source file we're building. If we're building a lot of files, this can get very slow.

The second problem with this is when we change an often-reused piece of code, such as a header file, we have to compile the whole lot again. In order to cut the amount of things to build down, we can set up complex dependency management systems to try to limit the amount of things built. We can also set up a precompiled header which tries to minimise disk access by building a lot of the code in advance for us, but more and more of our time is handling the side effects of pushing for an incremental build system.

Trying to get a build tool set up is like searching for a pot of gold at the end of a rainbow, which gets further away no matter how much effort we put into finding it. Even when it's working, it's not that fast, and it requires constant tinkering to get it right.

## How I build code now: the Unity build

How about instead of building incrementally, we *build everything every time?* Sounds counter-intuitive, doesn't it? It's actually faster, easier to maintain, and doesn't require setting up a complicated build tool.

We create one `Unity.cpp` file. This includes all the C files and headers that I wish to build. We build that one file each time, and then link it with the 3rd party libraries. Done. It takes about 3-4 seconds to run, or 10 seconds on the Jenkins server.

Now, when I change a header, the script just builds everything again, so it doesn't take any long that a few seconds to see the effects of any change I want to make.

## Caveats

*"Strategy is about making choices, trade-offs; it's about deliberately choosing to be different."*

-- Michael Porter

There are a few caveats with Unity builds that we should be aware of:

**One compilation unit means no code isolation**

The `static` keyword will stop working as we expect: we won't be able to constrain variables and methods to one file any longer. The [power of good naming](/2012/09/-the-power-of-good-naming) helps us out here. We also have to be disciplined about keeping our code modular and not referring to code that we shouldn't.

**We still need to discover platform-specific properties**

On an open source project which must be built everywhere, we're never going to get away with something as simple as this: we're going to need to check to see what headers exist and which libraries are available.

However, there's no reason we can't set up `make` to do a simple unity build such as this one.

Also, many of these portability problems we patch over with our build tools stem from the fact that our code wasn't correctly written to be portable in the first place. Also, many build systems still in wide use today have a lot of cruft left over from the 1980s - do we really still need to check for the presence of `<stdlib.h>`?

Additionally, in the case where we can control our build environment, it becomes even easier: we simply create a build script for each compilation platform we need to support (a `build.bat` for Windows, for example).

## Sol Trader's Unity build setup

This is my current build setup for [Sol Trader](http://soltrader.net) in its entirety.

{% highlight bash %}

#!/usr/bin/env bash

MACOSX_DEPLOYMENT_TARGET=10.6
CC=clang++
EXE=sol
CFLAGS=" -DGLEW_STATIC -DSOL_SLOW -DCURL_STATICLIB -DNDEBUG -D_GNU_SOURCE=1 -D_THREAD_SAFE -g -O0 -I.. -I../src -I ../lib/include -I ../dist/build/include -I../dist/build/include/boost -O0 -I ../dist/build/include/freetype2 -I ../dist/build/osx/include -I ../dist/build/osx/include/SDL -Wall -Werror -Wno-unused-private-field -Wno-unused-variable -Wno-missing-braces -mmacosx-version-min=10.6 -F../dist/build/osx/frameworks"

LIBS="../dist/build/osx/lib/libSDL_mixer.a ../dist/build/osx/lib/libvorbis.a ../dist/build/osx/lib/libogg.a ../dist/build/osx/lib/libvorbisfile.a ../dist/build/osx/lib/libyaml-cpp.a ../dist/build/osx/lib/libRocketCore.a ../dist/build/osx/lib/libRocketControls.a ../dist/build/osx/lib/libRocketDebugger.a ../dist/build/osx/lib/libfreetype.a ../dist/build/osx/lib/libpng15.a ../dist/build/osx/lib/libboost_system-mt.a ../dist/build/osx/lib/libboost_filesystem-mt.a ../dist/build/osx/lib/libboost_thread-mt.a -l SDL_image -l SDLmain -l SDL -L ../dist/build/osx/lib ../lib/libcurl.a ../dist/build/osx/lib/libz.a -Wl,-framework,Cocoa -Wl,-framework,OpenGL -headerpad_max_install_names"

set -e
set -x

mkdir -p build
pushd build
$CC $CFLAGS -c ../src/Unity.cpp -o Unity.o 2>&1 | sed 's|../src|src|'
$CC $CFLAGS -o ../$EXE Unity.o ../src/main.cpp $LIBS 2>&1 | sed 's|../src|src|'
date
popd

{% endhighlight %}

This is working fine for me right now. It'll need expanding on in the future, but instead of spending endless time screwing with my build system now, I'm actually adding game features instead.

Want to hear the other side of the debate? Here's a well-argued opposing point of view: [the evils of unity builds](http://engineering-game-dev.com/2009/12/15/the-evils-of-unity-builds).
