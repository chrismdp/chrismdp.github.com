---
layout: post
title: "Webinar: Am I Behind in AI?"
date: 2026-01-08 14:00:00 +0000
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
    Next session: {{ page.webinar_date | date: "%B %-d, %-I%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    Everyone wants to know: am I behind with AI? What is everyone else doing? The noise is deafening, the anxiety is real, and most organisations have no way of actually knowing.
  </p>

  <p class="text-xl text-brand-black mb-8">
    They are measuring the wrong things and comparing themselves to the wrong benchmarks.
  </p>

  <p class="text-xl text-brand-black mb-8">
    By the end of this session, you will know exactly where you stand and how that shapes your rollout.
  </p>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>The AI landscape:</strong> AI is a field, not a single tool. We will map the different categories, where they overlap, and why this matters for adoption</li>
      <li><strong>Readiness vs maturity:</strong> Most organisations confuse these two, but you need readiness before maturity matters. We will cover what the difference is and why getting this wrong wastes months</li>
      <li><strong>Key assessment questions:</strong> Specific questions that reveal where you actually stand, tailored by team type. We will work through the most important ones for engineering, product, and operations</li>
      <li><strong>What shapes your rollout:</strong> How your assessment should shape your AI adoption strategy, and what to do next</li>
    </ul>
  </div>

  <div class="bg-brand-orange/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">This Is The Opening Framework From The AI Leader Accelerator</h3>
    <p class="text-brand-black mb-4">
      This webinar is a condensed version of Week 1 from the <a href="/ai-leader-accelerator/" class="text-brand-deep-turquoise hover:underline">AI Leader Accelerator</a>, an 8-week peer learning programme for senior technical leaders navigating AI adoption.
    </p>
    <p class="text-brand-black">
      If the session resonates, consider joining the pioneer cohort starting 19th January.
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
