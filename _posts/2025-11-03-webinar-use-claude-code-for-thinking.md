---
layout: post
title: "Use Claude Code for Thinking"
date: 2025-11-03 09:00:00 +0000
permalink: /webinar-claude-code-thinking/
redirect_from: /webinar
image: /assets/img/use-claude-code-webinar-thinking.png
image_portrait: false
kit_tag: webinar8
webinar_date: "2025-11-06T14:00:00+00:00"
categories:
- ai
- webinar
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    You have probably heard Claude Code is great for shipping features. But what if I told you I use it more for strategy documents than actual coding?
  </p>

  <p class="text-lg text-brand-black mb-8">
    Join me for live demonstrations of how I use Claude Code to write blog posts, create LinkedIn articles, and think through business strategy. See real terminal sessions with actual workflows you can use.
  </p>

  <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What You'll Learn:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>Beyond Code:</strong> Why AI agents outperform chat interfaces for complex thinking tasks, and how to use them as thought partners</li>
      <li><strong>Live Demos - Writing:</strong> Strategy documents, content creation, and knowledge management workflows that actually work</li>
      <li><strong>Live Demos - Thinking:</strong> Research synthesis, decision frameworks, strategic planning, and stakeholder communication</li>
      <li><strong>Real Workflows:</strong> See actual terminal sessions showing multi-file workflows, Q&A sessions, iterative improvement, and context management</li>
    </ul>
  </div>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12">
    <div class="rm-area-embed-webinar"></div>
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
        const webinarDate = new Date('{{ page.webinar_date }}');
        const dayOptions = {
          day: 'numeric',
          timeZone: 'Europe/London'
        };
        const monthOptions = {
          month: 'short',
          timeZone: 'Europe/London'
        };
        const timeOptions = {
          hour: 'numeric',
          hour12: true,
          timeZone: 'Europe/London'
        };

        const day = webinarDate.toLocaleDateString('en-GB', dayOptions);
        const month = webinarDate.toLocaleDateString('en-GB', monthOptions);
        const ukTime = webinarDate.toLocaleTimeString('en-GB', timeOptions).toLowerCase();
        const ukFormatted = `${day}${getOrdinalSuffix(day)} ${month}, ${ukTime}`;

        const etOptions = {
          hour: 'numeric',
          hour12: true,
          timeZone: 'America/New_York'
        };
        const etTime = webinarDate.toLocaleTimeString('en-US', etOptions).toLowerCase();

        titleElement.textContent = `Next Webinar: ${ukFormatted} UK / ${etTime} ET`;
      } else {
        // Try again in 500ms if element not found yet
        setTimeout(updateWebinarTitle, 500);
      }
    }

    // Initial attempt
    updateWebinarTitle();
  });
  </script>
</div>

<div id="previous-webinars" class="border-t border-brand-light-blue/20 pt-12">
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
