---
layout: default
title: Thanks!
permalink: /thanks/
redirect_from:
  - /thanks
---

<!-- Hero Section with Page Title -->
<section class="pt-20 pb-12 bg-white">
  <div id="thanks-header" class="max-w-4xl mx-auto px-6 text-center">
    <h1 class="text-4xl md:text-5xl lg:text-6xl font-heading font-bold mb-6 leading-tight text-brand-black">{{ page.title }}</h1>
  </div>
  <div id="confirm-email-header" class="hidden max-w-4xl mx-auto px-6 text-center">
    <div class="bg-brand-deep-turquoise text-white rounded-lg p-8">
      <h1 class="text-3xl md:text-4xl font-heading font-bold mb-4 leading-tight">Please check your email now and click the link to confirm</h1>
      <p class="text-xl text-white/90">You will not receive any emails from me until you do. Please check your junk folders if you cannot find it. The email will come from <strong>chris@chrismdp.com</strong></p>
    </div>
  </div>
</section>

<script>
  if (new URLSearchParams(window.location.search).has('please_confirm_email')) {
    document.getElementById('thanks-header').classList.add('hidden');
    document.getElementById('confirm-email-header').classList.remove('hidden');
  }
</script>

<div class="max-w-4xl mx-auto px-6 pb-12">
  <div id="thanks-questions" class="bg-brand-white rounded-lg p-8 border border-brand-light-blue/20 mb-12" hidden>
    <p class="text-lg text-brand-black/80 mb-6 text-center">
      Would you mind <strong>taking 20 seconds</strong> to answer a few quick questions?
    </p>
    <div class="rm-area-embed-thanks"></div>
  </div>
  <script>
    // Show the questions card only once RightMessage has rendered something into it.
    // Subscribers who have already answered everything get nothing, so the card stays hidden.
    (function () {
      var card = document.getElementById('thanks-questions');
      var embed = card.querySelector('.rm-area-embed-thanks');
      var observer = new MutationObserver(reveal);
      function reveal() {
        // RightMessage always inserts an empty wrapper div, so look for real content.
        var hasContent = embed.textContent.trim().length > 0 ||
          embed.querySelector('input, button, a, img, h1, h2, h3, p');
        if (hasContent) {
          card.hidden = false;
          observer.disconnect();
        }
      }
      observer.observe(embed, { childList: true, subtree: true });
      reveal();
    })();
  </script>

  <div class="border-t border-brand-light-blue/20 pt-12">
    <h2 class="text-2xl font-heading font-bold mb-8 text-brand-black">Latest Articles</h2>

    {% assign latest_posts = "" | split: "" %}
    {% for post in site.posts limit: 15 %}
      {% assign post_time = post.date | date: "%s" | plus: 0 %}
      {% assign now_time = site.time | date: "%s" | plus: 0 %}
      {% if post_time <= now_time %}
        {% assign latest_posts = latest_posts | push: post %}
        {% if latest_posts.size >= 5 %}{% break %}{% endif %}
      {% endif %}
    {% endfor %}
    {% include article-list.html posts=latest_posts %}

    <div class="text-center mt-8">
      <a href="{{ site.baseurl }}/articles/" class="inline-block bg-brand-deep-turquoise text-white px-6 py-3 rounded-lg hover:bg-brand-turquoise transition-colors">View All Articles</a>
    </div>
  </div>
</div>
