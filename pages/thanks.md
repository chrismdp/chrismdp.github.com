---
layout: page
title: Thanks!
permalink: /thanks
---

<div class="text-center mb-12">
  <p class="text-xl text-brand-black/80 mb-8">
    Do check your email if you haven't already to see if you need to confirm anything there.
  </p>
</div>

<div class="bg-brand-white rounded-lg p-8 border border-brand-light-blue/20 mb-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black text-center">Help me send you the right content</h2>
  <p class="text-lg text-brand-black/80 mb-6 text-center">
    <strong>Take 20 seconds to answer a few quick questions</strong>, so I can avoid clogging your inbox with irrelevant stuff, and send you the specific things you're interested in!
  </p>
  
  <div class="rm-area-embed-thanks"></div>
</div>

<div class="border-t border-brand-light-blue/20 pt-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">While you're here, check out these popular articles:</h2>
  <div class="space-y-1 mb-12">
    {% for post in site.posts limit:10 %}
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