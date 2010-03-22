---
layout: post
title: Multiple CI Joes with Rack and Passenger
date: 2010-03-22 20:18:00 +00:00
categories:
  - continuous integration
  - cijoe
  - howto
---
I've recently set up several [CI Joe](http://github/com/defunkt/cijoe) instances to handle our various projects at [Eden](http://edendevelopment.co.uk). We've been using [Integrity](http://integrityapp.com) for several months, but it's caused us a few problems and I yearned for something simpler. CI Joe is about as simple as it gets, and the brevity of the code encourages hacking and customisation.

I've now set it up to run multiple Joes using Rack and Passenger for the various different projects we run. Being as I didn't find much on the net about setting up CI Joe in this way, I thought a fairly detailed howto would be helpful. Let me know how you get on with it.

## Folder structure

Our structure looks like this:

{% highlight bash %}
/var/www/rails-apps/
  cijoe/        
    project1    # symlinked to ../cijoe-repos/project1/public
    project2    # symlinked to ../cijoe-repos/project2/public
    index.html  # the front page of your CI site.
  cijoe-repos/
    config.ru   # Master config.ru: see below
    build-hook  # Build hook file: see below
    credentials # username/password for the build-hook POST
    project1/
      config.ru # symlinked to ../config.ru
      app/      # contains the actual git clone'd app
      public/   # empty: only there for Passenger
    project2/
      etc.
{% endhighlight %}

Our index file is simply a javascript redirect to our dashboard app, which I [mentioned here](/2010/03/radiating-stats-at-eden) but will discuss more thoroughly in future posts.

## Passenger config

The main Passenger vhost is set up for the cijoe/ directory, and each CI Joe installation has to be symlinked in this way for it to pick them all up.

We put the following file in /etc/httpd/sites.d/ci.conf:

{% highlight apacheconf %}
<VirtualHost *:80>
  SetEnv PATH /usr/local/bin:/opt/ruby-ee/bin:/bin:/usr/bin
  DocumentRoot /var/www/rails-apps/cijoe
  RackBaseURI /project1
  RackBaseURI /project2
  PassengerMaxInstancesPerApp 1 
  PassengerMaxPoolSize 2 
  ErrorLog logs/ci-error_log
  CustomLog logs/ci-access_log combined
  <Directory "/">
        AuthName "Eden Development CI"
        AuthType Basic
        AuthUserFile /var/www/rails-apps/integrity/app/htpasswd
        require valid-user
  </Directory>
  SetEnv RAILS_RELATIVE_URL_ROOT
</VirtualHost>
{% endhighlight %}

The key bits here are as follows:

* Passenger by default runs ruby processes without a path set, so set the path so CI Joe can call git correctly.
* RackBaseURI is used to start multiple Joe's, one for each project.
* PassengerMaxInstancesPerApp needs to be set to one, otherwise you'll get weird results.
* Set your PassengerMaxPoolSize to exactly the number of Joes you've got running, so Passenger doesn't kill the build processes.
* Clear the RAILS_RELATIVE_URL_ROOT environment variable: this will be set by the RackBaseURI calls, and will bleed into your tests, break any that rely on absolute paths.

## config.ru

The config.ru we're using for the individual Joes is as follows:

{% highlight ruby %}
# Required so that we can set path correctly for Config, which 
# is loaded statically due to a bug in cijoe
$project_path = File.dirname(__FILE__) + "/app"
require 'cijoe'

# setup middleware
use Rack::CommonLogger
# configure joe
CIJoe::Server.configure do |config|
  config.set :project_path, $project_path
  config.set :show_exceptions, true
  config.set :lock, true
end

run CIJoe::Server
{% endhighlight %}

We keep this in the cijoe-repos/ folder, and symlink it into the different project folders. We also apply a monkey patch to the run_hooks method to strip out backticks: these can stop the hooks running correctly.

## Build hooks

If you want to use our build hooks, read on, otherwise you can safely skip the next section.  

We have one master build hook script living in cijoe-repos/ which we symlink everywhere. This reads the file structure to find out which project we're in, and its own symlinked name to work out what's happened. It then HTTP POSTs the results to our dashboard application:

{% highlight bash %}
#!/bin/bash
FULLPATH=`cd $(dirname $0); pwd`
echo $FULLPATH >&2
PROJECT=`echo $FULLPATH | awk -F/ '{print $(NF-3)}'`
STATUS=`echo $0 | awk -F- '{print $NF == "worked" ? "pass" : ($NF == "reset" ? "building" : "fail")}'`
PW=`cat $FULLPATH/../../../../credentials`
curl -u $PW -d"author=$AUTHOR" -- http://ci.edendevelopment.co.uk/dashboard/build/$PROJECT/$STATUS
echo "Project: "$PROJECT", Status: "$STATUS", Fullpath: "$FULLPATH >&2
{% endhighlight %}

It's not very pretty: my bash-fu isn't up to much. Suggestions for improvement are welcome.

## credentials

The credentials file mentioned above is a file which lives in cijoe-repos/. It has one line in it:

{% highlight text %}
username:password
{% endhighlight %}

These are the user authentication credentials for the POST to your dashboard.

## Adding a project

To add a project to the structure:

{% highlight bash %}
cd cijoe-repos
mkdir -p project/public
cd project
git clone git@github.com/path/to/my/project.git app
ln -sf ../config.ru
# If you're using hooks:
ln -sf /var/www/rails-apps/cijoe-repos/build-hook app/.git/config/build-worked
ln -sf /var/www/rails-apps/cijoe-repos/build-hook app/.git/config/build-failed
ln -sf /var/www/rails-apps/cijoe-repos/build-hook app/.git/config/after-reset
{% endhighlight %}

Then you need to poke the apache vhost configuration to add another RackBaseURI and up the number of processes by 1.

## Conclusion

This setup works well for us. We've only been running it a few days, but it does feel cleaner and more manageable that the old Integrity system. It's nice to have each server in seperate processes, with a fully customisable dashboard distinct from the build servers themselves.

With this setup a project could even choose to run a different server: as long as a config.ru file was defined and the HTTP POST notifications are made correctly, it will all work the same way. 

I'd love to make it a bit less complex to set up new projects. If you have any ideas for how to improve the setup then do let me know!
