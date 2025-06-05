---
layout: page
title: "Actionable AI help, without the hype."
permalink: /
excerpt: "I help CTOs, engineering managers, and technical founders cut through AI hype and deliver results for their teams in minutes a week."
redirect_from:
  - /about
  - /coaching
  - /cto

---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-full.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width: 50%; max-width: 250px;'/>

AI is changing everything, but most of what you hear is noise. If you are a CTO, engineering manager, or technical founder and feel pressure to deliver AI results, you are not alone. New AI products appear every day, and it is hard to know what is real and what is hype.

I have spent years as a founder and CTO. I've tested many AI tools and techniques, and learned what actually works now. I use AI every day to speed up my work, and I can help your team do the same.

For more [view my services](/services) or join my newsletter below:

<div class="rm-area-embed-subscribe"></div>

## Hi, I'm Chris.

- I co-founded [Cherrypick](https://cherrypick.co), a VC-backed AI startup in food retail.
- I bootstrapped a software agency to $1M ARR as CEO, hiring a team of 12. The company became internationally known for great software practices.
- I scaled [Gower Street](https://gower.st), a film data analytics company, as CTO from a handful of people to over 50 staff.
- I have [shipped two LLM-based AI systems](/how-to-build-a-robust-llm-application) to production, complete with evals.

**_"Fantastic at building self-sufficient teams and giving them what they need."_** -- [Tadas T](https://www.linkedin.com/in/tamosauskas/)

**_"If you're looking for someone to help build a great team, or you need someone experienced to help develop a sound tech strategy, I would thoroughly recommend Chris."_** -- [Roisi P](https://www.linkedin.com/in/roisiproven/)

**_"Chris has clearly learned a lot about the world of being a delivery-focused CTO"_** -- [Ian O](https://www.linkedin.com/in/ianozsvald/)

<!--more-->
---

{% for post in site.posts limit:3 %}
   <div class="post-preview py-4">
   <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>

   <div style='font-style: italic' class="pb-1 post-date">
   {% assign original_date = post.path | split: "/" | last | split: "-" | slice: 0, 2 | join: '' %}
   {% assign current_date = post.date | date: "%Y%m" %}
   {% if original_date != current_date %}Updated: {% endif %}
   {{ post.date | date: "%B %Y" }}
   </div>
   {% if post.badges %}{% for badge in post.badges %}<span class="badge badge-{{ badge.type }}">{{ badge.tag }}</span>{% endfor %}{% endif %}
   {{ post.excerpt }}
   <a class='underline' href="{{ site.baseurl }}{{ post.url }}">Read more</a>
   <div style="clear: both;"></div>
   </div>
{% endfor %}

<hr>

See the <a href="{{ site.baseurl }}/all/">Archive</a> for more articles. You can also find me on [BlueSky](https://bsky.app/profile/chrismdp.com), [X](https://x.com/chrismdp) and [LinkedIn](https://linkedin.com/in/chrisparsons). Subscribe with <a href="{{ site.baseurl }}/feed.xml">RSS</a> to keep up with the latest.

{% include ai-newsletter-short.html %}