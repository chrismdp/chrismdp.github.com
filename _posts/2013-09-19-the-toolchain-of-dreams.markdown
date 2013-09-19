---
layout: post
title: "The toolchain of dreams"
date: 2013-09-19 15:11:58 +0100
categories:
  - ruby
  - continuous delivery
  - continuous integration
  - tools
  - code
  - rails
  - git
  - craftsmanship
  - bdd

---

Seems like yesterday people were saying that it
was difficult to host Ruby apps. It was around the time people were saying "Rails doesn't scale", which thankfully [has](http://twitter.com) [been](http://github.com) [proved](http://groupon.com) [dramatically](http://ask.fm) [wrong](http://gov.uk).

For a while now Ruby apps have been unbelieveably easy to run and host,
especially when you're getting started.

But it's got even better than that in the last few months. I've
now got a complete Continuous Delivery toolchain set up for [my latest app](http://online.soltrader.net),
entirely in the cloud. It's Continuous Delivery As A Service, and it's
dreamy. This is how to set it up, and how it works.

## Source control: Github

I'm using [Github](http://github.com) for code hosting and source control. You probably are already too. Most of the other services integrate with it very well, so setting this toolchain up is so much easier if you're using it.

## Build server: Semaphore

Cloud-based build services have been running for a while now. I like [Semaphore](http://semaphoreapp.com) - the user interface is clean and easy to read, and it does automatic deploys of passing code:

![Semaphore](http://chrismdp.com/files/semaphore.png)

Set up Semaphore by creating a trial account, connecting it with your Github account and picking the repository you'd like to build. It automatically analyses your project for a build script so if you have a standard Ruby or Rails project you probably won't need to configure it much.

## Deployment: Heroku

If you're using Heroku to deploy your code, set it up to deploy to [Heroku](http://heroku.com). It takes a few seconds in the settings menu for your project to do so. You can also make it use a Capistrano deploy script.

## Quality Analysis: Code Climate

Lastly, set up [Code Climate](http://codeclimate.com) to monitor the quality of your app's code. Setting up Code Climate is similar to Semaphore: sign up for a trial, connect to Github, select the repository. It will automatically set up the Github commit hooks for you.

To get code coverage integration, you'll need to [install a gem](https://codeclimate.com/docs#test-coverage), but it only takes a few minutes.

## How the toolchain works

Out of the box, Github tells Semaphore to build every commit I push. If I push a branch, Semaphore builds that, too, and updates the build status of the commit so that everyone can see if the pull request is ready:

![Github build status](http://chrismdp.com/files/github-build-status.png)

## Merging code into master

When the pull request is merged, the code goes into master:

* Semaphore builds the master branch. If the tests pass, the code is deployed to Heroku.
* Code Climate automatically gets notified by Github and checks to see whether coverage has improved or decreased, whether I've introduced any Rails security problems, or whether my code is bad:

![Code climate](http://chrismdp.com/files/codeclimate.png)

## Logging

Builds, deploys and Code Climate notifications are all automatically posted to Hipchat, so I get a log of everything that's happened without being inundated with emails:

![Hipchat](http://chrismdp.com/files/hipchat.png)

Just set up a Hipchat account, get a Room API key from the settings page, and plug that into Github, Code Climate and Semaphore. Done.

## The dream toolchain

This is how you use this toolchain:

{% highlight bash %}

    $ git push

{% endhighlight %}

Every time I push some code, it's checked carefully, and monitored for quality and security holes. The tests are run and coverage reports are generated and presented nicely. If all the tests pass the code immediately gets deployed to production, and all of this activity is reported and logged in one central place.

This is the future. It really doesn't get much better.

## Time is valuable: and this didn't take long

This took me about 40 minutes to set up. 30 minutes of that was fiddling with the settings of the various tools: but actually leaving them all set to default does the right thing for me in all cases. Most of the tools simply connect to your Github account to set up all the access controls and keys for you.

## The cost

For one project, this incredible toolchain will cost you the following:

* Github: $7 a month for the micro plan
* Semaphore: $14 a month for the solo plan
* Code Climate: $24 a month for the solo plan
* Hipchat: Free for one room
* Heroku: Free for a one dyno app.

**That's $45 a month.** That's next to nothing for such an amazingly powerful toolchain. Plus if you run more than one project, the per-project cost decreases dramatically.

I used to run one server to host one Rails app for $140 a month, for *years*, with no build server, deployment or code metrics built into the toolchain. Today I pay half that for a much more sophisticated setup.

Admittedly, the hosting costs with Heroku will go up once your app becomes popular, but this is a good problem to have, and at that point you shoud have the cash to invest in a chef-based cloud server deployment solution. I run one of those for [an old SaaS service I run](http://pininthemap.com) to keep costs down. It's still very easy to connect a different deployment strategy in to this toolchain.

So: what are you waiting for?
