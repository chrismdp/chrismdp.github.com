---
layout: page
title: Talks
permalink: /talks/
image: /assets/img/google-cloud-llm-talk.jpg
image_portrait: false
---

<style>
  .talks-section a {
    text-decoration: none !important;
  }
</style>

{% assign today = 'now' | date: '%s' %}
{% assign upcoming_talks = "" | split: "" %}
{% assign recent_talks = "" | split: "" %}

{% for post in site.posts %}
  {% if post.categories contains 'talk' %}
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

<div class="talks-section">
{% if upcoming_talks.size > 0 %}
<h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Upcoming Talks</h2>

{% for post in upcoming_talks %}
<article class="py-6 border-b border-brand-light-blue/10 last:border-0">
  <h3 class="text-xl font-heading font-semibold mb-2">
    <a href="{{ site.baseurl }}{{ post.url }}" class="text-brand-black hover:text-brand-deep-turquoise transition-colors">
      {{ post.title }}
    </a>
  </h3>
  <div class="text-sm text-brand-black/60 italic mb-4">
    {{ post.talk_date | date: "%B %-d, %Y" }}{% if post.venue %} • {{ post.venue }}{% endif %}{% if post.event_name %} • {{ post.event_name }}{% endif %}
  </div>
  <div class="prose prose-lg mb-4 text-brand-black/80 leading-relaxed content-styled">
    {{ post.excerpt }}
  </div>
  <a href="{{ site.baseurl }}{{ post.url }}" class="text-brand-deep-turquoise hover:text-brand-turquoise font-semibold">
    View talk details →
  </a>
</article>
{% endfor %}
{% endif %}

<h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Recent Talks</h2>

{% for post in recent_talks %}
<article class="py-6 border-b border-brand-light-blue/10 last:border-0">
  <h3 class="text-xl font-heading font-semibold mb-2">
    <a href="{{ site.baseurl }}{{ post.url }}" class="text-brand-black hover:text-brand-deep-turquoise transition-colors">
      {{ post.title }}
    </a>
  </h3>
  <div class="text-sm text-brand-black/60 italic mb-4">
    {% if post.talk_date %}
      {{ post.talk_date | date: "%B %-d, %Y" }}
    {% else %}
      {{ post.date | date: "%B %-d, %Y" }}
    {% endif %}
    {% if post.venue %} • {{ post.venue }}{% endif %}
    {% if post.event_name %} • {{ post.event_name }}{% endif %}
  </div>
  <div class="prose prose-lg mb-4 text-brand-black/80 leading-relaxed content-styled">
    {{ post.excerpt }}
  </div>
  <a href="{{ site.baseurl }}{{ post.url }}" class="text-brand-deep-turquoise hover:text-brand-turquoise font-semibold">
    Read more →
  </a>
</article>
{% endfor %}
</div>

<div class="my-12">
  {% include ai-newsletter-short.html %}
</div>

<div class="talks-section">
<h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Other Recent Articles</h2>

{% assign other_count = 0 %}
{% for post in site.posts %}
  {% unless post.categories contains 'talk' %}
    {% assign other_count = other_count | plus: 1 %}
    {% if other_count <= 10 %}
<article class="py-6 border-b border-brand-light-blue/10 last:border-0">
  <h3 class="text-xl font-heading font-semibold mb-2">
    <a href="{{ site.baseurl }}{{ post.url }}" class="text-brand-black hover:text-brand-deep-turquoise transition-colors no-underline">
      {{ post.title }}
    </a>
  </h3>
  <div class="text-sm text-brand-black/60 italic mb-4">
    {{ post.date | date: "%B %Y" }}
  </div>
  <div class="prose prose-lg mb-4 text-brand-black/80 leading-relaxed content-styled">
    {{ post.excerpt }}
  </div>
  <a href="{{ site.baseurl }}{{ post.url }}" class="text-brand-deep-turquoise hover:text-brand-turquoise font-semibold no-underline">
    Read more →
  </a>
</article>
    {% endif %}
  {% endunless %}
{% endfor %}
</div>

<hr class="my-8 border-brand-light-blue/20">

{% include ai-newsletter-short.html %}