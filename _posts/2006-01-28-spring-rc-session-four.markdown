---
layout: post
title: Spring Richclient ~ Session One ~ Beans, Shmeans and services
date: 2006-01-28 12:48:00 +00:00
categories:
  - spring richclient 
  - java 
  - spring
  - tutorial
---
<div class='notice'><h1>By the way...</h1><p>This content is now pretty old: check <a href='/'>the homepage</a> for the latest.</p></div>
          
<p>This session, let's have a brief look at some of the other in the richclient-application-context.xml file, and see if we can at least work out roughly what they're for. First however, a word about ApplicationServices.</p>
<h3>The ApplicationServices singleton</h3>
<p>It looks like ApplicationServices is implemented as an old fashioned singleton bean. Have a look at the method below as an example of a service initialisation performed in this class:</p>
<p>{% highlight java %}
    private void initImageSource() {
        try {
            this.imageSource = (ImageSource)getApplicationContext().getBean(IMAGE_SOURCE_BEAN_ID, ImageSource.class);
        }
        catch (NoSuchBeanDefinitionException e) {
            logger.info("No image source bean found in context under name '" + IMAGE_SOURCE_BEAN_ID
                    + "'; configuring defaults.");
            this.imageSource = new DefaultImageSource(new HashMap());
        }
    }
{% endhighlight %}</p>
<p>Most of the other services are similarly initialised. </p>
<p>This means that ApplicationServices <i>looks</i> for beans to help in configuring the application backbone, but doesn't <i>have</i> to have them. If it can't find the relevant bean, it'll just create a default and use that.</p>
<p>How is it used? Well, there are lots of calls in the code like this:</p>
<p>{% highlight java %}
	iconSource = Application.services().getIconSource();
{% endhighlight %}</p>
<p>Let's dive off on a tangent for a moment. Why is this class necessary? After all, with dependency injection, why have a central singleton defining services at all? Surely various beans would simply have their dependencies wired up as and when they need them, rather than referring to a central dependency. Is this class a legacy requirement, or does it prevent us having pages of standard spring wiring XML which is inefficient, difficult to maintain, and unnecessary?</p>
<p>I'd be interested in finding out your thoughts on this, especially if you are further along the "way of the Rich Client" than I - feel free to leave a comment.</p>
<p>Right, on to some of the other beans. I feel we're getting diminishing returns from looking at these, but we'll press on with a few.</p>
<h3>componentFactory</h3>
<p>The componentFactory is of type DefaultComponentFactory, and is one of the Application Services mentioned in the previous section.</p>
<p>{% highlight bash %}$ grep -nH -r componentFactory *
richclient-application-context.xml:53:	<bean id="componentFactory"
{% endhighlight %}</p>
<p>Searching for files which access ApplicationServices' getComponentFactory() method turns up a whole bunch of results in the Rich Client source, but not very much in the Petclinic source. Looks like the component factory is used to create components all over the place in the main Rich Client source. I'm guessing that the Petclinic does not require the ability to create many components - and a quick look at some of the code confirms this to be the case. More on this later.</p>
<h3>imageSource</h3>
<p>Here's the "imageSource" bean definition:</p>
<p>{% highlight xml %}
	<bean id="imageSource"
		class="org.springframework.richclient.image.DefaultImageSource">
		<constructor-arg index="0">
			<ref bean="imageResourcesFactory"/>
		</constructor-arg></p>
<property name="brokenImageIndicator">
			<value>images/alert/error_obj.gif</value>
		</property>
	</bean>
{% endhighlight %}</p>
<p>This provides a "broken image indicator" path - useful, so we can actually see the dodgy images like on a web page, rather than just having invisible ones). </p>
<p>The bean references imageResourcesFactory, which create a Map of strings to resource locations, for the imageSource bean to use, from a couple more properties files.</p>
<p>{% highlight xml %}
	<bean id="imageResourcesFactory"
		class="org.springframework.context.support.ResourceMapFactoryBean"></p>
<property name="locations">
<list>
				<value>classpath:org/springframework/richclient/image/images.properties</value>
				<value>classpath:org/springframework/richclient/samples/petclinic/ui/images.properties</value>
			</list>
		</property>
<property name="resourceBasePath">
			<value>images/</value>
		</property>
	</bean>
{% endhighlight %}</p>
<p>There's another "standard" Rich Client properties file here (just as there was one for the messageSource bean last session) which defines paths for basic icons (like those for "New", "Open", "Save" etc). These ship in spring-richclient-resources.jar, so you can use them out of the box. If you don't want to, simply define your own icon location with the same name in your own images.properties. Easy.</p>
<h3>applicationEventMulticaster</h3>
<p>This one looks straightforward - it appears to simply be the event transport for the application context, and is part of standard Spring from the classpath. That looks to be how events are passed around the application.</p>
<h3>rulesSource</h3>
<p>This seems to provide sets of rules to use when validating entered data. Looking at the source for PetClinicValidationRulesSource, the class being instantiated, it sets up certain constraints for the owner and pet data that is entered into the app. More on this in a future session, when we create our own data entry box.</p>
<h3>And... stop</h3>
<p>Right, that's enough. Apart from the ui beans which we'll cover next session, the other beans all look far too scary. Plus, I'm bored with looking at XML. I think we'll learn more going forward by looking at some of the windows, views and dialogs represented by the GUI beans.</p>
<p>Mmm. GUI beans. Now there's a thought.</p>
<h3>Summary</h3>
<p>We've come some way today in understanding the Rich Client architecture, and how the core ApplicationServices code initialises and configures itself. We discussed the ApplicationServices class and it's usefulness/right to exist, without really knowing the answer. Comments welcome.</p>
<p>We also went through a few more of the beans in the richclient-application-context.xml and didn't learn all that much, apart from one important thing - we've come to the end of this file's usefulness in teaching us anything new.</p>
<p>Next session: windows, views, dialog boxes and perhaps even a field or two.</p>
