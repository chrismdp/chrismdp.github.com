---
layout: page
title: Hi, I'm Chris.
permalink: /
---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-2022-cropped.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width:200px'/>

I have 25 years of experience running tech teams and founding startups. I'm co-founder/CTO of [Cherrypick](//cherrypick.co), the best meal-led grocery shopping assistant on the market.

I also advise startup founders on tech strategy, and coach first-time CTOs &amp; solo startup devs - if you think I might be able to help you [message me to book a free 30 minute call](https://bsky.app/profile/chrismdp.com).

Previously I spent three years in charge of film and technology teams at [Gower Street](https://gower.st), consulted widely in technical architecture and agile management, and trained and coached teams in [agile](/tags#agile), [BDD](/tags#bdd), [automated testing](/tags#testing), [clean code](/tags#craftsmanship), and [great team practices](/tags#team). I ran the team that released the indie game [Sol Trader](http://soltrader.net) in 2016, and I was CEO of Eden Development, a client services software company, from 2005 to 2011.

Past clients have included large organisations such as the [BBC](http://bbc.co.uk) and [Cabinet Office](http://www.cabinetoffice.gov.uk/). I worked at [GDS](http://digital.cabinetoffice.gov.uk/about/) on the new [GOV.UK](http://gov.uk) platform and the first version of [e-petitions](/tags#e-petitions)).

You can find me on [BlueSky](https://bsky.app/profile/chrismdp.com) and on [LinkedIn](https://linkedin.com/in/chrisparsons). Here are some of my more recent articles - subscribe with <a href="{{ site.baseurl }}/feed.xml">RSS</a> to keep up with the latest.

{% for post in site.posts limit:3 %}
   <div class="post-preview py-4">
   <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
   <div style='font-style: italic' class="py-1 post-date">{{ post.date | date: "%B %d, %Y" }}</div>
   {% if post.badges %}{% for badge in post.badges %}<span class="badge badge-{{ badge.type }}">{{ badge.tag }}</span>{% endfor %}{% endif %}
   {{ post.content | split:'<!--more-->' | first }}
   {% if post.content contains '<!--more-->' %}
      <a href="{{ site.baseurl }}{{ post.url }}">Read more</a>
   {% endif %}
   </div>
{% endfor %}

Want to see more? See the <a href="{{ site.baseurl }}/all/">Archive</a>.
