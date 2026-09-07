---
layout: post
title: "Webinar: Make Your AI Rollout Stick"
date: 2026-09-07 09:45:00 +0100
categories:
- ai
- webinar
- leadership
- strategy
redirect_from:
- /webinar
- /webinar/
image: /assets/img/make-your-ai-rollout-stick-webinar.jpg
image_portrait: true
kit_tag: webinar18
webinar_date: "2026-09-10T14:30:00+01:00"
series: "AI In Action Webinars"
description: "Who owns the AI workflows your people have already built? Why rollouts built on Cowork, Copilot and Claude Code stall after the demos, the engineers nobody budgets for, and what a rollout looks like when it sticks."
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    Who in your company owns the AI workflows people have already built, and who fixes them when the model changes or the person who made them leaves? If the answer is nobody, this session is about the part of an AI rollout that never gets budgeted: the engineers who turn prototypes into workflows that last.
  </p>

<!--more-->

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both">
    <div class="rm-area-embed-webinar"></div>
  </div>

  <p class="text-lg text-brand-black mb-8 text-center">
    If you cannot make it, sign up anyway to grab the recording and slides.
  </p>

  <p class="text-xl text-brand-black mb-8">
    Cowork, Copilot agents and Claude Code are landing on every desk this autumn. Licences arrive, a policy goes out, and within a month people are building their own automations. One person has a bot that triages their inbox. Another has a tool that visualises client work, and it turns out the AI put it behind a public link. It all feels productive, then six months later the demos are still impressive and the business runs at the same speed, because none of it became anything a colleague can use, a manager can see, or a team can trust.
  </p>

  <p class="text-xl text-brand-black mb-8">
    The AI vendors have worked this out and committed nearly $10bn this year to forward deployed engineers, their own people who sit inside a customer's company to map the real process, wire the model into its systems, decide where a human reviews, and stay until it runs in production. I traced those numbers in <a href="/a-thousand-flowers-is-not-enough/">A Thousand Flowers Is Not Enough</a>. Unless you are a 5,000 person company, nobody is sending you those engineers, and if a vendor does send them, you have the opposite problem: renting your own work practices instead of owning them. Doing it yourself means naming who inside your company owns this work, whether that is one engineer part of the time or a small platform team, deciding what they stop doing to pay for it, and budgeting for maintaining what they build, and almost nobody has.
  </p>

  <p class="text-xl text-brand-black mb-8">
    By the end of this session you will have a map of where your rollout is stuck, the shape of the team that unsticks it at your size, a way to fund it, and the questions to ask before any vendor or consultant embeds in your company.
  </p>

  <p class="text-lg text-brand-black mb-8 text-center">
    If you are not a technical leader, join anyway. The money question is yours, and you will leave able to judge what your engineering lead is asking for, with a cleaner story for your board than "still in pilots".
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
      <li><strong>Why rollouts stall:</strong> the thousand flowers phase where everyone builds their own version, and the hidden failures a non-specialist cannot see until the data is already exposed</li>
      <li><strong>Tools are not a rollout:</strong> what Cowork, Copilot and Claude Code do well, and the maintenance debt they leave behind when nobody owns the workflow</li>
      <li><strong>The engineers you have not budgeted for:</strong> what the people who build and maintain AI workflows do on a Tuesday, who belongs in the role, and how to fund it without a new department</li>
      <li><strong>How it works when it sticks:</strong> prototypes from the people who know the work, a small team turning the winners into shared, secure workflows, and leaders who can see the outcome</li>
      <li><strong>Keeping ownership:</strong> the questions to ask before any vendor or consultant embeds in your company</li>
    </ul>
  </div>

  <p class="text-xl text-brand-black mb-8">
    I have done this work with clients: <a href="/case-studies/instem/">Instem</a> stood up two teams to build agentic engineering in-house after our coaching sessions, and a <a href="/case-studies/ventured/">VenturEd</a> India team we trained picked up a product that had not moved in six months. I will walk through what that looked like, what has lasted, and how to start it in your company.
  </p>

  <div class="text-center text-sm text-brand-black/60 mb-8">
    All attendees receive the full recording and any resources mentioned
  </div>
</div>
