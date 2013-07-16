---
layout: post
title: "Kanogo: vapourware to beta in 24 hours"
date: 2011-09-12 11:30:37 +0100
categories:
  - code
  - products
  - business
  - kano analysis
  - rails
  - heroku
  - ruby
  - kanogo
---
<div class='alert alert-info alert-block'>
  <h2>TL;DR</h2>
  <p>Last week I built the first beta of a new web product called <a href="http://kanogo.com">Kanogo</a>. It’s designed to gather feedback and perform <a href="http://en.wikipedia.org/wiki/Kano_model">Kano analysis</a> to determine which direction you should take with your website.</p>
  <p>Here's an example, designed specifically for this blog. Thanks for your feedback!</p>
  <iframe allowtransparency='true' frameborder='0' scrolling='no' src='http://kanogo.com/surveys/13/embed?' style='width: 100%; height: 120px'>
  </iframe>
  <p>Sign up for the beta <a href='http://kanogo.com'>here</a>.</p>
</div>

## The backstory

A while back I agonising over which should be the next greatest feature for one of my products. I thought the best thing to do would be to conduct some Kano analysis on the product in question, and realised there wasn't an easy way of doing this. I've used [kanosurvey.com](http://kanosurvey.com) in the past, but it didn't really feel like the right tool. How was I to get users to answer my survey?

"Wouldn't it be great," I thought, "if I could embed a little survey box on the site that asked customers what they thought and provided me with Kano analysis stats?" The concept behind [Kanogo](http://kanogo.com) was born.

Fast forward several months to last week. I found myself with a few days spare and decided that the best use of them would be to build a beta of this product. Always up for a challenge, I decided to give myself 24 hours to build and launch.

That's not very long, so I had to hustle.

## Timeline

*7 Sep: 12:10am:* [I announced my intentions](https://twitter.com/#!/chrismdp/status/111214768651636736), mostly to motivate myself through fear of failing in public. I finally decided on a name, and registered the domain and the twitter account. I announced the product [to the world](https://twitter.com/#!/chrismdp/status/111240345341263872) (well, a [subset](https://twitter.com/#!/chrismdp/followers)).

*7 Sep: 01:55am:* Got a new Rails 3.1 app running on Heroku cedar. It's a one page app using a Campaign Monitor signup form. Got my first beta signup. Finished for the night.

*7 Sep: 07:40am:* Announced Kanogo again, just in case anyone had been sleeping at 2am :) Got another 3 beta signups and a bunch of feedback on spelling errors.

*7 Sep: 10:13am:* Simple twitter sign in done using [Omniauth](https://github.com/intridea/omniauth) and this really useful [tutorial](https://github.com/RailsApps/rails3-mongoid-omniauth/wiki/Tutorial).

*7 Sep: 02:45pm:* The USA woke up and I got more beta signups: now up to 5. Got the basic data entry for surveys and features done. Started work on the embed. Was feeling fairly pessimistic about a beta launch for that night, but didn't want to let myself down.

*7 Sep: 05:53pm:* Embed done, quicker than expected. Took a break. Now feeling [cautiously optimistic](https://twitter.com/#!/chrismdp/status/111482135218626560).

*7 Sep: 09:12pm:* Basic response mechanism in: now needed to apply the Kano analysis magic! Adrenalin took over from caffiene as primary stimulant.

*7 Sep: 11:20pm:* Turned on twitter sign in as basic method of getting registered on the site. Removed redundant Campaign Monitor signup: emailed subscribers manually to ask them to sign in via twitter. Beta [went live!](https://twitter.com/#!/kanogoapp/status/111564545708929024)

## The result

![Embed](/files/kanogo-1.png)

![Results](/files/kanogo-2.png)

After 24 hours, I had a beta running, which worked. Granted, it wasn't great, but it was something that had some value.

I spent the rest of the evening and following morning promoting the beta on mailing lists and on twitter. By the end of the following day I had 30 or so beta signups.

It's already adding value to beta users. Two sites using the beta already on their own products. One beta user has now decied to implement a feature as he's realised his customers consider it a "must have". There's no substitute for real feedback.

## Learnings

Some of the things I've learned so far:

* *Cloud tools are the business.* It was so easy to register the domain with [dnsimple.com](http://dnsimple.com), start up a [twitter account](http://twitter.com/kanagoapp) for marketing and customer interaction, deploy to [Heroku](http://heroku.com), get initial beta signups with [Campaign Monitor](http://campaignmonitor.com).

* *Modern development tools rock.* I used Rails 3.1 for this app, which worked beautifully, and I love the use of sprockets to help manage the asset pipeline. Running the app on Heroku cedar went without a hitch. I used twitter for authentication, and it only took an hour to set up.

* *There is no "quick and dirty".* The app is (almost) fully tested: I confess I left a couple of methods only covered by end-to-end tests (which doesn't really count). I definitely proved that the only way to go fast is to go clean: [Jason was right](http://agileage.blogspot.com/2011/07/slow-and-dirty-rant-by-jason-gorman-at.html) that there is no "quick and dirty" only "slow and dirty". This came back to bite me instantly: the code I didn't use specs for took me the longest to get working.

* *Technology is the easy part.* It didn't take me long to build the site, but the trick is to build a business. After initial interest, the analytics on the site are way down as the next new thing appears on the internet and people move on. To gain traction I need to build the app my beta users actually want. Thankfully, quick feedback is what Kanogo does, so we're eating our own dogfood and asking our users what they think at every turn. This is already directing which features I work on next, which has to be the most efficient way of moving forward, right?

## What's next?

I plan to continue working on this, listening to beta user feedback, refining the features, and accepting new beta signup for the moment. I hope to turn this into a paid product at some point, as I think there's a huge amount of value here to websites if I can get the messaging right.

## Can I get involved?

Sure! It's not too late to join the beta: you can [do so here](http://kanogo.com). I'd love your feedback on the product. It can give you value anywhere you have users of a website, even on a blog as shown above.
