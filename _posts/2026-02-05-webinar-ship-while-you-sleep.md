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

What if you could assign a task to an AI agent before bed and wake up to find it done? I'll show you how to run autonomous coding agents overnight, including real failures and what I learned from them.

<!--more-->

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    What if you could give an AI agent a task and wake up to find it done?
  </p>

  <p class="text-xl text-brand-black mb-8">
    Autonomous coding agents are no longer science fiction. Tools like Claude Code can now run for hours on complex tasks, making decisions, writing code, and recovering from errors without your involvement. But making this work reliably requires understanding the patterns that succeed and the failure modes that burn through your token budget with nothing to show for it.
  </p>

  <p class="text-xl text-brand-black mb-8">
    By the end of this session, you will understand how to structure overnight agent runs, what guardrails actually matter, and how to wake up to useful work instead of expensive chaos.
  </p>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>What Ralph Loops Actually Are:</strong> The pattern behind running autonomous agents on extended tasks, named after leaving them running overnight</li>
      <li><strong>Setting Up Guardrails:</strong> Token limits, timeout configurations, and permission boundaries that prevent runaway costs</li>
      <li><strong>Task Definition That Works:</strong> How to scope tasks so agents can make meaningful progress without getting stuck in loops</li>
      <li><strong>My Failures and Lessons:</strong> Real examples of overnight runs that went wrong and what I changed to fix them</li>
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
