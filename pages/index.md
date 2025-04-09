---
layout: page
title: "Hi, I'm Chris."
permalink: /
excerpt: "I help teams deliver fast, reliable and profitable AI products and processes."
redirect_from:
  - /about
  - /services
  - /coaching
  - /cto

---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-full.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width: 50%; max-width: 250px;'/>

I've been a tech leader for 25 years. I've seen what works, and what doesn't.

I've also seen what happens when a new technology comes along and transforms the world. The ChatGPT launch in November 2022 was one of those moments.

I'm a builder and five time founder. I've run data teams, product teams, and engineering teams. I was struck by the raw potential I saw, and knew then the rest of my career would likely be defined by this technology.

I am determined to learn how to use AI to create better products, think differently and work more efficiently, and how to build AI _into_ products so others can benefit.

## How to get ahead with AI

Sign up to my newsletter and join me on the journey of learning to use AI well in your working life, in your processes and in your products. Get one quick story, one idea, and one question every week.

<script async data-uid="d90200305f" src="https://chrismdp.kit.com/d90200305f/index.js"></script>

## I help businesses build reliable AI systems.

I have worked for years as a founder, CEO and CTO, and I use that experience to guide teams to amazing AI products.

I've built multiple production-level AI systems, and I've seen what works and what doesn't.

Spend thirty minutes with me, get some instant advice, and learn more about how I can help you:

{% include book-call-button.html %}

**_"Fantastic at building self-sufficient teams and giving them what they need."_** -- [Tadas T](https://www.linkedin.com/in/tamosauskas/)

**_"If you're looking for someone to help build a great team, or you need someone experienced to help develop a sound tech strategy, I would thoroughly recommend Chris."_** -- [Roisi P](https://www.linkedin.com/in/roisiproven/)

**_"Chris has clearly learned a lot about the world of being a delivery-focused CTO"_** -- [Ian O](https://www.linkedin.com/in/ianozsvald/)

<!--more-->

## Some of the reasons we should talk

Give me a call if any of these are true for you, or if something else is troubling you with your tech team:

- Your AI team has stopped shipping
- Your LLM costs are out of control
- The CEO and technical leaders aren't aligned
- You are endlessly fiddling with LLM prompts
- Your AI/LLM output never quite seem good enough
- You're not sure how to get started an AI project

## Recent articles

{% for post in site.posts limit:3 %}
   <div class="post-preview py-4">
   <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>

   <div style='font-style: italic' class="pb-1 post-date">
   {% assign original_date = post.path | split: "/" | last | split: "-" | slice: 0, 2 | join: '' %}
   {% assign current_date = post.date | date: "%Y%m" %}
   {% if original_date != current_date %}Updated: {% endif %}
   {{ post.date | date: "%B %Y" }}
   </div>
   {% if post.badges %}{% for badge in post.badges %}<span class="badge badge-{{ badge.type }}">{{ badge.tag }}</span>{% endfor %}{% endif %}
   {{ post.excerpt }}
   <a class='underline' href="{{ site.baseurl }}{{ post.url }}">Read more</a>
   </div>
{% endfor %}

<hr>

See the <a href="{{ site.baseurl }}/all/">Archive</a> for more articles. You can also find me on [BlueSky](https://bsky.app/profile/chrismdp.com), [X](https://x.com/chrismdp) and [LinkedIn](https://linkedin.com/in/chrisparsons). Subscribe with <a href="{{ site.baseurl }}/feed.xml">RSS</a> to keep up with the latest.
