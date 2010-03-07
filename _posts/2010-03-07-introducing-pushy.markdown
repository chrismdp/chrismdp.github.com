---
layout: post
title: Introducing Pushy - github notifications to google wave
date: 2010-03-07 20:18:00 +00:00
categories:
  - google wave
  - coding
---
I've been having a bit of a love affair with [Google Wave](http://wave.google.com) recently. Like most people I watched the [long introductory video](http://wave.google.com/about.html#video), then tried out the sandbox last July and didn't really get it. I then read [this interesting post](http://blog.cubeofm.com/on-how-google-wave-surprisingly-changed-my-li) which spurred me on to try using it for actual work.

Guess what? It works. Our conversations have become more structured and organised. We're finding that it does help with keeping everything together in one place, and is more 'alive' somehow than a traditional wiki. 

So I thought: "Wouldn't it be cool if you could have your github messages popping up in wave?"

So here's the results of my handiwork: Pushy.

In simple terms, it's a robot which accepts any form of HTTP post and adds the content as a new message on the wave. It has special handling for github post-receive hooks: it formats them nicely using a gadget.

## How to use it

Log on to [wave.google.com](http://wave.google.com) and add pushyrobot@appspot.com to a new wave. The robot will add a message giving you the URL to post to:

![Pushy's receive message](/files/pushy-1.png)

Then, when you post to this url (here I'm using curl):

{% highlight bash %}$ curl -d "testing pushy" http://pushyrobot.appspot.com/push/googlewave.com/fjWFoDWkf{% endhighlight %}

It will add the message to the wave:

![The message appears](/files/pushy-3.png)

If you're using the github notifications, simply add the URL verbatim to your project's service hooks as a Post-Receive hook:

![Github service hook configuration page](/files/pushy-4.png)

Click "Test Hook" and the wave will update. Any new commits to this project should now appear.

Here's what the commit messages for github commits look like:

![Github commit message view](/files/pushy-5.png)

## Source code

The source code is at [github.com/chrismdp/pushy](http://github.com/chrismdp/pushy). It's my first Python project and first App Engine deployment, so be gentle :) I'd welcome forks and patches: especially if you extend the special formatting for other services.

Enjoy! Do let me know if you use it for anything useful. 

*UPDATE:* The wave forum post discussing the robot is [here](http://bit.ly/bKCOkV).
