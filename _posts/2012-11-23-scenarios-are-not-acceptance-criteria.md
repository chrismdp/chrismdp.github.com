---
layout: post
title: Scenarios are not Acceptance Criteria
date: 2012-11-23 08:55:47.000000000 +00:00
categories:
- cucumber
- bdd
- testing
- tdd
redirect_from:
- "/2012/11/scenarios-are-not-acceptance-criteria"
---
<p><i>"That's all very well, but how do I know that it works?"</i></p>

<p><i>"What will that actually look like on screen?"</i></p>

It can be hard to nail down a feature file. Some people like to argue over the wording of the preamble and jump into the scenario writing (much) later. Some prefer to get on with writing concrete examples to help jumpstart their thinking, and frame the story with the acceptance criteria later.

<p><i>"So what's the point of this feature again?"</i></p>

Whichever way we approach writing our feature files, it's important that we iterate over our wording. Let's not neglect either our acceptance criteria, or scenarios detailing concrete example behaviour. Without both, we're making it hard for our developers to implement a feature, and making it hard for us to understand its purpose a few months down the line.

<p><i>"Can you give me an example of that?"</i></p>

It's very easy to conflate the concept of scenarios with acceptance criteria: they aren't the same thing. *Scenarios are concrete examples of acceptance critera:* they help flesh out and explore complex criteria, and ground them in reality. Without concrete examples it can be hard to get a handle on where to start when implementing a feature, and it's difficult to wrap our minds around what needs to be done.

## Lack of acceptance criteria: hesitation and confusion

Here's a feature without acceptance criteria:

{% highlight text %}

    Feature: Relating two people

    Scenario:
      Given a person called Joe
      And a person called Bob
      When I set Joe to be the father of Bob
      Then their relationship is recorded in the system

{% endhighlight %}

When we skip the acceptance criteria and jump straight into examples, we lose context. It's hard to see how and why this feature exists, and who is using it?

Example scenarios aren't good at describing design and user experience constraints on a feature. Developers will be tempted to rush straight through the implementation without paying attention to the detail. They're also no good at communicating the need for other edge cases. Is there something else that we've missed here? What about distinguising between biological and adoptive parents, for instance? Or checks for age to ensure the father could be old enough to have children?

## Lack of concrete example scenarios: haziness and obfuscation

We might be tempted to shoe-horn all that information into the scenario:

{% highlight text %}

    Scenario: Relating two people
      Given a father and two children
      When I relate them either at adoptive or biological parents
      Then the relationship should be recorded
      And the sibling relationships should be worked out
      And we are warned if the father appears too young to have children
      But only if the relationship is biological

{% endhighlight %}

This isn't a real scenario any more. We're trying to describe several different things in one place. It could be implemented as several different scenarios joined together, but by itself the lack of concreteness means that we can't easily reason about it, and it's also nigh on impossible to automate without skipping some of the intent. Using 'Given', 'When' and 'Then' does not automatically make something a concrete example - all this information belongs in the preamble.

## Combining acceptance criteria with real examples

Let's try and combine both these techniques:

{% highlight text %}

    Feature: Relating two people
      As Robert the royal historian, I want to show parent/child relationships
      in my family history system so that I can track royal lineage over many centuries.

      * I should be able to relate people as parent and child very simply and quickly
      * Sibling relationships can be automatically worked out
      * Each person can have biological parents, and adoptive parents
      * Ensure we warn our historian if the father is too young

    Scenario: Relate Joe and Bob as father and son

    Scenario: Bob and Elaine are siblings as Joe is father of both
      Given a person called Joe
      And a person called Bob
      And a person called Elaine
      When I set Joe to be the father of Bob
      And I set Joe to be the father of Elaine
      Then Bob and Elaine are shown as brother and sister

    Scenario: Bill is the adopted father of Elaine and Bob
    Scenario: Charlie is too young to be the father of Joe

{% endhighlight %}

Have a look at the acceptance criteria as listed in the preamble. They state both the reason for the story and they flesh out some more of the thinking. You can often leave the feature like this up until the point I want to work it, with criteria in bullet form. If the feature is complex and there's a danger information will be lost, I'd recommend writing down examples during the planning of the story in order to properly capture the behaviour (like I've done here with the second scenario), but you don't need to do this for every scenario until you come to automate it.

## Summary

Think back on what you have just read. This post would have been hard to understand without the two examples above. Without concrete examples, it's very easy to gloss over content.

Alternatively, if this post had just consisted of the two features above, followed by "Don't do this! Any comments?", our natural reaction would have been one of confusion. Don't do what exactly? And what exactly should we do instead?

Just like a blog post without an example, or a teaching workshop without a practical element, if there's no concrete example then acceptance criteria can lead to wishy-washing thinking. Similarly, if we just sit down and start working on something concrete without any clear context, we'll struggle to see the reasons for doing it and we'll miss edge cases. When you have both, that's when you know you'll understand.

Personally, I tend to the second error: because I can read code, I sometimes fall into the trap of not making my examples concrete enough. Which of these two do you more tend towards?

## Postscript

For more, see [Liz Keogh's post](http://lizkeogh.com/2011/06/20/acceptance-criteria-vs-scenarios/) on this topic from last year. For a slightly different point of view, check out Antony Marcano's thoughts on [scenario oriented acceptance criteria](http://antonymarcano.com/blog/2011/10/scenario-oriented-vs-rules-oriented-acceptance-criteria). Antony argues for using scenario titles as our list of criteria. I find it helpful to keep Scenario titles and Acceptance Criteria separate, as I don't think there is always a clear mapping between the two. One is an evolution of the other, and it's useful even when the scenario titles are written to keep the Acceptance Criteria around for context. What do _you_ think?
