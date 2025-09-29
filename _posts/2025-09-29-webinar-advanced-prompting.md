---
layout: post
title: "Advanced Prompting Webinar: How to Make AI Work For You"
date: 2025-09-29 08:00:00 +0000
image: /assets/img/advanced-prompting-webinar.png
categories:
- ai
- webinar
- prompting
redirect_from: /webinar
kit_tag: webinar7
webinar_date: "2025-10-02T14:00:00+01:00"
---

<div class="mb-12">
  <div class="text-4xl text-brand-black font-bold mb-4 text-center">
    October 2nd<br/>2pm UK / 9am ET
  </div>

  <div class="text-3xl text-brand-black mb-8 text-center">
    Move beyond simple prompts and put AI to work with systematic techniques that deliver consistent results.
  </div>

  <a href="#signup" style="display: block; clear: both" class="bg-brand-deep-turquoise text-center rounded-lg p-8 m-12">
    <div style="color: white !important; text-decoration: none !important" class="text-3xl font-bold">
      SIGN UP BELOW
    </div>
  </a>

  <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What You'll Learn:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>LLM Fundamentals:</strong> How large language models actually work and why most people get disappointing results</li>
      <li><strong>The Power of Questions:</strong> Teaching AI to interview you for better context and more valuable outputs</li>
      <li><strong>Meta-Prompting:</strong> Systematic approaches to complex problem-solving with AI</li>
      <li><strong>The Goldilocks Principle:</strong> Balancing context perfectly - avoiding too little or too much information</li>
      <li><strong>The Prompt Cycle:</strong> An iterative refinement methodology for consistent quality</li>
    </ul>
  </div>

  <div class="bg-brand-orange/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">Why This Webinar Is Different:</h3>
    <ul class="space-y-2 text-brand-black">
      <li>✅ <strong>Model-agnostic techniques</strong> that work with any AI system</li>
      <li>✅ <strong>Proven with technical audiences</strong> including genomics scientists and developers</li>
      <li>✅ <strong>Immediately actionable</strong> for technical environments</li>
      <li>✅ <strong>Live demonstration</strong> with real-world technical examples</li>
    </ul>
  </div>

  <div id="signup" class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="text-center text-sm text-brand-black/60 mb-8">
    All attendees receive the full recording and presentation slides
  </div>
</div>

<script>
// Update webinar title once page loads
document.addEventListener('DOMContentLoaded', function() {
  function getOrdinalSuffix(day) {
    const num = parseInt(day);
    if (num >= 11 && num <= 13) return 'th';
    switch (num % 10) {
      case 1: return 'st';
      case 2: return 'nd';
      case 3: return 'rd';
      default: return 'th';
    }
  }
  
  function updateWebinarTitle() {
    const titleElement = document.querySelector('.rm-area-embed-webinar .rm-title');
    if (titleElement) {
      titleElement.textContent = `Advanced Prompting Webinar: October 2nd, 2pm UK / 9am ET`;
    } else {
      // Try again in 500ms if element not found yet
      setTimeout(updateWebinarTitle, 500);
    }
  }
  
  // Initial attempt
  updateWebinarTitle();
});
</script>

<div id="previous-webinars" class="border-t border-brand-light-blue/20 pt-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Previous Webinars</h2>
  <div class="space-y-1 mb-12">
    {% for post in site.categories.webinar limit:5 %}
      {% unless post.title contains 'Advanced Prompting' %}
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
