---
layout: default
title: "AI Leader Accelerator: Turning Technical Leaders into AI Leaders"
permalink: /ai-leader-accelerator/
excerpt: "A peer learning programme for senior technical leaders navigating AI adoption. 8 weeks. 3 hours per week. A small group of CTOs and VPs working through AI strategy together."
---

{% include header.html style="overlay" %}

<!-- Sticky CTA Bar (appears on scroll) -->
<div id="sticky-cta" class="fixed top-0 left-0 right-0 z-50 bg-brand-deep-turquoise/95 backdrop-blur-sm py-3 transform -translate-y-full transition-transform duration-300">
  <div class="flex items-center justify-center gap-6 px-6">
    <span class="text-white font-heading font-bold hidden sm:inline">AI Leader Accelerator</span>
    <div class="flex gap-4">
      <a href="#apply" class="inline-block bg-white hover:bg-white/90 text-brand-deep-turquoise font-bold py-2 px-6 rounded-lg transition-colors text-sm">Begin Application</a>
      <a href="#syllabus" class="inline-block bg-white/20 hover:bg-white/30 text-white font-bold py-2 px-6 rounded-lg transition-colors text-sm">See the Syllabus</a>
    </div>
  </div>
</div>

<!-- Hero Section -->
<section class="relative bg-gradient-to-br from-brand-deep-turquoise to-brand-turquoise text-white pt-40 pb-20 overflow-hidden">
  <div class="w-full px-6 relative z-10">
    <div class="text-center mb-12">
      <p class="text-lg uppercase tracking-wide mb-4 text-white/80">For Senior Technical Leaders</p>
      <h1 class="text-5xl md:text-6xl font-heading font-bold mb-6 leading-tight mx-4">AI Leader Accelerator</h1>
      <p class="text-2xl md:text-2xl mb-8 text-white mx-4 sm:mx-24">8 weeks to transform how your organisation adopts AI.</p>

      <div class="max-w-3xl mx-auto mb-8">
        <div class="grid md:grid-cols-3 gap-4 text-left">
          <div class="bg-white/10 rounded-lg p-4">
            <p class="text-white/90 text-sm"><strong class="text-white">You will build</strong> an AI strategy that is peer-tested and fits your organisation</p>
          </div>
          <div class="bg-white/10 rounded-lg p-4">
            <p class="text-white/90 text-sm"><strong class="text-white">You will gain confidence</strong> to answer board and team questions on security, compliance, and tradeoffs</p>
          </div>
          <div class="bg-white/10 rounded-lg p-4">
            <p class="text-white/90 text-sm"><strong class="text-white">You will form</strong> a network of CTO peers facing the same challenges that lasts for years</p>
          </div>
        </div>
      </div>

      <p class="text-lg mx-4 sm:mx-24 text-white/70 mb-8">3 hours a week commitment.</p>

      <!-- Countdown Timer -->
      <div class="mb-8">
        <p class="text-white/80 text-sm uppercase tracking-wide mb-4">Programme Starts 19th January 2026</p>
        <div id="countdown" class="flex justify-center gap-4 md:gap-8">
          <div class="bg-white/10 rounded-lg p-4 min-w-[80px]">
            <p id="countdown-days" class="text-3xl md:text-4xl font-bold">--</p>
            <p class="text-white/70 text-sm">Days</p>
          </div>
          <div class="bg-white/10 rounded-lg p-4 min-w-[80px]">
            <p id="countdown-hours" class="text-3xl md:text-4xl font-bold">--</p>
            <p class="text-white/70 text-sm">Hours</p>
          </div>
          <div class="bg-white/10 rounded-lg p-4 min-w-[80px]">
            <p id="countdown-minutes" class="text-3xl md:text-4xl font-bold">--</p>
            <p class="text-white/70 text-sm">Minutes</p>
          </div>
          <div class="bg-white/10 rounded-lg p-4 min-w-[80px]">
            <p id="countdown-seconds" class="text-3xl md:text-4xl font-bold">--</p>
            <p class="text-white/70 text-sm">Seconds</p>
          </div>
        </div>
      </div>

      <div class="flex flex-wrap justify-center gap-4">
        <a href="#apply" class="inline-block bg-white hover:bg-white/90 text-brand-deep-turquoise font-bold py-3 px-8 rounded-lg text-lg transition-colors">Begin Application</a>
        <a href="#syllabus" class="inline-block bg-white/20 hover:bg-white/30 text-white font-bold py-3 px-8 rounded-lg text-lg transition-colors">See the Syllabus</a>
      </div>
    </div>
  </div>
</section>

<script>
  function updateCountdown() {
    const targetDate = new Date('2026-01-19T17:00:00Z');
    const now = new Date();
    const diff = targetDate - now;

    if (diff <= 0) {
      document.getElementById('countdown-days').textContent = '0';
      document.getElementById('countdown-hours').textContent = '0';
      document.getElementById('countdown-minutes').textContent = '0';
      document.getElementById('countdown-seconds').textContent = '0';
      return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    document.getElementById('countdown-days').textContent = days;
    document.getElementById('countdown-hours').textContent = hours;
    document.getElementById('countdown-minutes').textContent = minutes;
    document.getElementById('countdown-seconds').textContent = seconds;
  }

  updateCountdown();
  setInterval(updateCountdown, 1000);
</script>

<!-- The Situation Section -->
<section class="py-20 bg-white">
  <div class="max-w-4xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-8 text-brand-black">AI Is The Technology Shift That Cannot Wait.</h2>

    <div class="space-y-6 text-xl text-brand-black/80 text-center mb-10">
      <p>Previous technology shifts gave you time to wait and learn from others. AI does not. Your teams are already using it whether you are steering it or not, and the signal-to-noise ratio on who to trust is terrible.</p>
    </div>

    <div class="grid md:grid-cols-2 gap-6 mt-12 mb-16">
      <div class="bg-brand-light-blue/20 rounded-lg p-6">
        <p class="text-brand-black/80 italic mb-4">"Everyone is doing cool stuff with AI, and I have no one to talk to about it."</p>
        <p class="text-brand-deep-turquoise font-semibold text-sm">CTO, Media Company</p>
      </div>
      <div class="bg-brand-light-blue/20 rounded-lg p-6">
        <p class="text-brand-black/80 italic mb-4">"I often find it difficult to share ideas with people because there is nobody else really in the same situation."</p>
        <p class="text-brand-deep-turquoise font-semibold text-sm">Head of Engineering, Automotive</p>
      </div>
      <div class="bg-brand-light-blue/20 rounded-lg p-6">
        <p class="text-brand-black/80 italic mb-4">"I am doing a month's work in a day, but I do not know how to move that to my team."</p>
        <p class="text-brand-deep-turquoise font-semibold text-sm">Fractional CTO</p>
      </div>
      <div class="bg-brand-light-blue/20 rounded-lg p-6">
        <p class="text-brand-black/80 italic mb-4">"Everyone is an expert now. The content is mental. It is horrendous knowing who to trust."</p>
        <p class="text-brand-deep-turquoise font-semibold text-sm">Head of Engineering</p>
      </div>
      <div class="bg-brand-light-blue/20 rounded-lg p-6 md:col-span-2 md:max-w-md md:mx-auto">
        <p class="text-brand-black/80 italic mb-4">"How do we go from pilots to something more deliberate? Do we have a platform team dedicated to this? That is where I would love to be sharing challenges with peers."</p>
        <p class="text-brand-deep-turquoise font-semibold text-sm">CTO, E-commerce</p>
      </div>
    </div>

    <h3 class="text-2xl font-heading font-bold text-center mb-8 text-brand-black">Is This You?</h3>
    <div class="max-w-3xl mx-auto space-y-4">
      <div class="flex items-start gap-4 bg-brand-light-blue/10 rounded-lg p-5">
        <i data-lucide="square" class="w-6 h-6 text-brand-orange flex-shrink-0 mt-0.5"></i>
        <p class="text-brand-black/80">You constantly feel like your organisation is behind in AI, but you have no way of knowing whether you actually are</p>
      </div>
      <div class="flex items-start gap-4 bg-brand-light-blue/10 rounded-lg p-5">
        <i data-lucide="square" class="w-6 h-6 text-brand-orange flex-shrink-0 mt-0.5"></i>
        <p class="text-brand-black/80">You have been experimenting with new techniques, but have nobody at your level to test your thinking against</p>
      </div>
      <div class="flex items-start gap-4 bg-brand-light-blue/10 rounded-lg p-5">
        <i data-lucide="square" class="w-6 h-6 text-brand-orange flex-shrink-0 mt-0.5"></i>
        <p class="text-brand-black/80">You are squeezed between excessive caution on one side and unrealistic optimism on the other, with pressure coming from both the board and the grass roots</p>
      </div>
      <div class="flex items-start gap-4 bg-brand-light-blue/10 rounded-lg p-5">
        <i data-lucide="square" class="w-6 h-6 text-brand-orange flex-shrink-0 mt-0.5"></i>
        <p class="text-brand-black/80">Consultants and vendors are telling you how to implement AI, but none of them have had to roll it out to your team with your constraints</p>
      </div>
      <div class="flex items-start gap-4 bg-brand-light-blue/10 rounded-lg p-5">
        <i data-lucide="square" class="w-6 h-6 text-brand-orange flex-shrink-0 mt-0.5"></i>
        <p class="text-brand-black/80">The only AI training you can find teaches tools, not how to lead organisational change</p>
      </div>
    </div>
  </div>
</section>

<!-- A Different Approach Section -->
<section class="py-20 bg-brand-deep-turquoise">
  <div class="max-w-5xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-4 text-white">A Different Approach</h2>
    <p class="text-xl text-center text-white/80 mb-8">8 weeks of peer learning with expert facilitation. The relationships outlast the programme.</p>

    <div class="bg-white rounded-lg p-8 shadow-lg mb-12">

      <div class="bg-brand-light-blue/30 rounded-lg p-6 mb-8">
        <h3 class="text-2xl font-heading font-bold mb-4 text-brand-deep-turquoise text-center">Weekly Structure: 3 Hours Online</h3>
        <div class="grid md:grid-cols-3 gap-6">
          <div class="text-center">
            <p class="font-semibold mb-2 text-brand-black">Monday Afternoon</p>
            <p class="text-brand-black/70 text-sm">1 hour taught session with frameworks and provocations</p>
          </div>
          <div class="text-center">
            <p class="font-semibold mb-2 text-brand-black">Weekly Clinic</p>
            <p class="text-brand-black/70 text-sm">1 hour thematic small group session to work through your specific blockers</p>
          </div>
          <div class="text-center">
            <p class="font-semibold mb-2 text-brand-black">Thursday Afternoon</p>
            <p class="text-brand-black/70 text-sm">1 hour to ask questions, hold each other accountable, and celebrate wins</p>
          </div>
        </div>
      </div>

      <div class="bg-brand-light-blue/20 rounded-lg p-6 mb-6">
        <h4 class="text-lg font-bold text-brand-deep-turquoise mb-6 text-center">Gain Confidence Through Expert Input</h4>
        <div class="grid md:grid-cols-2 gap-6">
          <div class="flex items-start gap-4">
            <img src="/assets/img/chris-twitter-headshot.png" alt="Chris Parsons" class="w-16 h-16 rounded-full object-cover flex-shrink-0">
            <div>
              <p class="text-brand-black font-semibold mb-1">Chris Parsons</p>
              <p class="text-brand-black/70 text-sm">14 years in senior roles with multiple teams. Currently CTO and Strategic AI Advisor to organisations including Genomics and Cherrypick.</p>
            </div>
          </div>
          <div class="flex items-start gap-4">
            <div class="w-16 h-16 rounded-full bg-brand-deep-turquoise/20 flex items-center justify-center flex-shrink-0">
              <i data-lucide="users" class="w-8 h-8 text-brand-deep-turquoise"></i>
            </div>
            <div>
              <p class="text-brand-black font-semibold mb-1">Guest Experts As Needed</p>
              <p class="text-brand-black/70 text-sm">Specialists in specific techniques and areas, brought in when the cohort needs them.</p>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-6">
        <h4 class="text-lg font-bold text-brand-deep-turquoise mb-3 text-center">Build an Action Plan in Weekly Clinics</h4>
        <p class="text-brand-black/80 text-center mb-6">Intimate, coach-led sessions to help you deal with blockers. Each week has a theme matching that week's content, and you join one clinic per week in a small group of a few people. Multiple clinics run at different times so there is one you can get to.</p>
        <p class="text-brand-black/80 text-center mb-6">Clinics are carefully curated: we group people solving similar problems in compatible time zones, and we ensure no direct competitors share a clinic so you can speak freely about your real challenges.</p>
        <div class="grid md:grid-cols-3 gap-4">
          <div class="bg-white rounded-lg p-4 text-center">
            <i data-lucide="users" class="w-8 h-8 mx-auto mb-2 text-brand-deep-turquoise"></i>
            <p class="text-sm text-brand-black/80">Curated groups solving similar problems</p>
          </div>
          <div class="bg-white rounded-lg p-4 text-center">
            <i data-lucide="shield-check" class="w-8 h-8 mx-auto mb-2 text-brand-deep-turquoise"></i>
            <p class="text-sm text-brand-black/80">No competitors in your clinic</p>
          </div>
          <div class="bg-white rounded-lg p-4 text-center">
            <i data-lucide="globe" class="w-8 h-8 mx-auto mb-2 text-brand-deep-turquoise"></i>
            <p class="text-sm text-brand-black/80">Time zones that work for you</p>
          </div>
        </div>
      </div>

      <div class="bg-brand-light-blue/20 rounded-lg p-6 mt-8">
        <h4 class="text-lg font-bold text-brand-deep-turquoise mb-3 text-center">Forge Relationships That Will Last for Years</h4>
        <div class="space-y-4 text-brand-black/80">
          <p class="text-center">You will be surrounded by CTOs and senior technical leaders solving the same problems as you. Share your wins, struggles, and areas of expertise. Hold each other accountable.</p>
          <p class="text-center">These relationships continue long after the eight weeks end. You will have peers you can call on for years: to sanity-check a decision, to ask how they handled a similar situation, or to compare notes on what is actually working.</p>
          <p class="text-center">Pioneer members become founding members of a network that grows with each cohort.</p>
        </div>
      </div>
    </div>

    <div class="grid md:grid-cols-2 gap-6 mt-12 max-w-5xl mx-auto">
      <div class="bg-white/10 rounded-lg p-6">
        <h4 class="text-lg font-bold text-white mb-4">This Is For You If You Are:</h4>
        <ul class="space-y-3 text-white/90">
          <li class="flex items-start">
            <i data-lucide="check" class="w-5 h-5 mr-2 text-white flex-shrink-0 mt-0.5"></i>
            <span class="text-sm">Working as a CTO, VP of Engineering, Engineering Director, or Fractional CTO</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="check" class="w-5 h-5 mr-2 text-white flex-shrink-0 mt-0.5"></i>
            <span class="text-sm">Running teams of teams (10+ reports)</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="check" class="w-5 h-5 mr-2 text-white flex-shrink-0 mt-0.5"></i>
            <span class="text-sm">Responsible for AI adoption decisions at your organisation</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="check" class="w-5 h-5 mr-2 text-white flex-shrink-0 mt-0.5"></i>
            <span class="text-sm">Wanting strategic clarity on AI adoption for your organisation</span>
          </li>
        </ul>
      </div>

      <div class="bg-white/10 rounded-lg p-6">
        <h4 class="text-lg font-bold text-white/60 mb-4">This Is Not For:</h4>
        <ul class="space-y-3 text-white/70">
          <li class="flex items-start">
            <i data-lucide="x" class="w-5 h-5 mr-2 text-white/50 flex-shrink-0 mt-0.5"></i>
            <span class="text-sm">Individual contributors wanting hands-on coding skills</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="x" class="w-5 h-5 mr-2 text-white/50 flex-shrink-0 mt-0.5"></i>
            <span class="text-sm">Junior or mid-level engineers</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="x" class="w-5 h-5 mr-2 text-white/50 flex-shrink-0 mt-0.5"></i>
            <span class="text-sm">People between jobs</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="x" class="w-5 h-5 mr-2 text-white/50 flex-shrink-0 mt-0.5"></i>
            <span class="text-sm">People looking for tool tutorials</span>
          </li>
        </ul>
        <p class="mt-4 pt-4 border-t border-white/20 text-white/80 text-sm">This is for people making strategic decisions about how their organisations adopt AI.</p>
      </div>
    </div>
  </div>
</section>

<!-- 8-Week Syllabus Section -->
<section id="syllabus" class="py-20 bg-white">
  <div class="max-w-5xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-4 text-brand-black">The 8-Week Syllabus</h2>
    <p class="text-xl text-center text-brand-black/80 mb-12">3 hours online per week, plus implementation. Strategic frameworks. Peer learning. Real challenges.</p>

    <div class="space-y-6">
      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 1</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">The AI Landscape</h3>
        </div>
        <p class="text-brand-black/80">AI is a field, not a single tool. We map the landscape together: what the different categories of AI actually are, where they overlap, and why this matters for adoption. Then you chart exactly where your organisation is right now, comparing yourself to peers and the wider industry. By the end of this week, you will know whether you are behind and how urgent things actually are.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 2</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Level Up Your Own AI Use</h3>
        </div>
        <p class="text-brand-black/80">Some people seem superhuman with AI. What do they know that others do not? We uncover the techniques and mindsets that separate those getting transformative results from those just scratching the surface. Using AI specifically for senior technical strategy work, how to think and strategise better with AI as your partner, and interactive sharing of how others in the group are integrating AI into their leadership workflows. By the end of this week, you will be actively using AI in your daily work.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 3</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Leading Multi-Speed Change with High Uncertainty</h3>
        </div>
        <p class="text-brand-black/80">Simple change management approaches are insufficient. AI is many different things at once, your people are at wildly different stages, and some are actively resistant. We cover how to work through fragmented adoption, build your early adopter team, and create momentum when people are moving at different speeds. We also cover managing up: how to bring the board along, manage expectations, and confidently handle the "why are we not doing X" conversations when people have read about the latest AI trend. By the end of this week, you will have a concrete next step to move your team forward with AI, wherever they are starting from.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 4</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Compliance, Privacy, and Security</h3>
        </div>
        <p class="text-brand-black/80">The questions your board and team will ask, and how to answer them with confidence. Security, privacy, and deployment decisions. Third-party vendors vs hosting locally. Understanding data retention policies and their ambiguities. Risk management frameworks you can actually defend. By the end of this week, you will be able to answer security and compliance questions with confidence.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 5</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Using Advanced Agents for Strategic Thinking</h3>
        </div>
        <p class="text-brand-black/80">How agents differ from chat interfaces. Using agent memory and active journaling to build up a knowledge base your AI can draw on anytime. Beyond one-off tasks: AI as a persistent thinking partner for leadership work. By the end of this week, you will have started building a knowledge base that your AI can draw on anytime you need it.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 6</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">How to Oversee AI in Products</h3>
        </div>
        <p class="text-brand-black/80">Not the tactical work, but understanding strategic constraints and important decisions when building AI into products and internal tools. Where AI adds real value and where it does not. By the end of this week, you will know how to direct your teams with confidence.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 7</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Organising Teams for AI Speed</h3>
        </div>
        <p class="text-brand-black/80">How to structure and organise your teams to move at AI speed. What changes when AI accelerates individual productivity, and how team structures need to adapt. By the end of this week, you will have a concrete understanding of the next steps to take with your teams once AI is embedded.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 8</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Planning for the Future</h3>
        </div>
        <p class="text-brand-black/80">What is coming next in AI: the power of local models, emerging challenges, and how to stay current. Building your ongoing learning strategy and preparing for what is around the corner. By the end of this week, you will have a plan to keep your AI strategy current as the field evolves.</p>
      </div>
    </div>

    <div class="bg-brand-deep-turquoise text-white rounded-lg p-8 mt-12 text-center">
      <p class="text-xl font-semibold mb-2">One week break for half-term included</p>
      <p class="text-white/80">19th January to 20th March 2026</p>
    </div>
  </div>
</section>

<!-- What You Walk Away With Section -->
<section class="py-20 bg-brand-deep-turquoise text-white">
  <div class="max-w-4xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-12">What You Walk Away With</h2>

    <div class="grid md:grid-cols-3 gap-8">
      <div class="bg-white/10 rounded-lg p-6">
        <i data-lucide="map" class="w-10 h-10 mb-4 text-white"></i>
        <h3 class="text-xl font-bold mb-3">An AI Strategy</h3>
        <p class="text-white/80">Peer-tested and fits your organisation. Covering all of AI, not just one tool. A clear plan you can actually execute.</p>
      </div>

      <div class="bg-white/10 rounded-lg p-6">
        <i data-lucide="shield" class="w-10 h-10 mb-4 text-white"></i>
        <h3 class="text-xl font-bold mb-3">Confident Answers</h3>
        <p class="text-white/80">Clear understanding of security, compliance, and UX tradeoffs. Answer board questions and team concerns without hesitation.</p>
      </div>

      <div class="bg-white/10 rounded-lg p-6">
        <i data-lucide="users" class="w-10 h-10 mb-4 text-white"></i>
        <h3 class="text-xl font-bold mb-3">A Lasting Network</h3>
        <p class="text-white/80">CTO peers who have faced the same challenges. A group you can call on for years, not just during the programme.</p>
      </div>
    </div>
  </div>
</section>

<!-- Your Guide Section -->
<section class="py-20 bg-brand-white">
  <div class="max-w-4xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-12 text-brand-black">Your Guide</h2>

    <div class="bg-white rounded-lg p-8 shadow-lg border border-brand-light-blue/20">
      <div class="md:flex items-start gap-8">
        <div class="md:w-1/3 mb-6 md:mb-0">
          <img src="/assets/img/chris-twitter-headshot.png" alt="Chris Parsons" class="w-48 h-48 rounded-lg object-cover mx-auto">
        </div>
        <div class="md:w-2/3">
          <h3 class="text-2xl font-heading font-bold mb-4 text-brand-black">Chris Parsons</h3>
          <div class="space-y-4 text-brand-black/80">
            <p>I am a CTO myself. I am not a consultant who has read about AI adoption; I am in the trenches making these decisions alongside you. 14 years in senior roles with multiple teams, currently CTO and Strategic AI Advisor to startups and scaleups including Genomics and <a href="https://cherrypick.co" target="_blank" class="text-brand-deep-turquoise hover:underline">Cherrypick</a>.</p>
            <p>This programme works because you are surrounded by CTOs and senior technical leaders who understand the same pressures. I facilitate and provoke, bringing frameworks that challenge assumptions. The value comes from testing your thinking against people solving the same problems.</p>
            <p>I spend a significant chunk of my time keeping up with AI so you do not have to filter the noise yourself. Then as a group we work through what actually makes sense for your organisation.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Pioneer Programme Section -->
<section class="py-20 bg-white">
  <div class="max-w-4xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-4 text-brand-black">Pioneer Programme</h2>
    <p class="text-xl text-center text-brand-black/80 mb-12">This is the first cohort. You shape the format.</p>

    <div class="bg-brand-light-blue/20 rounded-lg p-8 mb-8">
      <p class="text-lg text-brand-black/80 mb-6">You provide feedback. You help build something that works for technical leaders.</p>
      <h3 class="text-xl font-bold mb-4 text-brand-deep-turquoise">In exchange:</h3>
      <ul class="space-y-3 text-brand-black/80">
        <li class="flex items-start">
          <i data-lucide="gift" class="w-6 h-6 mr-3 text-brand-deep-turquoise flex-shrink-0"></i>
          <span>Pioneer pricing (up to 44% off future price)</span>
        </li>
        <li class="flex items-start">
          <i data-lucide="infinity" class="w-6 h-6 mr-3 text-brand-deep-turquoise flex-shrink-0"></i>
          <span>Lifetime access to future cohort materials and community</span>
        </li>
        <li class="flex items-start">
          <i data-lucide="users" class="w-6 h-6 mr-3 text-brand-deep-turquoise flex-shrink-0"></i>
          <span>Founding member of a peer network that outlasts the programme</span>
        </li>
        <li class="flex items-start">
          <i data-lucide="message-circle" class="w-6 h-6 mr-3 text-brand-deep-turquoise flex-shrink-0"></i>
          <span>Direct input into what we cover and how</span>
        </li>
      </ul>
    </div>
  </div>
</section>

<!-- Investment Section -->
<section class="py-20 bg-brand-deep-turquoise text-white">
  <div class="max-w-4xl mx-auto px-6 text-center">
    <h2 class="text-3xl md:text-4xl font-heading font-bold mb-12">Investment</h2>

    <div class="grid md:grid-cols-2 gap-6 mb-8 max-w-2xl mx-auto">
      <div class="bg-white/10 rounded-lg p-8">
        <p class="text-white/60 text-sm mb-2 line-through">Future price: $8,000</p>
        <p class="text-lg text-white/80 mb-1">Pioneer: Pay Upfront</p>
        <p class="text-4xl font-bold text-white mb-4">$4,500</p>
        <p class="text-white/70 text-sm mb-6">10% discount for upfront payment</p>
        <a href="#apply" class="inline-block bg-white hover:bg-white/90 text-brand-deep-turquoise font-bold py-2 px-6 rounded-lg transition-colors">Begin Application</a>
      </div>
      <div class="bg-white/10 rounded-lg p-8">
        <p class="text-white/60 text-sm mb-2 line-through">Future price: $8,000</p>
        <p class="text-lg text-white/80 mb-1">Pioneer: Two Instalments</p>
        <p class="text-4xl font-bold text-white mb-4">$5,000</p>
        <p class="text-white/70 text-sm mb-6">$2,500 before start, $2,500 at week 4</p>
        <a href="#apply" class="inline-block bg-white hover:bg-white/90 text-brand-deep-turquoise font-bold py-2 px-6 rounded-lg transition-colors">Begin Application</a>
      </div>
    </div>

    <p class="text-white/60 text-sm mb-8">Pioneer pricing. Plus local taxes where applicable.</p>

    <div class="max-w-2xl mx-auto text-lg text-white/90">
      <p>You walk away with a peer-tested AI strategy, the confidence to answer difficult questions on security and compliance, and a network of CTO peers you can call on for years.</p>
    </div>
  </div>
</section>

<!-- FAQ Section -->
<section class="py-20 bg-white">
  <div class="max-w-3xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-12 text-brand-black">Frequently Asked Questions</h2>

    <div class="space-y-6">
      <div class="border-b border-brand-light-blue/30 pb-6">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">Will this be run again in future?</h3>
        <p class="text-brand-black/80">We plan to run more cohorts, but no future dates have been announced yet. Join now to secure your place in the community and get pioneer pricing.</p>
      </div>

      <div class="border-b border-brand-light-blue/30 pb-6">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">Is there a limit to attendees?</h3>
        <p class="text-brand-black/80">Clinics are limited to 8 people in total so you can honestly discuss your own challenges in a safe environment. Everyone on the course gets personal attention, so we will cap numbers when that is no longer possible.</p>
      </div>

      <div class="border-b border-brand-light-blue/30 pb-6">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">What if I miss a session?</h3>
        <p class="text-brand-black/80">All Monday sessions are recorded. For clinics, multiple sessions run at different times each week so you can find one that works. The community stays active between sessions so you will not fall behind.</p>
      </div>

      <div class="border-b border-brand-light-blue/30 pb-6">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">What time zone are the sessions in?</h3>
        <p class="text-brand-black/80">Monday and Thursday sessions run in UK afternoon time. Clinics run at multiple times throughout the week to accommodate different time zones.</p>
      </div>

      <div class="border-b border-brand-light-blue/30 pb-6">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">Can my company pay for this?</h3>
        <p class="text-brand-black/80">Yes. When we approve your application, send us your invoice details including company name, address, and any VAT or tax numbers as appropriate. We will invoice your company directly.</p>
      </div>

      <div class="pb-6">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">Is my information kept confidential?</h3>
        <p class="text-brand-black/80">Yes. All participants sign an NDA as part of the programme agreement. Small group clinics are deliberately curated to reduce competitor conflicts. You can discuss challenges, tools, and techniques openly without concerns about confidentiality. Nothing shared in the programme is discussed outside the group.</p>
      </div>
    </div>
  </div>
</section>

<!-- Next Step Section -->
<section id="apply" class="py-20 bg-gradient-to-br from-brand-turquoise to-brand-deep-turquoise text-white">
  <div class="max-w-4xl mx-auto px-6 text-center">
    <h2 class="text-4xl md:text-5xl font-heading font-bold mb-6 text-white">Begin Application</h2>

    <div class="max-w-2xl mx-auto bg-brand-deep-turquoise rounded-lg p-8 border border-brand-turquoise mb-8">
      <div class="rm-area-embed-ai-leader-accelerator"></div>
    </div>

    <div class="max-w-3xl mx-auto bg-white/10 rounded-lg p-6 text-left">
      <h3 class="text-lg font-heading font-bold mb-4">What Happens Next</h3>
      <div class="grid grid-cols-3 md:grid-cols-6 gap-4">
        <div class="flex flex-col items-center text-center">
          <div class="w-8 h-8 bg-white rounded-full flex items-center justify-center text-brand-deep-turquoise text-sm font-bold mb-2">1</div>
          <p class="text-white/90 text-xs">Submit the form</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center text-white text-sm font-bold mb-2">2</div>
          <p class="text-white/90 text-xs">Confirm your email</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center text-white text-sm font-bold mb-2">3</div>
          <p class="text-white/90 text-xs">We review and send invoice</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center text-white text-sm font-bold mb-2">4</div>
          <p class="text-white/90 text-xs">Complete payment</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center text-white text-sm font-bold mb-2">5</div>
          <p class="text-white/90 text-xs">Join the Early Bird Zone</p>
        </div>
        <div class="flex flex-col items-center text-center">
          <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center text-white text-sm font-bold mb-2">6</div>
          <p class="text-white/90 text-xs">Programme starts 19 Jan</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Sticky CTA Script -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const stickyCta = document.getElementById('sticky-cta');
    const heroSection = document.querySelector('section');

    function handleScroll() {
      const heroBottom = heroSection.offsetTop + heroSection.offsetHeight;

      if (window.scrollY > heroBottom) {
        stickyCta.classList.remove('-translate-y-full');
        stickyCta.classList.add('translate-y-0');
      } else {
        stickyCta.classList.add('-translate-y-full');
        stickyCta.classList.remove('translate-y-0');
      }
    }

    window.addEventListener('scroll', handleScroll);
    handleScroll();
  });
</script>
