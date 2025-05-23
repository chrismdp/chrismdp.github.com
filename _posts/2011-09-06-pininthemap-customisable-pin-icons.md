---
layout: post
title: 'Pin in the map: customisable pin icons'
date: 2011-09-06 21:18:13.000000000 +01:00
categories:
- code
- cucumber
- ruby
- legacy
- products
- pininthemap
redirect_from:
- "/2011/09/pininthemap-customisable-pin-icons"
- "/2011/09/pininthemap-customisable-pin-icons/"
---
I've just spent some time updating my first ever Rails project, [Pin in the map](http://pininthemap.com). Now you can change the icons associated with premium (paid for) pins. There are over 100 new icons to choose from: [have fun!](http://pininthemap.com)

![pininthemap example](/assets/img/pininthemap-example.png)

## Learnings

This codebase is from 2006, so this has proved a nice little exercise in adding testing to a legacy project. I had no tests at all to speak of when I wrote the code five years ago, and the code shows it. I began by installing cucumber and rspec and quickly wrapping the two most common features in acceptance tests: creating and editing pins. Even on old code it was super easy to get capybara, cucumber and rspec up and running, thanks to the fact that we've upgraded the codebase to Rails 2 and started using bundler to manage gem dependencies. We stuck to Selenium for the tests as the code is very Google Maps heavy.

It's always worth keeping old apps vaguely up to date: the less inertia surrounding a codebase the more likely you'll spend an afternoon adding an often-requested feature.
