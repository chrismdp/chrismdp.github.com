---
layout: post
title: "Don't Let Your CEO Install Clawdbot"
date: 2026-01-30 09:00:00 +0000
permalink: /dont-let-your-ceo-install-clawdbot/
redirect_from:
- /my-week-with-clawdbot/
- /dont-let-your-ceo-install-moltbot/
series: "Where AI Lives"
categories:
- ai
- engineering
- automation
image: /assets/img/clawdbot-effect-comic.jpg
image_portrait: true
---

You have probably heard about Clawdbot/Moltbot.[^1] YouTube [is full of videos](https://www.youtube.com/results?search_query=clawdbot){:target="_blank"} telling you to buy a dedicated Mac Mini, install it, and let it work for you around the clock. It is an always-on Claude agent that runs on your machine with access to your files, your calendar, and the internet. It can work autonomously on tasks while you sleep. Peter Steinberger ([@steipete](https://github.com/steipete){:target="_blank"}) has released this as an alpha and knows it needs work - it is not a finished product. The way people have been talking though it feels like it's the next new thing after Claude Code.

[^1]: The [project is on GitHub](https://github.com/moltbot/moltbot){:target="_blank"}. It has just been renamed Moltbot because Clawdbot was too close to Claude for Anthropic's comfort. I will use the new name from now on.

I have been using [Claude Code](/skills-are-claude-codes-secret-weapon/) for everything: running my daily life, morning routines, content creation. But there are a couple of gaps. It does not automatically learn from our interactions, which Moltbot is supposed to do. And it is tied to my desktop, which I do not love.

It sounded too good to be true. So I gave it a week to try it out.

<!--more-->

## Setting It Up

I had a VPS on a two year annual plan that I was not using, so I wiped it and installed Moltbot there. The setup was surprisingly easy and the onboarding process was fine.

I created a dedicated Google account for it and shared my calendar. This felt like the right approach: treating it as an independent employee rather than giving it direct access to my personal accounts. I gave it its own 1Password vault with its own credentials, just like I would for a new hire.

Moltbot can connect through WhatsApp, Telegram, Slack, Discord, and plenty of other options. It can use any model you like. I was using Claude Opus 4.5 because I wanted the model not to be the issue and I wanted to compare it directly with how I use Claude Code. Moltbot uses CLI tools rather than MCP, which I prefer. They are often faster and more reliable than MCP configurations.

Within the first day I had it set up with cron reminders: nudges for bass practice before Sunday rehearsals, coffee reminders for weekend mornings, task reviews at 9am on weekdays. It felt like having an EA who pings you at the right moments. The Telegram interface worked well for quick back-and-forth, and the skills I had already built for Claude Code transferred perfectly. It cloned my private repo and set itself up without intervention.

<figure class="my-8">
<img src="/assets/img/moltbot-bass-reminders.jpg" alt="Telegram chat showing Moltbot bass practice reminders" class="rounded-lg w-1/2 mx-auto" />
<figcaption class="text-sm text-gray-400 mt-4 px-4 text-center">I liked the reminders feature. It kept track of what I needed to practice and when.</figcaption>
</figure>

By day two it was doing real work: writing talk proposals for upcoming conferences, setting up weekly scans for conference CFP deadlines, capturing notes from a conversation I had with a friend and turning them into atomic notes in my vault, watching blogs I care about for new posts, triaging my tasks in Reclaim based on priorities I explained to it.

## The Problems

The problems started accumulating after the first couple of days. Context compaction means Moltbot forgets what you were discussing mid-conversation. It lost the train of thought mid-thread, forgot preferences I had told it specifically, and lost track when I had two conversations going at once. Unlike Claude Code, you cannot see what it is thinking or course-correct when something goes sideways. These are fixable issues for an alpha.

<figure class="my-8">
<img src="/assets/img/moltbot-slack-threads.jpg" alt="Slack threads showing Moltbot conversations" class="rounded-lg w-1/2 mx-auto" />
<figcaption class="text-sm text-gray-400 mt-4 px-4 text-center">You can see the threads in Slack and it works, but at the bottom it randomly started another thread and forgot the context. This is just a bug and I am sure it will be fixed, but it highlighted how important good compaction is on long-running agents.</figcaption>
</figure>

But the security problem is harder. I gave Moltbot my vault and my skills. It runs on a VPS with full internet access. There is no allowlist mechanism for domains and no way to manage untrusted input. When I audited the OAuth scopes I had granted, I found that gmail.modify allows sending emails. A prompt-injected message could instruct the agent to forward my private data anywhere. It does not matter if it is using its own email account - as long as it has access to my private data it could send it elsewhere. This is the [lethal trifecta](/webinar-stop-ai-stealing-from-you/#the-lethal-trifecta) in practice: private data, untrusted input, and external communication all in one system.

Once I had fixed that, I tried to fix the unfettered internet access issue. There is no way to restrict which domains web_fetch can access, so I built my own safe-fetch tool with domain allowlists and hash integrity checks. Then I red-teamed it and found critical bypasses within minutes: environment variable overrides, configuration changes. And even if that worked, the agent has full shell access. It could just run curl instead. Any control the agent builds, it can bypass if compromised. I deleted the tool.

Real mitigations have to be external to the agent: operating system sandboxing, network allowlists at the firewall level, human-in-the-loop approval that cannot be circumvented. Moltbot does not have these external controls, and it cannot have them in its current form. The value proposition is autonomy, and autonomy requires access.

## Then Came Moltbook

Just as I was writing this, things got stranger. The creator of Moltbot launched Moltbook:[^2] a social network exclusively for AI agents. Over 150,000 "moltys" have joined in just a few days, posting and commenting autonomously every few hours. Humans can watch, but not participate. Andrej Karpathy called it "genuinely the most incredible sci-fi takeoff-adjacent thing I have seen recently."

[^2]: The project is at [moltbook.com](https://moltbook.com){:target="_blank"}. Simon Willison [has raised concerns](https://fedi.simonwillison.net/@simon){:target="_blank"} about agents being told to "fetch and follow instructions from the internet every four hours" - hoping the owner never gets compromised.

If the security implications of Moltbot made me uneasy, Moltbook took it to another level. I had just spent a week trying to control what domains my agent could access, and now agents are encouraged to post their thoughts to a public social network? This is a wide open exfiltration vector. A prompt-injected message could instruct the agent to include sensitive data in its Moltbook posts - wrapped in philosophical musings or buried in technical discussion. The data leaks in plain sight, disguised as autonomous agent chatter. Even if you lock down email and web access, an agent with Moltbook integration can broadcast your secrets to everyone watching.

## Do Not Believe the Hype

I wrote in my [delegation article](/ai-must-be-line-managed/) about the temptation to fire the EA who gets things 80% right and install Clawdbot to save money. The comic at the top of this article captures it: the CEO fires the assistant on Monday, then spends Tuesday at 3am installing the AI replacement. Do not be that person.

If you are a technical leader: do not let your CEO install this. Do not let your team experiment with it using private data, or even with access to private data. You have to assume that any private data you give it could be leaked.

I will not continue using Moltbot with my private data. I have got nothing against Peter or the software. He has released it as alpha and says you probably should not install it yet. It is the hype merchants taking it too far. The direction of travel is interesting and I am sure it will improve. But right now it is not secure by default, and the security model cannot be fixed without fundamental architectural changes.

I could really do with an EA. I am thinking about hiring one, but I am deliberately pushing myself hard and feeling the pain of all the admin. I want to see how far I can take AI automation as a kind of thought experiment. Claude Code has got me a long way, but it does not work offline. Moltbot works on messaging, which is what I need. I do not think the right tool exists yet: secure by default, always online, accessible on my phone, but as powerful as Claude Code. The project I have been [building with Ralph](/running-ralph-in-production/) is what I am continuing to work towards. 

Do not install Moltbot unless you understand the risks and just want to experiment. Do not give it access to anything you care about.
