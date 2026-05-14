---
layout: post
title: "Webinar: Unblock Your Team"
date: 2026-05-14 16:00:00 +0100
categories:
- ai
- webinar
- teams
- leadership
- productivity
image: /assets/img/greg-ai-coding-tool-outpaced-all-others.jpg
image_portrait: true
infographic: /assets/img/spacex-fix-any-process-infographic.png
series: "AI In Action Webinars"
---

On 14 May 2026, I gave a webinar about why one engineer can be ten times faster with AI and the team can still be delivering twenty percent slower. The opening word in the chat as people came in was "challenging". Then "uneven", then "blocked by BAU", then someone wrote "slop", and I could not tell whether they had typed it themselves or whether their AI had just generated it. The virtual room had named the problem before I had spoken a sentence.

<!--more-->

## Productivity Theatre

There is now enough independent data to call it. Will Lytle at Plandek presented an MIT study at CTO Craft Con in March that found twenty percent of engineers in the study claimed AI made them twenty percent faster, but when you measured the same teams' end-to-end software delivery they were going twenty percent slower[^lytle]. Yigit Darcin from Trendyol, presenting at the same conference, independently found the same thing in a two-thousand-engineer organisation: ninety percent of developers believed they were faster with AI, but the measured delivery showed teams twenty percent slower because of the downstream overhead of teaching the AI, debugging its output, and managing the volume of artefacts and pull requests that come out the other side[^trendyol]. Ryan Greenblatt at Redwood Research has been running a different measurement on the most AI-advanced engineering organisations in the world. The right question, he argues, is not how much faster you feel, but the serial speed-up: how much faster would you need to work to be indifferent between that speed-up and having your AI tools at all? His estimate for engineering at Anthropic and OpenAI in April 2026 was about 1.6 times, against the three-times to twenty-times that people commonly claim[^greenblatt].

## Not the AI

This is a systems problem, not an AI problem and not a people problem. W. Edwards Deming spent the second half of his life arguing that ninety-four percent of the performance of any organisation is a property of the system, and only six percent is down to the people in it[^deming]. A bad system, he said, will beat a good person every time. We took a software delivery lifecycle we had spent decades reasonably optimising and injected a step-change in coding speed into one part of it. The rest of the system breaks because we broke it.

Eli Goldratt's Theory of Constraints picks this up: the system has a single throughput-limiting bottleneck, and improving anywhere else is decoration. AI removes the coding bottleneck, so the constraint moves. Your job as a technical leader is to find where it went, and decide whether to fix it, redesign it, or delete it.

## Three Places It Goes

I see the new constraint show up in three places repeatedly, and each has a different fix.

### Data and Context

The first place the constraint shows up is access. Your AI is fast but blind: it cannot see Zendesk, the data warehouse, the internal wiki, the CRM. So the engineer copy-pastes context in by hand, or worse, does not, and the AI confidently invents an answer about a system it cannot reach. If it can only see ten percent of your business reality, the best output it can give is ten-percent-shaped.

The fix is wiring the AI directly into the systems it needs: Model Context Protocol servers, function calling, plug-in integrations. Microsoft's Co-work is impressive here and, for the first time in a while, gives them an edge over Google for non-technical productivity workflows. Prompt injection and the lethal trifecta are real, so start with read-only tools and bring in engineering before you let the AI write or act. The same logic you would apply to a new junior team member.

This constraint hits hardest in finance, operations, and customer service. Engineers are rarely data-blind because code is already accessible, but everyone else is starved.

### Handoffs and Process

The second place the constraint shows up is where the work passes from one person to the next. The code arrives at [code review faster than reviews can be done](/code-review-is-dying/). Product definitions good enough for a five-day build are not good enough for a twenty-minute build, and the AI happily ships the wrong thing fast. QA is drowning. Deployment pipelines are now the slow part of the loop.

The 2024 DORA report puts it bluntly: AI does not fix a team, it amplifies what is already there[^dora]. The practices that used to mark out the top one percent of engineering teams (trunk-based development, small changes, Ship-Show-Ask routing, good tests, fast CI, switched-on product engineers) are now table stakes for getting any real value out of AI.

When you find the constraint at a handoff, the temptation is to throw automation at it. Resist that. SpaceX's five-step approach is one of the cleanest pieces of process thinking I have come across: make the requirements less dumb, find the owner of each step and delete the step if no one will own it, simplify what is left, accelerate it, *then* automate, last. If you have not had to add back at least ten percent of the process afterwards because you went too far, you did not delete enough.

Most teams skip straight to step five and automate a broken process. That is the win they bought. Deleting process is only safe with the right nets underneath: automated tests, type checks and linters, small changes that are cheap to review and easy to roll back, and Ship-Show-Ask routing so not every change pays the same gate cost.

### Knowledge Stays Stuck

The third place the constraint shows up is at the team boundary. Your data is connected and your process is in shape, and one or two engineers are still dramatically faster with AI while the rest of the team is not. The patterns, the prompts, the workflows, the small tricks that ten-times someone's output stay locked in their head, or worse, locked in their personal chat history. The constraint has shifted from "we do not have AI" to "we do not share AI."

The first instinct is to create a channel: `#ai-tips`, a Notion page, an "AI Wins" wiki. It does not work; the posts go in, nobody reads them. What works is active surfacing: getting the patterns onto people's screens whether they asked for them or not. A client of mine had an engineer who had built a brilliant little query-builder tool using AI. Nobody else on the team knew it existed until he demoed it in a sprint review, and by the end of the week half the team were using it. The channel is the archive; the demo is the surface.

The layer above demos is *skills*: short markdown files that codify how a particular thing is done at this particular company, that can be loaded by anyone's AI to get the benefit. The Perplexity team make this point well in a recent piece on how they design skills internally: you only need a skill when the agent will get the task wrong without special context, or where the behaviour has to be extremely consistent across runs. Writing a skill that restates things the model already knows (their example: a sequence of git commands the model can already execute correctly) is good documentation and a poor skill[^perplexity][^skillbench]. Skills only earn their keep when they contain something the public training set does not have: your company's tone of voice, your team's idiosyncratic conventions, the specific shape of your internal APIs, the way you do code review here.

There are not good tools yet for managing skills as a shared organisational asset, propagating them across teams, and letting non-technical people contribute. GitHub is not the right shape for it: skills are not code. I am building [Airskills](https://airskills.ai) to solve this. It is currently free and very early. If you have a team wrestling with skill propagation, give it a try and tell me what is missing.

## Keep Tweaking

The answer to "what do I do once I have fixed these three constraints?" is that the constraint will have moved again. Fix data, and process is now the slowest part. Fix process, and knowledge is now the slowest part. Fix knowledge, and you might find that pricing, or product definition, or something nobody had thought about is now the slowest part. The job is to notice where the constraint went this week and fix it there. If that sounds exhausting, it is the work of running a team. AI just makes the speed at which the constraint moves quite a lot faster than it used to be.

## Two Q&A Threads Worth Surfacing

**On pull requests.** I am not a fan. PRs came from GitHub's open-source contribution flow, where reviewing code from strangers is essential. Most internal teams do not have that problem but import the pattern anyway. I run almost everything on trunk-based development. If you want someone to review your code, open a PR and have the conversation, but do not make it the default. This is the kind of process step the SpaceX move asks you to question.

**On open-source contributions.** Open-source projects are getting flooded with low-quality AI-generated PRs and are closing them automatically. The model that probably works better in the long run is *incorporation*: contributors submit very good issues with all the context around the problem, and you point your own agent at the issue to write the solution. You incorporate the *idea* rather than accepting the *code*. That is roughly what Airskills does for skills, and it will likely be how a lot of open source ends up working.

## One Thing to Try This Week

Pick one team and run this exercise: find the engineer who feels most productive with AI and the engineer who feels least productive. Sit them in a room together for forty-five minutes. Ask the productive one to demo, in detail, the workflow that has changed their week. Ask the unproductive one to describe, in detail, what they tried last and where it broke down. You will almost certainly identify which of the three constraints is biting on that team within the first twenty minutes, then fix that one.

## Tools and Resources

- [Feedback is the new bottleneck](/feedback-is-the-new-bottleneck/): the longer-form version of the productivity-paradox argument
- [Code review is dying](/code-review-is-dying/): what to do when AI generates faster than humans can review
- [What to put in your AI knowledge base](/what-to-put-in-your-ai-knowledge-base/): getting the data and context constraint right
- [How to use Claude Code skills](/how-to-use-claude-code-skills/): the layer above CLAUDE.md
- [Always be unblocking](/always-be-unblocking/): the broader systems-thinking principle this all rests on
- [Airskills](https://airskills.ai): skill management for teams, currently free

[^lytle]: Will Lytle, Plandek. Presented at CTO Craft Con London, March 2026. Cited an MIT study from 2025.
[^trendyol]: Yigit Darcin, Trendyol. Presented at CTO Craft Con London, March 2026.
[^greenblatt]: Ryan Greenblatt, [My picture of the present in AI](https://www.lesswrong.com/posts/WjaGAA4xCAXeFpyWm/my-picture-of-the-present-in-ai), LessWrong, 7 April 2026.
[^deming]: W. Edwards Deming, *Out of the Crisis*, 2nd edition (MIT Press, 2000), p. 315: "94% belongs to the system (responsibility of management), 6% special."
[^dora]: Google Cloud, [State of DevOps Report 2024](https://cloud.google.com/devops/state-of-devops).
[^perplexity]: Perplexity Research, [Designing, Refining, and Maintaining Agent Skills at Perplexity](https://research.perplexity.ai/articles/designing-refining-and-maintaining-agent-skills-at-perplexity), May 2026. The piece walks through their internal taxonomy of when a skill earns its keep and when it does not.
[^skillbench]: SkillBench (105 researchers, 7,000+ test runs) found that carefully curated skills improved task pass rates by 16.2 percentage points; self-generated skills added zero benefit. A complementary ETH Zurich study on CLAUDE.md files found that auto-generated context files decreased coding task performance by 3% and increased costs by 20%. Both studies confirm the same underlying pattern: generic content already in the model's training set adds noise rather than signal. Only company-specific context — tone of voice, internal conventions, proprietary workflows — provides measurable lift.
