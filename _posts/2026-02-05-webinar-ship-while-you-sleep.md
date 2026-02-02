---
layout: post
title: "Webinar: Ship While You Sleep"
date: 2026-02-05 14:00:00 +0000
categories:
- ai
- webinar
- agents
- automation
redirect_from:
- /webinar
- /webinar/
- /webinar-ralph-loops/
image: /assets/img/ralph-loops-webinar.jpg
infographic: /assets/img/ralph-loops-webinar-advert.jpg
kit_tag: webinar12
webinar_date: "2026-02-05T14:00:00+00:00"
---

What if you could assign a task to an AI agent before bed and wake up to find it done? We're closer to this than most people realise. In this webinar I'll show you exactly what it takes to get there.

<!--more-->

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    What if you could give an AI agent a task and wake up to find it done?
  </p>

  <p class="text-xl text-brand-black mb-8">
    The tools are ready. Claude Code can run for hours, make decisions, and recover from errors. Token limits, permission boundaries, and checkpoints already exist. What's missing is the playbook.
  </p>

  <p class="text-xl text-brand-black mb-8">
    In this session, we'll map out exactly what it takes to go from interesting experiment to trusted overnight workflow.
  </p>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>Task Patterns That Work:</strong> Which tasks are safe to hand off completely, and how to scope them for unsupervised runs</li>
      <li><strong>Guardrail Configuration:</strong> Token limits, permissions, and checkpoints that prevent expensive surprises</li>
      <li><strong>Verification Steps:</strong> How to trust the output in the morning without reviewing every line</li>
      <li><strong>The Path Forward:</strong> What's left to figure out, and how to close the gap</li>
    </ul>
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

  <div class="text-center text-sm text-brand-black/60 mb-8">
    All attendees receive the full recording and any resources mentioned
  </div>
</div>
