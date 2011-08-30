---
layout: post
title: Spring Richclient ~ Session Five ~ Applications, windows, views
date: 2006-02-03 15:21:00 +00:00
categories:
  - richclient 
  - java 
  - spring
  - tutorial
---
<div class='notice'><h1>By the way...</h1><p>This content is now pretty old: check <a href='/'>the homepage</a> for the latest.</p></div>
          
<p>Thanks to the recently discovered <a href="http://opensource2.atlassian.com/confluence/spring/display/RCP/Home">Spring Rich Client wiki</a>, I've discoved the basic architecture of a Rich Client application. </p>
<p>After reading the <a href="http://opensource2.atlassian.com/confluence/spring/display/RCP/Introduction#Introduction-PlatformOverview">platform overview section</a> on the wiki, I was at a bit of a loss with all the terms, so I thought I'd better draw a diagram. I cranked up OpenOffice Draw and the GIMP, and came up with this:</p>
<p><img src="/files/rcp-layout.jpg"></p>
<p>Basically, we've got an Application object, which contains one or more windows. Each of these contains a page, which in turn contains one or more views laid out upon it. The page manages the views, passing them lifecycle notifications and arranging them as it sees fit.</p>
<p>Ok, that makes more sense now it's in a diagram. Let's have a look at the Petclinic application, and see how that fits into this mould.</p>
<p>Taking a look back at our old friend richclient-application-context.xml, we can now understand Application and ApplicationDescriptor much more clearly. The ApplicationDescriptor simply defines properties of the standard Application object that's instantiated.</p>
<p>We were correct about the PetclinicLifecycleAdvisor: it backs the Application object and allows us to control coarse-grained application behaviour. There's an example of this sort of control on <a href="http://opensource2.atlassian.com/confluence/spring/display/RCP/Core+Concepts">this wiki page</a> which shows us how to add a confirmation window before closing the application. We've also got other examples in the PetclinicLifecycleAdvisor implementation - the "setupWizard" window is thrown up before the main application window is starting. See <a href="/node/10">Session Three</a> for the code.</p>
<p>Ok, so where in Petclinic are the main application windows defined? From running the application, we can clearly see that there's only one of them. Unfortunately looking at richclient-application-context.xml wasn't very helpful. In the end I did a search for ownerManagerView, which I figured must be added to the ApplicationPage somewhere. In my search I noticed that we pass the ownerManagerView into the Lifecycle advisor configuration:</p>
<p>{% highlight xml %}
	<bean id="petclinicLifecycleAdvisor"
		class="org.springframework.richclient.samples.petclinic.PetClinicLifecycleAdvisor"></p>
<property name="windowCommandBarDefinitions">
			<value>org/springframework/richclient/samples/petclinic/ui/commands-context.xml</value>
		</property>
<property name="startingPageId">
			<value>ownerManagerView</value>
		</property>
	</bean>
{% endhighlight %}</p>
<p>Interesting. Time to look up "startingPageId" in ApplicationLifecycleAdvisor.java. The most helpful thing we run into is the afterPropertiesSet() method. This method, if it exists, this is called by the regular Spring Framework to allow people to check values were set correctly at the time of application launch. The relevant bit of Java code is below:</p>
<p>{% highlight Java %}
public void afterPropertiesSet() throws Exception {
  final Properties systemProperties = System.getProperties();
  if (systemProperties.get(EXCEPTION_HANDLER_KEY) == null) {
    systemProperties.put(EXCEPTION_HANDLER_KEY, getEventExceptionHandler().getName());
  }
  Assert.state(startingPageId != null,
    "startingPageId must be set: it must point to a page descriptor, or a view descriptor for a single view per page");
  }
{% endhighlight %}</p>
<p>The only relevant statement is the last one - it tells us that we need to set startingPageId to a "page descriptor", or a "view descriptor". I'm assuming here that Spring Rich Client uses the term "descriptor" classes to mean objects that describe how to set up other objects.</p>
<p>Ok, so what code actually sets up the page? A search for getStartingPageId leads to the jackpot, in ApplicationLauncher.java:</p>
<p>{% highlight java %}
private void launchMyRichClient() {
  ...
  Application application = (Application)rootApplicationContext.getBean(APPLICATION_BEAN_ID, Application.class);
  application.openWindow(application.getLifecycleAdvisor().getStartingPageId());
  application.getLifecycleAdvisor().onPostStartup();
  ...
}
{% endhighlight %}</p>
<p>If I'd remembered ApplicationLauncher, I might have started there at the beginning of this session! This clearly starts the application and opens a window, passing the startingPageId (which refers to the ownerManagerView for PetClinic).</p>
<p>Hang on a minute though: the diagram above clearly states that a window contains a page, which contains a view - you might be asking "How can a window be opened with a view?". The afterPropertiesSet() error message above tells us that if you pass a view descriptor instead of a page descriptor, it'll just create a page with the one view you've described. Excellent.</p>
<h3>Summary</h3>
<p>We've learnt today how the main windows of applications are defined. It appears that creating your first main window is as simple as passing either PageDescriptor or a ViewDescriptor into the standard ApplicationLifecycleAdvisor. If you pass a PageDescriptor, an ApplicationPage will be created according to the descriptor object you pass. If, however, you pass ViewDescriptor, an ApplicationPage will be created with one view, created again according to the descriptor you passed in.</p>
<p>Next session, we'll have a look at that "ownerManagerView" ViewDescriptor, take it apart, and work out how to change it.</p>
