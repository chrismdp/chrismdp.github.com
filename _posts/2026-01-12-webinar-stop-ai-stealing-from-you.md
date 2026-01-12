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
    <li>"How do I explain AI risk to the board?"</li>
    <li>"What if our data ends up training someone else's model?"</li>
    <li>"How do I balance innovation with governance?"</li>
    <li>"My team is already using AI whether I've approved it or not."</li>
  </ul>

  <p class="text-xl text-brand-black mb-8">
    I have analysed the T&Cs so you know what to look for. By the end of this session, you will know exactly what OpenAI, Anthropic, and Google do with your data, how to avoid leaking your data, and how local models will help fix this going forward. You will walk away confident enough to greenlight AI tools for your team.
  </p>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>The T&Cs Decoded:</strong> What OpenAI, Anthropic, and Google actually say about data retention, training, and IP</li>
      <li><strong>Data Exfiltration:</strong> How your data can leak through AI tools and the security basics every CTO should enforce</li>
      <li><strong>Browser Agents:</strong> Why AI tools with web access create new attack surfaces and what to watch for</li>
      <li><strong>Tiers of Risk:</strong> A practical framework for which tools to approve for which use cases</li>
      <li><strong>Local Models:</strong> Where self-hosted AI is heading and why it is not quite ready for most organisations yet</li>
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
