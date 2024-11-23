---
layout: post
title: Spring Richclient ~ Session One ~ Making Petclinic work
date: 2006-01-23 14:31:00.000000000 +00:00
categories:
- richclient
- java
- spring
- tutorial
redirect_from:
- "/2006/01/spring-rc-session-one"
- "/2006/01/spring-rc-session-one/"
---
{% include callout.html color="#f5f5f5" text="By the way...This content is now pretty old: check the homepage for the latest." %}
          
<p>Right, here goes.</p>
<p>Initially I wasn't sure where to begin. I searched for "Spring Rich Client" on google, looking for a tutorial and found zero. I found the <a href="http://www.springframework.org/spring-rcp">Rich Client homepage</a> on the spring site, which was a start, and read the rather text-heavy introduction carefully.</p>
<p>I was rather suprised at this point that there wasn't an alpha release to download, but never mind, I suppose the framework is still in early development; and hey, I'm supposed to be a coder, and coders can handle checking out CVS, right? :)</p>
<p>Armed with an appropriate sense of coder machismo, I headed off to the sourceforge pages and checked out the code. Hit a hurdle trying to find the correct module name (spring-richclient, by the way - it's not mentioned on the webpage), but got there in the end by browsing the Sourceforge repository.</p>
<p>{% highlight bash %}$ cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/spring-rich-c login{% endhighlight %}</p>
<p>{% highlight bash %}$ cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/spring-rich-c co -P spring-richclient{% endhighlight %}</p>
<p>This got me the code, which looked to be a standard java project buildable with ant. Time to fire up emacs (I'm a JDE freak, away you Eclipse acolytes with your fancy iconry and easy-to-use plugins):</p>
<p>{% highlight bash %}M-x jde-ant-build / build{% endhighlight %}</p>
<p>So far, so good. Lots of text whirred past and I've built a version of the latest framework and packages it into three nice jars in the 'dist' directory. I've still no idea what anything does, but I'm feeling good at this point. I'm even brave enough to try running the unit tests...</p>
<p>{% highlight bash %}M-x jde-ant-build / test{% endhighlight %}</p>
<p>More whirring text. There are lots of tests passing, which is encouraging to a TDD fanboy. Most seem to pass without a hitch, I'm rather encouraged, then I see one failure:</p>
<p>{% highlight bash %}Test org.springframework.richclient.security.support.DefaultSecurityControllerManagerTests FAILED{% endhighlight %}</p>
<p>I haven't a clue what a DefaultSecurityControllerManager is, and decide to ignore it completely at this stage. I figure that if I encounter a problem later, I'll do a cvs update and see if that tests was fixed, and try again, then post to the Spring forum if it still doesn't work.</p>
<p>So, onto the sample application. I find a samples directory which contains 'petclinic' - most encouraging. Another build.xml - excellent:</p>
<p>{% highlight bash %}M-x jde-ant-build / usage
Petclinic Rich sample application build file
------------------------------------------------------
Available targets are:
clean  --> Clean output dirs
build  --> Compile main Java sources and copy libraries
build-standalone  --> Compile standalone main Java sources and copy libraries
warfile  --> Create WAR deployment units
javadoc  --> Create API documentation
{% endhighlight %}</p>
<p>Hmm. Clean, build and javadoc I understand, but what's with the standalone and warfile variants? This is initially rather confusing, as I figured that there wouldn't be any need to run a web application to use Spring Rich Client. I peer at the build.xml file for a bit longer, until I see the Java Web Start (JWS) references and figure the web application must just be to demonstrate a Rich Client application running through JWS.</p>
<p>(Note: it's only later that I saw that you need a web application because petclinic can be a client-server application - this wasn't at all clear on first read. Perhaps two samples would be clearer, rather<br />
than combining both in the same place? Or perhaps a simple "Hello, World?" application would bridge the gap?)</p>
<p>I decided to take one step at a time and forget about JWS for now:</p>
<p>{% highlight bash %}M-x jde-ant-build / build{% endhighlight %}</p>
<p>More whirring text, with the petclinic jar placed in the 'dist' directory. Excellent - it seems all is well so far and I didn't need the web application stuff. Ok, let's give it a go. Thinking that it's ten to one I've missed something, I try:</p>
<p>{% highlight bash %}$ java -jar petclinic-standalone.jar{% endhighlight %}</p>
<p>Ooo. A splash screen. A frog, even better. And then, to my great delight:</p>
<p><img src="/files/spring-rcp-1.jpg"/></p>
<p>Wow. <a href="http://www.jgoodies.com">JGoodies</a> support right out of the box. I couldn't have hoped for anything better.</p>
<p>After clicking next a few times, and bypassing the login screen with a "Cancel", I get:</p>
<p><img src="/files/spring-rcp-2.jpg"/></p>
<p>Wonderful. I've now got the source code compiling and I've a sample application I can tweak and see what happens - the only way I can really learn anything. I'm set.</p>
<p>A couple of thoughts before I close out this session. Firstly it's clear the bad old days of ugly java apps are over. I'm blown away by how good the application looks, for a java application. That's partly due to the wonders of JGoodies, but it looks like Spring Rich Client is going to help me produce a lovely looking application for the client. Excellent.</p>
<p>Secondly, I'm pleased that there really weren't that many steps for the average java developer who's used to ant to go through before getting this working. The only real hurdles were finding the right CVS module, and deciphering the ant build targets which at first glance are rather impeneterable. I'm also pleased it compiled straight from CVS and (almost) all the tests passed; a failing build, and I would have mostly likely given up there and then.</p>
<p>Coming soon: "Session Two: Hello, world!"</p>

