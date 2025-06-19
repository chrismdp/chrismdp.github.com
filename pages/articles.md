---
layout: page
title: All Articles
permalink: /articles/
redirect_from:
  - /blog
  - /all/
---

{% for post in site.posts %}
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
{% endfor %}

---

{% include ai-newsletter-short.html %}