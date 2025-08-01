---
layout: page
title: "From Demo to Production: Making AI Agents Work at Scale"
permalink: /webinar
excerpt: "Learn how to take AI agents from impressive demos to reliable production systems."
image: /assets/img/ai-agents-production-webinar.png
image_portrait: false
---

<div class="mb-12">

  <p class="text-2xl text-brand-black mb-8">
    Join me for a live workshop on taking AI agents from demo to production.
  </p>

  <p class="text-xl text-brand-black font-bold mb-4">
    Next session: August 7th, 2pm
  </p>

  <p class="text-lg text-brand-black mb-8">
    <strong>From Demo to Production: Making AI Agents Work at Scale</strong><br>
    It's not about whether AI agents work (they work). It's about making them work reliably at scale.
  </p>

  <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What You'll Learn:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>The Five Pillars:</strong> Do you even need an LLM? Taming randomness, choosing the right architecture, mitigating security issues, and building evaluations</li>
      <li><strong>Why Agents Fail:</strong> Works great in demo, breaks with real users - unpredictable edge cases and security collapse through too many tools</li>
      <li><strong>Architecture Patterns:</strong> Big Prompt Agents vs Workflow Agents - when to use each and why workflow agents are often better</li>
      <li><strong>Security Reality:</strong> Prompt injection, data leakage, and real mitigation strategies that actually work</li>
      <li><strong>Production Checklist:</strong> The essential steps before deploying any AI agent system</li>
    </ul>
  </div>

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
