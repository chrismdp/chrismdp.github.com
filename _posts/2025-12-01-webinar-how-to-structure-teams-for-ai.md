---
layout: post
title: "How to Structure Your Teams for AI"
date: 2025-12-01 14:00:00 +0000
categories:
- webinar
- ai
- team-topology
- leadership
description: "The critical org design decision every CTO must make: amplify your multidisciplinary teams or break them into AI-powered solos? Why the wrong choice will slow you down, and what to do instead."
image: /assets/img/tortoise-scooter-hare.png
image_caption: "Yes it's cryptic. I'll explain on the call."
kit_tag: webinar9
webinar_date: "2025-12-04T14:00:00+00:00"
redirect_from: /webinar
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    Your developers are writing code faster than ever. But your organisation is not getting faster. Revenue is not increasing. Your boss is looking at the AI bills wondering why the bottom line is getting worse.
  </p>

  <p class="text-xl text-brand-black mb-8">
    If coding speeds up but your organisation does not, coding was not the bottleneck. So where has the constraint moved?
  </p>

  <p class="text-xl text-brand-black mb-8">
    How do you structure your teams to take full advantage of AI?
  </p>

  <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>The constraint shift:</strong> Why faster coding does not mean faster organisations, and what becomes the new bottleneck</li>
      <li><strong>The Amplify vs Hybridise choice:</strong> Two fundamentally different paths for team structure. Should you keep multidisciplinary teams but smaller, or break them apart into AI-powered solos?</li>
      <li><strong>What each approach looks like:</strong> Team sizes, platform teams, enabling teams, and the new skills your organisation needs</li>
      <li><strong>The hidden costs:</strong> What happens when you choose the wrong path (and how to recognise it)</li>
      <li><strong>Three things you can do this week</strong> to start making the shift</li>
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
