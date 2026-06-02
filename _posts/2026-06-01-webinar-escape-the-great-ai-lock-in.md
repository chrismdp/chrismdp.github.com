---
layout: post
title: "Webinar: Escape the Great AI Lock-In"
date: 2026-06-01 09:00:00 +0100
categories:
- ai
- webinar
- leadership
- strategy
redirect_from:
- /webinar
- /webinar/
image: /assets/img/escape-the-great-ai-lock-in-webinar.jpg
image_portrait: true
kit_tag: webinar16
webinar_date: "2026-06-04T14:00:00+01:00"
series: "AI In Action Webinars"
description: "The flat-rate AI era is ending. Cheap tokens, metered pricing, and how local and open-source models let technical leaders escape dependence on frontier AI they do not control."
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    Your team runs on AI that feels free. Flat monthly fee, unlimited frontier models, no meter running. That is about to change, and the workflows you have quietly built on cheap tokens are more exposed than they look.
  </p>

<!--more-->

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <p class="text-xl text-brand-black mb-8">
    Agentic usage burns through tokens at a rate no flat fee absorbs forever, and the gap is already stark: Claude Opus at full tilt costs £80 to £100 an hour, while frontier-class open-source models rent for £15 to £25. The unlimited era was an acquisition strategy, not a business model. I have already moved the bulk of my own heavy work off Opus and onto cheaper models, and I am planning now for the day the flat-rate generosity stops. When the meter comes back, your dependence on cheap frontier access becomes a line item your CFO will question, and a supplier relationship you never chose to be locked into.
  </p>

  <p class="text-xl text-brand-black mb-8">
    This is not only about cost. Running your own models is about control: your data, your intellectual property, and your uptime stop depending on someone else's pricing, terms, and roadmap.
  </p>

  <p class="text-xl text-brand-black mb-8">
    By the end of this session you will know which of your AI workflows are exposed to a metered world, where running your own models makes sense, and how to build an AI strategy that does not depend on a pricing page you do not control.
  </p>

  <p class="text-lg text-brand-black mb-8 text-center">
    If you cannot make it, sign up anyway to grab the recording and slides.
  </p>

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
          minute: '2-digit',
          hour12: true,
          timeZone: 'Europe/London'
        };

        const day = webinarDate.toLocaleDateString('en-GB', dayOptions);
        const month = webinarDate.toLocaleDateString('en-GB', monthOptions);
        let ukTime = webinarDate.toLocaleTimeString('en-GB', timeOptions).toLowerCase();
        // Remove :00 for times on the hour
        ukTime = ukTime.replace(':00', '');
        const ukFormatted = `${day}${getOrdinalSuffix(day)} ${month}, ${ukTime}`;

        const etOptions = {
          hour: 'numeric',
          minute: '2-digit',
          hour12: true,
          timeZone: 'America/New_York'
        };
        let etTime = webinarDate.toLocaleTimeString('en-US', etOptions).toLowerCase();
        // Remove :00 for times on the hour
        etTime = etTime.replace(':00', '');

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

  <div class="mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>The economics shift:</strong> why flat-rate frontier access was always temporary, and what the autonomous-model pricing change is really signalling</li>
      <li><strong>What you actually own:</strong> rented frontier tokens versus models you run yourself, and where the line should sit</li>
      <li><strong>Local and open-source models in practice:</strong> what the frontier-class open weights can and cannot do, the data and IP control you get back, and the honest hardware reality from a single used GPU to a rented cluster</li>
      <li><strong>Building for a metered world:</strong> what to keep on frontier, what to move, and how to decide</li>
    </ul>
  </div>

  <div class="text-center text-sm text-brand-black/60 mb-8">
    All attendees receive the full recording and any resources mentioned
  </div>
</div>
