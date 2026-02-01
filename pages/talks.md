---
layout: page
title: Talks
permalink: /talks/
full_width: true
---

{% assign today = 'now' | date: '%s' %}
{% assign upcoming_talks = "" | split: "" %}
{% assign recent_talks = "" | split: "" %}
{% assign all_talks = "" | split: "" %}

{% for post in site.posts %}
  {% assign post_time = post.date | date: "%s" | plus: 0 %}
  {% assign now_time = site.time | date: "%s" | plus: 0 %}
  {% if post_time > now_time %}{% continue %}{% endif %}
  {% if post.categories contains 'talk' %}
    {% assign all_talks = all_talks | push: post %}
    {% if post.talk_date %}
      {% assign talk_timestamp = post.talk_date | date: '%s' %}
      {% if talk_timestamp >= today %}
        {% assign upcoming_talks = upcoming_talks | push: post %}
      {% else %}
        {% assign recent_talks = recent_talks | push: post %}
      {% endif %}
    {% else %}
      {% assign recent_talks = recent_talks | push: post %}
    {% endif %}
  {% endif %}
{% endfor %}

{% if upcoming_talks.size > 0 %}
<div class="mb-16">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Upcoming Talks</h2>
  {% include article-cards.html posts=upcoming_talks %}
</div>
{% endif %}

<div class="mb-16">
  {% assign latest_talks = recent_talks | slice: 0, 4 %}
  {% include article-cards.html posts=latest_talks %}
</div>

<h2 class="text-2xl font-heading font-bold mb-6 text-brand-black border-t border-brand-light-blue/20 pt-8">All Talks</h2>

{% for post in all_talks %}
  {% capture this_year %}{{ post.talk_date | default: post.date | date: "%Y" }}{% endcapture %}
  {% capture next_year %}{{ post.previous.talk_date | default: post.previous.date | date: "%Y" }}{% endcapture %}

  {% if forloop.first %}
## {{ this_year }}
  {% endif %}

**{{ post.talk_date | default: post.date | date: "%b %-d" }}** - [{{ post.title }}]({{ post.url | prepend: site.baseurl }}){% if post.venue %} • {{ post.venue }}{% endif %}

  {% unless forloop.last %}
    {% if this_year != next_year %}

## {{ next_year }}
    {% endif %}
  {% endunless %}
{% endfor %}

---

{% include ai-newsletter-short.html %}