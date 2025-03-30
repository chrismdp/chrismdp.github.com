---
layout: page
title: "Helping tech teams become fast, focused and unstoppable."
permalink: /
excerpt: "I help rebuild momentum, gain clarity, and restore confidence across tech organisations large and small."
redirect_from:
  - /about

---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-2022-cropped.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width:200px'/>

I rebuild momentum, clarity, and confidence across tech organisations that have lost their mojo. I do this through coaching, workshops, and helping the team reshape how they work and think.

**_"Fantastic at building self-sufficient teams and giving them what they need."_** -- [Tadas T](https://www.linkedin.com/in/tamosauskas/)

**_"If you're looking for someone to help build a great team, or you need someone experienced to help develop a sound tech strategy, I would thoroughly recommend Chris."_** -- [Roisi P](https://www.linkedin.com/in/roisiproven/)

**_"Chris has clearly learned a lot about the world of being a delivery-focused CTO"_** -- [Ian O](https://www.linkedin.com/in/ianozsvald/)

<script async data-uid="dadc23073e" src="https://chrismdp.kit.com/dadc23073e/index.js"></script>

<!--more-->

## Recent articles

You can also find me on [BlueSky](https://bsky.app/profile/chrismdp.com), [X](https://x.com/chrismdp) and [LinkedIn](https://linkedin.com/in/chrisparsons). Subscribe with <a href="{{ site.baseurl }}/feed.xml">RSS</a> to keep up with the latest.

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

See the <a href="{{ site.baseurl }}/all/">Archive</a> for more articles.
