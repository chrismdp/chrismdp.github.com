---
layout: post
title: "Time To Hire An AI Head"
date: 2026-09-28 09:00:00 +0100
published: true
series: "Software Factory"
article_collection: open-models
categories:
- ai
- leadership
image: /assets/img/time-to-hire-an-ai-head-motif.jpg
infographic: /assets/img/time-to-hire-an-ai-head-infographic.jpg
---

For a long time I have wanted to hand AI a senior job. When I was a CTO, this was the kind of work I would have delegated to a head of department: take a loosely described outcome, work out what it really needs, split it up, get other people to do the pieces, and come back with something finished while I got on with my own work.

That goal has been elusive for years. Until very recently, the best description of an AI model was an overeager junior. Delegating to one meant giving it lots of context, and then watching it closely. That was fine, but frustrating.

<!--more-->

Working with a junior model came with a lot of approval steps, because I could not trust it. Every run needed me to check the plan, answer its questions, approve its commands and review what came back. Cory Doctorow has a name for this: the reverse centaur: a human used up by the machine, pressing the buttons it cannot press itself.[^centaur] I built a whole review board to cope with my agents' output, and found I had turned myself into the button-presser, which I wrote about [back in March](/feedback-is-the-new-bottleneck/). A week later I was warning that [the 85th correct approval trains you to blindly approve the 86th](/stop-prompting-start-briefing/), and by May I could see that [the board itself was training me into drive-by decisions](/i-dont-want-an-ai-god/). (See anti-pattern 2 below.)

Fable and Astra changed that. After reading Steve Yegge's essay on the shape of things to come,[^yegge] I moved to Astra, stepped up a level and stopped managing individual tasks. Astra in particular is genuinely more than a senior: it behaves like a Head. I can give Astra or Fable a high-level instruction and it will just crack on: it reads what it needs, splits the job up, hands the bounded pieces to cheaper workers and comes back with something finished.

This all works very well, until the tokens run out. Using Astra or Fable as my main conversation partners burns through even the top subscription plan at a frightening rate, and I do not want to spend one every day. So some finesse is needed: I want to delegate at a high level without paying Head rates for every piece of the work.

Something else has happened at the same time: the open models have caught up. The previous open models I tried were straight up incompetent at anything beyond a narrow script, but GLM 5.3 Flash is a competent junior.[^mimo] It has a stab at most things, including coding, and runs most of my agent fleet for pennies. On its first day as the standard model for my agents it handled 32 jobs with no failures and no invented facts. It still often misses things or does not quite finish, like any junior, but it has matured enough to be useful and does not break the bank.

So I now have expensive Heads who can take a whole outcome, and cheap juniors who can do a lot of the work. Here are the patterns I have found for combining them.

## Pattern 1: Put A Head In Charge

{% include pattern-diagram.html pattern="head-of" %}

This is the pattern I use most. I give the Head an outcome, it works out the approach, and it splits the job into bounded pieces that cheap juniors can finish. It briefs them, resolves the dependencies between them, reviews what comes back and owns whether the whole thing is accepted. I have a [delegate skill](https://airskills.ai/chrismdp/delegate) that manages this for me, choosing the right level of model depending on the task. Stephen Bungay calls this middle layer operations in *The Art of Action*: strategy sets the intent, tactics carry out the tasks, and operations turns one into the other.[^bungay]

Across three matched coding tasks, GLM 5.3 Flash cost about $0.61 against $16.95 for the flagship model from the same family. If you want to use these more junior models, you need to make sure something competent catches what they miss. In one audit Flash built a feature that forwarded messages between channels. The tests passed, but the code did not do what I had asked for when the original channel could not be read, because the test only checked a weaker fallback. The real fix is an acceptance test that checks the actual requirement, and the Head should insist on one before it accepts the work. Part of that failure was mine, too: the reviewers I brought in afterwards were never shown the original brief, so they judged the work against the wrong standard. The Head needs the original request, the boundaries and the evidence, not just a message from the junior saying it is done.

## (Anti) Pattern 2: Do Not Manage The Juniors Yourself

{% include pattern-diagram.html pattern="do-not-manage" %}

When the juniors got good enough and my Max plans were exhausted, I spent a few days last week handing them work directly. This was not good: it took me straight back to the reverse centaur and the bad old days of 2025, when I was [testing coding agents head to head](/which-coding-agent-is-best/) and concluding that [independent coding agents were not ready](/independent-coding-agents-arent-ready/). I found myself shaping my work around what they could do, deciding the pieces, checking for omissions, answering their questions and keeping everything moving. Worst of all, I had to give them loads of information every time, because a junior only knows what you tell it.

{% include inline-image.html src="/assets/img/context-provider-org-chart.jpg" alt="Comic: Joe stands on a stage in an empty auditorium, laser-pointing at an org chart of robots with a CEO at the top and one human box at the bottom labelled Context Provider. Caption: Joe's big picture message to the company had 100% positive feedback." align="right" width="40%" %}

A friend asked me how you give a senior model enough context to do the job the way you want it done. For a junior, that really is the hard problem, but for a good Head, it mostly goes away. A good Head fetches its own context and works things out from the wider picture, which in my case is my vault: years of notes, projects, decisions and skills describing how I like things done. In an organisation it might be the repo docs, a wiki or the ticket history. If the context is not written down anywhere, the Head cannot fetch it, so writing it down is the first job. I do not need to give it anything more than that, and the juniors get a tight brief from someone who understands the whole job. The answer is simple: only talk to really good agents, and let them delegate the rest as in pattern 1.

## Pattern 3: Give The Head Room To Think

{% include pattern-diagram.html pattern="room-to-think" %}

There are two choices hiding inside "which model". The first is capability: have I picked someone who can do the job at all? The second is how much reasoning effort I let it spend. A Head at low reasoning feels like a senior person on too little sleep and too much coffee. They are still senior, but they move fast and miss things. At high reasoning it is the same person, rested and with an afternoon clear. Setting the two separately saves a lot of tokens: medium effort for day-to-day coordination, and high effort only when a job needs real thought. How much it saves depends on the model. On Anthropic's own coding benchmark runs, Opus 5.5 at medium effort scored about 2.5 points below high for about 70% of the cost, and extra-high effort bought only 1.4 more points for two and a half times the cost of high.[^effort]

## Pattern 4: Visit The Expert In Their Den

{% include pattern-diagram.html pattern="expert-den" %}

Some problems deserve a second opinion. My Head can run at medium effort and call in a fresh expert at high effort, either another copy of the same model or a different one entirely. The fresh expert gets the original problem, the evidence and the specific doubt, with none of the baggage of the conversation so far. The Head weighs what comes back and stays responsible for the result.

I used to do this with Fable. It felt like visiting the brilliant expert that every organisation has, sitting in their office den: you go occasionally, and you dread the experience, mostly because of what Ethan Mollick calls "Claudish", the nonsense-speak these models drift into.[^claudish] Opus 5 had the same problem, which is why I never used it as a Head. The advice was excellent, but I did not want to deal with it directly all day, and I certainly could not afford to use a top-end model every time: the plan usage was just too great. So I sent the Head to visit on my behalf, and Fable only ever saw a well-prepared question. Now that Opus 5.5 is my go-to Head, I make that visit far less often. I suspect the den will come back, though. In future there could be specialised and very expensive models built for exactly this kind of work, and the pattern will be the same: prepare the question well, send the Head, and keep the expert out of the day-to-day.

## Pattern 5: Try The Junior Head

{% include pattern-diagram.html pattern="junior-head-of" %}

This is the newest pattern, and the one that makes the whole arrangement affordable: run most of the work through a cheaper Head, and escalate to the expensive one only when a job needs it. For me, that cheaper Head is Opus 5.5, which seems to have fixed the Claudish. It is proving to be the first model I can use as a Head without watching my subscription drain. It is capable, it is fast and it is almost as good as Astra at strategic work. I am also not using it to delegate as much, because it can do the work itself at a reasonable cost. I think of it as a junior Head, or a Head who has almost got it. Astra is still my head of everything, but Opus 5.5 runs the day-to-day.

Because it does not burn through my tokens, it widens what I can experiment with. I can hand it outcomes I would never have risked on Astra's budget, see what comes back and learn from it. When a job turns out to need more, I escalate to Astra or send the junior Head to visit Fable.

## Pattern 6: Ask The Head To Explain Strategy

{% include pattern-diagram.html pattern="explain-strategy" %}

In May I wrote that [I did not want an AI god](/i-dont-want-an-ai-god/), because asking AI for a strategy gets you something "plausible, coherent and mind-numbingly average". I still believe that about asking a model to decide for me. What has changed is how good the Heads have become at helping me understand a strategic situation. Increasingly I ask them to read everything relevant and give me a good understanding of where things stand, and that is proving very helpful. The call is still mine, but I make it with a better picture than I could have put together myself in the time.

Understanding a situation is different from interpreting it and expressing what to do about it. Tara Seshan put this well on Lenny's Podcast:[^lenny] as AI takes on more of the work, three things stay human, and they are expression, accountability and relationships. The Head can help me understand the strategy, but saying what we will do, standing behind it and bringing people with me are still my job.

## Head Of Everything

I am not the only one reaching for the org chart. Every's Context Window newsletter reported engineers describing Anthropic's models as a company: Fable as the CEO, Opus 5 as a senior engineer and Sonnet 5 as a junior engineer or analyst.[^ceo] The same piece has a theory for the Claudish, too: that Opus 5 was trained mainly to work as a subagent under Fable, so its prickly style matters less because it mostly talks to another model.

Where I differ is on how far to take the chart. I do not think giving agents human job titles works well. Agents have properties that humans do not, which are genuinely useful, and mapping them onto a human role can limit them. It also suggests that AI is a direct replacement for a person, which is wrong: AI takes on [slices of people's work](/slice-your-job-into-skills/), not whole jobs. Human job titles are far too generic for that anyway. The best title for an agent is one you never see in the real world, like "financial reconciler" or "productivity coach": a single slice. The level you give it, junior or Head, then depends on how powerful the model is and how much you want to spend.

This will likely change in future. The same piece reports the labs moving towards specialised models, with one to orchestrate and another to execute. We may yet end up with truly specialised intelligences, and who knows where that goes. For now, the level is what I notice first: they are good at everything.

The employee metaphor is not perfect, but where it breaks, it mostly breaks in the agent's favour. An agent can be made to forget things completely, which would get very strange in a human (*Eternal Sunshine of the Spotless Mind*[^sunshine] is a fantastic thought experiment on exactly that!). And we never hire a junior model and promote it: we pick the right level for each job, so the Peter Principle does not apply.[^peter]

## Buy Back Your Attention

All of this comes back to the goal I started with. With a team of juniors, I end up squeezing every last drop out of my subscription while spending the attention I was trying to free up. With a capable Head, I can say "please get that done" and go away for hours. So I have stopped comparing models and started comparing teams: the whole cost of an accepted outcome, including the briefing, the review, the repairs and above all my own time spent stepping in.

If you are putting together a team of models, start with the management questions rather than the benchmark tables. Who understands the whole task? What can each worker reliably own? Who fetches the context? What evidence proves the work is done? What can the Head read, and where does that data go? The juniors are now good enough to do a lot of the work. They still need somebody to manage them, and, for many tasks, that somebody no longer has to be you.

[^centaur]: Cory Doctorow sets out the reverse centaur in [his speech on the AI bubble](https://pluralistic.net/2025/12/05/pop-that-bubble/#u-washington): a centaur is a human helped by a machine, and a reverse centaur is a human used up by one.
[^claudish]: Ethan Mollick coined the term [on X in June 2026](https://x.com/emollick/status/2064542441848422611), watching long agent tasks drift into a private dialect of labels, fragments and shorthand.
[^mimo]: The next one I am keen to try is Xiaomi's [MiMo-V2.6](https://mimo.mi.com/docs/en-US/news/latest/v2-6), released with open weights on 21 September 2026. My setup only uses hosts that offer zero data retention (ZDR), and there are not enough of those for MiMo yet.
[^yegge]: Steve Yegge, [*The Shape of Things to Come, Part 1: The Continuous Thunderdome*](https://yegge.ai/essays/the-shape-of-things-to-come/), August 2026.
[^lenny]: Tara Seshan on [Lenny's Podcast](https://www.lennysnewsletter.com/p/ais-third-era-the-rise-of-persistent).
[^sunshine]: [*Eternal Sunshine of the Spotless Mind*](https://en.wikipedia.org/wiki/Eternal_Sunshine_of_the_Spotless_Mind) (2004), written by Charlie Kaufman and directed by Michel Gondry.
[^effort]: Anthropic, [*Optimizing for cost and intelligence*](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence), SWE-bench Pro results. The same page shows research tasks where higher effort bought no measurable accuracy at all.
[^bungay]: Stephen Bungay, *The Art of Action*. His [chapter summaries](https://www.pmi.org/-/media/pmi/microsites/disciplined-agile/bungay_artofaction_chapterrecaps_article.pdf) set out the strategy, operations and tactics distinction.
[^ceo]: Every, [*Fable as CEO*](https://every.to/context-window/fable-as-ceo), Context Window newsletter, July 2026.
[^peter]: Laurence J. Peter and Raymond Hull, *The Peter Principle* (1969): in a hierarchy, people tend to be promoted until they reach a role they cannot do.
