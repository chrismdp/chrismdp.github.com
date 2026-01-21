---
layout: default
title: "Cut Through the AI Chaos"
permalink: /
excerpt: "I help leaders cut through the hype and help them leverage AI to transform their business."
---

{% include header.html style="overlay" %}

<!-- Hero Section -->
<section class="relative bg-gradient-to-br from-brand-deep-turquoise to-brand-turquoise text-white pt-40 md:pb-20 overflow-hidden">
  <!-- Background Image - Desktop only -->
  <div class="hidden md:block absolute bottom-0 right-0 w-full h-2/3 overflow-hidden">
    <img src="/assets/img/chris-hero-bg.png" alt="Chris Parsons" class="absolute bottom-0 right-0 h-full w-auto object-cover object-bottom">
  </div>

  <div class="w-full px-6 relative z-10">
    <div class="text-center mb-16">
      <h1 class="text-4xl md:text-7xl font-heading font-bold mb-6 leading-tight mx-6">Cut Through The AI Chaos</h1>
      <p class="text-xl md:text-3xl mb-8 text-white mx-6 sm:mx-32">I help leaders leverage AI to transform their teams<br/>and dodge the chaotic hype that wastes time and money</p>
    </div>

    <div class="grid md:grid-cols-2 gap-12 items-center">
      <div class="md:ml-8">
        <div class="bg-brand-deep-turquoise rounded-lg p-6">
          <div class="rm-area-embed-subscribe"></div>
        </div>
      </div>
      <div class="relative z-20">
        <!-- This div maintains the grid layout but the image is now in the background -->
      </div>
    </div>

    <!-- Mobile Image - Show below form on mobile -->
    <div class="md:hidden -mx-6 flex justify-end">
      <img src="/assets/img/chris-hero-bg.png" alt="Chris Parsons" class="w-1/2 h-auto object-contain">
    </div>
  </div>
</section>

<!-- Why Subscribe Section -->
<section id="newsletter" class="py-20 bg-brand-white overflow-hidden">
  <div class="w-full">
    <div class="text-center mb-12 px-6">
      <h2 class="text-3xl md:text-4xl font-heading font-bold mb-6 text-brand-black">Try my newsletter to unlock my AI resource library</h2>
      <p class="text-xl text-brand-black/80 mb-8 mx-4 sm:mx-24">Dozens of free guides and practical AI advice for leaders, delivered weekly.</p>
    </div>

    <!-- Infographic Gallery - 3 slots, each cycles through different posts -->
    <style>
      .infographic-gallery {
        --transition-duration: 800ms;
        --transition-timing: cubic-bezier(0.4, 0, 0.2, 1);
      }

      .gallery-slot {
        position: relative;
        overflow: hidden;
      }

      .gallery-item {
        position: absolute;
        inset: 0;
        opacity: 0;
        transition: opacity var(--transition-duration) var(--transition-timing);
        pointer-events: none;
      }

      .gallery-item.active {
        opacity: 1;
        pointer-events: auto;
      }

      .gallery-item img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        object-position: center;
      }

      /* Mobile: stack and take more width */
      @media (max-width: 768px) {
        .infographic-gallery {
          padding-left: 0.5rem !important;
          padding-right: 0.5rem !important;
        }
        .gallery-grid {
          grid-template-columns: 1fr !important;
          gap: 0.75rem !important;
        }
        .gallery-slot {
          height: 340px !important;
        }
      }
    </style>

    {% assign infographic_posts = "" | split: "" %}
    {% assign sorted_posts = site.posts | sort: "date" | reverse %}
    {% for post in sorted_posts limit: 30 %}
      {% if post.infographic and post.infographic_carousel != false %}
        {% assign infographic_posts = infographic_posts | push: post %}
      {% endif %}
      {% if infographic_posts.size >= 9 %}
        {% break %}
      {% endif %}
    {% endfor %}

    <div class="infographic-gallery px-6 md:px-12">
      <div class="gallery-grid grid grid-cols-3 gap-6">
        <!-- Slot 1: posts 0, 3, 6 -->
        <div class="gallery-slot" style="height: 420px;" data-cycle-speed="5000">
          {% for post in infographic_posts %}
            {% assign mod = forloop.index0 | modulo: 3 %}
            {% if mod == 0 %}
          <a href="{{ post.url }}" class="gallery-item {% if forloop.index0 == 0 %}active{% endif %}">
            <img src="{{ post.infographic }}" alt="{{ post.title }}" loading="{% if forloop.index0 == 0 %}eager{% else %}lazy{% endif %}">
          </a>
            {% endif %}
          {% endfor %}
        </div>
        <!-- Slot 2: posts 1, 4, 7 -->
        <div class="gallery-slot" style="height: 420px;" data-cycle-speed="4000">
          {% for post in infographic_posts %}
            {% assign mod = forloop.index0 | modulo: 3 %}
            {% if mod == 1 %}
          <a href="{{ post.url }}" class="gallery-item {% if forloop.index0 == 1 %}active{% endif %}">
            <img src="{{ post.infographic }}" alt="{{ post.title }}" loading="{% if forloop.index0 == 1 %}eager{% else %}lazy{% endif %}">
          </a>
            {% endif %}
          {% endfor %}
        </div>
        <!-- Slot 3: posts 2, 5, 8 -->
        <div class="gallery-slot" style="height: 420px;" data-cycle-speed="6000">
          {% for post in infographic_posts %}
            {% assign mod = forloop.index0 | modulo: 3 %}
            {% if mod == 2 %}
          <a href="{{ post.url }}" class="gallery-item {% if forloop.index0 == 2 %}active{% endif %}">
            <img src="{{ post.infographic }}" alt="{{ post.title }}" loading="{% if forloop.index0 == 2 %}eager{% else %}lazy{% endif %}">
          </a>
            {% endif %}
          {% endfor %}
        </div>
      </div>
    </div>

    <p class="text-center mt-8 text-brand-black/60">Try my newsletter above to access all my guides in high resolution</p>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
      const slots = document.querySelectorAll('.gallery-slot');

      slots.forEach(slot => {
        const items = slot.querySelectorAll('.gallery-item');
        const totalItems = items.length;
        if (totalItems === 0) return;

        const cycleSpeed = parseInt(slot.dataset.cycleSpeed) || 5000;

        // Start at random index
        let currentIndex = Math.floor(Math.random() * totalItems);

        // Clear any server-side active class and set random start
        items.forEach((item, i) => {
          item.classList.remove('active');
        });
        items[currentIndex].classList.add('active');

        function cycleSlot() {
          items[currentIndex].classList.remove('active');
          currentIndex = (currentIndex + 1) % totalItems;
          items[currentIndex].classList.add('active');
        }

        // Start cycling with slight random offset to desync slots
        const randomOffset = Math.random() * 1000;
        setTimeout(() => {
          setInterval(cycleSlot, cycleSpeed);
        }, randomOffset);
      });
    });
    </script>
  </div>
</section>

<!-- More About Chris Section -->
<section class="py-20 bg-white">
  <div class="max-w-4xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-12 text-brand-black">More About Chris</h2>

    <div class="grid md:grid-cols-2 gap-12 items-top">
      <div>
        <img src="/assets/img/chris-twitter-headshot.png" alt="Chris Parsons" class="w-32 h-32 rounded-full object-cover mb-6">
        <p class="text-lg text-brand-black/80 mb-6">
          I've been a CTO and founder. I've scaled companies whilst building production AI systems and transformed delivery using AI tools.
        </p>

        <div class="grid grid-cols-2 gap-4 mb-6">
          <div class="text-center p-4 bg-brand-white rounded-lg border border-brand-light-blue/20">
            <div class="text-2xl font-bold text-brand-deep-turquoise">5</div>
            <div class="text-sm text-brand-black/70">Startups Founded</div>
          </div>
          <div class="text-center p-4 bg-brand-white rounded-lg border border-brand-light-blue/20">
            <div class="text-2xl font-bold text-brand-deep-turquoise">2</div>
            <div class="text-sm text-brand-black/70">Startups VC-backed</div>
          </div>
          <div class="text-center p-4 bg-brand-white rounded-lg border border-brand-light-blue/20">
            <div class="text-2xl font-bold text-brand-deep-turquoise">$1M+</div>
            <div class="text-sm text-brand-black/70">ARR Bootstrapped</div>
          </div>
          <div class="text-center p-4 bg-brand-white rounded-lg border border-brand-light-blue/20">
            <div class="text-2xl font-bold text-brand-deep-turquoise">4</div>
            <div class="text-sm text-brand-black/70">AI Systems Shipped to Production</div>
          </div>
        </div>
      </div>

      <div class="space-y-6">
        <div class="bg-brand-white rounded-lg p-6">
          <h3 class="text-xl font-heading font-bold mb-3 text-brand-black flex items-center">
            <i data-lucide="rocket" class="w-6 h-6 mr-3 text-brand-deep-turquoise"></i>
            Experienced Tech Founder
          </h3>
          <p class="text-brand-black/80">Scaled teams from 5-50. Built agencies, B2B, and B2C startups. VC-backed and bootstrapped experience.</p>
        </div>

        <div class="bg-brand-white rounded-lg p-6">
          <h3 class="text-xl font-heading font-bold mb-3 text-brand-black flex items-center">
            <i data-lucide="bot" class="w-6 h-6 mr-3 text-brand-deep-turquoise"></i>
            AI Systems Expert
          </h3>
          <p class="text-brand-black/80">Production AI systems with full evaluation frameworks, not demos. Real systems serving 500K+ users.</p>
        </div>

        <div class="bg-brand-white rounded-lg p-6">
          <h3 class="text-xl font-heading font-bold mb-3 text-brand-black flex items-center">
            <i data-lucide="zap" class="w-6 h-6 mr-3 text-brand-deep-turquoise"></i>
            High-Impact Enabler
          </h3>
          <p class="text-brand-black/80">{{ 'now' | date: "%Y" | minus: 2001 }} years in tech leadership. I go into organisations and deliver value fast, for leaders who need quick high impact results.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Testimonials Section -->
<section class="py-20 bg-brand-deep-turquoise">
  <div class="max-w-6xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-12 text-white">What Leaders Say</h2>

    <div class="grid md:grid-cols-3 gap-8">
      <div class="bg-white rounded-lg p-6 shadow-md">
        <div class="flex items-center mb-4">
          <a href="https://www.linkedin.com/in/tamosauskas/" target="_blank" class="flex items-center">
            <img src="/assets/img/testimonials/tadas-t.jpeg" alt="Tadas T" class="w-12 h-12 rounded-full mr-4 object-cover">
            <div>
              <div class="font-semibold">Tadas T</div>
              <div class="text-sm text-brand-black/70">CTO</div>
            </div>
          </a>
        </div>
        {% include five-star.html %}
        <p class="text-brand-black italic">"Fantastic at building self-sufficient teams and giving them what they need."</p>
      </div>

      <div class="bg-white rounded-lg p-6 shadow-md">
        <div class="flex items-center mb-4">
          <a href="https://www.linkedin.com/in/roisiproven/" target="_blank" class="flex items-center">
            <img src="/assets/img/testimonials/roisi-p.jpeg" alt="Roisi P" class="w-12 h-12 rounded-full mr-4 object-cover">
            <div>
              <div class="font-semibold">Roisi P</div>
              <div class="text-sm text-brand-black/70">Product Leader</div>
            </div>
          </a>
        </div>
        {% include five-star.html %}
        <p class="text-brand-black italic">"If you're looking for someone to help build a great team, or you need someone experienced to help develop a sound tech strategy, I would thoroughly recommend Chris."</p>
      </div>

      <div class="bg-white rounded-lg p-6 shadow-md">
        <div class="flex items-center mb-4">
          <a href="https://www.linkedin.com/in/ianozsvald/" target="_blank" class="flex items-center">
            <img src="/assets/img/testimonials/ian-o.jpeg" alt="Ian O" class="w-12 h-12 rounded-full mr-4 object-cover">
            <div>
              <div class="font-semibold">Ian O</div>
              <div class="text-sm text-brand-black/70">Data Science Leader</div>
            </div>
          </a>
        </div>
        {% include five-star.html %}
        <p class="text-brand-black italic">"Chris has clearly learned a lot about the world of being a delivery-focused CTO"</p>
      </div>
    </div>
  </div>
</section>

<!-- Proof Section -->
<section class="py-20 bg-white">
  <div class="max-w-6xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-4 text-brand-black">I learn in public and share everything I discover</h2>

    <div class="grid md:grid-cols-3 gap-8 mt-12">
      <div class="bg-brand-white rounded-lg p-6 hover:shadow-lg transition-shadow border border-brand-light-blue/20">
        <i data-lucide="video" class="w-10 h-10 mb-4 text-brand-deep-turquoise"></i>
        <h3 class="text-xl font-heading font-bold mb-2">Webinars</h3>
        {% assign webinar_page = site.pages | where: "url", "/webinar" | first %}
        {% if webinar_page.webinar_date %}
          <p class="text-2xl min-h-16 font-bold text-brand-deep-turquoise mb-2">Next sessions: {{ webinar_page.webinar_date | date: "%B %-d, %-I%P UK" }}</p>
        {% else %}
          <p class="text-2xl min-h-16 font-bold text-brand-deep-turquoise mb-2">Next webinar coming soon</p>
        {% endif %}
        <p class="text-brand-black/80 mb-4 min-h-24">Join me for a hype-free AI deep-dive, and learn exactly how to leverage AI that works now</p>
        <a href="/webinar" target="_blank" class="inline-block bg-brand-deep-turquoise text-white px-4 py-2 rounded-lg hover:bg-brand-turquoise transition-colors mr-2 align-center">Reserve your place →</a>
        <a href="/webinar#previous-webinars" class="mt-2 inline-block text-brand-black px-4 py-2 rounded-lg hover:bg-brand-black/80 transition-colors">See previous webinars →</a>
      </div>

      <div class="bg-brand-white rounded-lg p-6 hover:shadow-lg transition-shadow border border-brand-light-blue/20">
        <i data-lucide="mic" class="w-10 h-10 mb-4 text-brand-deep-turquoise"></i>
        {% assign today = site.time | date: "%s" %}
        {% assign talk_posts = site.posts | where: "categories", "talk" %}
        {% assign upcoming_talks = "" | split: "" %}
        {% assign past_talks = "" | split: "" %}
        {% for talk in talk_posts %}
          {% assign talk_date_seconds = talk.talk_date | date: "%s" %}
          {% if talk_date_seconds >= today %}
            {% assign upcoming_talks = upcoming_talks | push: talk %}
          {% else %}
            {% assign past_talks = past_talks | push: talk %}
          {% endif %}
        {% endfor %}
        {% assign upcoming_talks = upcoming_talks | sort: "talk_date" %}
        {% assign past_talks = past_talks | sort: "talk_date" | reverse %}
        
        {% if upcoming_talks.size > 0 %}
          <h3 class="text-xl font-heading font-bold mb-2">Next Speaking Event</h3>
          {% assign next_talk = upcoming_talks.first %}
          <p class="text-2xl min-h-16 font-bold text-brand-deep-turquoise mb-2">{{ next_talk.event_name }}: {{ next_talk.talk_date | date: "%B %Y" }}</p>
          <p class="text-brand-black/80 mb-4 min-h-24">{{ next_talk.talk_title }}</p>
          <a href="{{ next_talk.url }}" target="_blank" class="inline-block bg-brand-deep-turquoise text-white px-4 py-2 rounded-lg hover:bg-brand-turquoise transition-colors mr-2">View session →</a>
          <a href="{{ site.baseurl }}/talks/" class="mt-2 inline-block bg-trans px-4 py-2 rounded-lg hover:bg-deep-turquoise/80 transition-colors">See all talks →</a>
        {% elsif past_talks.size > 0 %}
          <h3 class="text-xl font-heading font-bold mb-2">Latest Speaking Event</h3>
          {% assign latest_talk = past_talks.first %}
          <p class="text-2xl font-bold text-brand-deep-turquoise mb-2">{{ latest_talk.event_name }}: {{ latest_talk.talk_date | date: "%B %Y" }}</p>
          <p class="text-brand-black/80 min-h-24 mb-4">{{ latest_talk.talk_title }}</p>
          <a href="{{ latest_talk.url }}" class="inline-block bg-brand-deep-turquoise text-white px-4 py-2 rounded-lg hover:bg-brand-turquoise transition-colors mr-2">Read about talk →</a>
          <a href="{{ site.baseurl }}/talks/" class="inline-block mt-2 px-4 py-2 rounded-lg hover:bg-brand-black/80 transition-colors">See all talks →</a>
        {% else %}
          <h3 class="text-xl font-heading font-bold mb-2">Speaking Events</h3>
          <p class="text-2xl font-bold text-brand-deep-turquoise mb-2">No talks scheduled</p>
          <p class="text-brand-black/80 mb-4">Check back soon for my next speaking engagement</p>
          <a href="/articles/" class="inline-block bg-brand-deep-turquoise text-white px-4 py-2 rounded-lg hover:bg-brand-turquoise transition-colors">Read latest articles →</a>
        {% endif %}
      </div>

      <div class="bg-brand-white rounded-lg p-6 hover:shadow-lg transition-shadow border border-brand-light-blue/20">
        <i data-lucide="monitor-play" class="w-10 h-10 mb-4 text-brand-deep-turquoise"></i>
        <h3 class="text-xl font-heading font-bold mb-2">Production AI Systems</h3>
        <p class="text-2xl font-bold min-h-16 text-brand-deep-turquoise mb-2">Three evaluation frameworks built</p>
        <p class="text-brand-black/80 min-h-24 mb-4">From Cherrypick's meal generator to complex internal tools, I build systems with robust evaluation from day one</p>
        <a href="/case-studies/gpt-meal-generator" target="_blank" class="inline-block bg-brand-deep-turquoise text-white px-4 py-2 rounded-lg hover:bg-brand-turquoise transition-colors">Read case study →</a>
      </div>
    </div>
  </div>
</section>


<!-- Services Section -->
<section id="services" class="py-20 bg-white">
  <div class="max-w-6xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-12 text-brand-black">My Services</h2>
    <p class="text-xl text-center mb-12 text-brand-black/80 max-w-3xl mx-auto">Your board wants AI strategy. Your team needs practical guidance. Your company needs results without implementation disasters.</p>
    <p class="text-xl text-center mb-12 text-brand-black/80 max-w-3xl mx-auto">Here's how I help CEOs and leaders succeed where others fail.</p>

    <!-- Main Services - Two Columns -->
    <div class="grid md:grid-cols-2 gap-8 mb-12">
      <div class="bg-white border-2 border-brand-light-blue/30 rounded-lg p-8 hover:border-brand-deep-turquoise transition-colors">
        <i data-lucide="users" class="w-8 h-8 mb-4 text-brand-deep-turquoise"></i>
        <h3 class="text-2xl font-heading font-bold mb-4">AI TRAINING</h3>
        <p class="text-lg font-semibold mb-4 text-brand-black">Modular training that fits your team's needs</p>
        <p class="text-brand-black/80 leading-relaxed mb-4">
          From half-day foundations to multi-day programmes, with tailored pathways for developers, product managers, researchers, and executives. Transform random ChatGPT questions into systematic AI workflows with security and quality standards built in.
        </p>
        <a href="/training/" class="inline-block bg-brand-deep-turquoise text-white px-6 py-2 rounded-lg hover:bg-brand-turquoise transition-colors">View Details →</a>
      </div>

      <div class="bg-white border-2 border-brand-light-blue/30 rounded-lg p-8 hover:border-brand-deep-turquoise transition-colors">
        <i data-lucide="compass" class="w-8 h-8 mb-4 text-brand-deep-turquoise"></i>
        <h3 class="text-2xl font-heading font-bold mb-4">C-LEVEL AI ADVISORY</h3>
        <p class="text-lg font-semibold mb-4 text-brand-black">Direct access when you need experienced perspective</p>
        <p class="text-brand-black/80 leading-relaxed mb-4">
          Monthly strategic sessions with someone who's been in your position. Get advice on tool selection, team challenges, vendor negotiations, and board communication. Plus urgent access for critical decisions.
        </p>
        <a href="#contact" class="inline-block bg-brand-deep-turquoise text-white px-6 py-2 rounded-lg hover:bg-brand-turquoise transition-colors">Get in Touch →</a>
      </div>
    </div>

    <!-- AI Leader Accelerator - Smaller -->
    <div class="bg-brand-light-blue/10 border border-brand-light-blue/30 rounded-lg p-6 mb-12">
      <div class="flex flex-col md:flex-row gap-6 items-center">
        <div class="flex-1">
          <div class="flex items-center gap-3 mb-2">
            <i data-lucide="graduation-cap" class="w-6 h-6 text-brand-deep-turquoise"></i>
            <h3 class="text-xl font-heading font-bold">AI Leader Accelerator</h3>
            <span class="text-sm bg-brand-black/10 text-brand-black/60 px-2 py-1 rounded">Applications closed</span>
          </div>
          <p class="text-brand-black/70 text-sm">
            8-week peer learning programme for senior technical leaders. <a href="/ai-leader-accelerator/" class="text-brand-deep-turquoise hover:underline">Learn more</a> or <a href="mailto:chris@chrismdp.com?subject=AI%20Leader%20Accelerator" class="text-brand-deep-turquoise hover:underline">get in touch</a> for future cohorts.
          </p>
        </div>
      </div>
    </div>


    <!-- Contact Form -->
    <div id="contact" class="max-w-2xl mx-auto">
      <div class="bg-brand-deep-turquoise rounded-lg p-8">
        <div class="rm-area-embed-services"></div>
      </div>
    </div>
  </div>
</section>

<!-- TFC Case Study Section -->
<section class="py-20 bg-brand-deep-turquoise">
  <div class="max-w-4xl mx-auto px-6">
    {% include testimonial-tfc.html %}
  </div>
</section>


<!-- Latest Articles Section -->
<section class="py-20 bg-white">
  <div class="max-w-4xl mx-auto px-6">
    <h2 class="text-3xl font-heading font-bold mb-8 text-brand-black">Latest Articles</h2>

    {% assign latest_posts = site.posts | slice: 0, 3 %}
    {% include article-list.html posts=latest_posts %}

    <div class="text-center space-x-4 mt-8">
      <a href="{{ site.baseurl }}/articles/" class="inline-block bg-brand-black text-white px-6 py-3 rounded-lg hover:bg-brand-black/80 transition-colors">View All Articles</a>
      <a href="{{ site.baseurl }}/talks/" class="inline-block bg-brand-deep-turquoise text-white px-6 py-3 rounded-lg hover:bg-brand-turquoise transition-colors">See All Talks</a>
    </div>
  </div>
</section>

<!-- Final CTA Section -->
<section class="py-20 bg-gradient-to-br from-brand-deep-turquoise to-brand-turquoise text-white">
  <div class="max-w-4xl mx-auto text-center px-6">
    <h2 class="text-4xl md:text-6xl font-heading font-bold mb-6 text-white">Your Board's Asking About AI. Your Team's Waiting for Direction.</h2>
    <p class="text-2xl mb-8 text-white">Join hundreds of leaders getting weekly AI insights that actually work now</p>

    <div class="max-w-md mx-auto bg-brand-deep-turquoise rounded-lg p-6 border border-brand-turquoise">
      <div class="rm-area-embed-subscribe"></div>
    </div>
  </div>
</section>
