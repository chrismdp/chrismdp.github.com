---
layout: post
title: 'Layers of abstraction: combining BDD and UX'
date: 2011-09-05 20:44:03.000000000 +01:00
categories:
- bdd
- cucumber
- agile
- ux
redirect_from:
- "/2011/09/layers-of-abstraction-bdd-ux"
---
I first came across [Gokjo Adzic's thoughts on the different levels of UI test automation](http://gojko.net/2010/04/13/how-to-implement-ui-testing-without-shooting-yourself-in-the-foot-2/) some time ago: it's a really nice way to think not just about test automation, but about the different levels of behaviour in any software project.

I've been considering the similarities between these levels of behaviour and the user experience discipline, and how we might leverage that thinking to iterate towards a better way of combining agile methods with UX.

## Three ways to think of behaviour

Applying these rules to any software system gives us three ways to think about the behaviour of that system.

*The business rules.* These are high level and abstract. To take the example of a Payroll system: the business rules represent such things as "Staff members always get paid on the last Friday of the month", or "Temporary staff workers must submit a timesheet before being paid."

*The workflow.* The workflow represents the logical steps a user might go through to fulfil a business rule. For example: "As a HR person, I want to see a list of temporary workers and pay those who are shown to have submitted a timesheet."

*The specific activity.* The detailed steps a user goes through to achieve the workflow: "I click on the 'show temp workers' link; I see an icon next to those who have submitted timesheets, along with the last date they submitted; I click the 'Pay' button..."

The key differentiator here is *variance.* The business rules of a system are the least likely to change: changing these might represent a [pivot](http://venturebeat.com/2010/04/14/business-plan-not-working-time-to-pivot/) and will incur significant development cost.

The specific activities change most often: perhaps at a designer's whim, or through localisation or other text changes. We should therefore strive to ensure that changing the activities incurs as small a development cost as possible.

## The agile / user experience process is similar

If you think about it, the three layers represent the different and progressive stages of thinking that we go through when designing the user experience of new applications.

*Business rules of the system are laid down by the product owner at the start of a project.* When considering the user experience of the application, we are careful to first understand a high level overview of the purpose of the software, getting as much useful information as possible from the product owner at an inception.

*Workflow design is led by the UX team and happens when a new story is created.* When creating a new slice of functionality, we carefully think through the workflow of that particular feature, using wireframing, [personas](/2011/04/cucumbers-with-personality) or [whatever works](/2010/02/the-story-card-is-not-the-story) combined with [lots of discussion](/2010/02/the-story-card-is-not-the-story). The net result is a basic step by step workflow of the new feature, without too much detail added.

*Specific activities are created by developers and graphic designers.* Developers and designers make a thousand little decisions about the user experience of the application as they build the feature, hopefully discussing their thoughts with the UX experts on their team if they feel out of their depth.

## From general to specific

As we create features, we are iterating from the general to the specific; from the high level to the detail. To determine all the granular behaviour up front (and all the precise graphical designs) is inefficient: we are likely to change our minds about the detail. Yet this is what many user experience practioners and designers try to do: if not for the whole project, then for whole sections of the project.

For example, if you're doing more than a dozen wireframes or so in advance, are you doing too much thinking ahead of time? Why not resist, have more agility, and let the completion of some of the features guide your future thinking? Likewise, I have often been presented with dozens of perfect photoshop mockups to code up, often without any clear direction on the behaviour represented within them. It is more agile to keep things as high level as possible for as long as possible. How about producing a guidance mockup and a style guide, and then sitting down and guiding the developers on the design when they come to build the feature?

This doesn't mean you can avoid the detail. You need both ends of the behaviour spectrum: neglect the detail of the experience and you [settle for mediocrity](/2010/05/ux-is-everything). Conversly if we neglect the high level our application becomes a ship without a rudder and the user experience will become confused.

In the future I plan to discuss how the use of [Cucumber](http://cukes.info) fits in to this, and how we can progressively iterate our cucumber features as we get more and more specific about a particular feature.
