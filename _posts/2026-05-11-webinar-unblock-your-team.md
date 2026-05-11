---
layout: post
title: "Webinar: Unblock Your Team"
date: 2026-05-11 09:00:00 +0100
categories:
- ai
- webinar
- teams
- leadership
- productivity
redirect_from:
- /webinar
- /webinar/
image: /assets/img/unblock-your-team-webinar.jpg
image_portrait: true
kit_tag: webinar15
webinar_date: "2026-05-14T15:00:00+01:00"
excerpt: "A live webinar for engineering leaders on team productivity with AI."
---

**Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}**

Your power user is not making your team faster.

AI leverage in a team comes from propagation. The playbooks, conventions, and patterns your best engineer has worked out need to live somewhere AI can run against them directly, the way that engineer would. Most teams put theirs in a Notion page nobody reads. That does not propagate.

<div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12 clear-both"><div class="rm-area-embed-webinar"></div></div>

## What We Will Cover

- **The Productivity Paradox:** why your power user feels faster while your team delivers slower, with data from MIT, Trendyol, and Anthropic
- **Where The Constraint Moved:** Theory of Constraints applied to agentic teams, and the new bottlenecks (code review, requirements, QA, deployment)
- **The SDLC Is The Unblock:** how Ship-Show-Ask, trunk-based development, and DORA change once agents are in the loop
- **Knowledge Propagation:** lunch-and-learns, sprint demos, AI-first experiment teams, and the feedback flywheel for compounding team learning
- **Skills As The Payoff:** the layer above CLAUDE.md where senior knowledge becomes runnable for the whole team, with a live walkthrough

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

_All attendees receive the full recording, slides, and any resources mentioned, so sign up even if you cannot make the live session._
