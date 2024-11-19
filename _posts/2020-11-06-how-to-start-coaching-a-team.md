---
layout: post
title: "How To Start Coaching a Tech Team: 10 Questions To Ask"
date: 2025-11-17 00:00:00 +00:00
categories:
- agile
- team management
- coaching
---

Confused? That’s normal. When you’re figuring out the beginning of your tech team’s journey, it’s normal to feel a sense of uncertainty. Maybe you’ve just taken on a brand new team. Whilst there might be lots of activity, you’re unsure if there’s much progress. Perhaps you’ve read [other articles here](https://deliverydoubled.com/category/process/) on tech processes, and you’re not sure if they’re right for this team.

When starting out with a new agile team, how do you know what to do first?

There’s a myth that certain “super agile” consultants know exactly what to improve within minutes of encountering a new team. It’s true that sometimes there are obvious changes to suggest. However, there’s also a lot of listening and understanding to do before it’s sensible to begin making recommendations. (I’d recommend [this Agile Coaching book](https://amzn.to/37xjIO7) to learn more about this process of coaching a team.)

Whenever I walk into an existing agile team, here are ten key questions I ask.

<!--more-->

## How quickly can the team deliver something?

If I asked the team to make a trivial yet non-urgent change to the code, how quickly can they get that into production?

I’ve heard a range of answers to this question. For a high-functioning team, it’s in the order of minutes. The longest answers I’ve heard for a non-hardware product is 6-9 months. In general, if an active project last deployed more than a week ago, [that’s a health warning](https://deliverydoubled.com/deploy-faster-4-ways-your-deployment-is-killing-your-agile-project/).

The metric above is called “[cycle time](https://codeclimate.com/blog/software-engineering-cycle-time/)”. If you’re not measuring it, then to start doing so is a really good idea. If an agile team can make a change fast, they are able to react quickly to anything that might be needed.

## Is the team writing automated tests?

Are there any automated tests checking that the software is still working, giving any change that the team might make?

This is the companion question to the one above. Running automated tests can slow down your ability to deploy code. However, it does allow a team to make changes to the system with confidence, which makes a team more agile.

## Are the *developers* writing automated tests?

In many agile teams, the testing is left to testers. This is normally a bad move. If your Quality Assurance (QA) team are writing automated tests, they often use a bridging technology like [Cucumber](https://cucumber.io/) to write tests in a natural language. If this is the case, the developers should also help with the plumbing to connect Cucumber to the code. However, developers should also be writing their own tests in this circumstance. If not, the team can fail to find problems with stories until right at the end of the development process. This leads to zombie stories that drag on forever.

## Are the team having “real retrospectives”?

A retrospective is a meeting where the team gathers together to discuss and take steps to improve their working practices. I’m not interested if the team is simply doing “Agile Theatre”. I’m looking for something much more dynamic and awkward where people share how they’re really feeling. I want to see concrete actions that come out of them, and things actually changing afterwards.

I’ve written [much more](https://deliverydoubled.com/deliver-faster-boost-teamwork-a-simple-guide-to-development-focus/) about this here along with a guide to [running these remotely](https://deliverydoubled.com/how-to-run-a-remote-retrospective-a-step-by-step-guide/).

## How quickly does QA get involved in a story?

If you have a Quality Assurance (QA) outfit, what’s their primary function? Are they handling stories at the end of a process? Or are they involved at the beginning, thinking of edge cases, analysing the stories as they are created, and wondering where they could go wrong?

In my experience, people normally thought of as testers often make excellent business analysts. I’ve seen hybrid QA/Project/Delivery Managers work well as well, assisting the Product Manager so they can concentrate on the bigger picture.

## Is there a clear product vision and strategy?

> “Be stubborn on the vision, and flexible on the details.” — Jeff Bezos

A key job of senior product management is to set a clear 3-5 year vision for the product. In many places, this is clear at the top of the organisation, but not at all clear within the actual teams. In very few places have I seen a product strategy describing the key problems to [focus on](https://deliverydoubled.com/deliver-faster-boost-teamwork-a-simple-guide-to-development-focus/), and in which order. Most teams have a roadmap (or worse, just a backlog) stuffed with half-finished stories and features. There’s no big picture understanding or plan of why these are here and in which order.

The best voice I’ve come across on product vision is Marty Cagan — I’d strongly recommend all his writings, especially [his INSPIRED book](https://amzn.to/31AGKQj). Read more about his [thoughts on vision vs. strategy](https://svpg.com/vision-vs-strategy/).

## Who decides the details around the product?

It should be the team itself: ideally, a Product Manager is responsible for key decisions, assisted by the whole team or at least the more experienced members. There should be a high level of trust, tolerance for failure, and willingness to iterate on ideas extremely rapidly.

Again, I’d recommend [reading INSPIRED](https://amzn.to/31AGKQj) for more.

## Does the team work well cross-functionally?

Accountability should be structured across disciplines, so all members share the same goals, rather than being siloed by function.

## Does the team use story points?

My facetious response when teams ask about story points is “story points are fine, as long as every story is one point.” My argument is that stories should all be of roughly equal complexity.

## How long do planning meetings take?

Long estimation meetings waste time. Planning should be just-in-time, with rapid experimentation and minimal meetings.

Starting with these questions can reveal the real limiting factors to progress and help focus on what truly matters.
