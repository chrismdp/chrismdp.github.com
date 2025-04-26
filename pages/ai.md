---
layout: page
title: "Level up your AI agents."
permalink: /ai
excerpt: "I help teams build reliable, scalable and cost-efficient AI agents."
redirect_from:
  - /coaching
  - /cto
---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-full.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width: 50%; max-width: 250px;'/>

You have built an AI agent. The demos are great. But it is costing you too much, and you never quite know when it is going to let you down, or do something you could be sued for.

I have [built and shipped AI agents to production](/how-to-build-a-robust-llm-application/) and have now created three separate home-grown agent evaluation systems, each one better than the last. I have used all that learning to [create a platform](https://kaijo.ai/?utm_source=chrisdp&utm_medium=website&utm_campaign=ai){:target="_blank"} to make AI agents more reliable.

__I can help you improve your AI agent's reliability, scalability and cost-efficiency.__

Fill in this form and I'll email you straight back:
<script async data-uid="2c57927fef" src="https://chrismdp.kit.com/2c57927fef/index.js"></script>

<!--more-->

<hr/>

{% for post in site.categories.ai limit:5 %}
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

<script async data-uid="dadc23073e" src="https://chrismdp.kit.com/dadc23073e/index.js"></script>

<br/>