---
layout: post
title: 'e-petitions: deconstructed'
date: 2011-07-29 15:57:09.000000000 +01:00
categories:
- code
- chef
- agile
- adn
- government
- e-petitions
redirect_from:
- "/2011/07/e-petitions-deconstructed"
---
<div class='alert'>Update: I've posted more about the massive traffic surge and how we responded <a href='/2011/08/e-petitions-handling-traffic'>here</a>.</div>

The project that I've been working on at the Government Digital Service (GDS) for the last few weeks has just been launched. It's the new Government [e-petitions](http://epetitions.direct.gov.uk) service, which replaces the old Number 10 petitions website run by the previous government. Time to talk about the architecture, how we set the team up and the effect the project is having within government.

![e-petitions](/files/e-petitions.png)

## The project

The project was overseen and run by [Skunkworks](http://twitter.com/HMGSkunks), the new innovation arm of the GDS that specialises in quick projects with small teams. They hired the [Agile Delivery Network](http://agiledelivery.net) (ADN) to do the work: this is a non-profit organisation I'm involved with that's trying to help government deliver IT projects more quickly.

We put together a team consisting of myself and two other developers, a designer, a tester/project manager, our customer and an analyst to help with the copy and training the staff who will be moderating petitions.

We originally started the project at the very beginning of June, knowing that we only had six weeks to get the site live. We ran three two-week iterations, during which requirements shifted around as the important deliverables came into focus.

There were a number of major technical hurdles. We spent a lot of time getting the accessibility of the site right, and tweaking the feel of the search feature. Getting the site hosted was difficult: it's not straightforward finding website hosting for a government website that collects personal data.

Whilst we tried to find the right place to host the site, we spent a lot of time using [Chef](http://www.opscode.com/chef) to test our build configuration on Amazon EC2. When the hosting came online, it was relatively simple (thankfully) to deploy the site to the production environment, as we'd already prepared all the configuration scripts in advance.

## The tech

We built the site in Rails, with a MySQL and a Solr search backend. It's running in production on two application servers, through nginx for static content with unicorn at the backend. There is one dedicated DB server, and one dedicated Solr server. Our JMeter testing showed that we may not need the dedicated Solr server, so that might also share CPU with a read-only MySQL slave in future if the site traffic gets heavier.

For server configuration, we're running a customised version of chef-solo on each of the servers, bootstrapped with a little bespoke script. We didn't want to set up a chef server as we didn't get the hosting environment set up until quite late in the day, and we didn't want an external server with access to the production environment.

Chef turned out to be awesome: it was very satisfying to watch all the scripts we'd built on EC2 "just work" (well, almost) on the live environment. Nginx + Unicorn was also a highlight: it's more Unix-y that Apache + Passenger and handles graceful restarting very nicely.

## The reaction

The site has been well received by those outside government, but perhaps just as importantly the way that we ran the project caused a bit of a stir within Whitehall too. Agile projects are still rare in government, and IT spending is a [hot topic](http://www.bbc.co.uk/news/uk-politics-14314935) right now. It's great that people are beginning to think about how to deliver software in better ways and the guys at Skunkworks are doing really well at promoting agile methods internally.

## The team

Everyone who worked hard to make the site what it is: it was great fun working with you!

* [Tom Dickinson](http://www.unboxedconsulting.com/people/tom-dickinson) from [Unboxed](http://unboxedconsulting.com)
* [Peter Herlihy](http://uk.linkedin.com/in/peterherlihy)
* [Charlie MacLoughlin](http://uk.linkedin.com/pub/charlie-macloughlin/3/183/821)
* [Jolyon Pawlyn](http://www.unboxedconsulting.com/people/jolyon-pawlyn) from [Unboxed](http://unboxedconsulting.com)
* [Alan Thomas](http://www.unboxedconsulting.com/people/alan-thomas) from [Unboxed](http://unboxedconsulting.com)
* [Will Tomlins](http://www.unboxedconsulting.com/people/will-tomlins) from [Unboxed](http://unboxedconsulting.com)
* Me

We're planning to get the code out on github soon. Hope you like the site and enjoy using it.
