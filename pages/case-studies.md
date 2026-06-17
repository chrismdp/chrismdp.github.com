---
layout: page
title: Case Studies
permalink: /case-studies/
excerpt: "Real engagements, real outcomes — how teams have used AI to ship faster and build things that matter."
---

{% assign sorted_pages = site.pages | sort: "date" | reverse %}
{% assign case_studies = "" | split: "" %}
{% for p in sorted_pages %}
  {% if p.url contains "/case-studies/" and p.categories contains "case-studies" %}
    {% assign case_studies = case_studies | push: p %}
  {% endif %}
{% endfor %}

<div class="not-prose">
  {% for study in case_studies %}
  <article class="py-8 border-b border-brand-light-blue/20 last:border-0 flex flex-col sm:flex-row gap-6">
    {% if study.image %}
    <a href="{{ site.baseurl }}{{ study.url }}" class="sm:w-56 flex-shrink-0" style="text-decoration: none;">
      <img alt="{{ study.title | replace: "'", "&#39;" }}" src="{{ study.image }}" class="rounded-lg w-full h-40 sm:h-32 object-cover">
    </a>
    {% endif %}
    <div class="flex-1 min-w-0">
      <h2 class="text-2xl font-heading font-semibold mb-2">
        <a href="{{ site.baseurl }}{{ study.url }}" class="text-brand-black hover:text-brand-deep-turquoise transition-colors" style="text-decoration: none;">
          {{ study.title | remove: "Case Study: " }}
        </a>
      </h2>
      <p class="text-brand-black/80 leading-relaxed mb-4">{{ study.excerpt }}</p>

      {% if study.client_quote %}
      <div class="border-l-4 border-brand-turquoise/40 pl-4 mb-5">
        <p class="italic text-brand-black/90" style="margin-bottom: 0.75rem;">"{{ study.client_quote }}"</p>
        <div class="flex items-center gap-3">
          {% if study.client_image %}<img src="/assets/img/testimonials/{{ study.client_image }}" alt="{{ study.client_name }}" class="rounded-full object-cover" style="width: 40px; height: 40px; margin: 0;">{% endif %}
          <div>
            <div class="font-semibold text-sm text-brand-black">{{ study.client_name }}</div>
            <div class="text-xs text-brand-black/70">{{ study.client_role }}</div>
          </div>
        </div>
      </div>
      {% endif %}

      <a href="{{ site.baseurl }}{{ study.url }}" class="inline-block bg-brand-deep-turquoise px-5 py-2.5 rounded-lg hover:bg-brand-turquoise transition-colors font-semibold" style="color: #ffffff; text-decoration: none;">
        Read the full case study →
      </a>
    </div>
  </article>
  {% endfor %}
</div>

{% include ai-newsletter-short.html %}
