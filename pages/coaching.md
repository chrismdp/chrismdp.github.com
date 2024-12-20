---
layout: page
title: I coach technical founders and startup CTOs to build the tech organisation of their dreams.
permalink: /coaching
excerpt: "Book in a call if you need some help with your startup journey."

---

<script>
if (window.location.search.includes('?thanks')) {
  document.write(`
    <div class="bg-green-50 border-l-4 rounded-lg border-green-500 text-green-700 p-4 mb-8" role="alert">
      <p class="font-bold">Thanks for booking!</p>
      <div>Looking forward to our call.</div>
    </div>
  `);
}
</script>


<img alt='Chris Parsons' src='/assets/img/chris-headshot-2022-cropped.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width:200px'/>

- Do you feel like you never have enough time?
- Do you want to know exactly how to find problem/solution and product/market fit?
- Do you need help working with product, your board and your CEO?
- Do you need technical help with AI/LLM apps?
- Do you need help building the right technical architecture for your stage?
- Do you want to know how to set culture and build a world class team?
- Do you want to raise your next round?

<div class="flex justify-center pb-8">
  <a href="https://app.reclaim.ai/m/cp/coaching-discovery-call" class="inline-block px-8 py-4 text-lg font-bold text-white bg-violet-600 hover:bg-violet-700 transition-colors rounded-lg">
    Book a free discovery call
  </a>
</div>

<!--more-->

I have been working for 20 years as a founder, CEO and CTO, and it's time to give back.

I'm looking to coach and mentor a small number of technical founders and CTOs in 2025 to build the tech organisation of their dreams.

I know a lot about being a founder/early stage CTO of fast growing startups, both consumer D2C and B2B SaaS. I can help you hire great technical teams, set culture, find product market fit and build [just enough tech](/the-job-is-not-to-build).

I've also got several years of experience working on AI products so can help you [build robust LLM application](/how-to-build-a-robust-llm-application) that scales well and that your customers love.

[Read more about me](/)

## Recent articles

{% for post in site.posts limit:3 %}
   <div class="post-preview py-4">
   <h3><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h3>

   <div style='font-style: italic' class="pb-1 post-date">
   {% assign original_date = post.path | split: "/" | last | split: "-" | slice: 0, 2 | join: '' %}
   {% assign current_date = post.date | date: "%Y%m" %}
   {% if original_date != current_date %}Updated: {% endif %}
   {{ post.date | date: "%B %Y" }}
   </div>
   {% if post.badges %}{% for badge in post.badges %}<span class="badge badge-{{ badge.type }}">{{ badge.tag }}</span>{% endfor %}{% endif %}
   {{ post.excerpt }}
   <a class='underline' href="{{ site.baseurl }}{{ post.url }}">Read more</a>
   </div>
{% endfor %}

<hr>

See the <a href="{{ site.baseurl }}/all/">Archive</a> for more articles.
