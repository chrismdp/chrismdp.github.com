---
layout: page
title: Hi, I'm Chris.
permalink: /
excerpt: "I have 25 years of experience running tech teams and founding startups. I offer fractional CTO services and technical leadership coaching to help startups build great teams and scale effectively."

---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-2022-cropped.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width:200px'/>

I have spent the last 25 years starting things. Building tech teams, founding startups, and helping other founders and CTOs succeed. My aim is to make startups that make this world better for my kids generation to grow up in.

**I offer [fractional CTO services](/cto) and [technical leadership coaching](/coaching) to help startups build great teams and scale effectively.**

<!--more-->

I started in tech in 2000 as a programmer at [Elixir Studios](https://en.wikipedia.org/wiki/Elixir_Studios), making games and learning how to code and lead teams. After that I founded a software agency called [Eden Development](/tags#eden), where I first began learning how to build and run a company.

I helped build [GOV.UK](http://gov.uk) in the early days, trained hundreds of developers in software skills at the BBC, and led a small team that made [Sol Trader](/tags#sol-trader) which was released on Steam in 2016.

In 2017 I joined Gower Street as CTO and helped scale the team from 5 to 50 people, leading a large film analysis + engineering team building prediction tools for major film studios. In 2021 I co-founded [Cherrypick](//cherrypick.co) as CTO, building an AI-powered grocery shopping assistant to help people eat better effortlessly.

I split my time between Cherrypick and helping other startups through:
- [Fractional CTO services](/cto) for startups needing experienced technical leadership
- [Technical leadership coaching](/coaching) for CTOs wanting to level up their skills

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
