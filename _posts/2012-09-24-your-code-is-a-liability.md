---
layout: post
title: Your code is a liability
date: 2024-11-25 20:00:31 +0000
categories:
- code
- craftsmanship
- lean
- agile
- team
- liability
redirect_from:
- "/2012/09/code-is-a-liability"
- "/2012/09/code-is-a-liability/"
- "/code-is-a-liability/"
- "/code-is-a-liability"
---

Every line of code you commit is more for someone else to read, digest and understand.

Every complex “clever” regular expression requires another few minutes of effort for each of your team. They must now interpreting what you wrote and why you wrote it.

Every line you add limits your project’s responsiveness to change.

Your code is a liability. Never forget this.

<!--more-->

## Only the features are an asset

We need code: it’s a major way we deliver features. But how much code do our features really need?

The more that we can reduce the amount of code we write, without reducing the value by the same amount, the more lightweight and agile the result. The smaller our codebase, the easier it is to understand.

## Write code in conversation

If you have a team to talk to, try this: rather than diving in to coding your next feature, have a discussion.

Talk about different ways to achieve the same thing. Argue about the architecture and the arrangement of the different concepts you’re planning. Write down a spec of the work you're attemping and have the team critique it.

Zone in on the simplest and lightest code structure you can find. Solutions developed with others will always be better than us implementing our own ideas in isolation at a ridiculous rate.

The simplest form of code in conversation is is pairing. Every line of code we write when pairing is scrutinised by our partner. If it doesn’t make sense, or shouldn’t be there, they can let us know straight away.

## Remove code wherever possible

The best pull requests are the ones that remove more code than they add.

If we spot a duplicated concept or idea, it often makes sense to remove it there and then. I normally do this as a standalone change, so that it’s obvious that the change has nothing to do with what I’m working on.

This is not "Don't repeat yourself". Often code is removed too early, before you know what the abstraction is. Solve the problem in front of you.

## Don’t write any code at all

Can we solve this problem with a high quality library, or API? Are we able to reconfigure an existing module to make it do what we need? Can we buy in a solution that is good enough for what our business requires?

Avoiding writing code at all is especially important when we’re navigating a new complex idea. Plenty of times we’re not exactly sure how the feature we’re working on will evolve yet. The fewer lines of code we write, the better chance we have of changing the feature later into what we discover it actually needs to do.

When we embrace that our code is a liability, everything becomes lighter. Our functionality is set free from heavyweight code drag. It allows our features to soar, responsive to change requests, and easily debugged - there's just not that much code to go through.
