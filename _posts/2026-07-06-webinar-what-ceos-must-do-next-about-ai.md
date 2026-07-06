---
layout: post
title: "Webinar: What CEOs Must Do Next About AI"
date: 2026-07-06 10:30:00 +0100
categories:
- ai
- webinar
- leadership
- strategy
redirect_from:
- /webinar
- /webinar/
image: /assets/img/what-ceos-must-do-next-about-ai-webinar.jpg
image_portrait: true
kit_tag: webinar17
webinar_date: "2026-07-09T14:00:00+01:00"
series: "AI In Action Webinars"
description: "A plain briefing for CEOs on the AI decisions only they can make: funding real learning time, platform bets, the Chief AI Officer question, and governance that enables rather than gates."
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    AI is the first technology shift where the CEO's own fluency sets the ceiling. This is a plain briefing on the decisions only you can make, and how to use the summer to set your company up for a strong September.
  </p>

<!--more-->

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <p class="text-lg text-brand-black mb-8 text-center">
    If you cannot make it, sign up anyway to grab the recording and slides.
  </p>

  <p class="text-xl text-brand-black mb-8">
    The AI rollouts I see start with tools: subscriptions bought, a policy written, a pilot blessed. Six months later the demos are impressive and the business results are thin, because the missing investment is nearly always people. Your teams are worried, they want to do the right thing, and they have been handed a login instead of the time and space to learn. Upskilling your people, not just giving them tools, is the decision that delivers the real gains.
  </p>

  <p class="text-xl text-brand-black mb-8">
    And it starts with you: a CEO who does not use AI personally cannot see the potential or the limitations, and every downstream call gets harder to judge: which platforms to back, who to hire, how much governance is enough. Saying yes to AI properly means saying no to another initiative, and that trade is yours alone to make. This session gives you my current answers, straight, with the reasoning behind them.
  </p>

  <p class="text-xl text-brand-black mb-8">
    By the end of this session you will know the handful of decisions to make before September: how to fund real learning time and what to stop to pay for it, which AI platforms deserve your money, whether to appoint an AI leader and how to define the role, and the governance posture that unlocks value instead of gating it.
  </p>

  <p class="text-lg text-brand-black mb-8 text-center">
    Not the CEO? Join anyway. You will leave with the business case for real learning time ready to make internally, and every registrant gets the recording and a summary built to send upward.
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
      <li><strong>People before tools:</strong> why learning time beats licences, what it costs, and what to say no to so your teams can say yes to AI</li>
      <li><strong>It starts with you:</strong> why a CEO who does not use AI cannot set direction on it, and the fastest way to build your own fluency</li>
      <li><strong>Which AIs to bet on:</strong> one frontier provider or a diversified spread, what your engineers should be fluent in, and what the rest of the business needs</li>
      <li><strong>The Chief AI Officer question:</strong> when to appoint one, why interim beats permanent, and the difference between AI in your product and AI for productivity</li>
      <li><strong>Governance that enables:</strong> what an enabling but safe posture looks like, which risks are real, which are overblown, and how to tell the difference</li>
    </ul>
  </div>

  <div class="text-center text-sm text-brand-black/60 mb-8">
    All attendees receive the full recording and any resources mentioned
  </div>
</div>
