---
layout: post
title: Effective bloom in OpenGL for Sol Trader
date: 2012-02-02 16:28:30.000000000 +00:00
categories:
- products
- c++
- code
- opengl
- bloom
- sol trader
- game development
redirect_from:
- "/2012/02/effective-bloom-in-open-gl-for-sol-trader"
---
<div class='alert alert-block alert-info'>
  <h2>TL;DR</h2>
  <p>Skip to the <a href='#pictures'>pictures</a>.</p>
</div>

I've been working on and off on [Sol Trader](http://soltrader.net) ([C++ version](/2012/01/why-i-switched-from-ruby-back-to-c-plus-plus/)) for about a month now. At the beginning of this week, I've been coded up an effective type formatting system using freetype2 natively with OpenGL, which is now in and showing even rather esoteric fonts nicely.

The second half of this week was spent adding on a bloom filter to the graphics engine.

## Bloom filtering: making your world stand out

A bloom filter causes bright areas of the image to 'take over' their surrounding area, simulating the high dynamic range of real light. It stops your game world from looking dull and flat and really makes it stand out. See [this article](http://www.gamasutra.com/view/feature/2107/realtime_glow.php) for some nice screenshots from Tron 2.0 - it can also be used for all sorts of glow and blur effects.

So how's it done? The trick is to render your scene to a texture, rather than to the screen. Once you've done that, you blur and downsample that texture a few times, and then display the results combined with the original texture.

Specifically, this is the process my bloom filter follows:

* Render to a texture
* Copy that texture to two more textures, one a quarter of the screen size, and one an eighth of the screen size.
* Blur the two smaller textures using gaussian blur. There are [clever techniques](http://prideout.net/archive/bloom/) which mean you only need six texture lookups to perform a 5x5 gaussian blur. Texture lookups are expensive, so it's worth doing as few as possible.
* Add all these textures together and add an exposure function to cause the white to saturate for strong color values.

Writing the initial bloom filter was fairly easy. Making it fast was *hard:* you have to work at combining the different aspects of the effect to get what you want, with the absolute minimum of effort for your graphics card. My first attempt ran at a paltry 27 frames a seconds, although it looked very nice: I eventually managed to get it to the point where it runs in roughly 150 frames per second and still looks 80% as good.

<div name="pictures">
  <h2>What's the result?</h2>
</div>

A picture is worth a thousand words, so here are three:

![bloom-1](/assets/img/sol-trader-bloom-1.png)

![bloom-2](/assets/img/sol-trader-bloom-2.png)

![bloom-3](/assets/img/sol-trader-bloom-3.png)

I've deliberately upped the bloom exposure to show off the effect: it is much more obvious when it's moving. Hopefully you can see the volcanic eruptions on Venus are making the outline of the players' ship that much more hazy. The label of the planet also currently has the bloom effect applied: I'll be able to turn that off when I have a more functional GUI in place.

I plan to use this effect for all sorts of things: laser fire, explosions, you name it.

## Next...

I'm going to tackle the gui. I now have AI characters with names trading on Earth's main commodity market: it's time the player joins them in making trades.

<div class='alert alert-info'>
  If you'd like to purchase Sol Trader you can now do so at <a href='http://soltrader.net'>soltrader.net</a>!
</div>
