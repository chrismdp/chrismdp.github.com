---
layout: post
title: Cucumbers with personality
date: 2011-04-18 15:17:31.000000000 +01:00
categories:
- cucumber
- personas
- agile
- ux
redirect_from:
- "/2011/04/cucumbers-with-personality"
---
<p><i>"Personality is everything in art and poetry."</i></p>

-- [Johann Wolfgang von Goethe](http://en.wikipedia.org/wiki/Johann_Wolfgang_von_Goethe)

One element of Cucumber feature-writing that is often neglected is the *role.* This is the section that sits between the well known *In order that* and *I want to.*

It's very easy to concentrate on *what* we wish to accomplish, and *why* we want to do it. The role that we're in, however, affects the *way* that we do it, and how the action is perceived as it is carried out. It is in fact, *the key to user experience of the feature.*

How often have we lazily written features like this?

{% highlight text %}
In order to know how much money I am making
As a user
I want to see a report of widgets sold this month
{% endhighlight %}

What we want is clear, as is why we want it. What's not clear is who is doing the asking, and therefore there's no clue as to what the user experience should be like.

## A sprinkling of personality

Next time we find ourselves writing "as a user", let's take a minute to stop and think whether we can be more specific.

Consider this feature:

{% highlight text %}
In order to know how much money I am making
As the head of the company
I want to see a report of widgets sold this month
{% endhighlight %}

This guy is time poor, and just wants the facts, right now. Sure, he might want it to look good, but doesn't care much beyond the numbers.

Now how about this one?

{% highlight text %}
In order to know how much money I am making
As a design assistant responsible for collating reports
I want to see a report of widgets sold this month
{% endhighlight %}

This person possibly has a little more time on their hands, and their overriding concern might be to impress their boss. Therefore the aesthetics of the report layout might be very important, and it might not matter so much if the page is slower to load.

## Personas driving stories

On a recent project for a coaching company we took this a step further. We produced some great personas during the inception (Bob Coachee, Jean Coach), and then went so far as to use them in our features:

{% highlight text %}
In order to know who I am coaching next
As Jean the coach
I want to see a calendar showing today's appointments
{% endhighlight %}

Because everyone on the project knew the background behind these characters, the resulting features communicated a lot of knowledge. We all knew exactly how they were using the system, and what they needed out of it. We had about six personas in total, and they proved very helping in communicating the user experience of the feature to the team.

Do you create specific personas for your projects, and have you ever used them when writing your features? Did you see a benefit?
