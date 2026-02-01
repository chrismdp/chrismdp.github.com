---
layout: page
title: Pre-Training Questionnaire
permalink: /training/questionnaire
---

<div class="bg-brand-white rounded-lg p-8 border border-brand-light-blue/20 mb-12">
  <p class="text-lg text-brand-black/80 mb-6 text-center">
    Please <strong>take a few moments</strong> to complete your pre-training questionnaire.
  </p>
  
  <div class="rm-area-embed-training"></div>
</div>

<div class="border-t border-brand-light-blue/20 pt-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">While you're here, check out these popular articles:</h2>
  <div class="space-y-1 mb-12">
    {% assign shown_count = 0 %}
    {% for post in site.posts %}
      {% assign post_time = post.date | date: "%s" | plus: 0 %}
      {% assign now_time = site.time | date: "%s" | plus: 0 %}
      {% if post_time > now_time %}{% continue %}{% endif %}
      {% if shown_count >= 10 %}{% break %}{% endif %}
      {% assign shown_count = shown_count | plus: 1 %}
    <div class="flex flex-col md:flex-row md:items-center gap-2 border-b border-brand-light-blue/10 py-2">
      <div class="text-sm text-brand-black/60 md:w-24 flex-shrink-0">
        {{ post.date | date: "%b %-d" }}
      </div>
      <div class="flex-1">
        <a href="{{ post.url | prepend: site.baseurl }}" class="text-brand-black hover:text-brand-deep-turquoise transition-colors">
          {{ post.title }}
        </a>
      </div>
    </div>
    {% endfor %}
  </div>
  
  <div class="text-center">
    <a href="{{ site.baseurl }}/articles/" class="inline-block bg-brand-black text-white px-6 py-3 rounded-lg hover:bg-brand-black/80 transition-colors">View All Articles</a>
  </div>
</div>