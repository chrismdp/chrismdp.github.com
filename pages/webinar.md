---
layout: page
title: "AI-First Coding Webinar"
permalink: /webinar
excerpt: "Learn how to add major features to your application 3x faster with AI-first coding."
---

<div class="mb-12">
  <img alt='Chris Parsons' src='/assets/img/chris-headshot-full.jpg' class='rounded-lg float-right ml-6 mb-6 w-64 h-auto'/>
  
  <p class="text-lg text-brand-black/80 mb-6">
    How do you make AI agents thrive in ever more complex codebases? Most developers believe that more code means more power for AI agents. That is a mistake. The real breakthrough comes from setting clear boundaries and limiting the context your AI can access.
  </p>

  <p class="text-lg text-brand-black/80 mb-6">
    I learned this the hard way. My early projects grew out of control. Agents became unpredictable, and debugging was a nightmare. Everything changed when I started treating boundaries as a feature, not a restriction.
  </p>

  <h2 class="text-2xl font-heading font-bold mb-4 text-brand-black">In this live webinar, I will show you how to:</h2>
  <ul class="list-disc list-inside text-brand-black/80 mb-6 space-y-2">
    <li>Define project boundaries that make AI agents more reliable</li>
    <li>Limit context to boost performance and reduce errors</li>
    <li>Build complex features without losing control</li>
  </ul>

  <p class="text-lg text-brand-black/80 mb-6">
    You will see real examples from my own work, including the latest updates to Kaijo, my AI reliability tool. I will demonstrate how to keep your agents focused, functional, and ready for anything.
  </p>

  <p class="text-lg text-brand-black/80 mb-8">
    If you are building with AI and your codebase is only getting more complex, this session is for you.
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