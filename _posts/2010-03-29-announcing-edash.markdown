---
layout: post
title: Announcing edash
date: 2010-03-29 22:05:00.000000000 +01:00
categories:
- information radiator
redirect_from:
- "/2010/03/announcing-edash"
---
I've been hinting at the dashboard application I've been hacking on recently and after showing it off to a few people at the [Scottish Ruby Conference](http://scottishrubyconference.com) it's about time I released it open source.

## Introducing edash

![edash screenshot](/files/edash-1.png)

This is the version currently running on a screen at [Eden](http://edendevelopment.co.uk). 

*IMPORTANT NOTE: This application only works on [Chrome](http://google.com/chrome).* There is enough browser specific hackery to render it unusable in other browsers currently. Patches to fix this are most welcome.

That said, I've put together a short screencast showing it off, along with how to get it running:

<object width="550" height="344"><param name="allowfullscreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=10535751&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=c9ff23&amp;fullscreen=1" /><embed src="http://vimeo.com/moogaloop.swf?clip_id=10535751&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=c9ff23&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="550" height="344"></embed></object>

<p><a href="http://vimeo.com/10535751">edash demo and usage instructions</a> from <a href="http://vimeo.com/user2596622">Chris Parsons</a> on <a href="http://vimeo.com">Vimeo</a>.</p>

## Getting it running

Here's a minimal set of steps to get it running:

{% highlight bash %}
gem install sinatra haml json eventmachine em-http-request
git clone git://github.com/edendevelopment/edash.git
cd edash
git submodule update --init
# runs the websocket server, make sure port 8080 is readable from where you are. Use nohup to run as a daemon.
scripts/server &
# Run rackup in place, or use your favourite rack-compatible server
rackup &
# post a message to the server. Add a form of this to your build hooks.
curl -d "project=<project>" -d "status=<pass|fail|building>" [-d "author=Name <email>"] -- http://localhost:9292/build
{% endhighlight %}

Check out the screencast for a walkthrough.

## Under the hood

The code is [on github](http://github.com/edendevelopment/edash).

Check it out and let me know if you find it useful. I'm trying to keep it pretty thin and build server agnostic: it should work with a number of build servers out of the box just by configuring (hacking) your server to fire off HTTP posts as shown in the screencast.

I'd welcome patches and fixes: it should be under fairly active development in the next few weeks. The plan is to add a generic statistic tracking module that will allow us to keep track of MetricFu stats, and you to keep track of almost anything... watch this blog for updates.


