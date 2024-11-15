---
layout: post
title: Spring Richclient ~ Session Two ~ Hello World
date: 2006-01-24 14:40:00.000000000 +00:00
categories:
- richclient
- java
- spring
- tutorial
redirect_from:
- "/2006/01/spring-rc-session-two"
---
<div class='alert'><h1>By the way...</h1><p>This content is now pretty old: check <a href='/'>the homepage</a> for the latest.</p></div>
          
<p>Ok. Today, it's time to look under the hood.</p>
<p>Firstly, I decided to move the petclinic application to its own directory and clean up the paths a bit so that they reflected the usual way I organise java applications. Also, I wanted this to be a standalone application and therefore I needed to remove some of the relative paths in project.properties so that we didn't need the Rich Client source around to compile and run it. Finally, to satisfy my TDD cravings, I added junit test build targets in and created a dummy test to ensure junit was up and running. </p>
<p>After fixing a number of little build.xml bugs, I got the project compiling again in its own directory. So far, so good. Right, time to look at how this all works. </p>
<p>A look at the build.xml shows that the petclinic-standalone.jar we ran in the first session uses PetClinicStandalone.java as its entry point, so let's start with that:</p>
<p>{% highlight java %}
public class PetClinicStandalone {
    public static void main(String[] args) {
        try {
            String rootContextDirectoryClassPath = "/org/springframework/richclient/samples/petclinic/ctx";
            String startupContextPath = rootContextDirectoryClassPath + "/common/richclient-startup-context.xml";
            String richclientApplicationContextPath = rootContextDirectoryClassPath
                    + "/common/richclient-application-context.xml";
            String businessLayerContextPath = rootContextDirectoryClassPath + "/common/business-layer-context.xml";
            String securityContextPath = rootContextDirectoryClassPath + "/standalone/security-context.xml";
            new ApplicationLauncher(startupContextPath, new String[] { richclientApplicationContextPath,
                    businessLayerContextPath, securityContextPath });
        } catch (Exception e) {
            System.exit(1);
        }
}
{% endhighlight %}</p>
<p>Ok, that looks straightforward. We hard code a number of paths to what look like XML files of spring beans, and pass them into an "ApplicationLauncher". They're split into two groups: the "startup context file", and an array of "the other context files".</p>
<h3>The startup context</h3>
<p>I'm guessing a "startup context file" contains special beans to help with the startup of the application. A quick look at ApplicationLauncher.java confirms this; the javadoc for the constructor reads:</p>
<p>{% highlight html %}
Launch the application using the spring application context
at the provided paths for configuration. The startup context
path is loaded first to allow for quick loading of the
application splash screen.
{% endhighlight %}</p>
<p>Excellent. That must be what stuck that frog picture on my screen in session one. Let's have a look at the richclient-startup-context.xml file:</p>
<p>{% highlight xml %}
  <beans>
    <bean id="splashScreen" class="org.springframework.richclient.application.SplashScreen" singleton="false">
      <property name="imageResourcePath">
        <value>/images/splash-screen.jpg</value>
      </property>
    </bean>
  </beans>
{% endhighlight %}</p>
<p>A little more digging in the code shows that that "splashScreen" bean is actually a hard coded bean name in the ApplicationLauncher, so I guess if you want a splash screen in your application, just do exactly as the sample does.</p>
<p>At this point a strong temptation to vandalise splash-screen.jpg with a cheeky "Hello, world!" came over me (that would satisfy my brief for this session in one go, right?). But we wouldn't learn much from that, and I feel like I'm on a roll here. </p>
<p>Right, what about those other application context files? More looking through ApplicationLauncher.java shows me that they're piped into a good ol' ClassPathXmlApplicationContext, familiar to Spring aficionados the world over. One application context is created from all the files: I guess they're split up into different files so different variants of Petclinic (I'm thinking client/server here) can mix and match different beans as they wish.</p>
<p>Let's look at each of these files in turn: </p>
<h3>security-layer-context.xml</h3>
<p>This file contains a bunch of familiar looking ACEGI Security beans. I'm not going into the details of setting up ACEGI security - being a totally non-invasive security architecture, if you don't want it you shouldn't have to worry about it. At least, that's true for 'regular' Spring, and I'm guessing that it'll be the same here too.</p>
<h3>business-layer-context.xml</h3>
<p>This is familiar territory for anyone using spring for web applications. We find a data source (petclinic uses HSQL to store its data), a transaction manager, and a DAO in the form of a "clinic" bean. No suprises here.</p>
<h3>richclient-application-context.xml</h3>
<p>That leaves us with richclient-application-context.xml, which is all new. I have to say at this point I baulked slightly at the sheer number of new beans to learn. But hey, somebody wrote it, so someone must understand it, right? Therefore it must be possible to figure it out... </p>
<p>With that in mind, let's start with the first three beans:</p>
{% highlight xml %}
<p>
  <bean id="application"
    class="org.springframework.richclient.application.Application">
    <constructor-arg index="0">
      <ref bean="applicationDescriptor"/>
    </constructor-arg>
    <constructor-arg index="1">
      <ref bean="petclinicLifecycleAdvisor"/>
    </constructor-arg>
  </bean></p>
  <p>
  <bean id="applicationDescriptor" class="org.springframework.richclient.application.support.DefaultApplicationDescriptor">
    <property name="version">
      <value>1.0</value>
    </property>
    <property name="buildId">
      <value>20041025001</value>
    </property>
  </bean>
  </p>
  <p>
    <bean id="petclinicLifecycleAdvisor"
    class="org.springframework.richclient.samples.petclinic.PetClinicLifecycleAdvisor">
<property name="windowCommandBarDefinitions">
      <value>org/springframework/richclient/samples/petclinic/ui/commands-context.xml</value>
    </property>
<property name="startingPageId">
      <value>ownerManagerView</value>
    </property>
  </bean></p>
{% endhighlight %}
<p>From looking at ApplicationLauncher, "application" is a "magic name" for a bean - that is, the framework looks specifically for a bean called "application" in one of its XML files. It's set up with two other beans - applicationDescriptor and a lifecycle advisor. ApplicationDescriptor looks very straightforward - a version and a build number. I'm guessing that goes in the title, and perhaps an automated "Help - About" screen later on (here's hoping, anyway :).</p>
<p>The lifecycle advisor looks a little more involved. It appears to be configured with another xml file, which I'll look at in a bit, and a "starting page id" which refers to an "owner manager view". Looking at ApplicationLauncher (again), it appears that on launch a window is opened with this "owner manager view" page displayed first. After that, onPostStartup() is called on the lifecycle advisor. </p>
<p>From this it looks like the lifecycle advisor is used here as the application flow manager. The two methods overridden for the petclinic application look like they create the Setup Wizard and the login screen. I guess that there are many things one could add to this to perform custom actions at various points within the application.</p>
<h3>Look and Feel</h3>
<p>At this point I notice that the JGoodies support I raved about earlier is neatly encapsulated in one bean:</p>
<p>{% highlight xml %}
  <bean id="lookAndFeelConfigurer"
    class="org.springframework.richclient.application.config.JGoodiesLooksConfigurer">
<property name="popupDropShadowEnabled" value="false" />
<property name="theme">
      <bean class="com.jgoodies.looks.plastic.theme.ExperienceBlue"/>
    </property>
  </bean>
{% endhighlight %}</p>
<p>Searching through the Rich Client codebase turns up another magic bean name in ApplicationServices.java:</p>
<p>{% highlight java %}public static final String LOOK_AND_FEEL_CONFIGURER_BEAN_ID = "lookAndFeelConfigurer";{% endhighlight %}</p>
<p>There's a whole lot of other magic bean names in there - if you are wondering what to name a bean, that's a good place to start looking!</p>
<h3>Changing the Setup Wizard</h3>
<p>Most of the rest of the beans I think I'll have to leave for this session, save the last one - the "setupWizard":</p>
<p>{% highlight xml %}
  <bean id="setupWizard"
    class="org.springframework.richclient.application.setup.SetupWizard">
<property name="licenseTextLocation">
      <value>/org/springframework/richclient/samples/petclinic/license.html</value>
    </property>
  </bean>
{% endhighlight %}</p>
<p>If I can modify the wizard to show a "Hello, World!" page, then I'll be happy. </p>
<p>Looking at the code for SetupWizard, I notice that it adds a SetupIntroWizardPage object. This object references a number of messages, including "setup.intro.description". Hah! I remembered that richclient-application-context.xml had some references to "message source" type beans, but rather than work all that stuff out at this stage, I cheat and search the whole source tree for "setup.intro.description". This turns up a reference in petclinic/ui/messages.properties:</p>
<p><code>setup.intro.description=The petclinic sample application
demonstrates the base capabilities  of Spring's Rich Client
Project, built on standard J2SE Swing.</code></p>
<p>Right, time to fulfill the brief:</p>
<p><code>setup.intro.description=Hello, world!  This page shows
that I can trivially change a text file and by making text appear
differently, I can impress my peers without really knowing what I'm
doing.</code></p>
<p>A quick recompile, and here's the result:</p>
<p><img src="/files/spring-richclient-2-1.jpg"/></p>
<p>It's not that impressive, I grant you. But at least it shows that if a Rich Client application is written correctly, you can leverage Spring's built in message support. This is vital for things like localisation.</p>
<h3>Summary</h3>
<p>A quick summary of what we've learnt in this session:</p>
<ul>
<li>To launch a Spring Richclient Application, you use some boilerplate code in a standard main() method to initialise an ApplicationLauncher with some Spring beans XML files.</li>
<li>You may include an optional startup XML file containing one specially named bean for a splash screen.</li>
<li>Many Rich Client specific beans in the XML files are specially named and are probably required to be present. This means I'll most likely copy the Rich Client specific file and modify it, rather than creating from scratch.</li>
<li>Look and feel configuration is trivially handled through a specially named bean in the XML configuration files.</li>
<li>The setup wizard shipped with the Rich Client framework uses standard spring messaging by default, allowing us to trivially customise the text.</li>
</ul>
<p>Next session, we'll look at some those of the other beans in richclient-application-context.xml and work out what on earth they're for. Stay tuned.</p>
