---
layout: post
title: "Webinar: AI Has a People Problem"
date: 2026-03-26 17:00:00 +0000
categories:
- ai
- webinar
- leadership
- teams
image: /assets/img/webinar-ai-people-problem.jpg
series: "AI In Action Webinars"
---

On 26 March 2026, I gave a webinar about the human dysfunction that shows up in every organisation trying to make AI work. I framed it around seven personas I keep encountering in my training and consulting work, and the virtual room immediately recognised them.

<!--more-->

## Seven Kinds of Trouble

Every team adopting AI contains some combination of these people. Most teams contain all of them.

![Angela the Addict](/assets/img/webinar-angela-the-addict.jpg)

**Angela the Addict** is your best engineer. She discovered AI tools six months ago and now cannot stop using them. She worked sixteen days straight because it is so easy and fun to start the next thing. She runs six or seven concurrent sessions, starts new ones at midnight on her phone, and dreads looking at a terminal window in the morning. I know Angela exists because this was my story. The tools create a variable reward schedule[^1] like a slot machine: sometimes the output is brilliant, sometimes mediocre, and the randomness keeps you pulling the lever. Steve Yegge recently called this the AI Vampire[^2]: who captures the value of Angela's 10x productivity? If she is not getting 10x her salary and the company is simply expecting 10x the output, we are working her into the ground.

![Pete the Prejudiced](/assets/img/webinar-pete-the-prejudiced.jpg)

**Pete the Prejudiced** tried ChatGPT in early 2023, got confidently told complete nonsense, and decided AI does not work. His boss gave him Copilot, it generated the wrong function, and he turned it off. Pete has not touched AI since. The problem is that Pete's mental model is locked to how AI used to work, and the tools in September 2025 were not that good either. You might need to [update your view of what AI can do](/stop-prompting-start-briefing/) every three months. Pete is often one of your most respected engineers, which means when he dismisses it, he implicitly gives everyone else permission to dismiss it too. You can freeze an entire team this way. His mental model is all about determinism: code compiles or it does not, tests pass or they fail. AI is probabilistic, more like civil engineering where you work with tolerances rather than guarantees. One mistake does not mean you discount the whole thing.

![Ray the Rusty](/assets/img/webinar-ray-the-rusty.jpg)

**Ray the Rusty** learned how to do his job ten years ago and has been reapplying the same skills ever since. He is good at what he does, but has not had to learn anything new in quite some time. AI requires you to relearn how to learn, and admitting "I do not know how to use this" feels worse than admitting "I do not like it." Ray is used to being an expert and suddenly is not. The data on seniority and AI comfort splits in an unexpected way: juniors feel good about it, mid-level and senior people struggle, and super-senior people who have spent their careers pushing themselves often feel good about it again. There is a real dip at the ten to fifteen years of experience mark.

![Neville the Neogeneralist](/assets/img/webinar-neville-the-neogeneralist.jpg)

**Neville the Neogeneralist** is an identity crisis I did not see coming until a couple of client conversations this week. Engineers who are productive with AI want to be product engineers because the AI handles the building and they want to think about product. Product people who can now code also want to be product engineers. Everyone wants the same job title, nobody can agree what it means, and your progression framework is out the window. How do you manage that transition without crushing their momentum or creating chaos?

![Marvin the Maintainer](/assets/img/webinar-marvin-the-maintainer.jpg)

**Marvin the Maintainer** is the person left behind when you put your best people in a small room to [move fast without constraints](/why-ai-fast-teams-still-ship-slowly/). Those small teams ship fast, but what about the engineer maintaining the old product line? Why should those people shoot ahead while Marvin gets left behind? How do you make sure Marvin gets investment and the opportunity to learn when he is on a system that is not suitable for rapid prototyping?

![Harold the Hollowed Out](/assets/img/webinar-harold-the-hollowed-out.jpg)

**Harold the Hollowed Out** uses AI for everything, is very productive, but the output is not very good. He has stopped thinking and started approving. The AI does the interesting work, Harold clicks approve. Cory Doctorow called this the [reverse centaur](/ai-must-be-line-managed/): instead of humans doing the interesting thinking with AI handling the drudgery, AI does the thinking and humans do the boring parts. There is a deeper cultural risk here too. The models we use embed particular cultural assumptions from whoever trained them. If everybody's documents start sounding the same, everybody's strategies focus the same way, and everybody's progression frameworks embed the same values, the organisation converges on the average and [hollows out its own distinctions](/the-slow-and-dangerous-loss-of-self/). Simon Wardley speaks quite strongly about this being a form of cultural warfare, and while that may sound dramatic, we are importing values from whoever trained the model whether we notice or not.

![Carole the Clueless](/assets/img/webinar-carole-the-clueless.jpg)

**Carol the Clueless** is not like Harold. She works fast and hard with AI, ships effective code, features work, metrics look fantastic. She just cannot explain her own codebase. Margaret-Ann Storey called this cognitive debt[^3]: the debt from going fast lives in the developer's brain. A research study found that student teams using AI went brilliantly for about six weeks, then ground to a halt at week seven because they could not make simple changes to their own code. The system worked but nobody understood why. If you are building anything where people need to understand the code, which is most systems and certainly anything regulated, this is a serious problem.

## The Journey

One attendee pointed out that his development teams go through the personas in order. First there is reluctance, then they try AI, it goes wrong, and they stop. Eventually they get persuaded back in and become Angela the Addict, generating code at full tilt. The cognitive debt catches up and they become Carol the Clueless before reaching a more sustainable path. The personas are stages of a journey, almost like stages of grief for the way we used to work.

Another attendee described a two-mode approach: allow yourself to vibe-code freely to explore ideas, then step back and deliberately guide the AI to build something architecturally sound. A third described a version where the non-technical prototype becomes the specification for engineers to build properly. The addict phase becomes useful if you treat its output as exploration rather than production.

Every persona represents some level of personal dysfunction. Angela is addicted. Pete is angry. Ray is scared. Neville is opportunistic but confused. Marvin feels abandoned. Harold does not know who he is any more. Carol is one audit away from disaster. These are people problems, and none of them has a technical fix.

## What Might Help

I have ideas, not answers, but some of them seem to be working.

**Iterate fast.** Long-term AI strategies are obsolete before they ship. Small bets, weekly learning cycles, and honest admission that leadership does not have all the answers gives teams more safety than a detailed plan they do not believe. When you [gain evidence through small experiments](/webinar-how-not-to-screw-up-your-ai-rollout/) and demonstrate progress, people trust the process.

**Teach people to learn.** Going on a Copilot course or a Claude Code course is not the point. The mindset shift matters far more than the feature demo: learning to think probabilistically, practising deliberate questioning, getting AI to interview you about your own context rather than asking it to generate answers. I have noticed it takes about three or four repetitions of this instruction before people internalise it. The instinct to say "give me a strategy" is deeply entrenched, and replacing it with "ask me questions to help figure out what I should tell you" takes real practice.

**Invest in the transition.** This needs real time, real effort, and real money. Rolling out Copilot access and saying "have at it" produces a whole menagerie of the personas above without anyone realising. Different messages matter for different people: for juniors, build judgement not speed; for mid-level engineers, help them understand their value is in [thinking about problems](/feedback-is-the-new-bottleneck/), not typing code; for seniors, their experience and strategic perspective is what matters. Build centres of excellence, create champion structures, and invest in people teaching each other so nobody ends up as Marvin the Maintainer.

**Measure the right things.** Do not measure tokens consumed or output volume. Measuring tokens produces Carols and Angelas. Measuring output volume optimises for Harold. Measure learning, quality, and whether people are still thinking. I do not know exactly how to measure those things, but those are the metrics that matter.

## Tools and Resources

- [Stop Prompting, Start Briefing](/stop-prompting-start-briefing/) on why mental model shifts matter more than prompt engineering
- [AI Must Be Line Managed](/ai-must-be-line-managed/) on preventing the reverse centaur problem
- [Why AI-Fast Teams Still Ship Slowly](/why-ai-fast-teams-still-ship-slowly/) on team structure and the Marvin problem
- [Feedback Is the New Bottleneck](/feedback-is-the-new-bottleneck/) on where the real constraint moves when coding gets fast
- The AI Vampire[^2] by Steve Yegge on who captures the value of AI productivity
- [AI training for technical teams](/training) for mindset-shift workshops, not feature demos

## Key Takeaway

{% include shareable-quote.html text="AI works — that is no longer a debate. Most applied AI problems are now people problems, and none of them have a technical fix." %}

Every organisation adopting AI will find these seven personas on their teams. Each person is going through their own version of a difficult transition, and managing that transition takes empathy, investment, and honest admission of what we do not yet know.

## One Thing to Try This Week

Pick one person on your team and figure out which persona they most resemble right now. Do not tell them. Instead, have a conversation about how their work with AI is going. Listen for the signals: are they working too many hours, dismissing the tools, struggling to learn, confused about their role, feeling left behind, rubber-stamping output, or shipping code they cannot explain? The persona gives you a framework for understanding the conversation, not a label for the person.

[^1]: [Variable reward schedules](https://en.wikipedia.org/wiki/Reinforcement#Schedules){:target="_blank"} — the same reinforcement pattern that makes slot machines compulsive
[^2]: Steve Yegge, [The AI Vampire](https://steve-yegge.medium.com/the-ai-vampire-eda6e4f07163){:target="_blank"}
[^3]: Margaret-Ann Storey, [How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/){:target="_blank"}
