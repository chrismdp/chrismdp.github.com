---
layout: post
title: Spring Richclient ~ Session Eight ~ Such a bind
date: 2006-03-09 09:46:00 +00:00
categories:
  - richclient 
  - java 
  - spring
  - tutorial
---
<div class='notice'><h1>By the way...</h1><p>This content is now pretty old: check <a href='/'>the homepage</a> for the latest.</p></div>
          
<p>Let's look at the binding framework today. I've got an options dialog to write, and it looks like the binding framework could be just the ticket...</p>
<p>For the uninitiated, when we talk about "binding" we mean linking values in a text field on a form to values in our Java class. Essentially we want to turn:</p>
<p>{% highlight java %}
  public class TrafficWarden {
    String name = "Trevor the Traffic Warden";
    String parkingTicketCount = 124023;
  }
{% endhighlight %}</p>
<p>into this:</p>
<p><img src="/files/rcp-8-0.png"></p>
<p>And when the user hits "Save", we want the values in our java object to change.</p>
<p>This is a standard well-defined problem for which there exists a number of solutions. So what does Spring Rich Client give us to aid us in our quest? Let's have a look.</p>
<h2>How do we make a form?</h2>
<p>The first example that comes to mind of a view with fields on it is the "owner properties view" in the petclinic sample. This is shown when we right click an owner:</p>
<p><img src="/files/rcp-8-1.png"></p>
<p>Let's have a look at the code which created this page, from OwnerManagerView.java:</p>
<p>{% highlight java %}
  public void execute() {
    final Owner owner = getSelectedOwner();
    ownerFormModel = FormModelHelper.createCompoundFormModel(owner);
    ownerGeneralForm = new OwnerGeneralForm(FormModelHelper.createChildPageFormModel(ownerFormModel, null));</p>
<p>    compositePage = new TabbedDialogPage("ownerProperties");
    compositePage.addForm(ownerGeneralForm);
    compositePage.addForm(new OwnerAddressForm(FormModelHelper.createChildPageFormModel(ownerFormModel, null)));</p>
<p>    TitledPageApplicationDialog dialog = new TitledPageApplicationDialog(compositePage, getWindowControl()) {
      protected void onAboutToShow() {
        ownerGeneralForm.requestFocusInWindow();
        setEnabled(compositePage.isPageComplete());
      }</p>
<p>      protected boolean onFinish() {
        ownerFormModel.commit();
        clinic.storeOwner(owner);
        ownersTreeModel.nodeChanged(getSelectedOwnerNode());
        return true;
      }
    };
    dialog.showDialog();
  }
{% endhighlight %}</p>
<p>Ok, to create a form, we do the following things:</p>
<ol>
<li>Grab the currently selected Owner.</li>
<li>Create a form model for this Owner. So what's one of those? Turns out that the class has got some documentation - from FormModel.java:
{% highlight text %}
      A form model represents the state and behavior of a form independently from
      the UI used to present the form.
{% endhighlight %}
    Ok, so it's an abstract representation of a form. Fine.</li>
<li>Create an OwnerGeneralForm, passing a "child page" version of the form model. This makes sense - we've got two tabs, one for "General Info" one for "Address". Rich Client seems to links the "child page" FormModel it creates with the main wizard's FormModel.</li>
<li>Do a similar thing for the OwnerAddressForm.</li>
<li>Add both of these forms to a TabbedDialogPage, which I guess does the fancy tab stuff.</li>
<li>Create a new TitledPageApplicationDialog which takes the TabbedDialogPage we created earlier. We override this dialog to provide stuff to do when it closes.</li>
<li>Show the dialog!</li>
</ol>
<p>When we're done with a form, we do the following:</p>
<ol>
<li>"Commit" the form; I guess this allows it to reconstruct our data from the form fields.</li>
<li>Store the updated owner in the clinic.</li>
<li>Signal to the main view that we might have changed something.</li>
</ol>
<p>Ok, so we've seen how to create a new form, and how to extract the data. Let's try one of our own, and see how far we get.</p>
<h2>Having a go at an options dialog</h2>
<p>Ok, first things first - create an options command in commands-context.xml and add it to the edit menu. I was going for the tools menu, but I don't need one for this app, so I'll just call the menu option 'Preferences' and be all 'mac-like' :)</p>
<p>{% highlight xml %}
<bean id="optionsCommand" class="uk.co.myco.myproj.command.OptionsCommand"></p>
<property name="optionsDao"><ref bean="myDao"/></property>
</bean>
...
<bean id="editMenu" class="org.springframework.richclient.command.CommandGroupFactoryBean"></p>
<property name="members">
<list>
      <value>selectAllCommand</value>
      <value>separator</value>
      <ref bean="optionsCommand"/>
    </list>
  </property>
</bean>
{% endhighlight %}</p>
<p>I need a data access object (DAO) wired into the "OptionsCommand", as the command has got to load and save the options from somewhere...</p>
<p>Ok, so we create a new command class in OptionsCommand.java and come to writing doExecuteCommand() (see <a href="/node/17">session seven</a> for details on writing commands). First we need the existing options, and then we need to create a FormModel based on these options, as explained above:</p>
<p>{% highlight java %}
final Options opt = optionsDao.getOptions();
optionsForm = new OptionsForm(FormModelHelper.createFormModel(opt));
{% endhighlight %}</p>
<p>As we're not splitting up the options onto different pages (there are only three for this application!) we don't need any of that compound form model stuff. A simple call to FormModelHelper.createFormModel() is all we need.</p>
<p>We'll come to writing OptionsForm in a minute.</p>
<p>After that, we need a new dialog:</p>
<p>{% highlight java %}
TitledPageApplicationDialog dialog = new TitledPageApplicationDialog(new FormBackedDialogPage(optionsForm), null) {
  protected boolean onFinish() {
    optionsForm.commit();
    optionsDao.storeOptions(opt);
    return true;
  }
};
{% endhighlight %}</p>
<p>This seems straightforward. We create a new TitledPageApplicationDialog, with a FormBackedDialogPage (and therefore our optionsForm) controlling the contents. We override the onFinish() method to 'commit' the form and save the options in the DAO.</p>
<p>Then we show it:</p>
<p>{% highlight java %}
dialog.showDialog();
{% endhighlight %}</p>
<p>...and that's it for OptionsCommand! Easy, huh?</p>
<p>Hang on, you're probably thinking: what about supplying the text to go into this dialog? This is all controlled by the FormModel we supplied, our own OptionsForm. Let's take a look at how that is implemented:</p>
<p>{% highlight java %}
public class OptionsForm extends AbstractForm
{
  public OptionsForm(FormModel model)
  {
    super(model, "optionsForm");
  }</p>
<p>  protected JComponent createFormControl()
  {
    TableFormBuilder builder = new TableFormBuilder(getBindingFactory());
    builder.add("url");
    builder.row();
    builder.add("user");
    builder.row();
    builder.add("password");
    return builder.getForm();
  }
}
{% endhighlight %}</p>
<p>I've shown the whole class, simply to show how short it is. The createFormControl starts up a new builder, adds a "url" field, a "user" field and a "password" field and then spits out a JComponent (the basic Swing GUI object, for the uninitiated). There's not much to creating these FormModels, is there?</p>
<p>Note that a lot of what I've done here is based on convention. The names of the rows given to the form builder are expected to exist as JavaBean properties in the object you pass to the model. For example, when I do this in OptionsCommand:</p>
<p>{% highlight java %}
final Options opt = optionsDao.getOptions();
optionsForm = new OptionsForm(FormModelHelper.createFormModel(opt));
{% endhighlight %}</p>
<p>...the Options object <i>must</i> contain getUrl()/setUrl(), getUser()/setUser(), and getPassword()/setPassword() methods for this to work. I'm a big fan of convention over configuration, it saves a lot of hassle.</p>
<p>How to we get those aforementioned messages to work? In the constructor show above, you pass a string detailing what you want the form to be called (mine is called "optionsForm", although it could easily be called "allyourbasebelongtous" if desired). Then, you simply add message keys to messages.properties based on that key:</p>
<p>{% highlight text %}
optionsForm.title=Options
optionsForm.description=Change options <b>Note:</b> Clicking on 'OK' will save the options.<br />
{% endhighlight %}</p>
<p>Note that you can use basic HTML for formatting. Lovely.</p>
<p>The actual field names are controlled by further message keys in messages.properties, the names of which are simply the names of the JavaBean properties of our Options class:</p>
<p>{% highlight text %}
url.label=The U&amp;rl
user.label=&amp;Username
{% endhighlight %}</p>
<p>(Password already seems to have an internal Spring Rich Client label set up, so I didn't bother adding it)</p>
<p>And... we're done. We're done? Surely not!</p>
<p><img src="/files/rcp-8-2.png"></p>
<p>No, we really are done. That wasn't at all hard, was it? When I first implemented this, after I got it compiling, it actually worked first time, too, which shows how little code I needed to write to make it work; if there was any more than a tiny amount of code to write, I would have made a mistake :)</p>
<p>Regular Swing types are probably thinking: "That's <i>it</i>? There must be some catch!" No, that really is all the coding you have to do to get a bound form up and running in Spring Rich Client; and there's not a GridBagLayout in sight. This framework is rather good, isn't it? :)</p>
<p>Next time, we'll probably look the validation framework to ensure the user actually types in valid values...</p>
