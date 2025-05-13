---
layout: page
title: "I help people get ahead with AI."
permalink: /
excerpt: "I help transform your business and team with AI in just a few minutes a week."
redirect_from:
  - /about
  - /coaching
  - /cto

---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-full.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width: 50%; max-width: 250px;'/>

AI has changed the world forever. New AI products come out every day. Everyone else seems to be moving fast and it's easy to feel left behind.

I've dedicated myself to learning the very latest AI tools and techniques and have used my experience as a founder and CTO of multiple businesses to separate out hype from what works now.

__I've applied what I've learned so far to my own businesses, and it's transforming everything. It can for you too.__

Sign up, and I'll send you more.

<div style="clear: both; background-color: #f8f8f8; padding: 1em 2em 1em 2em; border-radius: 8px;">

<script async data-uid="d90200305f" src="https://chrismdp.kit.com/d90200305f/index.js"></script>

<small style="display: block; text-align: center;">I'll never spam you (promise) and you can unsubscribe at any time.</small>

</div>


## Hi, I'm Chris.

- I co-founded [Cherrypick](https://cherrypick.co), a VC-backed AI startup in food retail.
- I bootstrapped a software agency to $1M ARR as CEO, hiring a team of 12. The company became internationally known for great software practices.
- I scaled [Gower Street](https://gower.st), a film data analytics company, as CTO from a handful of people to over 50 staff.
- I have [shipped two LLM-based AI systems](/how-to-build-a-robust-llm-application) to production, complete with evals.


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
   <div style="clear: both;"></div>
   </div>
{% endfor %}

<hr>

See the <a href="{{ site.baseurl }}/all/">Archive</a> for more articles. You can also find me on [BlueSky](https://bsky.app/profile/chrismdp.com), [X](https://x.com/chrismdp) and [LinkedIn](https://linkedin.com/in/chrisparsons). Subscribe with <a href="{{ site.baseurl }}/feed.xml">RSS</a> to keep up with the latest.
