---
layout: page
title: Hi, I'm Chris.
permalink: /
excerpt: "I have 25 years of experience running tech teams and founding startups. I'm co-founder/CTO of Cherrypick, the best meal-led grocery shopping assistant on the market. I advise startup founders on tech strategy, and coach first-time CTOs &amp; founding developers at funded startups - if you think I might be able to help you, get in touch."

---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-2022-cropped.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width:200px'/>

I have 25 years of experience running tech teams and founding startups. I'm co-founder/CTO of [Cherrypick](//cherrypick.co), the best meal-led grocery shopping assistant on the market.

**I coach a limited number of technical founders and CTOs at funded startups. [Book in a call](https://forms.gle/ee5gWQznBG5yNwwt9) if you need some help with your startup journey.**

I know a lot about being a founder/early stage CTO of a fast growing startup, including hiring great technical teams, board and [founder relationships](/the-first-thing-a-startup-cto-must-do), setting culture, finding product market fit, building [just enough tech](/the-job-is-not-to-build) and how to build [great AI products](/how-to-build-a-robust-llm-application).

<!--more-->

Previously I helped scale [Gower Street](https://gower.st) from 7 to 50 employees and built a data science team from scratch. I trained hundreds of developers at the [BBC](http://bbc.co.uk) and other organisations, and I helped [GDS](http://digital.cabinetoffice.gov.uk/about/) get started in the early days, working on [GOV.UK](http://gov.uk) and [e-petitions](/tags#e-petitions). I ran the team that released the indie game [Sol Trader](/tags#soltrader) in 2016, and I was Founder/CEO of [Eden Development](/tags#eden), a 12 person client services software firm, from 2005 to 2011.

You can find me on [BlueSky](https://bsky.app/profile/chrismdp.com), [X](https://x.com/chrismdp) and [LinkedIn](https://linkedin.com/in/chrisparsons). Here are some of my more recent articles - subscribe with <a href="{{ site.baseurl }}/feed.xml">RSS</a> to keep up with the latest.

{% for post in site.posts limit:3 %}
   <div class="post-preview py-4">
   <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>

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
