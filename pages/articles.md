---
layout: page
title: All Articles
permalink: /articles/
full_width: true
redirect_from:
  - /blog
  - /all/
---

{% assign all_posts = site.posts %}
{% assign latest_posts = "" | split: "" %}
{% for post in all_posts limit: 20 %}
  {% assign post_time = post.date | date: "%s" | plus: 0 %}
  {% assign now_time = site.time | date: "%s" | plus: 0 %}
  {% if post_time > now_time %}{% continue %}{% endif %}
  {% assign webinar_time = post.webinar_date | date: "%s" | plus: 0 %}
  {% if post.webinar_date == nil or webinar_time <= now_time %}
    {% assign latest_posts = latest_posts | push: post %}
    {% if latest_posts.size >= 4 %}{% break %}{% endif %}
  {% endif %}
{% endfor %}

<div class="flex flex-col md:flex-row gap-8">
  <div class="flex-1 min-w-0">
    {% include article-cards.html posts=latest_posts mode="featured" %}

    <hr class="my-8 border-brand-light-blue/20">
    <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">All Articles</h2>

    {% assign current_year = "" %}
    {% for post in site.posts %}
      {% assign post_time = post.date | date: "%s" | plus: 0 %}
      {% assign now_time = site.time | date: "%s" | plus: 0 %}
      {% if post_time > now_time %}{% continue %}{% endif %}
      {% assign webinar_time = post.webinar_date | date: "%s" | plus: 0 %}
      {% if post.webinar_date == nil or webinar_time <= now_time %}
        {% assign this_year = post.date | date: "%Y" %}
        {% if this_year != current_year %}
          {% assign current_year = this_year %}
          <h3 class="text-xl font-heading font-semibold mt-6 mb-3 text-brand-black">{{ this_year }}</h3>
        {% endif %}
        <p class="mb-1"><strong>{{ post.date | date: "%b %-d" }}</strong> - <a href="{{ post.url | prepend: site.baseurl }}" class="text-brand-deep-turquoise hover:text-brand-turquoise">{{ post.title }}</a></p>
      {% endif %}
    {% endfor %}

    <hr class="my-8 border-brand-light-blue/20">

    {% include ai-newsletter-short.html %}
  </div>

  <div class="md:w-72 lg:w-80 flex-shrink-0">
    {% include related-articles-sidebar.html mode="recent" limit=12 offset=1 title="" %}
  </div>
</div>
