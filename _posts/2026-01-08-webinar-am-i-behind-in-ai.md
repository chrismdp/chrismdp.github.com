---
layout: post
title: "Webinar: Am I Behind in AI?"
date: 2026-01-04 14:00:00 +0000
categories:
- ai
- webinar
- leadership
redirect_from: /webinar
redirect_from: /webinar/
image: /assets/img/am-i-behind-in-ai-webinar.jpg
kit_tag: webinar10
webinar_date: "2026-01-08T14:00:00+00:00"
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Thursday 8th January, 2pm UK
  </p>

  <div class="text-lg text-brand-black mb-8 space-y-4">
    <p>
      Should you buy AI subscriptions for everyone or wait? Invest in training now or is it too early? Use Copilot as your CISO says it is compliant, despite mixed team feedback? Push harder on AI in your product despite security concerns, or hold back despite board pressure? How far ahead is everyone else, and are you losing ground?
    </p>
    <p>
      Every technical leader I talk to (and I have talked to lots) is wrestling with these same questions, squeezed between excessive caution on one side and unrealistic optimism on the other. The signal-to-noise ratio on who to trust is terrible.
    </p>
    <p>
      Most organisations are measuring the wrong things and comparing themselves to the wrong benchmarks. They are confusing readiness with maturity, and that confusion wastes months.
    </p>
  </div>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li>Mapping the AI landscape: what is becoming standard vs what is cutting edge</li>
      <li>Readiness vs maturity: the distinction most organisations miss</li>
      <li>Hard questions that reveal where your team actually stands compared to others</li>
    </ul>
    <p class="mt-4 text-brand-black/80 italic">
      This is a quick preview of the opening framework from Week 1 of the <a href="/ai-leader-accelerator/" class="text-brand-deep-turquoise hover:underline">AI Leader Accelerator</a>. We will work through it in much more depth on the course.
    </p>
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

  <div class="text-center text-sm text-brand-black/60 mb-8">
    All attendees receive the full recording and any resources mentioned
  </div>
</div>

<img src="/assets/img/am-i-behind-in-ai-infographic.jpg" alt="Am I Behind in AI?" style="width: 50%;" />

<div id="previous-webinars" class="border-t border-brand-light-blue/20 pt-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Previous Webinars</h2>
  <div class="space-y-1 mb-12">
    {% for post in site.categories.webinar limit:5 %}
      {% unless post.title contains 'Behind in AI' %}
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
