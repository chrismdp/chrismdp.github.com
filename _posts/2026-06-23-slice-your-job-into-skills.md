---
layout: post
title: "Slice Your Job Into Skills"
permalink: /slice-your-job-into-skills/
date: 2026-06-23 07:00:00 +0000
series: "Claude Code for Leaders"
categories:
  - ai
  - productivity
  - leadership
image: /assets/img/ai-and-your-org-chart.jpg
image_portrait: true
infographic: /assets/img/which-slices-become-skills.jpg
published: true
---

Ask most people how they feel about AI and the answer is worry, not excitement. A recent Pew poll found that only 16 percent of Americans think AI will have a positive impact on society, while almost a third expect it to harm them personally, even as more people use AI chatbots than ever before.[^pew] The more people use it, the less they seem to trust it.

Underneath a lot of that worry is the fear of replacement, that one day the whole job is handed to a machine. It does not need to work that way.

AI comes for the boring slices of your work, not the whole job, and the people who do well with it are the ones who learn to make it work for them rather than waiting to find out what it does to their work.

This post is about how you do that: how to slice your own work into small, repeatable skills, and then invoke them when you need them.

<!--more-->

## Slices, not jobs

In the [first part of this series](https://chrismdp.com/build-an-ai-knowledge-base-from-scratch/) you set up a folder and gave Claude somewhere to think. In the [second](https://chrismdp.com/what-to-put-in-your-ai-knowledge-base/) you fed it with the things you read, record, and decide. This part is about handing it work: not all of your work, and not your judgement, but the small recurring slices that quietly eat your week.

The idea that machines take over tasks rather than whole jobs is not new, and economists have made the point for years.[^tasks] What is new is that you can now do the carving yourself, from your own desk, without a transformation programme or a vendor beyond your favourite AI tool.

You simply identify a recurring piece of your week, break that slice out, and work with your AI to specify it in a skill.

When AI takes slices rather than roles, the org chart does not empty out with wholesale replacements. The same people can take on more work. People keep the slices that need them and pick up new ones from elsewhere. The business grows and is able to breathe.[^recombine]

## Pay attention to your work

It is quite easy to teach the AI to do the task itself - you can just talk to Claude about it! It is quite a bit harder to figure out the right kind of slice to give the AI in the first place.

Most of what we call our "job" is actually a bundle of smaller tasks tangled together, some very dull, and a lot requiring just a little human input at random points. "Give it to AI" fails when the bundle is still a tangle. The decomposition of a portfolio of work has always been a managerial skill - now everyone needs to learn it.

To get started **simply pay attention to the work you are doing.** Do not plan out or second guess slices in advance. Do the work by hand a few times with Claude alongside you, then ask it about the steps you just took. Some steps turn out to be you following a rule, and some are you stopping to make a judgement.

Every one of my own agents began as a slice I caught myself repeating. I was reconciling the same finance numbers each morning, so that became Charles. The product analytics I kept pulling by hand for [Airskills](https://airskills.ai){:target="_blank"} became Ari, the first pass over each incoming [sales enquiry](/services) became Bobby, and the watch on my content calendar became Maggie. None of it started as a plan. I noticed the repetition, wrote down how I did it, and handed that slice over.

If you run an engineering team, the slices are in plain sight: the pull-request description you keep rewriting, the first pass over a code review, the weekly on-call summary. Each one is a slice long before it is a skill.

## Think before delegating

{% include inline-image.html src="/assets/img/how-to-delegate-tasks-to-ai.jpg" alt="A hand-drawn 2x2 for deciding what to give AI, by how much consistency and how much competence the work needs. High-consistency, lower-competence work is where to invest in AI; high-competence high-consistency work stays with people for now; low-value work is dropped; your edge is talented people amplified by AI." align="right" width="50%" link="https://chrismdp.com/ai-is-consistently-mediocre/" %}

Now talk to Claude about the work you have done. Can that judgement be reliably made by AI, or do you need to keep it? If you're not sure, the infographic on the right shows how I think about it, drawn from my post on why [AI is consistently mediocre](https://chrismdp.com/ai-is-consistently-mediocre/) and why that is exactly what makes it useful.

In [my post on line-managing AI](https://chrismdp.com/ai-must-be-line-managed/) I called this finding the decision point: a simple decision you make all the time, the one you would never normally hand to a computer because it needs just a little nuance. That is the stuff to give the AI.

Figure out if this slice will come round again, or was it a one-off? (Most work repeats in some form.) And is the slice properly mechanical, or does it need your taste and your name on it?

{% include inline-image.html src="/assets/img/which-slices-become-skills.jpg" alt="A grid for sorting slices of work along two axes: how often the slice recurs, and how much judgement it needs. Recurring and mechanical slices become skills. Recurring work that needs judgement keeps you at the boundary. One-off mechanical work is just a chat. One-off work that needs judgement you do yourself." %}

The slice you want is recurring and mechanical, the top left of the grid. It happens often enough to be worth the effort, and it is clear enough that you can say what a good result looks like. Capturing notes, turning a meeting transcript into decisions and actions, pulling together a weekly review: these are the first slices to write down.

Recurring work that needs your judgement is a different shape. You do not hand it over, you keep yourself at the boundary. The skill drafts, you correct it, and it gets a little better every time you do, with you watching more or less closely depending on what is at stake. After enough weeks of correction these slices grow into something with a name and a remit, which is where this is heading.

The bottom of the grid is where people waste effort. A one-off mechanical task is just a thing to ask Claude in a chat, and writing a skill for it is overhead you will never earn back. A one-off that needs real judgement is not a delegation problem at all, but work to sit with yourself.

Never turn a slice into a skill that can act in an irreversible way without you. The [briefing approach I teach](https://chrismdp.com/stop-prompting-start-briefing/) assumes you are in the room, and an irreversible action is the one moment you are not. For me, anything that sends an email, publishes something, spends money, or speaks to a client keeps an approval step. The riskier the slice, the closer you need to stay to it.

## A skill is a slice written down

For a leader, a skill is easier to picture as a job description than as code. It is a short file that tells Claude when to use it, what to read first, what rules to follow, what to produce, and when to stop. You do not need to write the file by hand. Describe the slice to Claude in plain English and it will draft the skill for you; your job is to say what the work is and what a good result looks like. It is less a clever prompt and more a written standard for how one slice of work gets done. Writing it down is also what makes the slice manageable, because you cannot supervise work you have never specified, which is the first thing [managing AI like a team member](https://chrismdp.com/ai-must-be-line-managed/) asks of you.

The one I reach for most is capture. It runs on a single instruction: when I give it a link, a transcript, or a rough thought, it pulls out what is useful, keeps a record of where the idea came from, updates the notes I already have, and files the original. This is a low-level granular skill, but saves me a huge amount of time each time I use it. You can [install it and read how it works](https://airskills.ai/chrismdp/capture){:target="_blank"} if you want a worked example to start from.

## Climb the ladder

Skills are the first step. You do something once in a chat. You notice you are doing it again, so you write the steps down as a skill. The parts that never needed judgement, the fetching and formatting and filing, [turn into small scripts the skill calls](https://chrismdp.com/stop-saving-tokens-start-writing-scripts/). When the same mistake starts to repeat, you add a check that catches it. Once the boundary is trusted, you can do more with it: let it run on a schedule, or hand to others in your team, so you all benefit.

Do not rush this process. The first few runs by hand are how you learn what the slice really is (and what your job really is!), and a skill written before you understand the work just encodes your confusion. Do it manually until it is boring, then automate the boredom.

## Three safe slices

If you want to try this, start where it is safe. Three slices are almost always worth writing down first, because they are internal, reversible, and useful straight away:

1. capturing sources into your notes;
2. turning meeting transcripts into decisions and actions;
3. and preparing a weekly review from your recent notes and calendar.

None of them can embarrass you, and all of them save time the same week.

Leave the tempting ones alone for now. Sending email, writing strategy, and deciding what matters most either need your judgement or carry your name, so they are the worst place to begin - it is so easy to get this wrong and [outsource yourself, not just your work](https://chrismdp.com/i-dont-want-an-ai-god/). Build your agent delegation skills and confidence on the dull, safe slices first. Pick one, write down how you already do it, and you have your first skill.

## Pass it on

Your folder should become a small workplace where well-defined slices of work get done the same way every time, rather than an oracle that does everything and explains nothing, so you can spend your attention on the work that really needs you.

{% include inline-image.html src="/assets/img/airskills-mark.png" alt="Airskills logo" align="right" width="200px" link="https://airskills.ai" %}

Because a skill is just a file, you are not the only one who can run it. [Skills are meant for sharing](https://chrismdp.com/skills-are-meant-for-sharing/): you can hand one to a colleague, drop it in a shared repository, or publish it for anyone to install. That is why I built [Airskills](https://airskills.ai){:target="_blank"}, my own platform for sharing skills and the simplest way I have found to pass a working one to someone else with no setup on their end.

That portability is what makes the next step possible. Once a slice is a reliable skill, you can give it to an agent that runs it for you, the way Maggie and the others already do with mine. The next part of this series is about exactly that: handing your skills to small, named agents that pick up the work, follow the playbook, and leave the result somewhere you can check it.

## Future: Slices become coworkers

When a recurring slice grows a boundary, a rhythm, and a name, it stops being a skill and becomes a colleague. This is what my own folder has turned into. Em, for instance, now sorts everything that comes in before it reaches me. None of these agents replaced a person. Each one took a cluster of slices that used to be mine and now has a clear owner, an inbox, and a voice. I will talk more about how I've set this up in future.


[^pew]: Pew Research Center, [*Americans and AI 2026: Chatbots, Smart Devices and Views on Impact*](https://www.pewresearch.org/internet/2026/06/17/americans-and-ai-2026-chatbots-smart-devices-and-views-on-impact/){:target="_blank"}, 17 June 2026. Only 16 percent of US adults expect AI to have a positive impact on society and 40 percent expect a negative one, with 31 percent expecting it to harm them personally, even as chatbot use has climbed to 49 percent from 33 percent in 2024.

[^tasks]: This is the "task-based" view of automation in labour economics: a job is a bundle of tasks, and machines tend to take over particular tasks while complementing the human work around them, rather than replacing whole occupations. The classic statement is David Autor, [*Why Are There Still So Many Jobs? The History and Future of Workplace Automation*](https://www.aeaweb.org/articles?id=10.1257/jep.29.3.3){:target="_blank"}, Journal of Economic Perspectives, 2015.

[^recombine]: There is evidence behind the optimistic reading. On capacity, Brynjolfsson, Li and Raymond studied more than five thousand support workers and found generative AI raised output by 14 percent on average, and by 34 percent for the least experienced: the same people doing more, rather than fewer people doing the same. On recombination, David Autor argues that AI can extend expert work to a wider set of workers and rebuild middle-skill roles rather than hollow them out. See [Generative AI at Work](https://www.nber.org/papers/w31161){:target="_blank"} (Brynjolfsson, Li and Raymond, 2023) and [Applying AI to Rebuild Middle Class Jobs](https://www.nber.org/papers/w32140){:target="_blank"} (Autor, 2024).
