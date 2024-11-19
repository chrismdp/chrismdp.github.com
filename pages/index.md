---
layout: page
title: Hi, I'm Chris.
permalink: /
---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-2022-cropped.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width:200px'/>

I have 25 years of experience running tech teams and founding startups. I'm co-founder/CTO of [Cherrypick](//cherrypick.co), the best meal-led grocery shopping assistant on the market.

I advise startup startup founders on tech, and first-time CTOs &amp; solo startup devs - if you think I might be able to help you [message me to book a free 30 minutes](https://bsky.app/profile/chrismdp.com).

Previously I spent three years in charge of film and technology teams at [Gower Street](https://gower.st), I consulted in technical architecture and agile management, and I trained and coached teams in [agile](/tag/agile), [BDD](/tag/bdd), [automated testing](/tag/testing), [clean code](/tag/craftsmanship), and [great team practices](/tag/team). I was CEO of Eden Development, a client services company, from 2005 to 2011. I also released the indie game [Sol Trader](http://soltrader.net) in 2016, and still work on games on the side.

Past clients have included large organisations such as the [BBC](http://bbc.co.uk) and [Cabinet Office](http://www.cabinetoffice.gov.uk/) (working at [GDS](http://digital.cabinetoffice.gov.uk/about/) on the new [GOV.UK](http://gov.uk) platform and the first version of [e-petitions](/tag/e-petitions)) as well as a number of startups.

You can find me on [BlueSky](https://bsky.app/profile/chrismdp.com) and on [LinkedIn](https://linkedin.com/in/chrisparsons).

## Latest articles
---

Subscribe with <a href="{{ site.baseurl }}/feed.xml">RSS</a> to keep up with the latest.

{% for post in site.posts limit:10 %}
   <div class="post-preview py-4">
   <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
   <span class="post-date">{{ post.date | date: "%B %d, %Y" }}</span><br>
   {% if post.badges %}{% for badge in post.badges %}<span class="badge badge-{{ badge.type }}">{{ badge.tag }}</span>{% endfor %}{% endif %}
   {{ post.content | split:'<!--more-->' | first }}
   {% if post.content contains '<!--more-->' %}
      <a href="{{ site.baseurl }}{{ post.url }}">read more</a>
   {% endif %}
   </div>
{% endfor %}

Want to see more? See the <a href="{{ site.baseurl }}/all/">Archive</a>.
