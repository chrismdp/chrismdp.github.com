---
layout: post
title: '"Project velocity is a useless metric." Discuss.'
date: 2013-01-21 15:29:25.000000000 +00:00
categories:
- process
- productivity
- bdd
- feedback
redirect_from:
- "/2013/01/project-velocity-is-a-useless-metric-discuss"
- "/2013/01/project-velocity-is-a-useless-metric-discuss/"
---
{% include callout.html color="#d9edf7" text="Here follows a conversation between myself and Matt Wynne on the merits of the velocity metric on software projects, after picking up on a discussion on Twitter. I've reproduced it here mostly verbatim, in the hope that it gives people some useful insights into velocity, and to show that we don't always agree on everything..." %}

## The conversation

Chris: "Velocity is useless, and at worst leads product people to focus on a number rather than their features. The only thing that is important is *'will this (small) story X be done by Y.'* and the PM saying: *'how confident are you in that?'* and *'what can I do to help you become more confident?'*"

Matt: "So I do disagree with that somewhat. I wouldn't call velocity useless, but it's a signal something is wrong."

Chris: "Ah, ok. Interesting."

Matt: "You can use velocity to build trust, where stakeholders are used to estimates on the scale of months, and slippages on the scale of weeks. Organisations in that kind of a state can benefit from a bit more transparency. It builds trust BUT the need for it shows you that you don't have the trust."

Chris: "I get that it can be used as training wheels. I prefer to count number of shipped features, but that's an equivalent metric. I don't like focusing on a number: I'd prefer to demo running software, rather than aggregate features artificially."

Matt: "Ultimately, almost all the questions like *'when is it going to be done?'* are asked because of a lack of trust."

Chris: "Not all, in my opinion. It's reasonable to ask when something will be done by. Roughly. If you're asking for the right reasons."

Matt: "Yes, sometimes you have fixed dates. What are the right reasons?"

Chris: "External reasons, not internal ones. Like 'the Olympics.'"

Matt: "Right, but why do we need to know whether this little story X will be done by this week, when the Olympics are 6 months away still?"

Chris: "Because sometimes there are external things that depend on little stories. When something is live, the deadlines get smaller and more frequent. External deadlines are sometimes imposed, even for small stories."

Matt Wynne: "Specifically, I'm saying stakeholders tend not to trust: 1) you're working on the highest priority things 2) you're working as hard as you could be. My experience is that when you really get that trust, stakeholders stop asking for estimates."

Matt: "Even with a fixed deadline, the project owners share the responsibility for finding the scope that's possible."

Chris: "My experience on my current project is we hardly ever get asked when something will be done."

Matt: "Perfect."

Chris: "...and velocity is mostly ignored. The general sense of "less stories this week" isn't ignored though, and sensible questions are asked."

Matt: "Aha, so that's another use for velocity: a signal that the team have built up technical debt that's starting to drag them down."

Chris: "Perhaps so. In this case its more likely to be external blockers."

Matt: "Yeah, and there are other better signals for that."

Chris: "I regard the infatuation with the 'numbers' as uselessly reductionistic."

Matt: "Right. This is where it starts to bite. People lose sight of the point of the numbers."

Matt: "(in mock jubilation) *'our velocity was 28.7 this week, up 0.3 from last week!'*"

Chris: "(in response) *'W00t! Let's spend 1.73 hours each next week sorting out technical debt. My spreadsheet tells us we're allowed to!'*"

Chris: "If you're going to track anything, track cycle time. But do it informally even so."

Matt: "Have I convinced you yet that velocity isn't useless?"

Chris: "No. Well... velocity is a loaded term."

Matt: "Points / week."

Chris: "Useless. Shipped features a week == useful training wheels."

Matt: "Ah ok."

Chris: "I can't be bothered to explain points to stakeholders; they don't care."

Matt: "So that's my thing: 1 story = 1 point. You can't have it any other way: then all your stories have to be small if you want a fast velocity! It's a game..."

Chris: "Fine. I like that game. Substitute 'story' for 'point' everwhere and I'm happy. List the features you delivered to stakeholders, not the points."

Matt: "So take a team who are already doing all of the scrum dances. What are you going to change first?"

Chris: "Yeah, I can see using that as a transition exercise. I'm being idealistic, of course. It's not how you'd transition a team. Change things slowly and get buy in everywhere for apparently superfluous changes."

Matt: "I have watched 8 people spend a whole morning fretting over estimating stories, then they spent another half day estimating all the tasks in hours."

Chris: "Oh yeah, I used to do that."

Matt: "Me too. I wrote [this post](http://blog.mattwynne.net/2010/07/11/hi-fidelity-project-management/) basically for that team."

Matt: "Oh, and here's something else I wrote on [BDD and velocity](http://blog.mattwynne.net/2011/09/17/using-bdd-scenarios-to-track-project-velocity/), too."

Chris: "(After reading the posts) Good articles. I like the idea of countings scenarios not points. I don't consider CFDs ([Cumulative Flow Diagrams](http://en.wikipedia.org/wiki/Cumulative_flow_diagram)) to have no value. The value is same as Kanban - it lies in in identifying blockages."

Matt: "The nice thing (about CFDs) is you can see how your flow is changing over time. A kanban board is just a snapshot."

Chris: "True. It's the same learning though. A CFD will show your learning history, which is useful for seperate reasons."

## The verdict

True to all good conversations, this one ended with me having a slightly different point of view to the one I came in with:

**Velocity isn't entirely useless.** Matt's game of "1 story = 1 point" will help a team to make a move away from an overreliance on a Big Agile approach, where a meaningless metric might hold sway over a common sense look at what's really going on inside a team.

Showing stakeholders a velocity metric each week to two helps to build trust in an organisation that's used to disappointment. However, an excessive thirst for these numbers from the business shows that a team has some way to go to earn that trust.

Finally, there's nothing quite like shipping working software to gain people's confidence. I prefer to provide a bulleted list of the new things that have been added, as opposed to wasting time over-analysing and reducing the week's changes into one potentially misleading number.

What's your opinion? Do you favour the velocity metric, or is it something you can do without?
