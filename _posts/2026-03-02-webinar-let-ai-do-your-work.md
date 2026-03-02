---
layout: post
title: "Webinar: Let AI Do Your Work"
date: 2026-03-01 14:00:00 +0000
categories:
- ai
- webinar
- leadership
- automation
redirect_from:
- /webinar
- /webinar/
image: /assets/img/webinar-let-ai-do-your-work-motif.jpg
infographic: /assets/img/webinar-let-ai-do-your-work.jpg
kit_tag: webinar13
webinar_date: "2026-03-05T14:00:00+00:00"
series: "AI In Action Webinars"
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}
  </p>

  <p class="text-xl text-brand-black mb-8">
    Most technical leaders have AI in one place: developer tooling. Copilot, maybe some ChatGPT. That is a fraction of what is possible.
  </p>

  <p class="text-xl text-brand-black mb-4">
    I use AI to run my entire consulting business:
  </p>

  <ul class="text-xl text-brand-black mb-8 space-y-2 ml-6 list-disc">
    <li>Morning routines that review my calendar, triage email and plan my day</li>
    <li>LinkedIn posts written, refined and scheduled before my coffee gets cold</li>
    <li>Xero reconciliation, runway spreadsheet reviews, contract drafting straight into Google Docs</li>
    <li>Training slides built from transcripts of previous sessions</li>
    <li>Inbox dumps processed into a personal knowledge base</li>
    <li>Even the reminder that pinged me to write this webinar page came from an AI agent running on a cron job</li>
  </ul>

  <p class="text-xl text-brand-black mb-8">
    In this session I will walk through all of it live, show you what works, what does not, and where to start in your own organisation.
  </p>

  <!--more-->

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>Beyond the IDE:</strong> Where AI creates value outside of code completion, and why most organisations are leaving 90% of the opportunity on the table</li>
      <li><strong>The Infrastructure Mindset:</strong> What changes when you treat AI as business infrastructure rather than a chatbot you occasionally ask questions</li>
      <li><strong>Where to Start:</strong> A practical framework for identifying your highest value AI opportunities, starting with the boring stuff that eats your week</li>
      <li><strong>Live Walkthrough:</strong> How AI runs across my consulting business end to end, from morning routines through client delivery</li>
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

        titleElement.textContent = `Next Webinar: ${ukFormatted} UK / ${etTime} ET`;
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
</div>
