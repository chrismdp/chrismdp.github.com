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
      <a href="#apply" class="inline-block bg-white hover:bg-white/90 text-brand-deep-turquoise font-bold py-2 px-6 rounded-lg transition-colors text-sm">Apply Now</a>
      <a href="#syllabus" class="inline-block bg-white/20 hover:bg-white/30 text-white font-bold py-2 px-6 rounded-lg transition-colors text-sm">See the Syllabus</a>
    </div>
  </div>
</div>

<!-- Hero Section -->
<section class="relative bg-gradient-to-br from-brand-deep-turquoise to-brand-turquoise text-white pt-32 pb-20 overflow-hidden">
  <div class="w-full px-6 relative z-10">
    <div class="text-center mb-12">
      <p class="text-lg uppercase tracking-wide mb-4 text-white/80">For Senior Technical Leaders and Fractional CTOs</p>
      <h1 class="text-4xl md:text-6xl font-heading font-bold mb-6 leading-tight mx-4">AI Leader Accelerator</h1>
      <p class="text-xl md:text-2xl mb-8 text-white mx-4 sm:mx-24">The collaborative course that turns technical leaders into AI leaders.</p>
      <p class="text-lg mx-4 sm:mx-24 text-white/90 mb-8">8 weeks. 3 hours online per week, plus your own implementation time. A small group of peers facing the same decisions and learning how to maximise their own and their team's use of AI.</p>

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
        <a href="#apply" class="inline-block bg-white hover:bg-white/90 text-brand-deep-turquoise font-bold py-3 px-8 rounded-lg text-lg transition-colors">Apply Now</a>
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
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-8 text-brand-black">Technical Leadership Used To Be Easier.</h2>

    <div class="space-y-6 text-xl text-brand-black/80 text-center mb-10">
      <p>Think about how you navigated previous technology shifts. When cloud computing emerged, or when microservices became mainstream, you had time. The technology evolved over years. Best practices became established. You could wait, learn from others, then adopt with confidence.</p>

      <p>More importantly, you had your network. When you needed to validate a technical decision, you knew who to call. You had peers at your level who understood the same challenges and could offer honest perspective.</p>

      <p class="text-2xl font-heading font-bold text-brand-black">Then AI arrived. And something broke.</p>

      <p>Your network still exists, but now nobody knows anything. The landscape changes weekly, best practice from last month is already outdated, and your trusted peers are just as uncertain as you are. Everyone is figuring it out alone.</p>
    </div>

    <div class="grid md:grid-cols-3 gap-6 mt-12 mb-16">
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
    </div>
  </div>
  <div class="max-w-6xl mx-auto px-6">
    <!-- First row: 3 columns -->
    <div class="grid md:grid-cols-3 gap-6 mb-6">
      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-orange">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">You are making decisions alone.</h3>
        <p class="text-brand-black/80">You have been experimenting with AI, probably more than anyone else in your organisation. But you have nobody at your level to test your thinking against.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-orange">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">Your CEO sends you startup success stories.</h3>
        <p class="text-brand-black/80">"Look what this company did with five people!" But you have a monolith, compliance requirements, and existing customers. It is not that easy.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-orange">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">Generic training does not help.</h3>
        <p class="text-brand-black/80">Most AI courses teach tools. You need to figure out where AI fits in your organisation and how to lead your teams through adoption.</p>
      </div>
    </div>

    <!-- Second row: 2 columns -->
    <div class="grid md:grid-cols-2 gap-6">
      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-orange">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">You are the filter.</h3>
        <p class="text-brand-black/80">Caught between board expectations and team reality. Your CEO wants AI transformation yesterday. Your team needs time to adopt properly. You are translating pressure from above into something your organisation can actually execute.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-orange">
        <h3 class="text-xl font-heading font-bold mb-3 text-brand-black">The cost of getting this wrong is high.</h3>
        <p class="text-brand-black/80">Bad AI investments waste six figures. Shadow AI creates security and compliance risks. Teams that adopt poorly get demoralised. And if your competitors figure this out first, you lose ground you will not easily recover.</p>
      </div>
    </div>
  </div>
</section>

<!-- The Cost of Staying Stuck Section -->
<section class="py-20 bg-brand-deep-turquoise text-white">
  <div class="max-w-4xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-12">The Cost of Staying Stuck</h2>

    <p class="text-xl text-center mb-12">Most companies do not even know what AI tools their teams are using, let alone what they are spending. You think some teams are on Cursor, a few people have Claude subscriptions on expenses, others default to Copilot because it came with GitHub. Vendors are pushing you to sign annual contracts, but you are not sure which tool is right. Every month without clarity costs you:</p>

    <div class="grid md:grid-cols-2 gap-6">
      <div class="bg-white/10 rounded-lg p-6">
        <i data-lucide="banknote" class="w-8 h-8 mb-3 text-white"></i>
        <h3 class="text-xl font-bold mb-2">Wasted spend</h3>
        <p class="text-white/80">Tools and experiments that go nowhere</p>
      </div>

      <div class="bg-white/10 rounded-lg p-6">
        <i data-lucide="help-circle" class="w-8 h-8 mb-3 text-white"></i>
        <h3 class="text-xl font-bold mb-2">Team confusion</h3>
        <p class="text-white/80">About what to use and when</p>
      </div>

      <div class="bg-white/10 rounded-lg p-6">
        <i data-lucide="clock" class="w-8 h-8 mb-3 text-white"></i>
        <h3 class="text-xl font-bold mb-2">Slower delivery</h3>
        <p class="text-white/80">Because nobody has confidence in the approach</p>
      </div>

      <div class="bg-white/10 rounded-lg p-6">
        <i data-lucide="user-x" class="w-8 h-8 mb-3 text-white"></i>
        <h3 class="text-xl font-bold mb-2">Your own credibility</h3>
        <p class="text-white/80">As the leader who should have answers</p>
      </div>
    </div>

    <p class="text-xl text-center mt-12 text-white/90">You can keep figuring this out alone. Or you can accelerate by learning alongside people facing the same decisions.</p>
  </div>
</section>

<!-- A Different Approach Section -->
<section class="py-20 bg-brand-white">
  <div class="max-w-5xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-4 text-brand-black">A Different Approach</h2>
    <p class="text-xl text-center text-brand-black/80 mb-8">Not a training course. Not a lecture series.</p>

    <div class="bg-white rounded-lg p-8 shadow-lg border border-brand-light-blue/20 mb-12">
      <h3 class="text-2xl font-heading font-bold mb-6 text-brand-deep-turquoise text-center">AI Leader Accelerator</h3>
      <p class="text-xl text-brand-black/80 text-center mb-8">A small group of CTOs, VPs of Engineering, and senior technical leaders working through AI adoption challenges together over 8 weeks.</p>

      <div class="bg-brand-deep-turquoise text-white rounded-lg p-6 mb-8">
        <h4 class="text-xl font-bold mb-4 text-center">3 Hours Online Per Week</h4>
        <div class="grid md:grid-cols-3 gap-6">
          <div class="text-center">
            <p class="font-semibold mb-2">Monday Afternoon</p>
            <p class="text-white/80 text-sm">1 hour taught session with frameworks and provocations</p>
          </div>
          <div class="text-center">
            <p class="font-semibold mb-2">Weekly Clinic</p>
            <p class="text-white/80 text-sm">1 hour thematic small group session to work through your specific blockers</p>
          </div>
          <div class="text-center">
            <p class="font-semibold mb-2">Thursday Afternoon</p>
            <p class="text-white/80 text-sm">1 hour Q&A and progress celebration with the full cohort</p>
          </div>
        </div>
      </div>

      <div class="bg-brand-light-blue/20 rounded-lg p-6 mb-6">
        <h4 class="text-lg font-bold text-brand-deep-turquoise mb-3 text-center">Expert Input</h4>
        <div class="flex items-center justify-center gap-4 mb-4">
          <img src="/assets/img/chris-twitter-headshot.png" alt="Chris Parsons" class="w-12 h-12 rounded-full object-cover">
          <p class="text-brand-black/70 text-sm max-w-md">I am <strong class="text-brand-black">Chris Parsons</strong>. 14 years in senior roles with multiple teams, currently Fractional CTO and AI advisor to organisations including Genomics and Cherrypick.</p>
        </div>
        <p class="text-brand-black/80 text-center">Plus guest experts who have done large-scale rollouts at major organisations, and your own implementation time to put what you learn into practice.</p>
      </div>

      <div class="bg-brand-light-blue/10 rounded-lg p-6 mb-6">
        <h4 class="text-lg font-bold text-brand-deep-turquoise mb-3 text-center">Weekly Clinics</h4>
        <p class="text-brand-black/80 text-center mb-6">Intimate, coach-led sessions to help you deal with blockers. Each week has a theme matching that week's content, and you join one clinic per week in a small group of a few people. Multiple clinics run at different times so there is one you can get to.</p>
        <div class="grid md:grid-cols-3 gap-4">
          <div class="bg-white rounded-lg p-4 text-center">
            <i data-lucide="calendar-check" class="w-8 h-8 mx-auto mb-2 text-brand-deep-turquoise"></i>
            <p class="text-sm text-brand-black/80">One clinic per person per week</p>
          </div>
          <div class="bg-white rounded-lg p-4 text-center">
            <i data-lucide="target" class="w-8 h-8 mx-auto mb-2 text-brand-deep-turquoise"></i>
            <p class="text-sm text-brand-black/80">Themed to keep conversations focused</p>
          </div>
          <div class="bg-white rounded-lg p-4 text-center">
            <i data-lucide="message-circle" class="w-8 h-8 mx-auto mb-2 text-brand-deep-turquoise"></i>
            <p class="text-sm text-brand-black/80">Direct feedback on your specific situation</p>
          </div>
        </div>
      </div>

      <div class="bg-brand-light-blue/20 rounded-lg p-6 mt-8">
        <h4 class="text-lg font-bold text-brand-deep-turquoise mb-3 text-center">Community and Accountability</h4>
        <div class="space-y-4 text-brand-black/80">
          <p class="text-center">Engage with fellow cohort members, support them on their AI journey, and hold each other accountable. Share your wins, struggles, and areas of expertise.</p>
          <p class="text-center">You will be surrounded by technical leaders solving the same problems as you, providing the perfect peer set to accelerate your progress. You could meet a future collaborator or form a peer group that lasts for years.</p>
          <p class="text-center">Stay connected with a community of ambitious technical leaders long after the 8-week programme is complete.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Who This Is For Section -->
<section class="py-20 bg-brand-deep-turquoise text-white">
  <div class="max-w-4xl mx-auto px-6">
    <h2 class="text-3xl md:text-4xl font-heading font-bold text-center mb-12">Who This Is For</h2>

    <div class="grid md:grid-cols-2 gap-8">
      <div class="bg-white/10 rounded-lg p-8">
        <h3 class="text-xl font-bold mb-6 text-white">This Is For You If:</h3>
        <ul class="space-y-4">
          <li class="flex items-start">
            <i data-lucide="check" class="w-6 h-6 mr-3 text-white flex-shrink-0 mt-1"></i>
            <span>CTO, VP of Engineering, Engineering Director, or Fractional CTO</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="check" class="w-6 h-6 mr-3 text-white flex-shrink-0 mt-1"></i>
            <span>Running teams of teams (10+ reports)</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="check" class="w-6 h-6 mr-3 text-white flex-shrink-0 mt-1"></i>
            <span>Responsible for AI adoption decisions at your organisation</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="check" class="w-6 h-6 mr-3 text-white flex-shrink-0 mt-1"></i>
            <span>Want strategic clarity on AI adoption for your organisation</span>
          </li>
        </ul>
      </div>

      <div class="bg-white/10 rounded-lg p-8">
        <h3 class="text-xl font-bold mb-6 text-white/60">This Is Not For:</h3>
        <ul class="space-y-4 text-white/80">
          <li class="flex items-start">
            <i data-lucide="x" class="w-6 h-6 mr-3 text-white/40 flex-shrink-0 mt-1"></i>
            <span>Individual contributors wanting hands-on coding skills</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="x" class="w-6 h-6 mr-3 text-white/40 flex-shrink-0 mt-1"></i>
            <span>Junior or mid-level engineers</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="x" class="w-6 h-6 mr-3 text-white/40 flex-shrink-0 mt-1"></i>
            <span>People between jobs</span>
          </li>
          <li class="flex items-start">
            <i data-lucide="x" class="w-6 h-6 mr-3 text-white/40 flex-shrink-0 mt-1"></i>
            <span>People looking for tool tutorials</span>
          </li>
        </ul>
        <p class="mt-6 pt-6 border-t border-white/20 text-white/90">This is for people making strategic decisions about how their organisations adopt AI.</p>
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
          <h3 class="text-xl font-heading font-bold text-brand-black">Advanced Prompting for Leaders</h3>
        </div>
        <p class="text-brand-black/80">Practical wins for self-use and team enablement. Start with something personal and practical, with immediate value from day one.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 2</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Building the Groundwork</h3>
        </div>
        <p class="text-brand-black/80">AI as an amplifier: it makes good teams better and bad teams worse. Establishing a learning culture, setting expectations, freeing up time for experimentation, and creating an experiment team.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 3</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Using Advanced Agents for Strategic Thinking</h3>
        </div>
        <p class="text-brand-black/80">How agents differ from chat interfaces. Using AI agents for writing, planning, and decision-making. Beyond coding: AI as thinking partner for leadership work.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 4</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Compliance, Privacy, and Security</h3>
        </div>
        <p class="text-brand-black/80">Calming fears about security and privacy. Making smart decisions about deployment, local vs cloud considerations, and risk management frameworks.</p>
      </div>

      <div class="bg-brand-white rounded-lg p-6 border-l-4 border-brand-deep-turquoise">
        <div class="flex items-start mb-3">
          <span class="bg-brand-deep-turquoise text-white text-sm font-bold px-3 py-1 rounded mr-4">Week 5</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">AI in Products</h3>
        </div>
        <p class="text-brand-black/80">Embedding AI into your products. Understanding the product lifecycle with AI, from prototyping to production, and making smart decisions about where AI adds real value.</p>
      </div>

      <div class="bg-brand-light-blue/20 rounded-lg p-6 border-l-4 border-brand-orange">
        <div class="flex items-start mb-3">
          <span class="bg-brand-orange text-white text-sm font-bold px-3 py-1 rounded mr-4">Weeks 6-8</span>
          <h3 class="text-xl font-heading font-bold text-brand-black">Customised Sessions Based on Need</h3>
        </div>
        <p class="text-brand-black/80">Topics shaped by the cohort. We will build these sessions around what emerges from the first five weeks, addressing your specific challenges with peer support and expert input.</p>
      </div>
    </div>

    <div class="bg-brand-deep-turquoise text-white rounded-lg p-8 mt-12 text-center">
      <p class="text-xl font-semibold mb-2">One week break for half-term included</p>
      <p class="text-white/80">19 January to 20 March 2026</p>
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
            <p>14 years in senior roles with multiple teams, including several years building AI products at startups and scaleups. Now focused on AI adoption, both hands-on implementation and advising technical leaders.</p>
            <p><strong>Current work:</strong> Fractional CTO and AI advisor to startups and scaleups including Genomics and <a href="https://cherrypick.co" target="_blank" class="text-brand-deep-turquoise hover:underline">Cherrypick</a>.</p>
            <p>I talk to a lot of technical leaders and I spend a significant chunk of my time keeping up with AI so that I can inject provocation and break old paradigms. Then as a group we pick up the pieces together and figure out what the brave new future looks like.</p>
            <p>That is how we truly become AI leaders.</p>
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
        <a href="#apply" class="inline-block bg-white hover:bg-white/90 text-brand-deep-turquoise font-bold py-2 px-6 rounded-lg transition-colors">Apply Now</a>
      </div>
      <div class="bg-white/10 rounded-lg p-8">
        <p class="text-white/60 text-sm mb-2 line-through">Future price: $8,000</p>
        <p class="text-lg text-white/80 mb-1">Pioneer: Two Instalments</p>
        <p class="text-4xl font-bold text-white mb-4">$5,000</p>
        <p class="text-white/70 text-sm mb-6">$2,500 before start, $2,500 at week 4</p>
        <a href="#apply" class="inline-block bg-white hover:bg-white/90 text-brand-deep-turquoise font-bold py-2 px-6 rounded-lg transition-colors">Apply Now</a>
      </div>
    </div>

    <p class="text-white/60 text-sm mb-8">Pioneer pricing. Plus local taxes where applicable.</p>

    <div class="max-w-2xl mx-auto text-lg text-white/90">
      <p>The decisions you are making about AI adoption affect budgets, teams, and competitive position worth far more than this.</p>
    </div>
  </div>
</section>

<!-- Next Step Section -->
<section id="apply" class="py-20 bg-gradient-to-br from-brand-turquoise to-brand-deep-turquoise text-white">
  <div class="max-w-4xl mx-auto text-center px-6">
    <h2 class="text-4xl md:text-5xl font-heading font-bold mb-6 text-white">Apply Now</h2>
    <p class="text-xl mb-12 text-white/90">Fill in the form below in just a few steps.</p>

    <div class="max-w-2xl mx-auto bg-brand-deep-turquoise rounded-lg p-8 border border-brand-turquoise">
      <div class="rm-area-embed-ai-leader-accelerator"></div>
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
