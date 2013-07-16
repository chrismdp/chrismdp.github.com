---
layout: post
title: Spring Richclient ~ Session Six ~ The View
date: 2006-02-10 10:07:00 +00:00
categories:
  - richclient 
  - java 
  - spring
  - tutorial
---
<div class='alert'><h1>By the way...</h1><p>This content is now pretty old: check <a href='/'>the homepage</a> for the latest.</p></div>
<p>In this session we will look at the ownerManagerView and its associated descriptor. This is the bit which displays the tree view on the "Owner Manager" screen of the Petclinic sample application. Looks like the author got the bean name right :) (What's the hardest problem in computer science? It's naming a class well, so that the next coder can understand what the class does. Believe it).</p>
<p>Ok, let's have a look at the view descriptor and see how one of those is defined.</p>
<p>{% highlight xml %}
<bean id="ownerManagerView"
	class="org.springframework.richclient.application.support.DefaultViewDescriptor">
<property name="viewClass">
		<value>org.springframework.richclient.samples.petclinic.ui.OwnerManagerView</value>
	</property>
<property name="viewProperties">
		<map>
			<entry key="clinic">
				<ref bean="clinic"/>
			</entry>
		</map>
	</property>
</bean>
{% endhighlight %}</p>
<p>This is fairly straightforward - a descriptor has a class name to instantiate, and what looks like a list of properties to apply to that class on creation. </p>
<p>The view is created by the descriptor, using the createView() method. This, amongst other things, adds the view to the 'ApplicationEventMulticaster' (defined in richclient-application-context.xml) if the view of type ApplicationListener. I guess this is so the view can get messages from the outside world if necessary. So far, so good.</p>
<p>So what does this view look like: The main window looks like this, with the ownerManagerView defined in the centre:</p>
<p><img src="/files/rcp-6-1.jpg"></p>
<p>Let's see how we define each segment of this view.</p>
<h3>View Caption</h3>
<p>AbstractView contains a bunch of accessor methods (that's a fancy word for a 'get' method, in case you weren't aware) to define things like caption, description, display name etc. These are mostly got from the descriptor class. In this case, our descriptor doesn't appear to define them - perhaps it uses defaults. Let's skip a few steps and cheat: We'll search for the caption text and see what we come up with.</p>
<p><code>messages.properties: ownerManagerView.label=&amp;Owner Manager</code></p>
<p>Aha. Our old friend messages.properties. Let's see what happens if we change this.</p>
<p><code>messages.properties: ownerManagerView.label=&amp;Chris' Owner Manager</code></p>
<p>Sure enough:</p>
<p><img src="/files/rcp-6-2.jpg"> <img src="/files/rcp-6-3.jpg"></p>
<p>Looks like to define a caption name, it looks like you define the "&lt;viewName&gt;.label" message. And even better, you can define the name in one place and it's changed across the whole application, including in the menus. Neat.</p>
<p>I'm guessing the icon and other text options are defined in the same way.</p>
<h3>Laying out the view</h3>
<p>The OwnerManagerView derives from AbstractView. Poking through AbstractView, we find the following:</p>
<p>{% highlight java %}protected abstract JComponent createControl();{% endhighlight %}</p>
<p>Ok, so that looks like the method that's called when the view needs to be created. How does OwnerManagerView define this?</p>
<p>{% highlight java %}
protected JComponent createControl() {
   JPanel view = new JPanel(new BorderLayout());
        createOwnerManagerTree();
        JScrollPane sp = new JScrollPane(ownersTree);
        view.add(sp, BorderLayout.CENTER);
        return view;
    }
{% endhighlight %}</p>
<p>Ok, we're in standard Java Swing territory here. First we create a shiny new panel, with a simple layout. We create the owner manager tree, a new scroll pane to hold it, and then add the scroll pane to the panel.</p>
<h3>The Tree</h3>
<p>The createOwnerManagerTree() method is fairly straightforward Java Swing component construction also, except that there are a number of utility classes and interfaces built into Spring Rich Client which help you out. The FocusableTreeCellRenderer class, for example, makes the tree cells work a little more like windows trees (therefore, how people expect them to work, for better or worse). Choosing what to display in each tree cell is standard Swing API legwork, except that Spring Rich Client makes it easy to pick an icon - see this snippet from the custom treeCellRenderer:</p>
<p>{% highlight java %}this.setIcon(getIconSource().getIcon("owner.bullet"));{% endhighlight %}</p>
<p>That refers to our plumbed in icon source bean, which we looked at in <a href="/node/11">Session Four</a>. Let's be mischievous and change this icon to the spring logo, and see what happens:</p>
<p><code>owner.bullet=spring-logo.gif</code></p>
<p>This is what we get:</p>
<p><img src="/files/rcp-6-4.jpg"> </p>
<p>Hmm - that doesn't look like the spring logo... But hang on, what's that on standard output?</p>
<p><code>WARNING: Unable to load image resource at 'class path resource [images/spring-logo.gif]';
returning the broken image indicator.</code></p>
<p>Oops. Looks like I typed the name incorrectly. Let's try:</p>
<p><code>owner.bullet=spring-logo.png</code></p>
<p><img src="/files/rcp-6-5.jpg"> </p>
<p>That's better. It's looks awful, but that's what you get for sticking so large an image on a tree cell. I'm surprised it worked at all, actually :)</p>
<h3>Tree Events</h3>
<p>How do we handle events generated by this tree? Check out this cool Spring Rich Client utility class, TreeStatusBarUpdater:</p>
<p>{% highlight java %}
  ownersTree.addTreeSelectionListener(new TreeStatusBarUpdater(getStatusBar()) {
    public String getSelectedObjectName() {
      Owner selectedOwner = getSelectedOwner();
      if (selectedOwner != null) {
        return selectedOwner.getFirstName() + " " + selectedOwner.getLastName();
      }
      else {
        return "Owners";
      }
    }
  });
{% endhighlight %}</p>
<p>When we select a new node, this inline class allows us to easily supply a String to update the status bar with. That's really neat.</p>
<p>Similar utilities exist for the mouse listeners:</p>
<p>{% highlight java %}
  ownersTree.addMouseListener(new PopupMenuMouseListener() {
    protected boolean onAboutToShow(MouseEvent e) {
      return !isRootOrNothingSelected();
    }</p>
<p>    protected JPopupMenu getPopupMenu() {
      return getSelectedOwner() != null ? createOwnerPopupContextMenu() : createPetPopupContextMenu();
    }
  });
{% endhighlight %}</p>
<p>All you do is define whether or not to show the popup, and which menu to show if you do. Creating Java's Swing components in Spring Rich Client seems to be a breeze...</p>
<h3>Summary</h3>
<p>This session, we learned how to create and lay out views in Spring Rich Client. We looked at the view descriptor and how it uses default labels to display captions and icons. We saw how easy it is to create tree components that feel 'right', and we oohed at the really useful utility classes Spring Rich Client provides to lay out controls and handle events.</p>
<p>Next time, let's have a look at all those commands and executors we've seen inside the OwnerManagerView.java, and try to work all that out.</p>
          
