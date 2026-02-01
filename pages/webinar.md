---
layout: page
title: "Webinars To Get You Ahead With AI"
permalink: /webinar/
excerpt: "Join our webinar series for leaders leveraging AI in their organisations."
image: /assets/img/ai-agents-production-webinar.png
image_portrait: false
kit_tag: webinar12
webinar_date: "2026-02-05T14:00:00+00:00"
---

<div class="mb-12">

  <p class="text-2xl text-brand-black font-bold mb-4">
    Next session: {{ page.webinar_date | date: "%B %-d, %-I:%M%P %Z" }}
  </p>

  <p class="text-2xl text-brand-black mb-8">
    Join me for live workshops on leveraging AI effectively in your organisation.
  </p>

  <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-8">
    <h3 class="text-lg font-bold text-brand-black mb-4">What We Cover:</h3>
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
</div>

<div id="previous-webinars" class="border-t border-brand-light-blue/20 pt-12">
  <h2 class="text-2xl font-heading font-bold mb-6 text-brand-black">Previous Webinars</h2>
  <div class="space-y-1 mb-12">
    {% for post in site.categories.webinar %}
      {% assign post_time = post.date | date: "%s" | plus: 0 %}
      {% assign now_time = site.time | date: "%s" | plus: 0 %}
      {% if post_time > now_time %}{% continue %}{% endif %}
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
    {% assign shown_count = 0 %}
    {% for post in site.categories.ai %}
      {% assign post_time = post.date | date: "%s" | plus: 0 %}
      {% assign now_time = site.time | date: "%s" | plus: 0 %}
      {% if post_time > now_time %}{% continue %}{% endif %}
      {% unless post.categories contains 'webinar' %}
        {% if shown_count >= 5 %}{% break %}{% endif %}
        {% assign shown_count = shown_count | plus: 1 %}
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
