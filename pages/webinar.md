---
layout: page
title: "Webinar: How Not to Screw Up Your AI Rollout"
permalink: /webinar
excerpt: "Plenty of teams have made massive gains with AI. Others show teams getting slower. Learn what makes the difference."
image: /assets/img/ai-rollout-failure-webinar.png
image_portrait: false
kit_tag: webinar6
webinar_date: "2025-09-04T14:00:00+01:00"
---

<div class="mb-12">


  <p class="text-xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I%P %Z" }}
  </p>

  <p class="text-lg text-brand-black mb-8">
    <strong>Plenty of teams have made massive gains with AI.</strong> Stanford research on 5,179 customer service workers found 14% productivity increases, with novice workers improving 34%. The Nielsen Norman Group's independent analysis shows 66% average productivity improvements across business tasks. Business professionals are writing 59% more documents with significantly higher quality.
  </p>

  <p class="text-lg text-brand-black mb-8">
    <strong>But other studies show AI making teams slower.</strong> Independent research found experienced developers took 19% longer to complete tasks when using AI tools. Teams often see initial productivity drops of up to 60 percentage points during the first 3-18 months of AI adoption. Even high-profile companies have stumbled badly on AI rollout communications and strategy.
  </p>

  <p class="text-lg text-brand-black mb-8">
    <strong>What makes the difference?</strong> Join me next week to discover the "Jagged Frontier" concept, why the mindset shift matters more than tool selection, and how to avoid the AI tools that backfire on unprepared teams.
  </p>

  <div class="bg-brand-black text-white rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold mb-4" style="color: white;">Who Should Attend:</h3>
    <ul class="space-y-2">
      <li><strong>Team Leaders & Managers:</strong> Responsible for team productivity and tool adoption</li>
      <li><strong>CTOs & Technical Directors:</strong> Planning AI adoption strategy across departments</li>
      <li><strong>Operations & Process Leaders:</strong> Implementing AI tools across teams and workflows</li>
      <li><strong>Founders & Department Heads:</strong> Looking to scale team capabilities with AI</li>
    </ul>
  </div>

  <div class="bg-brand-deep-turquoise rounded-lg p-8 text-center mb-12">
    <div class="rm-area-embed-webinar"></div>
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
          hour12: true,
          timeZone: 'Europe/London'
        };
        
        const day = webinarDate.toLocaleDateString('en-GB', dayOptions);
        const month = webinarDate.toLocaleDateString('en-GB', monthOptions);
        const ukTime = webinarDate.toLocaleTimeString('en-GB', timeOptions).toLowerCase();
        const ukFormatted = `${day}${getOrdinalSuffix(day)} ${month}, ${ukTime}`;
        
        const etOptions = { 
          hour: 'numeric', 
          hour12: true,
          timeZone: 'America/New_York'
        };
        const etTime = webinarDate.toLocaleTimeString('en-US', etOptions).toLowerCase();
        
        titleElement.textContent = `{{ page.title }} - ${ukFormatted} UK / ${etTime} ET`;
      } else {
        // Try again in 500ms if element not found yet
        setTimeout(updateWebinarTitle, 500);
      }
    }
    
    // Initial attempt
    updateWebinarTitle();
  });
  </script>
</div>

<div class="border-t border-brand-light-blue/20 pt-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Previous Webinars</h2>
  <div class="space-y-1 mb-12">
    {% for post in site.categories.webinar limit:5 %}
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
