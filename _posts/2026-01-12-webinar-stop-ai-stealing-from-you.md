---
layout: post
title: "Webinar: Stop AI Stealing From You"
date: 2026-01-12 08:00:00 +0000
categories:
- ai
- webinar
redirect_from:
- /webinar
- /webinar/
image: /assets/img/webinar-stop-ai-stealing.jpg
image_portrait: true
kit_tag: webinar11
webinar_date: "2026-01-15T15:30:00+00:00"
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    January 15, 3:30pm GMT
  </p>

  <ul class="space-y-3 text-xl text-brand-black/80 mb-8">
    <li>"What if our data ends up training someone else's model?"</li>
    <li>"How do I stop my team using AI dangerously?"</li>
  </ul>

  <p class="text-xl text-brand-black mb-8">
    That second question is the killer: IBM research last year found 20% of data breaches were caused by shadow AI.
  </p>

  <p class="text-xl text-brand-black mb-8">
    I have analysed the T&Cs for OpenAI, Anthropic, and Google, plus the latest AI legislation. We will cover what each tier (consumer, business, enterprise) actually means for your data, how to avoid the new "lethal trifecta" that lets attackers steal data through AI agents, when local models make sense, and what is already illegal (and what is coming).
  </p>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>The T&Cs Decoded:</strong> What OpenAI, Anthropic, and Google actually say about data retention, training, and IP at consumer, business, and enterprise tiers</li>
      <li><strong>The Lethal Trifecta:</strong> The three conditions that let attackers steal data through AI agents, and how to avoid them</li>
      <li><strong>Local Models:</strong> When self-hosted AI makes sense and when it does not</li>
      <li><strong>The Legal Landscape:</strong> What is already illegal and what legislation is coming</li>
    </ul>
  </div>

  <script>
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
          minute: '2-digit',
          hour12: true,
          timeZone: 'Europe/London'
        };

        const day = webinarDate.toLocaleDateString('en-GB', dayOptions);
        const month = webinarDate.toLocaleDateString('en-GB', monthOptions);
        let ukTime = webinarDate.toLocaleTimeString('en-GB', timeOptions).toLowerCase();
        ukTime = ukTime.replace(':00', '');
        const ukFormatted = `${day}${getOrdinalSuffix(day)} ${month}, ${ukTime}`;

        const etOptions = {
          hour: 'numeric',
          minute: '2-digit',
          hour12: true,
          timeZone: 'America/New_York'
        };
        let etTime = webinarDate.toLocaleTimeString('en-US', etOptions).toLowerCase();
        etTime = etTime.replace(':00', '');

        titleElement.textContent = `Stop AI Stealing From You: ${ukFormatted} UK / ${etTime} ET`;
      } else {
        setTimeout(updateWebinarTitle, 500);
      }
    }

    updateWebinarTitle();
  });
  </script>

  <div class="text-center text-sm text-brand-black/60 mb-8">
    All attendees receive the full recording and any resources mentioned
  </div>

  <div class="text-center mb-8">
    <img src="/assets/img/webinar-stop-ai-stealing-advert.jpg" alt="Stop AI Stealing From You - Webinar 15th January" class="w-1/2 mx-auto rounded-lg">
  </div>
</div>

<div id="previous-webinars" class="border-t border-brand-light-blue/20 pt-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Previous Webinars</h2>
  <div class="space-y-1 mb-12">
    {% for post in site.categories.webinar limit:5 %}
    {% unless post.title contains 'Stop AI Stealing' %}
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
