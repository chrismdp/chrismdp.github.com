---
layout: post
title: "Layers of abstraction: writing great cucumber code"
date: 2011-09-15 07:44:41 +0100
categories:
  - bdd
  - cucumber
  - agile
  - ux
---
I blogged about Gojko's thoughts on layers of abstraction [a week or so ago](/2011/09/layers-of-abstraction-bdd-ux), discussing three different ways we can think about the behaviour of any system. These way are: the business rules, the workflow of that system, and the specific activity the user is undertaking.

Today I want to think about how we can leverage these insights to help us write really good cucumber features and step code.

## I used to write terrible features

Do these look familiar?

{% highlight cucumber %}
Feature: Paul pays employees
  In order to retain staff
  As Paul the Payroll Manager I want to pay my staff

Scenario:
  Given an admin user called "Paul" with a password "password"
  And a user called "Bob"
  And "Bob" is an employee
  And "Bob" gets paid "$2,000" a month
  When I visit the homepage
  And I click on "Log in"
  And I fill in "username" with "Paul"
  And I fill in "password" with "password"
  And I click "Log in"
  And I click "Payroll"
  And I click "Bob"
  And I click "Pay"
  And I enter "$2,000"
  And I click "Pay"
  Then I should see "Bob has been paid"
{% endhighlight %}

We've all written features like this in the past: there's [plenty](http://benmabey.com/2008/05/19/imperative-vs-declarative-scenarios-in-user-stories.html) [of](http://dannorth.net/2011/01/31/whose-domain-is-it-anyway/) [guidance](http://elabs.se/blog/15-you-re-cuking-it-wrong) out there these days to help you write better features than this. However, rather than just accept "best practices" at face value, let's take a look under the hood and work out *why this is better.*

## Variance revisited

Last time I discussed this topic, I mentioned the key differentiator was variance. Business rules are unlikely to change significantly unless the company decides to pivot: this is more likely in a startup but still less likely overall. The workflow is normally fairly static, but the activity the user follows changes regularly.

Co-incidentally, there are three levels of behaviour implementation that we write when we work with Cucumber:

* *The feature files.* Ideally there are written in collaboration with the customer and are written out before coding begins.

* *The step definitions.* We implement each step of our feature with ruby code as we are writing the feature, sometimes reworking existing steps to be more powerful (often at our peril).

* *Support code.* Cucumber executes our steps inside a 'world object', which we can easily extend through the adding of modules and methods.

Each of these implementation levels is also differentiated in terms of variance:

* *The feature files are the most difficult to change,* as this ideally requires a conversation with the customer, and any wording changes have a knock on effect on step definitions.

* *Step definitions can be tricky to change,* especially if they are used by multiple feature files. Their implementation is closely tied to the regular expression they match, which can make them difficult to understand if highly reused: one case where Don't Repeat Yourself can fall down quickly.

* *Support code is easy to change* as it's plain ruby and as such very malleable: we can easily refactor and be careful with our naming to tease out duplication.

## Where to put the code?

If it's easy to change support code, then it follows that we should put our higest varying code there: namely the code which describes specific activity. Normally only programmers are interested in this code and it's easy enough to find and understand if the support methods are well-named.

The workflow code lives best in individual steps which aren't often reused and which have simple regular expressions. The people who are interested in this area are normally designers and User Experience people, who should be able to read well-named ruby code at a pinch and therefore can understand what's going on.

The code that's least likely to change (the business rules) can safely live in the feature files with impunity, where it can be discussed with product owners. The product owner is most interested in the rules of their system: they're only moderately interested in the workflow and usually aren't too opiniated about the specific activities. That's partly why we struggle to write features with our clients: if we're trying to discuss activity specifics like in the example feature above, we're probably nailing down details too early and bore our product owner to tears. It's hard enough for a programmer to read these sorts of features: how can we expect anyone else to understand them?

## An example

Given this, how would I refactor the feature above to improve things? After deleting web\_steps.rb, I would rewrite the feature with my customer citing the business rule, rather than any specific workflow:

{% highlight cucumber %}
Feature: Paul pays employees
  In order to retain staff
  As Paul the Payroll Manager I want to pay my staff

@paul_signed_in
Scenario:
  Given an employee called "Bob"
  Then I should be able to pay "Bob" his salary
{% endhighlight %}

My step definitions would look something like this:

{% highlight ruby %}
Given /^an employee called "([^"]+)"$/ do |employee_name|
  create_employee(employee_name)
end

Then /^I should be able to pay "([^"]+)" his salary$/ do |employee_name|
  pay_salary_to(employee_)
end
{% endhighlight %}

And the support code might look roughly like this:

{% highlight ruby %}
Before("paul_signed_in") do
  paul = create_employee("Paul")
  paul.assign_role("payroll")
  sign_in_as(paul)
end

def create_employee(name)
  Employee.create!(:name => name, :username => name,
    :password => "password")
end

def pay_salary_to(name)
  payee = Employee.find_by_name(name)
  visit payroll_employee_path(payee)
  fill_ :salary, :with => payee.salary
  click_button "Pay"
end
{% endhighlight %}

You're also free not to test the UI if you'd prefer not to in your support code. However, as we've given ourselves the ability to remove duplication, it's easy to change the code when the UI changes. So far I've not found UI brittleness to be too much of an issue.

## In conclusion

These are rules of thumb, but they can be very helpful in keeping the rate of development up as our codebase expands. One change that I've made recently to my own practice is to be more aggressive at pushing activity code down into support code, and it's really helped to keep feature code flexible and easy to change.

Many people have given up on Cucumber, citing long build times and the brittleness of the test code as primary reasons. Obie Fernandez recently [blogged](http://blog.obiefernandez.com/content/2011/05/the-dark-side-beckons.html) about finding "high-ceremony" development too much work in a startup. I think that's a real shame: it's a fantastic way to drill down to specific behaviour and ensure you're only building what you need. If you think about the behaviour of your system correctly, aggressively remove duplication in all your code (including test code), and only test code you own then you shouldn't be burdening yourself with too much of an overhead.

Have you given up using Cucumber? Or if you use it, is this the way you do it or do you have a better method?

