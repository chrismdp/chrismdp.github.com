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

What if you could assign a task to an AI agent before bed and wake up to find it done? I've been experimenting with this but haven't taken the plunge yet. In this webinar I'll explore why, and what it would take to trust an agent overnight.

<!--more-->

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    What if you could give an AI agent a task and wake up to find it done?
  </p>

  <p class="text-xl text-brand-black mb-8">
    Autonomous coding agents can now run for hours on complex tasks. But I haven't let one run overnight yet. The token costs, the risk of runaway loops, the question of whether I'd actually trust the output in the morning... there's a gap between what's possible and what I'm willing to try.
  </p>

  <p class="text-xl text-brand-black mb-8">
    In this session, I'll share my experiments so far, what's holding me back, and we'll figure out together what it would take to actually ship while we sleep.
  </p>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>My Experiments So Far:</strong> What I've tried with autonomous agents, what worked, and what made me nervous</li>
      <li><strong>The Trust Gap:</strong> Why it's hard to let an agent run unsupervised, even when the tools support it</li>
      <li><strong>Guardrails That Matter:</strong> Token limits, permissions, and checkpoints that could make overnight runs safer</li>
      <li><strong>What Would It Take:</strong> Working through the barriers together to figure out when this becomes practical</li>
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
