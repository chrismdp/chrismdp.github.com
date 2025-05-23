---
layout: post
title: How to test your node.js app
date: 2010-05-23 11:05:00.000000000 +01:00
categories:
- javascript
- code
- tdd
- node.js
redirect_from:
- "/2010/05/tdd-with-node-js"
- "/2010/05/tdd-with-node-js/"
---
I've wanted to hack on a [node.js](http://nodejs.org) project for a while, and a new app idea has given me the perfect excuse. My first question was: how do I test this? It's a fairly new field out there, and there isn't much help from node.js itself: it's much more like [Rack](http://rack.rubyforge.org/) than a proper framework. So I spent some time coming up with one way to do it.

Disclaimer: I'm not that experienced with Javascript, particularly with the best way to define objects. I'd be grateful for patches to help improve the quality of the code here. I've also borrowed heavily from [apprentice-us](http://github.com/redsquirrel/apprentice-us) - thanks to [Dave](http://twitter.com/redsquirrel) and [Corey](http://twitter.com/coreyhaines)!

## Overview 


This is what I've got so far (the actual app I'm working will remain closed-source for the mo):

[Example node.js github project](http://github.com/chrismdp/example-nodejs-project)

You probably want to refer to the code whilst reading the rest of this article.

To run the tests, run _rake_. To start the app, run _node app.js_ (you will need to have node.js installed obviously).

If you install the [watchr](http://github.com/mynyml/watchr) gem, and run _watchr autotest.watchr_, you'll get robust autotest like functionality. I'm liking watchr much better than ZenTest right now.

## How it works

The basic premise is to decouple the request/response handler from the server (see *app.js*, *lib/http.js* and *lib/router.js*). The interesting bit is in *test/ integration/ user_sees_homepage.js* - this then calls the dispatch method directly, passing in dummy Request and Response objects.

Note how I've [defined the Response object](http://github.com/chrismdp/example-nodejs-project/blob/master/test/integration/user_sees_homepage.js). This allows me currently to write an integration test that looks like this:

{% highlight javascript %}
router.dispatch(new Request("GET", "/"), new Response(function(headers, data) {
  assert.contains("200", headers['status'])
  assert.contains("Hello, world!", data)
}));
{% endhighlight %}

The assert.contains() method is not part of node.js: it's implemented in _test/helper.js_.

The reason you need the asserts to be fired in the end() function is that node.js is inherently asynchronous and will finish executing this file whilst waiting for the haml file to load in *lib/router.js*. Try it yourself: if you put an assert at the bottom of the file it will fire immediately.

## Unit tests

The plan is then to define whichever unit tests you need in *test/ unit/ (something)_test.js*, with the corresponding code in *lib/ models/ (something).js*. Just run javascript code in here and call methods on assert, and rake will execute it.

## Improvements

You could potentially use the Sinatra-like framework [Express](http://expressjs.com) to define *lib/router.js* - I've handrolled it for the moment. I'm of the opinion that you spot betterrefactorings by handrolling to start with: it could be that express.js isn't right for my app, and I can't easily tell yet.

There are a number of javascript testing libraries out there, but at the moment I'm happy with my own handrolled version, which just relies on the 'assert' package that node.js provides. There's nothing to stop you using JSpec or some other javascript testing library: I wanted to keep things simple to start with. 

I'm also aware that Cucumber [now supports javascript through V8](http://blog.josephwilk.net/ruby/testing-javascript-with-cucumber-in-javascript.html), which is an important step in the right direction. Unfortunately however it doesn't yet support the [commonjs](http://commonjs.org) package system, and doesn't run through node.js but through raw V8. This makes it hard to use with anything but toy examples. Ideally I've love to plug Cucumber in in the future, if we can get it to use node.js as the platform somehow.

If you use it for something useful, let me know! I'd be very happy to receive patches and suggestions.
