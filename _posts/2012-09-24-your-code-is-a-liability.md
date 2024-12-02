---
layout: post
title: Your Code Is A Liability
date: 2024-11-25 20:00:31 +0000
categories:
- code
- agile
- team
- startup
- liability
redirect_from:
- "/2012/09/code-is-a-liability"
- "/2012/09/code-is-a-liability/"
- "/code-is-a-liability/"
- "/code-is-a-liability"
---

Every chunk of code you commit is more for someone else to read, digest and understand.

Every complex “clever” expression requires another few minutes of effort for each of your team. They must now interpret what you wrote and why you wrote it.

Every line you add limits your project’s responsiveness to change.

Your code is a liability. Never forget this.

<!--more-->

## The features are the asset

We need code: it’s a major way we deliver features. The feature is the reason we write the code in the first place.[^1]

The only way to value features is through the code we write to create them. CFOs treat code an as asset, because it is the material connection they have to the feature provided and the business value behind it. It's not the code itself that has value. Counter-intuitively, the more code needed to deliver the value, the less valuable the asset.

If you're a startup, much of your company will not survive contact with customers. The quicker you find out what to remove the better. If you build a whole framework to serve a feature, and it's not needed, you're less likely to delete the feature when it proves superfluous. How much code does your feature really need? What's the simplest smallest version of the feature in front of you that you can learn from?

Thinking of code as a liability puts AI into perspective. It is possible to churn out code using language models and it may have some value. Who decides whether it is providing the feature? We need strong developers to determine this.

Code is a liability, but coders are a clear asset.

## Don't compromise on quality

Developers: don't skip the tests for critical code that's beyond your ability to understand at a glance. That limit is lower that you think. It's even lower for your future self.

As Dave Astels said: "Test where the risk is."

I don't write tests for everything when I'm just figuring out the feature. I rarely test UI directly. UI tests take too long to run and the maintenance is almost never worth it.

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

When we embrace that our code is a liability, everything becomes lighter. Our functionality is set free from heavyweight code drag. It allows our features to soar, responsive to change requests, and easily debugged. There's just not that much code to go through.

---

[^1]: Except when the feature isn't the reason we wrote the code. The allure of a "proper" architecture is real. Fight it. Force every part of your code to directly contribute value now.
