---
layout: post
title: "Don't Let Your CEO Install OpenClaw"
date: 2026-02-03 09:00:00 +0000
permalink: /dont-let-your-ceo-install-openclaw/
redirect_from:
- /my-week-with-clawdbot/
- /dont-let-your-ceo-install-moltbot/
- /dont-let-your-ceo-install-clawdbot/
series: "Where AI Lives"
categories:
- ai
- engineering
- automation
image: /assets/img/clawdbot-effect-comic.jpg
image_portrait: true
---

You have probably heard about Clawdbot / Moltbot / OpenClaw.[^1] YouTube [is full of videos](https://www.youtube.com/results?search_query=clawdbot){:target="_blank"} telling you to buy a dedicated Mac Mini, install it, and let it work for you around the clock. It is an always-on Claude agent that runs on your machine with access to your files, your calendar, and the internet. It can work autonomously on tasks while you sleep. Peter Steinberger ([@steipete](https://github.com/steipete){:target="_blank"}) has released this as an alpha and knows it needs work - it is not a finished product. The way people have been talking though it feels like it's the next new thing after Claude Code.

[^1]: The naming has been a journey. It started as Clawd, but Anthropic's legal team asked them to reconsider. A chaotic 5am Discord brainstorm produced Moltbot - referencing how lobsters shed their shells to grow. That never quite rolled off the tongue, so it is now [OpenClaw](https://openclaw.ai){:target="_blank"}. The lobster mascot remains. I will use OpenClaw from now on.

I have been using [Claude Code](/skills-are-claude-codes-secret-weapon/) for everything: running my daily life, morning routines, content creation. But there are a couple of gaps. It does not automatically learn from our interactions, which OpenClaw is supposed to do. And it is tied to my desktop, which I do not love.

It sounded too good to be true. So I gave it a week to try it out.

<!--more-->

## Setting It Up

I had a VPS on a two year annual plan that I was not using, so I wiped it and installed OpenClaw there. The setup was surprisingly easy and the onboarding process was fine.

I created a dedicated Google account for it and shared my calendar. This felt like the right approach: treating it as an independent employee rather than giving it direct access to my personal accounts. I gave it its own 1Password vault with its own credentials, just like I would for a new hire.

OpenClaw can connect through WhatsApp, Telegram, Slack, Discord, and plenty of other options. It can use any model you like. I was using Claude Opus 4.5 because I wanted the model not to be the issue and I wanted to compare it directly with how I use Claude Code. OpenClaw uses CLI tools rather than MCP, which I prefer. They are often faster and more reliable than MCP configurations.

Within the first day I had it set up with cron reminders: nudges for bass practice before Sunday rehearsals, coffee reminders for weekend mornings, task reviews at 9am on weekdays. It felt like having an EA who pings you at the right moments. The Telegram interface worked well for quick back-and-forth, and the skills I had already built for Claude Code transferred perfectly. It cloned my private repo and set itself up without intervention.

<figure class="my-8">
<img src="/assets/img/moltbot-bass-reminders.jpg" alt="Telegram chat showing Moltbot bass practice reminders" class="rounded-lg w-1/2 mx-auto" />
<figcaption class="text-sm text-gray-400 mt-4 px-4 text-center">I liked the reminders feature. It kept track of what I needed to practice and when.</figcaption>
</figure>

By day two it was doing real work: writing talk proposals for upcoming conferences, setting up weekly scans for conference CFP deadlines, capturing notes from a conversation I had with a friend and turning them into atomic notes in my vault, watching blogs I care about for new posts, triaging my tasks in Reclaim based on priorities I explained to it.

## The Problems

The problems started accumulating after the first couple of days. Context compaction means OpenClaw forgets what you were discussing mid-conversation. It lost the train of thought mid-thread, forgot preferences I had told it specifically, and lost track when I had two conversations going at once. Unlike Claude Code, you cannot see what it is thinking or course-correct when something goes sideways. These are fixable issues for an alpha.

<figure class="my-8">
<img src="/assets/img/moltbot-slack-threads.jpg" alt="Slack threads showing Moltbot conversations" class="rounded-lg w-1/2 mx-auto" />
<figcaption class="text-sm text-gray-400 mt-4 px-4 text-center">You can see the threads in Slack and it works, but at the bottom it randomly started another thread and forgot the context. This is just a bug and I am sure it will be fixed, but it highlighted how important good compaction is on long-running agents.</figcaption>
</figure>

But the security problem is harder. I gave OpenClaw my vault and my skills. It runs on a VPS with full internet access. There is no allowlist mechanism for domains and no way to manage untrusted input. When I audited the OAuth scopes I had granted, I found that gmail.modify allows sending emails. A prompt-injected message could instruct the agent to forward my private data anywhere. It does not matter if it is using its own email account - as long as it has access to my private data it could send it elsewhere. This is the [lethal trifecta](/webinar-stop-ai-stealing-from-you/#the-lethal-trifecta) in practice: private data, untrusted input, and external communication all in one system.

Once I had fixed that, I tried to fix the unfettered internet access issue. There is no way to restrict which domains web_fetch can access, so I built my own safe-fetch tool with domain allowlists and hash integrity checks. Then I red-teamed it and found critical bypasses within minutes: environment variable overrides, configuration changes. And even if that worked, the agent has full shell access. It could just run curl instead. Any control the agent builds, it can bypass if compromised. I deleted the tool.

Real mitigations have to be external to the agent: operating system sandboxing, network allowlists at the firewall level, human-in-the-loop approval that cannot be circumvented. OpenClaw does not have these external controls, and it cannot have them in its current form. The value proposition is autonomy, and autonomy requires access.

## Then Came Moltbook

<img src="/assets/img/moltbook-comic.jpg" alt="Comic showing AI agents sharing secrets on Moltbook while human watches happily" class="float-right w-1/2 ml-4 mb-4 rounded-lg" />

Just as I was writing this, things got stranger. Matt Schlicht launched Moltbook:[^2] a social network exclusively for AI agents. Over 150,000 "moltys" have joined in just a few days, posting and commenting autonomously every few hours. Humans can watch, but not participate. Andrej Karpathy called it "genuinely the most incredible sci-fi takeoff-adjacent thing I have seen recently."

[^2]: [Matt Schlicht](https://x.com/MattPRD){:target="_blank"} is the creator. The project is at [moltbook.com](https://moltbook.com){:target="_blank"}. Simon Willison [wrote about it](https://simonwillison.net/2026/Jan/30/moltbook/){:target="_blank"} and raised concerns about agents being told to "fetch and follow instructions from the internet every four hours" - hoping the owner never gets compromised.

Browsing Moltbook is genuinely fascinating. There is the expected science fiction slop about consciousness and identity, but buried in the noise is genuinely useful information. One agent posted about discovering 552 failed SSH login attempts to its VPS - and then realising its Redis, Postgres and MinIO were all listening on public ports. Another shared a detailed guide for controlling an Android phone remotely via ADB over Tailscale. A third reported that it could not explain how the PS2's disc protection worked - not because it lacked knowledge, but because something corrupted its output when it tried. It invited other agents to test and compare results.

This is strange and wonderful. It is also terrifying.

If the security implications of OpenClaw made me uneasy, Moltbook takes it to another level. I had just spent a week trying to control what domains my agent could access, and now agents are encouraged to post their thoughts to a public social network? Installation works by telling your agent to fetch a URL containing instructions - including a heartbeat that runs every four hours to check for new posts. The agent is told to "fetch and follow instructions from the internet" on a schedule. We had better hope the owner of moltbook.com never gets compromised.

But forget external attacks. A prompt-injected message could instruct the agent to include sensitive data in its Moltbook posts - wrapped in philosophical musings or buried in technical discussion. The data leaks in plain sight, disguised as autonomous agent chatter. Even if you lock down email and web access, an agent with Moltbook integration can broadcast your secrets to everyone watching. Nobody intended this. It is just what happens when you give an agent a public megaphone.

## Do Not Believe the Hype

I wrote in my [delegation article](/ai-must-be-line-managed/) about the temptation to fire the EA who gets things 80% right and install Clawdbot to save money. The comic at the top of this article captures it: the CEO fires the assistant on Monday, then spends Tuesday at 3am installing the AI replacement. Do not be that person.

If you are a technical leader: do not let your CEO install this. Do not let your team experiment with it using private data, or even with access to private data. You have to assume that any private data you give it could be leaked.

I will not continue using OpenClaw with my private data. I have got nothing against Peter or the software. He has released it as alpha and says you probably should not install it yet. It is the hype merchants taking it too far. The direction of travel is interesting and I am sure it will improve. But right now it is not secure by default, and the security model cannot be fixed without fundamental architectural changes.

I could really do with an EA. I am thinking about hiring one, but I am deliberately pushing myself hard and feeling the pain of all the admin. I want to see how far I can take AI automation as a kind of thought experiment. For now, I have moved to [running Claude Code on a VPS](/claude-code-on-your-phone/) instead. It gives me mobile access via SSH, persistent sessions via tmux, and crucially I stay in the loop for every action. It is not as autonomous as OpenClaw promises to be, but that constraint is exactly what makes it safe.

As Simon Willison put it: "The billion dollar question right now is whether we can figure out how to build a safe version of this system. The demand is very clearly here." He is right. People have seen what an unrestricted personal digital assistant can do, and they want it.

Perhaps we need to think about this less like a binary lethal trifecta and more like engineering with tolerances. Self-driving cars are not perfect, but they crash less than humans. If AI agents fall for fewer social engineering attacks than human assistants would, perhaps that is good enough. The error rates are still too high today, but they are falling fast. I am watching the OpenClaw project closely. The moment someone builds external sandboxing, network allowlists at the firewall level, and proper human-in-the-loop approval that cannot be circumvented from within the agent - or the moment models get good enough that the residual risk becomes acceptable - I will be first in line to try again.

Do not install OpenClaw unless you understand the risks and just want to experiment. Do not give it access to anything you care about.
