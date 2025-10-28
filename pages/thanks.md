---
layout: default
title: Thanks!
permalink: /thanks
---

<!-- Hero Section with Page Title -->
<section class="pt-20 pb-12 bg-white">
  <div class="max-w-4xl mx-auto px-6 text-center">
    <h1 class="text-4xl md:text-5xl lg:text-6xl font-heading font-bold mb-6 leading-tight text-brand-black">{{ page.title }}</h1>
  </div>
</section>

<div class="max-w-4xl mx-auto px-6 pb-12">
  <div class="bg-brand-white rounded-lg p-8 border border-brand-light-blue/20 mb-12">
    <p class="text-lg text-brand-black/80 mb-6 text-center">
      Would you mind <strong>taking 20 seconds</strong> to answer a few quick questions?
    </p>
    
    <div class="rm-area-embed-thanks"></div>
  </div>

  <div class="border-t border-brand-light-blue/20 pt-12">
    <h2 class="text-2xl font-heading font-bold mb-8 text-brand-black">Latest Articles</h2>

    {% assign latest_posts = site.posts | slice: 0, 5 %}
    {% include article-list.html posts=latest_posts %}

    <div class="text-center mt-8">
      <a href="{{ site.baseurl }}/articles/" class="inline-block bg-brand-deep-turquoise text-white px-6 py-3 rounded-lg hover:bg-brand-turquoise transition-colors">View All Articles</a>
    </div>
  </div>
</div>
