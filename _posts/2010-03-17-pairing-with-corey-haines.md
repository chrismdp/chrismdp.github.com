---
layout: post
title: Five things I learnt from Corey Haines
date: 2010-03-17 10:18:00.000000000 +00:00
categories:
- pairing
- code
redirect_from:
- "/2010/03/pairing-with-corey-haines"
- "/2010/03/pairing-with-corey-haines/"
---
Recently I attended [QCon](http://qconlondon.com) and got a chance on the last day to pair with [Corey Haines](http://coreyhaines.com). We worked on a new rails project we're building with a few friends (that's the subject of another post). We'd spent a fair amount of time hanging out, but I hadn't had a chance to sit down and actually code with him. We paired for a couple of hours in the QCon expo area just as everyone was packing up.

Here are a few lessons and some things I picked up.

*REALLY learn vim.* Watching Corey fire around [vim](http://vim.org) was something else: my brain could barely keep up with where the cursor was sometimes. Sometimes it felt like he'd just moved the cursor to where he wanted it to be through Sheer Power of Thought. I'm no slouch in vim, but was impressed by just how much faster I'll be able to go someday, as I continue to practice.

*resource_controller. formtastic. That is all.* These gems take out the legwork of building a thin restful resource-based rails app. You end up with a lot of tests and very little code to worry about. As webapps become more about [javascript and the front-end](/2009/12/rip-web-1-0/), rails apps are becoming thinner and thinner, and these gems make them really fast to write.

*Alias everything.* Corey has a few really useful little bash tricks, like:

{% highlight bash %}
alias c='script/console'
alias r='rake routes | grep'
{% endhighlight %}

..and some others I didn't catch. They save so much time and are so obvious that later I found myself banging 'c' into a console and wondering why it doesn't work. 

The summary of these lessons is another more general one:

*Work to remove whatever constrains you from getting the computer to do what you want.* We need to ensure that there is as little as possible in the way of getting stuff done. Everything else is [yak shaving](http://en.wikpedia.org/wiki/Yak_Shaving): slow typing, tool-illiteracy, whatever. Anytime we're not thinking about the problem, we're wasting time.

And finally, a meta-lesson:

*Extend your pairing gene pool.* It's amazing how much you learn when you pair with someone outside your immediate sphere. Rather like when I first paired with [Enrique](http://blog.nexwerk.com), I learnt about stuff I would never have heard of otherwise. 

I spent two hours working with Corey and it was a pleasure. Sadly we live a few thousand miles apart, but I'm looking forward to remote pairing sessions in the future.
