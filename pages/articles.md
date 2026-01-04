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
  {% assign all_posts = site.posts %}
  {% assign latest_posts = "" | split: "" %}
  {% for post in all_posts limit: 20 %}
    {% assign webinar_time = post.webinar_date | date: "%s" | plus: 0 %}
    {% assign now_time = site.time | date: "%s" | plus: 0 %}
    {% if post.webinar_date == nil or webinar_time <= now_time %}
      {% assign latest_posts = latest_posts | push: post %}
      {% if latest_posts.size >= 4 %}{% break %}{% endif %}
    {% endif %}
  {% endfor %}
  {% include article-cards.html posts=latest_posts %}
</div>

<h2 class="text-2xl font-heading font-bold mb-6 text-brand-black border-t border-brand-light-blue/20 pt-8">All Articles</h2>

{% for post in site.posts %}
  {% assign webinar_time = post.webinar_date | date: "%s" | plus: 0 %}
  {% assign now_time = site.time | date: "%s" | plus: 0 %}
  {% if post.webinar_date == nil or webinar_time <= now_time %}
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
