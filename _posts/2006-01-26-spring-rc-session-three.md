---
layout: post
title: Spring Richclient ~ Session Three ~ How did that work then?
date: 2006-01-26 23:09:00.000000000 +00:00
series: "Spring Richclient Tutorial"
categories:
- richclient
- java
- spring
- tutorial
redirect_from:
- "/2006/01/spring-rc-session-three"
- "/2006/01/spring-rc-session-three/"
---
{% include callout.html color="#f5f5f5" text="By the way...This content is now pretty old: check the homepage for the latest." %}
          
<p>At the end of the last session, we'd managed to get the Petclinic application up and running in its own directory, and located the main configuration file (richclient-application-context.xml). We'd also worked out what a few beans in there actually did, although there were many more still to look at. In the next couple of sessions, I'm going to have a closer look at the Rich Client specific beans in richclient-application-context.xml and work out what they do. </p>
<p>This session, let's find out how my "Hello, world!" change actually worked, by following the bean definitions through richclient-application-context.xml. We might even learn something about the Rich Client architecture on the way. Here goes...</p>
<h3>The Lifecycle Advisor</h3>
<p>The setup wizard from last session came up as the first thing after the splash screen, right? What controls in a Rich Client application which windows come up in which order? Let's do a search for setupWizard in the petclinic code and see what we come up with...</p>
<p>{% highlight bash %}
$ grep -nH -r setupWizard *
PetClinicLifecycleAdvisor.java:33:        if (getApplicationServices().containsBean("setupWizard")) {
{% endhighlight %}</p>
<p>Aha. We briefly mentioned the lifecycle advisor last session and labelled it as an "application flow controller". This is beginning to make sense.</p>
<p>Looking at the source code for this object, I'm guessing the following method is called just before the main window of the application is opened:</p>
<p>{% highlight java %}
    public void onPreWindowOpen(ApplicationWindowConfigurer configurer) {
        super.onPreWindowOpen(configurer);
        if (getApplicationServices().containsBean("setupWizard")) {
            SetupWizard setupWizard = (SetupWizard)getApplicationServices().getBean("setupWizard", SetupWizard.class);
            setupWizard.execute();
        }
		...
    }
{% endhighlight %}</p>
<p>Ok, so the "setupWizard" bean is searched for and "executed". Let's have a look at this bean.</p>
<h3>The "setupWizard" bean</h3>
<p>Here's the bean configuration from richclient-application-context.xml:</p>
<p>{% highlight xml %}
	<bean id="setupWizard"
		class="org.springframework.richclient.application.setup.SetupWizard">
<property name="licenseTextLocation">
			<value>/org/springframework/richclient/samples/petclinic/license.html</value>
		</property>
	</bean>
{% endhighlight %}</p>
<p>This is a simple bean to configure, a stock component of the Rich Client framework (from the class path), taking some license text from the petclinic application. So far, so good. Let's do what we did at the end of the last session in a little more detail, and look under the hood at SetupWizard.java. How does it create that first page?</p>
<p>{% highlight java %}
    public void addPages() {
        addPage(new SetupIntroWizardPage());
        addPage(licensePage);
    }
{% endhighlight %}</p>
<p>This addPages() method must be called at some point during creation ... and the first page is a SetupIntroWizardPage. Looking at SetupIntroWizardPage.java, we find the key for "setup.intro.description".</p>
<p>{% highlight java %}
    private JLabel createDescriptionLabel() {
        return new JLabel(LabelUtils.htmlBlock(getMessage("setup.intro.description")));
    }
{% endhighlight %}</p>
<p>That getMessage() method took quite a while to find - it can be traced right back to ApplicationServicesAccessor.java, a distant ancestor of this class:</p>
<p>{% highlight java %}
    protected String getMessage(String messageCode) {
        return getApplicationContext().getMessage(messageCode, null, messageCode, Locale.getDefault());
    }
{% endhighlight %}</p>
<p>This calls getMessage() on the application context. In a standard application context object, such as ours, this method looks for a bean with name "messageSource" and attempts to resolve the message key. Let's have a look at the "messageSource" bean next.</p>
<h3>The "messageSource" bean</h3>
<p>{% highlight xml %}
	<bean id="messageSource"
		class="org.springframework.context.support.ResourceBundleMessageSource">
<property name="basenames">
<list>
				<value>org.springframework.richclient.samples.petclinic.ui.messages</value>
				<value>org.springframework.richclient.application.messages</value>
			</list>
		</property>
	</bean>
{% endhighlight %}</p>
<p>Familiar Spring territory here. This is a standard Spring ResourceBundleMessageSource. Check the javadocs for ResourceBundleMessageSource if you need more explanation of this one.</p>
<p>Give the above configuration, ResourceBundleMessageSource will try these locations in this order to find the message key we supply:</p>
<p>{% highlight text %}
./src/org/springframework/richclient/samples/petclinic/ui/messages_&lt;language&gt;.properties
   (so messages_fr.properties if we have a french locale)
./src/org/springframework/richclient/samples/petclinic/ui/messages.properties
./src/org/springframework/richclient/application/messages_&lt;language&gt;.properties
{% endhighlight %}</p>
<p>The last path here refers to a "standard" Rich Client properties files which ships with the Rich Client framework. Looking inside, this defines words for things like "File", "Edit", "Paste", and standard icons used in many applications. The really neat thing is that these are already translated into French, German and Dutch for me, which gives me a whole lot of localisation for free! This framework really is awesome.</p>
<p>Oh look, we've traced our message back through the bean hierarchy. That wasn't too bad at all, was it?</p>
<h3>Summary</h3>
<p>A quick summary of what we've learnt in this session:</p>
<ul>
<li>The petclinic lifecycle advisor controls when windows appear when the application runs, and most likely can be used for many other things.</li>
<li>The standard spring "messageSource" bean is used by standard Rich Client objects such as SetupWizard to resolve message keys.</li>
<li>Rich Client provides many standard messages for you, pre-localised in four languages. Neat.</li>
</ul>
<p>Much of spring configuration we've looked at today looks like boilerplate xml to me - I don't think I'll need to change much at all. The only thing that looks like it needs changing here are the application specific messages.properties files, so that I can add the messages I want to appear.</p>
<p>Next session, we'll have a look at some of the other beans which use "messageSource".</p>
