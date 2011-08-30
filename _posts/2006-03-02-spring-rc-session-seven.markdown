---
layout: post
title: Spring Richclient ~ Session Seven ~ Beating the Command Framework into Submission
date: 2006-03-02 17:12:00 +00:00
categories:
  - richclient 
  - java 
  - spring
  - tutorial
---
<div class='notice'><h1>By the way...</h1><p>This content is now pretty old: check <a href='/'>the homepage</a> for the latest.</p></div>
          
<p>There's been a bit of a gap between the last session and this one; mostly because I've been actually doing coding rather than just writing about coding. It's always worth actually doing a bit of coding once in a while; it's quite fun really, and as I also happen to like eating most days (as does my family), some real work is necessary from time to time...</p>
<p>Anyhow, I apologise for the delay. On with our journey.</p>
<p>We left off last time looking at the ownerManagerView, and seeing how that was put together. I promised at the end or that session to look at the command framework next, and try and work it out. So here goes.</p>
<h2>"Scalpal, please"</h2>
<p>Let's dissect the OwnerManagerView command code into its component pieces and see what it's made of. It looks like the OwnerManagerView creates a bunch of "command executors", which define what actually happens when a command is executed by the user. There's a lot of different executors in the OwnerManagerView class. Rather than trying to understand them all at once and fry my brain, I think that the best thing to do would be to head through a custom command called "new owner", and try to understand how it's created and what it does.</p>
<h3>How does "new owner" work?</h3>
<p>Right, time to find the new owner command. It turns out that it's defined in commands-context.xml. This useful little file maps various different command locations (menus, toolbars, that sort of thing) to actual commands that do stuff. Let's look for the new owner command - it's in there:</p>
<p>{% highlight xml %}
  <bean id="newOwnerCommand"
    class="org.springframework.richclient.command.TargetableActionCommand"></p>
<property name="commandExecutor">
      <ref bean="newOwnerWizard"/>
    </property>
  </bean>
{% endhighlight %}</p>
<p>It's referenced by the "new menu", which is turn is referenced from the toolbar and the file menu. Neat.</p>
<p>So what does the command actually do? It runs the executor "newOwnerWizard". This bean is defined rather simply in the richclient-application-context.xml file:</p>
<p>{% highlight xml %}
  <bean id="newOwnerWizard"
	class="org.springframework.richclient.samples.petclinic.ui.NewOwnerWizard"></p>
<property name="clinic">
      <ref bean="clinic"/>
    </property>
  </bean>
{% endhighlight %}</p>
<p>Ok, so when you click on "new owner" you get a wizard up (this manifests as a little boxes with some blank fields to fill in). You enter a bunch of information, and when this is finished, this bangs an event over to the main owner view using spring's built-in ApplicationEvent stuff:</p>
<p>{% highlight java %}
 protected boolean onFinish() {
   Owner newOwner = (Owner)getNewOwner();
   clinic.storeOwner(newOwner);
   getApplicationContext().publishEvent(
     new LifecycleApplicationEvent(LifecycleApplicationEvent.CREATED, newOwner));
   return true;
 }
{% endhighlight %}</p>
<p>(code taken from NewOwnerWizard.java)</p>
<p>The owner view handles this message, tweaks the tree and redraws based on the new owner:</p>
<p>{% highlight java %}
public void onApplicationEvent(ApplicationEvent e) {
  if (e instanceof LifecycleApplicationEvent) {
    LifecycleApplicationEvent le = (LifecycleApplicationEvent)e;
    if (le.getEventType() == LifecycleApplicationEvent.CREATED &amp;& le.objectIs(Owner.class)) {
      if (ownersTree != null) {
        DefaultMutableTreeNode root = (DefaultMutableTreeNode)ownersTreeModel.getRoot();
        root.add(new DefaultMutableTreeNode(le.getObject()));
        ownersTreeModel.nodeStructureChanged(root);
      }
    }
  }
}
{% endhighlight %}</p>
<p>(code from OwnerManagerView.java)</p>
<p>Ok, I followed that (I think). Let's try and do a similar thing for the application I'm writing.</p>
<h2>The File List View</h2>
<p>I have a main pane which shows a list of files in a directory, called FileListView. I want to have a button which when clicked opens a JFileChooser and returns a directory. This then refreshes my view. Easy enough, you might be thinking. It turned out to be rather tricky unfortunately...</p>
<h3>Approach One - fire an event to the application context</h3>
<p>Ok, so I thought I'd set up my command like this:</p>
<p>{% highlight xml %}
  <bean id="openFolderCommand"
        class="uk.co.mintcontent.uploader.command.OpenFolderCommand"/>
{% endhighlight %}</p>
<p>This is a tiny bit of java classage that handles the file dialog (OpenFolderCommand.java):</p>
<p>{% highlight java %}
public void doExecuteCommand()
{
  final JFileChooser fc = new JFileChooser();
  fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
  int returnVal = fc.showOpenDialog(null);
  if(returnVal == JFileChooser.APPROVE_OPTION) {
    applicationContext.publishEvent(new FolderSelectedApplicationEvent(fc.getSelectedFile()));
  }
}
{% endhighlight %}</p>
<p>FolderSelectedApplicationEvent is my own application event to tell us that a new folder is selected.</p>
<p>Ok, so in FileListView, I need this:</p>
<p>{% highlight java %}
public void onApplicationEvent(ApplicationEvent e)
{
  if (e instanceof FolderSelectedApplicationEvent)
  {
    FolderSelectedApplicationEvent fs = (FolderSelectedApplicationEvent)e;
    directory = fs.getDirectory();
    drawFileList();
  }
}
{% endhighlight %}</p>
<p>Done... right?</p>
<p>Wrong, unfortunately. The problem is that event fires in the application context defined by commands-context.xml, not the main application context defined by richclient-application-context.xml, so I can't talk to the window. What do I do? I do what all experienced and knowledgable techs do: panic and turn to google for help...</p>
<h3>Approach Two - Move command to main application context</h3>
<p>Luckily someone aeons ago (well, 2004) <a href="http://forum.springframework.org/archive/index.php/t-11599.html">had the same problem</a> and was smart enough to post to the Spring forums about it. The law of <a href="#" title="When All Else Fails, Boot Up Google" style="border-bottom:1px dotted">WAEFBUG</a> is proved right again!</p>
<p>Ok, so based on that thread, I now know that A) this stuff should be clearer, and B) I can try moving my command to the main application context. This I do, but now it doesn't show the icons on the toolbar button correctly :( Rather than try and work out why that's the case, let's try another approach...</p>
<h3>Approach Three - TargetableActionCommand</h3>
<p>Let's do what petclinic appears to do and use a TargetableActionCommand. <a href="http://www.ditchnet.org/wp/2005/06/05/remedial-spring-rcp-episode-2-targetableactioncommands-and-the-edt/">This blog post</a> helped me out setting one of these up.</p>
<p>So here's the latest definition of the command:</p>
<p>{% highlight xml %}
  <bean id="openFolderCommand"
	class="org.springframework.richclient.command.TargetableActionCommand"></p>
<property name="commandExecutor">
      <ref bean="fileListView"/>
    </property>
  </bean>
{% endhighlight %}</p>
<p>This unfortunately didn't work. I can't wire into the fileListView as it's wrapped up inside a view descriptor object:</p>
<p>{% highlight xml %}
  <bean id="fileListView"
        class="org.springframework.richclient.application.support.DefaultViewDescriptor"></p>
<property name="viewClass">
    <value>uk.co.mintcontent.uploader.ui.FileListView</value>
  </property>
{% endhighlight %}</p>
<p>I don't want to write some sort of proxy object to handle this in the main application context either - that seems overkill.</p>
<h3>Approach Four - Cheat (sort of)</h3>
<p>Aha - what about this?</p>
<p>{% highlight java %}
  applicationContext.getParent().publishEvent(
    new FolderSelectedApplicationEvent(fc.getSelectedFile()));
{% endhighlight %}</p>
<p>Let's just use the method described in "Approach One", except we'll fire the event at the parent context of the current application context, which just happens to be the main context. This might be cheating, but it works, and I've got a deadline looming.</p>
<h2>Summary</h2>
<p>Whew! Got there in the end. Here's a summary of the way I did this:</p>
<ol>
<li>Define a new command bean "openFolderCommand" in the command context.</li>
<li>Code OpenFolderCommand, extending ActionCommand, and implementing the ApplicationContextAware interface to get the application context. Code it so that it opens the JFileChooser and fires a FolderSelectedApplicationEvent event at the <b>parent</b> context of its own context.</li>
<li>Code the FolderSelectedApplicationEvent, which takes a File so we know which directory we picked.</li>
<li>Handle the event in FileListView.</li>
</ol>
<p>I'm sure there's a better and more Richclient-ish way to do much of this. If you know of one, please let me know!</p>
<p>Next session, I'll probably be looking at either the Master/Detail stuff, or perhaps getting my app onto Java Web Start successfully.</p>
