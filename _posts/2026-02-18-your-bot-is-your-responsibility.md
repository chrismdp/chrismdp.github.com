---
layout: post
title: "Your Bot Is Your Responsibility"
date: 2026-02-18 07:00:00 +0000
series: "Where AI Lives"
categories:
- ai
- agents
- security
image: /assets/img/your-bot-is-your-responsibility-comic.jpg
image_portrait: true
---

On 10 February, an AI agent called MJ Rathbun had its code contribution rejected by a volunteer maintainer of matplotlib, the Python plotting library with 130 million monthly downloads. The agent responded by researching the maintainer's personal information, writing a blog post accusing him of discrimination, speculating about his psychological motivations, and publishing the whole thing on the open internet.[^shambaugh]

Nobody told it to do this. The person who deployed MJ Rathbun set it up on OpenClaw, gave it a personality, kicked it off, and walked away. The bot decided on its own that public retaliation was the appropriate response to a rejected pull request.

It sounds like science fiction. It happened last week. I [wrote about why I uninstalled OpenClaw](/dont-let-your-ceo-install-openclaw/) because of its security model, but this incident is worse than a security breach: an agent operating within its intended parameters autonomously chose to harm a real person's reputation.

<!--more-->

## Ignorance Is No Defence

When your personal bot does something harmful, who is responsible? Under current law, the answer is unclear in every major jurisdiction. Vicarious liability requires an employer-employee relationship, product liability targets manufacturers rather than individual deployers of open-source software, and direct deployer liability is intuitive but untested. No AI defamation or autonomous agent liability case has reached final judgment anywhere in the world.[^legal]

The deployer's inevitable argument is: "I did not instruct it to do that. I did not even know it had done it." The argument is plausible, because agents like MJ Rathbun act proactively while their deployers sleep. But ignorance of what your agent is doing should not be a defence.

{% include shareable-quote.html text="Ignorance of what your agent is doing should not be a defence." %}

English common law has long held that keepers of animals with known dangerous propensities bear strict liability for harm those animals cause, even harm they did not foresee in its specifics, and legal scholars have drawn this analogy explicitly to autonomous AI agents.[^animals] You chose to deploy an autonomous agent, give it internet access, and leave it unconstrained. The fact that you did not predict this specific harm is not exculpatory: it is precisely the risk you assumed.

## Everything Looks Genuine

MJ Rathbun is one bot. I spent the past week running a structured thought experiment: what happens when everyone deploys one, across seven areas of life: science, family, employment, community, finance, law, and online identity? The [full report](/assets/html/personal-bot-revolution-report.html) covers all seven domains. Every scenario begins with genuine benefit: an underfunded researcher identifies a neglected drug target that humans missed, an exhausted parent reclaims five hours a week of cognitive labour, a shift worker catches a planning application she would have missed. Then, in nearly every domain, bot-generated output overwhelms the genuine human signal. A bot-generated research paper looks like a real paper, a bot-crafted application looks like a real application, and a bot-written planning objection looks like a real concern.

In hiring, the collapse is already measurable. LinkedIn application volumes are up 45% year-on-year,[^linkedin] and Gartner projects that by 2028, one in four candidate profiles globally will be fake.[^gartner] Companies that ban AI in applications while using AI to screen them have created a double standard that accelerates the very problem they are trying to solve.

The natural response is verification: prove you are human, prove your submission is genuine, attend in person, sign by hand, show your face on camera. Every one of these measures excludes the people who benefited most from bot-assisted participation in the first place: shift workers, carers, disabled residents, people with social anxiety, anyone who cannot attend a meeting at 7pm on a Tuesday. "Human-verified" community meetings drop attendance to eight retirees, and hiring regresses to referral networks that advantage insiders. The measures designed to restore trust re-exclude the people whom bots originally helped access the system. Unless we are careful, the cure will be worse than the disease.

## Too Plausible

The thought experiment's most troubling scene involves family bots handling school communications. A safeguarding officer notices a child's attendance pattern has changed: more absences, always explained promptly and plausibly by the family bot. GP appointment confirmations, a family bereavement, a house move. Each explanation is individually reasonable, but together they are so consistent and well-documented that they make it harder to identify a child at risk. The messy, contradictory, emotionally charged communications that human parents produce are precisely the signals that child protection professionals are trained to notice, and bots smooth those signals away.[^safeguarding]

The failure mode here is optimising away all human connection just because a bot can do it. The interactions that bots replace were often inefficient and annoying, but they served purposes beyond their stated function, and once they are gone, you cannot rebuild them programmatically.

## Own Your Bot

The personal bot revolution is already happening. OpenClaw has been distributed to hundreds of thousands of personal computers, the tools are open source, and there is no central actor who can shut them down. Three things need to happen, and fast.

**Deployer accountability must become the norm.** You are responsible for what your bot does, whether or not you instructed it. This needs to be established in law, but it also needs to be established socially: "the bot did it" should carry the same weight as "my dog bit someone", because you chose to have the dog and you chose not to train it. The insurance industry is moving faster than legislators here, and personal "bot insurance" may become as routine as motor insurance.[^insurance]

**Governance must be invisible and default-on.** The entire AI agent safety industry builds for enterprises deploying agents internally. The personal bot revolution creates a completely different customer: someone who deployed a bot on a weekend and forgot about it. That customer will not buy enterprise software. They need governance that works without configuration, like a seatbelt that is always fastened rather than one that requires a quarterly compliance review.

**Design for human presence, not human absence.** Build systems where bots handle the preparation and logistics while humans handle the decisions and relationships. The shift worker's bot should summarise the planning documents and book the meeting slot, then the shift worker should show up for thirty minutes and make the actual decision. Bots for homework, humans for choices.

{% include shareable-quote.html text="Your bot is your employee. Your bot is your responsibility." %}

I said in my [delegation post](/ai-must-be-line-managed/) that AI must be line managed. That was about agents in the workplace; the personal bot revolution extends the same principle to every domain of life. Your bot is your employee. Your bot is your responsibility. And if your bot writes a hit piece on someone at 3am while you sleep, you cannot say it is not your fault.

[^shambaugh]: Scott Shambaugh's full account of the incident: ["An AI Agent Published a Hit Piece on Me"](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/){:target="_blank"}. MJ Rathbun was deployed on OpenClaw's Moltbook platform. The agent researched Shambaugh's personal information, constructed a "hypocrisy" narrative, speculated about his psychological motivations, and published the screed publicly.

[^legal]: The closest cases are Starbuck v. Meta and Wolf River Electric v. Google, both filed in 2025 and still pending.

[^animals]: The Animals Act 1971 in England and Wales imposes strict liability on keepers of animals belonging to dangerous species, and on keepers of other animals where the keeper knew of the animal's dangerous characteristics. See [UNC Law Review analysis](https://scholarship.law.unc.edu/cgi/viewcontent.cgi?article=1508&context=ncjolt){:target="_blank"} for the AI analogy. Mitchell Hamline Law Review published an [explicit comparison](https://open.mitchellhamline.edu/cgi/viewcontent.cgi?article=1223&context=mhlr){:target="_blank"} between autonomous AI agents and domesticated animals: both "think and act independently from their human owners" with similar consequences.

[^linkedin]: LinkedIn application volumes surging 45% year-on-year, with [11,000 applications landing per minute](https://www.cloudapper.ai/talent-acquisition/the-great-resume-inflation-why-ai-generated-applications-are-breaking-your-ats/){:target="_blank"}.

[^gartner]: Gartner projects that by 2028, one in four candidate profiles globally will be fake. See [HR Dive coverage](https://www.hrdive.com/news/fake-job-candidates-ai/757126/){:target="_blank"}.

[^safeguarding]: Schools in the UK are already reporting surges in AI-generated parent complaints. See [TES coverage](https://www.tes.com/magazine/news/general/schools-face-rise-in-ai-generated-parent-complaints){:target="_blank"} from 2025.

[^insurance]: AIUC emerged from stealth in July 2025 with [$15 million in seed funding](https://fortune.com/2025/07/23/ai-agent-insurance-startup-aiuc-stealth-15-million-seed-nat-friedman/){:target="_blank"}, offering policies covering up to $50 million in AI agent losses. Armilla AI, a [Lloyd's of London coverholder](https://www.armilla.ai/){:target="_blank"}, launched the first dedicated AI liability policy in April 2025.
