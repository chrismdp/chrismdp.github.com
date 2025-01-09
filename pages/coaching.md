---
layout: page
title: I help tech founders & CTOs get moving.
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

**Coaching first time/early stage CTOs and tech founders to cut through the noise, focus on what matters and test ideas within hours not months.**

- Need help working with product, your board and your CEO?
- Unsure about right technical architecture for your stage?
- Need technical guidance on your AI/LLM app?
- Want to set the right culture and avoid the wrong one?
- Want to hire and vet the right people and build a world class team?
- Worried you are not going fast enough?
- Unsure if you will progress enough to raise your next funding round?
- Want to know exactly how to find problem/solution and product/market fit?
- What to add just enough process to avoid chaos, but not enough to slow you down?
- Feel like you never have enough time to do all of this?

{% include book-call-button.html %}

<!--more-->

_"Chris is fantastic at building self-sufficient teams and giving them what they need to deliver impactful product changes and experiments. He provides a lot of freedom while setting clear goals, which creates highly productive teams in early-stage startups. At the same time, he’s an empathetic leader who always keeps a pulse on team morale. This is an extremely punchy combo when it comes to pre-product-market-fit companies, where hyper focus, productivity and seeding the right company culture are key."_

-- [Tadas Tamosauskas](https://www.linkedin.com/in/tamosauskas/)

I know a lot about being a founder/early stage CTO of fast growing startups, both consumer D2C and B2B SaaS. I can help you hire great technical teams, set culture, find product market fit and build [just enough tech](/the-job-is-not-to-build).

I've also got several years of experience working on AI products so can help you [build robust LLM application](/how-to-build-a-robust-llm-application) that scales well and that your customers love.  [Read more about me here](/).

## Why Founders and CTOs Need a Coach

Coaching helps founders and CTOs grow and achieve their goals. A startup has high stakes and huge potential value so getting support makes a real difference to your success. I have benefited from a number of excellent coaches and mentors over the years, and my startup experience has been vastly better and less stressful thanks to them.

Every technical leader faces common challenges:
- Making tricky architectural decisions under uncertainty
- Hiring and managing high-performing engineering teams
- Scaling up to manage high level tech strategy
- Scaling down to manage team performance and troubleshoot code
- Constantly learning new technology and figuring out how to apply it to your business

Having someone in your corner who's been through these challenges before, as I have at multiple startups, is the difference between struggling alone and confidently moving forward.

## Coaching vs Mentoring

I am part coach, part mentor.

Coaching is a conversation to move you from where you are now, to where you would like to be. You get independent assistance to help you move forward without any judgement or anyone telling you what to do. You find your own answers and are then supported while you make changes.

Mentoring is benefiting from past experience, knowledge and mistakes to help you make better decisions. You can be coached by a non-expert, but a mentor can provide lots of extra value as they have been in your position before.

A founder or CTO benefits from a coach but working with someone who has been through the same challenges before is much more valuable. I have walked this journey through several startups over 20 years and can help you avoid plenty of mistakes and find a way through the maze of uncertainty.

{% include book-call-button.html %}

## My Recent Articles

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
