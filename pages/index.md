---
layout: page
title: "Hi, I'm Chris."
permalink: /
excerpt: "I help teams deliver fast, reliable and profitable AI products and processes."
redirect_from:
  - /about
  - /coaching
  - /cto

---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-full.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width: 50%; max-width: 250px;'/>

I'm a four time founder with 25 years in tech leadership.

__I write a weekly newsletter on building insanely fast with AI, and I [help 1-2 founders a month](/services) to get their tech and AI on track.__

- I co-founded [Cherrypick](https://cherrypick.co), a VC-backed AI startup in food retail.
- I bootstrapped a software agency to $1M ARR as CEO, hiring a team of 12. The company became internationally known for great software practices.
- I scaled [Gower Street](https://gower.st), a film data analytics company, as CTO from a handful of people to over 50 staff.
- I have [shipped two LLM-based AI systems](/how-to-build-a-robust-llm-application) to production, complete with evals.


**_"Fantastic at building self-sufficient teams and giving them what they need."_** -- [Tadas T](https://www.linkedin.com/in/tamosauskas/)

**_"If you're looking for someone to help build a great team, or you need someone experienced to help develop a sound tech strategy, I would thoroughly recommend Chris."_** -- [Roisi P](https://www.linkedin.com/in/roisiproven/)

**_"Chris has clearly learned a lot about the world of being a delivery-focused CTO"_** -- [Ian O](https://www.linkedin.com/in/ianozsvald/)

<script async data-uid="dfec29bd93" src="https://chrismdp.kit.com/dfec29bd93/index.js"></script>

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
