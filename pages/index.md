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

I am a builder and four time founder with 25 years in tech leadership:

- I co-founded [Cherrypick](https://cherrypick.co) a VC-backed food retail startup
- I bootstrapped a software company to $1M ARR as CEO, hiring a team of 12. The company became internationally known for great software practices
- As CTO, I scaled [Gower Street](https://gower.st), a film data analytics company, from a handful of people to over 50 staff
- I advise multiple startups at board level
- I have trained hundreds of developers in great product and development practices
- I have run tech organisations consisting of data teams, cross-functional product teams, and engineering teams.
- I have personally built and shipped two production level generative AI systems.

## Subscribe to my newsletter

__In 2025, I am learning how to use AI to build agents and products in weeks, not years.__

The future of work is being reshaped before our eyes. Semi-autonomous agents are already changing the world. I want to be part of that transformation.

Will you join me? Follow along with weekly field notes as I share stories and learnings as I go:

<script async data-uid="d90200305f" src="https://chrismdp.kit.com/d90200305f/index.js"></script>

## I help companies get ahead with their AI and tech

I spend a limited amount of my time helping companies with what I've learned about tech, AI and building businesses.

__I have a couple of open slots right now.__ To find out more about how I can help, spend thirty minutes with me and get some instant advice:

{% include book-call-button.html %}

**_"Fantastic at building self-sufficient teams and giving them what they need."_** -- [Tadas T](https://www.linkedin.com/in/tamosauskas/)

**_"If you're looking for someone to help build a great team, or you need someone experienced to help develop a sound tech strategy, I would thoroughly recommend Chris."_** -- [Roisi P](https://www.linkedin.com/in/roisiproven/)

**_"Chris has clearly learned a lot about the world of being a delivery-focused CTO"_** -- [Ian O](https://www.linkedin.com/in/ianozsvald/)


<!--more-->

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
