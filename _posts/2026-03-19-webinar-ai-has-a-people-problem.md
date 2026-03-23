---
layout: post
title: "Webinar: AI Has a People Problem"
date: 2026-03-19 07:00:00 +0000
categories:
- ai
- webinar
- leadership
- teams
image: /assets/img/webinar-ai-people-problem.jpg
kit_tag: webinar14
webinar_date: "2026-03-26T17:00:00+00:00"
series: "AI In Action Webinars"
redirect_from: /webinar
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    AI adoption has its own jagged frontier. The same tools create completely different problems for different people on the same team.
  </p>

  <p class="text-xl text-brand-black mb-8">
    AI tools create a random reinforcement pattern like a slot machine: sometimes the output is brilliant, sometimes mediocre, and the variable reward schedule keeps power users pulling the lever until they burn out. Experienced engineers who formed a view of AI early on have frozen that impression in place. And a large group in the middle adopted it at surface level, quietly plateaued, and are not asking for the help they need. All of these problems land on your desk, and none has a technical fix.
  </p>

  <p class="text-xl text-brand-black mb-8">
    Whether you are setting the strategy or building the case for one, you will leave with practical ways to manage both sides of the AI people problem: the people who cannot stop and the people who cannot start.
  </p>

  <!--more-->

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <div class="mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Will Cover:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>The Slot Machine Effect:</strong> Why AI creates a variable reward pattern that hijacks daily routines and leads to burnout nobody sees coming</li>
      <li><strong>Frozen Mental Models:</strong> Why your most experienced engineers formed a fixed view of AI early on and stopped updating it, and what works to reopen that conversation</li>
      <li><strong>Exhaustion Asymmetry:</strong> AI brings fresh energy to every interaction while humans wear down. What this means for structuring AI-assisted work</li>
      <li><strong>The Leadership Playbook:</strong> Setting boundaries for power users, creating safe re-entry for sceptics, making the case to a cautious board, and spotting the warning signs before they become retention problems</li>
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
        const dayOptions = { day: 'numeric', timeZone: 'Europe/London' };
        const monthOptions = { month: 'short', timeZone: 'Europe/London' };
        const timeOptions = { hour: 'numeric', minute: '2-digit', hour12: true, timeZone: 'Europe/London' };

        const day = webinarDate.toLocaleDateString('en-GB', dayOptions);
        const month = webinarDate.toLocaleDateString('en-GB', monthOptions);
        let ukTime = webinarDate.toLocaleTimeString('en-GB', timeOptions).toLowerCase();
        ukTime = ukTime.replace(':00', '');
        const ukFormatted = `${day}${getOrdinalSuffix(day)} ${month}, ${ukTime}`;

        const etOptions = { hour: 'numeric', minute: '2-digit', hour12: true, timeZone: 'America/New_York' };
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
