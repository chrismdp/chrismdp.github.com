---
layout: post
title: "Sol Trader: a continuous deployment story"
date: 2012-03-23 12:13:27 +0000
categories:
  - sol trader
  - windows
  - jenkins
  - products

---

<div class='notice'>
  If you'd like to purchase Sol Trader you can now do so at <a href='http://soltrader.net'>soltrader.net</a>!
</div>

Continous Deployment is difficult, time consuming to set up and tends to require a high level of buy in from your stakeholders in order to trust the work that you're doing.

It's also one of the best things that could ever happen to your project. It prevents bugs, keeps the whole team on their toes, increases buy in and saves masses of time in the long run.

## Sol Trader on windows

For the last few weeks I've been working hard on getting Sol Trader building and running on Windows. I bought a brand new [low-spec Windows 7 PC](http://www.amazon.co.uk/Zotac-ZBOX-ID41-B-ZBOX-ID41-Mini/dp/B004SLVXYE/ref=sr_1_2?ie=UTF8&qid=1332504948&sr=8-2) for this very purpose, and installed [MinGW](http://www.mingw.org) on it in a blaze of optimism.

Why prioritise Windows? Well, apart from the fact that my artist, Aamar, runs Windows, most of the game playing world out there still seem to be stuck on Windows as a platform, so I decided I had to ensure that it should work earlier rather than later. I figured that the longer I left it, the worse it would be to port over.

Turns out I was *so right*. Getting the game running on Windows was extremely hard and fiddly to do, even after only a few weeks development. I'll post my specific experiences writing a cross-platform Rakefile and dealing with all the path issues another time.

After the game finally ran, my first thought was: "I'm never doing that again." If I leave the codebase to diverge again, who knows how hard it will be when it's three times the size with twice as many library dependencies.

What I really want to happen is whenever I push new code it's all checked on Windows to make sure that it compiles and runs without warnings or errors, and runs all the tests to ensure that my code never diverges again...

## Jenkins

Enter [Jenkins](http://jenkins-ci.org). Jenkins is the world's most fabulous build system. There are many out there, but I keep returning to Jenkins as the most powerful and flexible. Plus, it's Java, so it easily runs on Windows, so I can simply install it on the same Windows machine for now.

Most importantly for me, it can build using slave computers, so I installed it and set up my Windows machine as a headless slave using Java Web Start. That was thankfully pretty easy to do, once I'd figured out how to set up the build command so it called the right command. It's extremely easy to set Jenkins up to check for the latest pushed code and run a new build for me.

## Packaging

I have a fairly simple rake task which packages up my app in a windows ZIP:

{% highlight ruby %}
task :dist => [exe] do
  rev = "sol-#{VERSION}-#{fetch('git rev-parse HEAD')[0, 7]}"
  if windows?
    sh "cp /mingw/msys/1.0/local/bin/SDL2.dll ."
    sh "cp /mingw/msys/1.0/local/bin/libfreetype-6.dll ."
    sh "cp /mingw/msys/1.0/local/bin/libRocketCore*.dll ."
    sh "cp /mingw/msys/1.0/local/bin/libRocketControl*.dll ."
    sh "cp /mingw/bin/SDL2_image.dll ."
    sh "cp /mingw/bin/libz-1.dll ."
    sh "cp /mingw/bin/libgcc_s_dw2-1.dll ."
    sh "cp /mingw/bin/libstdc++-6.dll ."
    sh "zip -or #{rev}.zip data shaders media #{exe}.exe *.dll"
    sh "mv #{rev}.zip /c/dropbox/sol/builds/"
  end
end
{% endhighlight %}

This dumps a ZIP file containing all the different DLLs plus the executable and assets into Dropbox for Aamar to pick up. They're helpfully named after the latest commit (the latest one is `sol-0.1-0ead098.zip`) so Aamar and I can refer to them easily.

Now when I push the code, I only have to wait a few minutes and Dropbox informs me of a new build available. Bliss.

![Jenkins running](/files/sol-jenkins-build.png)

## Next steps

* I've an iMac at home which we use as a family PC, but they have SSH, right? There's nothing to stop me utilising that as my slave machine for building OSX builds automatically. Jenkins allows you to build multiple configurations at the same time, so soon there will be an OSX application appearing alongside the Windows ZIP. Just don't tell my son when he's playing Minecraft...
* I'd like to run the game for 100 frames or so just to ensure that it's starting, allocating all its memory and exiting cleanly without memory leaks.
* [Valgrind](http://valgrind.org) support would be fantastic to check for leaks.
* A screenshot showing the running game to double triple check it would be a great addition. There's a Jenkins plugin for this, which I've not tried yet.

This is all important infrastructure getting ready for a beta release. Putting in the effort now makes the job of releasing new builds so much easier when the pressure is on and I'm trying to get bugfixes out to multiple platforms.

What do you think of the system so far? Any improvements I could make?

<div class='notice'>
  If you'd like to purchase Sol Trader you can now do so at <a href='http://soltrader.net'>soltrader.net</a>!
</div>
