---
layout: post
title: "e-petitions: handling traffic"
date: 2011-08-30 13:51:38 +0100
categories:
  - code
  - scaling
  - agile
  - adn
  - e-petitions
  - government
---
Since I [last blogged about e-petitions](/2011/07/e-petitions-deconstructed) we had what conservatively could be described as "something of a traffic spike". The [amount of interest](http://www.bbc.co.uk/news/uk-politics-14474429) surrounding the site massively exceeded all our expectations.

Given the time available to us, we had rated the site for about 10 requests a second, basing our expectations on the usage of the original e-petitions site. However, during peak times we were seeing non-cached bursts of traffic through to the site of between 70-120 requests a second: we'd load tested up to about 40-50. This caused the site to intermittently produce [500 errors](http://epetitions.direct.gov.uk/500.html); this in turn [producing](http://www.thesun.co.uk/sol/homepage/news/3733792/E-petitions-website-down-on-first-day.html) [headlines](http://www.guardian.co.uk/politics/2011/aug/04/government-e-petition-website-crashes) that we really didn't want to see.

Most perplexingly, we were still seeing intermittent failure messages in the logs when the site was getting about 20-30 requests a second, even though that had worked fine in testing. During this time none of the servers were under a huge amount of load, so we struggled to find the bottleneck.

Eventually we discovered that the hardware firewall we'd put in place to help improve security wasn't able to handle the number of network connections required of it, and was randomly dropping network connections. This included connections on the internal network, which caused connectivity problems to the seach and database servers. This caused most of the intermittent failures people saw. The firewall had been set up after we had done our load testing and we'd not re-run our testing since then, so we hadn't spotted the problem
.

Once this had been fixed, we were on to more familiar territory. The dedicated solr server we were running for search was really struggling with only 4 CPUs, so we rebooted it using 8 CPUs and it started working much better.

We also made a number of other changes to the site to make it more robust:

* We brought an application server down, cloned the disk and set up a third application server within about half an hour. It's not as quick as running on Amazon EC2, but it's not a bad turnaround for a more traditionally hosted site.

* We set up monitoring on the site using [Munin](http://munin-monitoring.org/), which is a brilliant server montoring tool. This helped us discover the solr issues much more quickly.

* We went right through the code and turned on caching everywhere we hadn't yet thought of, including caching of more pages surrounding the signing step.

* We worked around a sunspot issue which was causing a petition to reindex after every signature, stressing the search server further.

## Lessons learnt

* Run your load tests again after any configuration change, even if it shouldn't make a difference. If we'd done this, we'd have spotted the firewall configuration issue before the public did.
* Set up proper measuring tools before the event. It took us a while to find the best cause of action with the search server because we were relying on [New Relic](http://newrelic.com) to monitor the application servers only. Once we had Munin running we could more easily make more CPUs available to the search server.

The nights were long during the few days of heavy traffic load, and I particularly wanted to thank the Alpha.gov guys ([Ben Griffiths](http://twitter.com/beng), [James Stewart](http://twitter.com/jystewart) and [Matt Patterson](http://twitter.com/fidothe)) and [Alex Tomlins](http://www.unboxedconsulting.com/people/alex-tomlins) from [Unboxed](http://unboxedconsulting.com) for stepping in and helping [Jolyon](http://www.unboxedconsulting.com/people/jolyon-pawlyn) and myself out. Jolyon and I are [giving a talk about e-petitions at LRUG](http://lanyrd.com/2011/lrug-september/sgzxr/) next month if you'd like to hear more.
