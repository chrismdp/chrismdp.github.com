---
layout: page
title: All Articles
permalink: /articles/
full_width: true
redirect_from:
  - /blog
  - /all/
---

<div class="mb-16">
  {% assign latest_posts = site.posts | where_exp: "post", "post.webinar_date == nil or post.webinar_date <= site.time" | slice: 0, 4 %}
  {% include article-cards.html posts=latest_posts %}
</div>

<h2 class="text-2xl font-heading font-bold mb-6 text-brand-black border-t border-brand-light-blue/20 pt-8">All Articles</h2>

{% for post in site.posts %}
  {% if post.webinar_date == nil or post.webinar_date <= site.time %}
  {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
  {% capture next_year %}{{ post.previous.date | date: "%Y" }}{% endcapture %}

  {% if forloop.first %}
## {{ this_year }}
  {% endif %}

**{{ post.date | date: "%b %-d" }}** - [{{ post.title }}]({{ post.url | prepend: site.baseurl }})

  {% unless forloop.last %}
    {% if this_year != next_year %}

## {{ next_year }}
    {% endif %}
  {% endunless %}
  {% endif %}
{% endfor %}

---

{% include ai-newsletter-short.html %}