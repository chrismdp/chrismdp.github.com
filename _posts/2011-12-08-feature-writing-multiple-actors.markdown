---
layout: post
title: "Feature writing: multiple actors"
date: 2011-12-08 11:01:23 +0000
categories:
  - bdd
  - cucumber
  - code
---
I've [written a fair amount](/tag/cucumber) in the past about Cucumber and the way I like to structure my features. After reading these through, someone recently asked me about a particular workflow concerning multiple actors.

They were starting from the following feature file:

{% highlight cucumber %}
Feature: Complimentary Accounts

Scenario: Creating a complimentary account
  Given I am signed-in to the admin area
  When I create a new complimintary account with these details:
    | Name  | John Smith           |
    | Email | john.smith@gmail.com |
  Then a welcome email should be sent to 'john.smith@gmail.com'

Scenario: Receiving a welcome email
  Given I have received a welcome email
  When I follow the link
  Then I should see a welcome page
  And I should be signed-in
  And I should see the details of my account
  And I should be able to set my password
{% endhighlight %}

The concern was that the feature had more than one actor involved: there was the administrator creating the complimentary account, and the recipient of that account. The feature as written just didn't feel right to them: it's not clear who the actors are from the text, although the feature has a certain workflow. Also the check that recipient can set the password is an important one, but isn't clearly called out in the feature.

How could this be written differently?

## Setting the scene

The first thing I noticed is that the feature is missing a preamble. People often leave these out, but I find them invaluable to set the context of the feature and to ensure there's a point to adding the feature at all.

To write the scenarios, I would approach this from the point of view of the personas involved, who I would [normally give names](/2011/04/cucumbers-with-personality). In this case there are two obvious personas: Angie the Administrator, and Victor the VIP. There's a more subtle role at play here too: It's unlikely that Angie decides who gets a complimentary accoun. Therefore we also have the particular stakeholder who wants this feature, who we will call Buster the Business Development Director.

This is how I'd structure the "non-executing" part of the feature:

{% highlight cucumber %}
Feature: Complimentary Accounts
  In order to cater for certain special people that promote our
    company in other ways
  As Buster the Business development director
  I want the ability to ask Angie the Administrator to create
    special free accounts for special people

  Scenario: Angie creates a complimentary account
    ..
  Scenario: Victor receives a welcome email
    ..
  Scenario: Victor can change his password
    ..
{% endhighlight %}

I'd check this with the customer too, just to make sure it made sense. If the password changing is important to them, I'd make that a separate scenario.

## Writing the scenarios

I keep my [scenarios really short](/2011/09/layers-of-abstraction-writing-great-cucumber-code). So I'd try and push some of these details down into steps. Let's take the scenarios in turn:

{% highlight cucumber %}
@angie
Scenario: Angie creates a complimentary account
  When I create a new complimintary account for Victor
  Then a welcome email should be sent to Victor
{% endhighlight %}

The `@angie` tag just ensures that Angie is signed in. It's neater than a separate `Given` step in my opinion. I don't include specifics such as email addresses: it's just noise.

{% highlight cucumber %}
@victor
Scenario: Victor receives a welcome email
  Given I have received a welcome email
  When I follow the link
  Then I am logged straight into my account
{% endhighlight %}

The fact that we've switched actor here isn't a problem in my view. It's still clear who "I" is in this case, because the scenario title is clear and descriptive.

{% highlight cucumber %}
@victor
Scenario: Victor receives a welcome email
  Given I have received a welcome email
  When I follow the link
  Then I can change my password from the first screen
{% endhighlight %}

This is a very similar scenario, but it's worth making it a separate one as the password change is an important business need for the customer. It's very tempting to tag the check onto the end of a previous scenario, but this reduces clarity and the perceived importance of that particular part of the feature in everybody's mind.

Feature files are [bookmarks for conversation](/2010/02/the-story-card-is-not-the-story) in just the same way that other agile tracking methods are. If they don't accurate represent the shared thinking, they're worse than useless.

## Get the customer input

I'm not sure if this feature had originally been run past the customer, but this point is so important that it's worth restating anyway:

*If you're not showing the customer the feature files you're missing out on 90% of the value of Cucumber.*

I'm still sometimes guilty of not doing this. I feel like I must have covered every detail and that discussing it with a customer is a waste of time, but I can't remember ever showing a feature file to a customer where we didn't change the feature to make it better. There's always some ambiguity you [can drive out](/2010/01/driving-out-feature-ambiguity).

<p><i>Have you got any feature files you'd like some input on? Send them over and I'll do my best to give some insight if I can.</i></p>

