---
layout: post
title: A cache-busting http server script in ruby
date: 2011-12-14 16:57:43.000000000 +00:00
categories:
- code
- javascript
- ruby
redirect_from:
- "/2011/12/cache-busting-ruby-http-server"
- "/2011/12/cache-busting-ruby-http-server/"
---
<p><i>"All of this can be yours/just give me what I want/and no one gets hurt"</i></p>

-- Bono, Vertigo

If you've done much Javascript development, or simple web development without a webserver backend, you don't want to set up a complex framework. Just give me the pages: I want to be able to start a simple webserver to give me the current directory structure as a website. You can't simply load the pages into a browser using `file://` because that screws up the relative paths that our sites rely on. What's the best way of doing this?

## Python's SimpleHTTPServer

One simple way is:

{% highlight bash %}
python -m SimpleHTTPServer
{% endhighlight %}

This does a great job, but there's one small problem: caching. Ordinarily during development you'll want the browser to request the HTML each time, and the python server doesn't do that out of the box.

## Ruby's WEBrick with adding cache-busting

Here's a small script I borrowed from [pmarti](http://github.com/pmarti) and tweaked. It lives in the `bin/http` file on my path: I just type `http` in the relevant folder and I'm set.

{% highlight ruby %}
#!/usr/bin/env ruby

require 'webrick'
class NonCachingFileHandler < WEBrick::HTTPServlet::FileHandler
  def prevent_caching(res)
    res['ETag']          = nil
    res['Last-Modified'] = Time.now + 100**4
    res['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    res['Pragma']        = 'no-cache'
    res['Expires']       = Time.now - 100**4
  end

  def do_GET(req, res)
    super
    prevent_caching(res)
  end
end

server = WEBrick::HTTPServer.new :Port => 8989

server.mount '/', NonCachingFileHandler , Dir.pwd
trap('INT') { server.stop }
server.start
{% endhighlight %}

Hope it's helpful. Do you know of a better way of doing it? Feel free to share...
