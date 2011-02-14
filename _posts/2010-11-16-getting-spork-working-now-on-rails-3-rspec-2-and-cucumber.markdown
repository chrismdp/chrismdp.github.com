---
layout: post
title: "How to get Spork working NOW on Rails 3, Rspec 2 and Cucumber"
date: 2010-11-16 21:41:57 +0000
categories:
  - rails
  - ruby
  - rspec
  - spork
  - cucumber
---
I've spent the evening trying to get [Spork](https://github.com/timcharper/spork) to work with Rails 3 and RSpec 2. I've never felt the need for it before, but the Rails 3 start up time is fairly hefty and I'm crying out for the extra seconds more than ever.

It's not that tricky, thankfully, and the following steps should see you running faster specs and features in no time.

## RSpec 2

Follow these instructions to get RSpec 2 working:

*Install Spork into your Gemfile, and update rspec to 2.1:*

{% highlight ruby %}
gem "spork", :git => "git://github.com/chrismdp/spork.git"
gem "rspec-rails", '>= 2.1.0'
{% endhighlight %}

You'll need [my fork of Spork](http://github.com/chrismdp/spork) for a quick patch to the latest release candidate of Spork.

*Add --drb on a new line in your .rspec file:*

If you don't have the .rspec file, create it.

*Modify your spec_helper.rb:*

You could follow the installation instructions, but not everything is relevant to Rails 3 and Rspec 2. It's pretty simple anyway: add "require 'spork'" to the top of your spec_helper.rb file, and put everything else inside spec_helper.rb inside a Spork.pre_fork do ... end block:

{% highlight ruby %}
require 'spork'

Spork.prefork do
  ENV["RAILS_ENV"] ||= 'test'
  require File.expand_path("../../config/environment", __FILE__)
  require 'rspec/rails'
  ...
end
{% endhighlight %}

That should be it. To start up the server, run:

{% highlight bash %}
$ bundle exec spork
{% endhighlight %}

...and then try running a spec or two. The following command takes about a second on my machine now, whereas it used to take about ten seconds!

{% highlight bash %}
$ bundle exec rspec spec/controllers/sessions_controller_spec.rb
{% endhighlight %}

## Cucumber

It's important to note that for more than about 10-20 scenarios, Spork is *slower* than running cucumber normally. Therefore only turn it on for a few profiles, such as autotest (but not autotest-all), wip, etc.

*Modify your cucumber.yml file:*

{% highlight yaml %}
wip: --drb -tags @wip:3 --wip features
autotest: --drb --color --format progress --strict
{% endhighlight %}

Leave 'autotest-all' and 'default' alone.

*Modify your features/support/env.rb:*

This is just the same process as with the spec_helper.rb file for RSpec:

{% highlight ruby %}
require 'spork'

Spork.prefork do
  ENV["RAILS_ENV"] ||= "test"
  require File.expand_path(File.dirname(__FILE__) + '/../../config/environment')
  require 'cucumber/formatter/unicode' # Remove this line if you don't want Cucumber Unicode support
  require 'cucumber/rails/rspec'
  ...
end
{% endhighlight %}

Again, that should be it. Run the follow to try it out:

{% highlight bash %}
$ bundle exec spork cucumber
{% endhighlight %}

Now try running a single feature in rerun or autotest mode. I'm getting 20% speedups for about 10 scenarios.

## Using them together

The RSpec and Cucumber versions of spork use different ports, so there's no problem running them together. Normally I run both in the same terminal window, one as a background process:

{% highlight bash %}
$ bundle exec spork cucumber & bundle exec spork
{% endhighlight %}

Then I run autotest in another window.

## How do I use this?

I'm really liking this setup. It makes rapid TDD possible again, even when dealing with fairly slow tests. 

Of course, we should be doing all we can to get the speed of our tests as high as possible: slow tests are a type of code smell. However, infrastructure load time is unavoidable and cutting it out is full of all kinds of win.

Use this setup with [autotest](https://github.com/grosser/autotest) and [autotest-growl](https://github.com/svoop/autotest-growl) for maximum win. Autotest has come a long way recently: there's a lightweight alternative to ZenTest now, and easy growl support. Cutting out even the 'Oh, I should run my tests now step' totally nails your debug cycle: not sure it gets much tighter than that.

## UPDATE: Even more speed!

[Jo Liss](http://opinionated-programmer.com/) got in touch: she's made some performance gains by skipping the "bundle exec" and requiring a few extra files in the prefork block. Read about what she has to say [here](http://opinionated-programmer.com/2011/02/profiling-spork-for-faster-start-up-time/).
