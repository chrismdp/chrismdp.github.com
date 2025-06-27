---
layout: page
title: "Kill Your Prompts"
permalink: /webinar
excerpt: "Build agents that actually work. No more prompt engineering."
image_portrait: /assets/img/chris-headshot-full.jpg
---

<div class="mb-12">

  <p class="text-2xl text-brand-black mb-8">
    Your agents break because you're still writing huge prompts like it's 2023.
  </p>

  <p class="text-xl text-brand-black font-bold mb-4">
    The best AI teams use:
  </p>

  <div class="space-y-3 mb-8">
    <li class="text-lg">Small focused functions, not giant prompts</li>
    <li class="text-lg">Multiple judges, not one big eval</li>
    <li class="text-lg">Auto-generated prompts from real verdicts</li>
  </div>

  <p class="text-lg text-brand-black mb-8">
    Watch me build a production agent using a much better method in minutes.
  </p>


  <p class="text-lg text-brand-black mb-8">
    No prompts. Just kaijo.ai doing the work.
</p>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12">
    <div class="rm-area-embed-webinar"></div>
  </div>
</div>

<div class="border-t border-brand-light-blue/20 pt-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Previous Webinars</h2>
  <div class="space-y-1 mb-12">
    {% for post in site.categories.webinar limit:5 %}
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
</div>

<div class="border-t border-brand-light-blue/20 pt-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">More AI Articles</h2>
  <div class="space-y-1 mb-12">
    {% for post in site.categories.ai limit:5 %}
      {% unless post.categories contains 'webinar' %}
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
      {% endunless %}
    {% endfor %}
  </div>
</div>

<div class="mt-12">
  {% include ai-newsletter-short.html %}
</div>
