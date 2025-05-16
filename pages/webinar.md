---
layout: page
title: "AI-First Coding Webinar"
permalink: /webinar
excerpt: "Learn how to add major features to your application 3x faster with AI-first coding."
---

![ai coding webinar](/assets/img/ai-coding-webinar.png)

Time for another live coding session!

I'll be showing how to add a major feature to an existing application with AI-first coding, 3x faster that previously possible. I'd love to see you there!

**Date: Friday 23rd May, 3pm - 4:30pm UK time**

Join me for this exciting webinar where we'll explore:
- How to build and ship AI-powered features in record time
- Real-world examples of AI-first coding that actually work
- Best practices for implementing major features with confidence
- Live Q&A to get your specific questions answered

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
See the <a href="{{ site.baseurl }}/all/">Archive</a> for more articles. 

{% include ai-newsletter-short.html %}