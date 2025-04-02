---
layout: page
title: "I help CEOs and founders transform their tech teams."
permalink: /
excerpt: "I help rebuild momentum, gain clarity, and restore confidence across tech organisations large and small."
redirect_from:
  - /about
  - /services

---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-2022-cropped.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width:200px'/>

If your tech is worrying you, I can help.

I work with CEOs, founders and tech leaders to transform tech teams. I rebuild momentum, create clarity, and restore confidence. I cut through the noise, reframe how the team works and think, and radically reduce time to value.

__Transform your tech team from a concerning cost centre into a powerful growth engine.__

I am an experienced founder, former CEO and CTO. I know what it takes to turn a tech team from a concerning cost centre into a powerful growth engine.

Spend thirty minutes with me and learn exactly how I can help:

{% include book-call-button.html %}

**_"Fantastic at building self-sufficient teams and giving them what they need."_** -- [Tadas T](https://www.linkedin.com/in/tamosauskas/)

**_"If you're looking for someone to help build a great team, or you need someone experienced to help develop a sound tech strategy, I would thoroughly recommend Chris."_** -- [Roisi P](https://www.linkedin.com/in/roisiproven/)

**_"Chris has clearly learned a lot about the world of being a delivery-focused CTO"_** -- [Ian O](https://www.linkedin.com/in/ianozsvald/)

<script async data-uid="dadc23073e" src="https://chrismdp.kit.com/dadc23073e/index.js"></script>

<!--more-->

## Some of the reasons we should talk

Give me a call if any of these are true for you, or if something else is troubling you with your tech team:

- Delivery has slowed to a crawl
- Your tech costs are out of control
- The CEO and technical leaders aren not aligned
- Your AI/LLM projects never quite seem good enough
- The tech team culture is heading in the wrong direction

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
