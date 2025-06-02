---
layout: page
title: "AI-First Coding Webinar"
permalink: /webinar
excerpt: "Learn how to add major features to your application 3x faster with AI-first coding."
---

<img alt='Chris Parsons' src='/assets/img/chris-headshot-full.jpg' class='rounded-lg' style='margin: 0 0 1em 1em; float: right; width: 50%; max-width: 250px;'/>

How do you make AI agents thrive in ever more complex codebases? Most developers believe that more code means more power for AI agents. That is a mistake. The real breakthrough comes from setting clear boundaries and limiting the context your AI can access.

I learned this the hard way. My early projects grew out of control. Agents became unpredictable, and debugging was a nightmare. Everything changed when I started treating boundaries as a feature, not a restriction.

In this live webinar, I will show you how to:
- Define project boundaries that make AI agents more reliable
- Limit context to boost performance and reduce errors
- Build complex features without losing control

You will see real examples from my own work, including the latest updates to Kaijo, my AI reliability tool. I will demonstrate how to keep your agents focused, functional, and ready for anything.

If you are building with AI and your codebase is only getting more complex, this session is for you.

Register below for a Google Meet link and calendar invite:

<div class="rm-area-embed-webinar"></div>

<br>
---
## Previous Webinars

{% for post in site.categories.webinar limit:5 %}
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

---
## More AI articles
{% for post in site.categories.ai limit:5 %}
   {% unless post.categories contains 'webinar' %}
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
   {% endunless %}
{% endfor %}

---
See the <a href="{{ site.baseurl }}/all/">Archive</a> for more articles. 

{% include ai-newsletter-short.html %}