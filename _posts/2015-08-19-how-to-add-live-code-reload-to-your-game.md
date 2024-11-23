---
layout: post
title: How to add live code reload to your game
date: 2015-08-19 09:55:34.000000000 +01:00
categories:
- sol trader
- game development
- code
- c++
- productivity
redirect_from:
- "/2015/08/how-to-add-live-code-reload-to-your-game"
- "/2015/08/how-to-add-live-code-reload-to-your-game/"
---
Adding live code reloading is one of the best things I did when working on my current game, [Sol Trader](http://soltrader.net).

Live code reload reduces our debug loop down to milliseconds. Now when I recompile the game, it notices I've done so *and loads new code whilst the game is still running.* Here's a demo:

![gif demo](http://i.imgur.com/D6hGkhA.gif)

Thanks to [Casey Muratori](http://mollyrocket.com) (again) and his excellent [Handmade Hero](http://handmadehero.org) series for teaching me the basics, and to [this github project](https://github.com/itfrombit/osx_handmade_minimal) for demonstrating how to do it in OSX, my development platform of choice.

There are a few architecture changes that we'll need in order to put this feature in our code. Here's how I did it.

## Splitting our game code from our platform

Sol Trader now has a clearly defined platform layer, separate from the game. The game code itself knows nothing about the platform at all and it passed in everything it needs in order to calculate what's next. Here's the method that we call to run a game loop:

{% highlight c++ %}

bool gameUpdateAndRender(Memory* memory, v2i screenDim, Input* input);

{% endhighlight %}

The update and render call takes some `Memory`, the screen dimensions and the input that we received this frame from the player. It is the job of this method to render the next frame to the screen, in under 16ms.

`Memory` is just a big chunk of raw memory allocated by the platform layer at the start of the game. The `gameUpdateAndRender` function is free to do what it likes with this space. It's important to note that it's *persistent across live reloads* which means that all state should be saved here. The game is not allowed to allocate any memory itself, it has to use the memory given to it.

`gameUpdateAndRender` actually is implemented as a call into a shared library (a DLL on windows, or a dylib on Linux/OSX) using a #define trick I learnt from Handmade Hero:

{% highlight c++ %}

// Platform.h
#define GAME_UPDATE_AND_RENDER(name) bool name(Memory* memory, v2i screenDim, Input* input)
typedef GAME_UPDATE_AND_RENDER(GameUpdateAndRender);

// Game.cpp
extern "C" GAME_UPDATE_AND_RENDER(GAME_updateAndRender) {
  // game code here
}

{% endhighlight %}

(We need the `extern "C"` here to stop the compiler from mangling the name, so we can find it in the shared library.)

## Running the game code

This is a cut down OSX version of the platform layer I'm using. Similar code exists for other platforms:

{% highlight c++ %}

// Platform.cpp
void OSX_loadGameCode(GameCode* game, char const* path) {
  if ((game->code = dlopen(path, RTLD_LAZY | RTLD_GLOBAL))) {
    game->updateAndRender = (sol::GameUpdateAndRender*)dlsym(game->code, "gameUpdateAndRender");
    game->lastWriteTime = OSX_lastWriteTime(gameCodePath);
  }
}

void main() {
  Memory memory;
  allocateMemory(&memory);

  initOpenGL();
  v2i screenDim = createGameWindow();

  GameCode game;
  char const* gameCodePath = "soltrader.dylib";
  OSX_loadGameCode(game, gameCodePath);

  // Main loop
  while (!quit) {
    Input newInput;
    getInput(&newInput);

    // Check if the game has been recompiled
    time_t newWriteTime = OSX_lastWriteTime(gameCodePath);
    if (newWriteTime != game->lastWriteTime) {
      OSX_unloadGameCode(&game);
      OSX_loadGameCode(&game, gameCodePath);
    }

    if (game.updateAndRender) {
      game.updateAndRender(&memory, screenDim, &newInput);
    }
  }
}

{% endhighlight %}

At the heart of it, it's a standard game loop. We first allocate enough memory using one big `alloc` call at the beginning. This is all platform specific code, so it's ok to use OSX, Linux or Windows specific calls here. We figure out our screen dimensions from the platform, create a window, and initialise OpenGL or whatever graphics library we're using.

Then we load the code using `dlopen` and if that succeeds, we find the `gameUpdateAndRender` function and save the location. In the main loop, assuming that all worked, we call the saved function with the info it needs to render the frame.

## Building the shared library

Here's how the `build.sh` script looks:

{% highlight bash %}

// Build the shared library
$CC $CFLAGS -dynamiclib ../src/Unity.cpp -o ../libsol.dylib $LIBS

// Build the executable
$CC $CFLAGS -o ../$EXE ../src/platforms/sdl2/Application.cpp $LIBS

{% endhighlight %}

We build the shared library containing *only* the game code, not the platform code. We then use the platform code to load and run the shared game library.

## Summary: everyone should have live code reload

This is an amazing way to develop games. For too long in the past I have sat watching a long compile, then ploughed through the game from the main menu, to find the bug I'm trying to fix, only to find that I've made a stupid error and have to start again. We need to [find fun as fast as possible](/2015/04/how-to-choose-between-realism-and-fun/) - anything we can do to reduce the debug loop is a good thing.

Live code reload also does away with much of the need to use a scripting language (fast feedback). I don't have any designers who don't write C (it's just me!) so I haven't implemented one for this game. I also don't need any GUI configuration files for layout, it's [all just implemented in C](/2015/08/why-i-rewrote-sol-trader-s-gui-from-scratch) with live code reload for positioning tweaks.

Trust me: once you've tried it, you'll never go back.
