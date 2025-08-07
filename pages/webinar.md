---
layout: page
title: "AI for Technical Leaders"
permalink: /webinar
excerpt: "Join our monthly webinar series for technical leaders implementing AI in their organisations."
image: /assets/img/ai-agents-production-webinar.png
image_portrait: false
kit_tag: webinar6
webinar_date: "2025-09-04T14:00:00+01:00"
---

<div class="mb-12">

  <p class="text-2xl text-brand-black mb-8">
    Join me for monthly live workshops on implementing AI effectively in technical organisations.
  </p>

  <p class="text-xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I%P %Z" }}
  </p>

  <p class="text-lg text-brand-black mb-8">
    <strong>AI for Technical Leaders</strong><br>
    Practical insights for CTOs, engineering managers, and technical founders implementing AI in their organisations.
  </p>

  <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Cover Each Month:</h3>
    <ul class="space-y-2 text-brand-black">
      <li><strong>Strategic AI Implementation:</strong> When and how to deploy AI tools and systems effectively in your organisation</li>
      <li><strong>Production Reality:</strong> Moving from impressive demos to reliable AI solutions that deliver business value</li>
      <li><strong>Technology Decisions:</strong> Choosing the right AI models, tools, and approaches for your specific use cases</li>
      <li><strong>Risk Management:</strong> Security, reliability, and governance considerations for AI adoption</li>
      <li><strong>Team Leadership:</strong> Building AI capabilities and literacy within engineering and product teams</li>
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
