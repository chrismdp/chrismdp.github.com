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
    <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black" id="{{ this_year }}-ref">{{ this_year }}</h2>
    <div class="space-y-1 mb-8">
  {% endif %}

  <div class="flex flex-col md:flex-row md:items-center gap-2 border-b border-brand-light-blue/10">
    <div class="text-sm text-brand-black/60 md:w-24 flex-shrink-0">
      {{ post.date | date: "%b %-d" }}
    </div>
    <div class="flex-1">
      <a href="{{ post.url | prepend: site.baseurl }}" class="text-brand-black hover:text-brand-deep-turquoise transition-colors">
        {{ post.title }}
      </a>
    </div>
  </div>

  {% if forloop.last %}
    </div>
  {% else %}
    {% if this_year != next_year %}
      </div>
      <h2 class="text-2xl font-heading font-bold mb-6 mt-12 text-brand-black" id="{{ next_year }}-ref">{{ next_year }}</h2>
      <div class="space-y-1 mb-8">
    {% endif %}
  {% endif %}
{% endfor %}

<div class="mt-12">
  {% include ai-newsletter-short.html %}
</div>