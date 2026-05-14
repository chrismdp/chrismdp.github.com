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
image: /assets/img/unblock-your-team-webinar.jpg
series: "AI In Action Webinars"
---

On 14 May 2026, I gave a webinar about why one engineer can be ten times faster with AI and the team can still be delivering twenty percent slower. The opening word in the chat as people came in was "challenging". Then "uneven", then "blocked by BAU", then someone wrote "slop", and I could not tell whether they had typed it themselves or whether their AI had just generated it. The virtual room had named the problem before I had spoken a sentence.

<!--more-->

## Productivity Theatre

When a single engineer ships ten times faster with AI, you would expect the team's throughput to go up, but it does not, and there is now enough independent data on this to call it.

Will Lytle at Plandek presented an MIT study at CTO Craft Con in March that found twenty percent of engineers in the study claimed AI made them twenty percent faster, but when you measured the same teams' end-to-end software delivery they were going twenty percent slower[^lytle]. Yigit Darcin from Trendyol, presenting at the same conference, independently found the same thing in a two-thousand-engineer organisation: ninety percent of developers believed they were faster with AI, but the measured delivery showed teams twenty percent slower because of the downstream overhead of teaching the AI, debugging its output, and managing the volume of artefacts and pull requests that come out the other side[^trendyol]. Ryan Greenblatt at Redwood Research has been running a different measurement on the most AI-advanced engineering organisations in the world. The right question, he argues, is not how much faster you feel, but the serial speed-up: how much faster would you need to work to be indifferent between that speed-up and having your AI tools at all? His estimate for engineering at Anthropic and OpenAI in April 2026 was about 1.6 times, against the three-times to twenty-times that people commonly claim[^greenblatt].

The individual gain is real, it just does not translate, and something is absorbing it.

## Not the AI

The instinct is to blame the AI or to blame the people, but neither is right. This is a systems problem, and we have known how to think about systems problems for a long time. W. Edwards Deming spent the second half of his life arguing that ninety-four percent of the performance of any organisation is a property of the system, and only six percent is down to the people in it[^deming]. A bad system, he said, will beat a good person every time. Most of what we attribute to engineering culture, hiring quality, or team commitment is system design.

Apply that to AI. We took the software delivery lifecycle, which we had spent a few decades reasonably optimising, and injected a step-change in coding speed into one part of it. Of course the rest of the system feels like it is breaking; we did this to it.

Eli Goldratt picked up where Deming left off. His Theory of Constraints argues that since the system determines the result, improving the system means finding the single point that limits throughput and fixing that. In his business novel *The Goal*, the worked example is a factory floor with new robots in one workstation. Throughput does not improve, because the workstation was not the constraint. The constraint just moves.

AI moves the constraint. Your job as a technical leader is to find where it went, and decide whether to fix it, redesign it, or delete it.

## Three Places It Goes

I see the new constraint show up in three places repeatedly, and each has a different fix. There are others, but these are the big three.

### Data and Context

The first place the constraint shows up is access. Your AI is fast, but it is blind to most of your business. The engineer wants to use AI to investigate a customer support issue, but the AI cannot see Zendesk, cannot query the data warehouse, cannot read the internal wiki, cannot access the CRM. So the engineer manually copy-pastes context in, slowly, by hand, or worse, they do not, and the AI gives a confident answer about a system it has no visibility into. Cheaper models will simply invent a plausible answer when they cannot reach the system you asked them about, and that hallucination then propagates downstream.

If the AI can only see ten percent of your business reality, the best output it can give is ten-percent-shaped. The constraint is access, not model capability. The fix is wiring the AI directly into the systems it needs: Model Context Protocol servers, internal MCP servers, function calling, plug-in integrations. Microsoft's Co-work is impressive in this area and, for the first time in a while, gives them an edge over Google for non-technical productivity workflows.

One caveat: connecting AI to internal systems sounds reckless, and it can be if you are sloppy about it. Prompt injection and the lethal trifecta are real, and you need an engineering team responsible for the design. My recommendation for non-technical teams starting out: start with read-only tools. Let the AI *see* before you let it *act*; the risk profile is very different. A read-only tool that hallucinates costs you a wrong answer. A write tool that hallucinates costs you a wrong email sent to a real customer, or a refund issued for the wrong amount, or a broken deploy. Get value from reads, build trust, then graduate specific high-confidence write actions one at a time. The same logic you would apply to a new junior team member.

This constraint hits hardest in finance, operations, and customer service teams. Engineers tend not to be data-blind because code is already accessible, but everyone else is starved.

### Handoffs and Process

The second place the constraint shows up is where the work passes from one person to the next. The code arrives at code review faster than reviews can be done. The product definition that was good enough to start a five-day build is not good enough to start a twenty-minute build, and the AI happily ships the wrong thing fast. QA was sized for the old throughput and is now drowning. Deployment pipelines that took thirty minutes are now the slow part of the loop.

I keep seeing the same pattern in the companies I work with. Code generation is no longer the bottleneck, so the bottleneck has moved one stage to the right. The 2024 DORA report puts it bluntly: AI does not fix a team, it amplifies what is already there[^dora]. If your delivery system is good, AI makes it better; if it is broken, AI makes the brokenness more obvious, faster. The practices that used to mark out the top one percent of engineering teams (trunk-based development, small changes, Ship-Show-Ask routing, good tests, fast CI, switched-on product engineers) are now table stakes for getting any real value out of AI.

When you find the constraint at a handoff, the temptation is to throw automation at it, but resist that until you have done the harder work first. There is a five-step approach used at SpaceX which is one of the cleanest pieces of process thinking I have come across. Make the requirements less dumb. Find the owner of each step and delete the step if no one will own it. Simplify what is left. Accelerate it. *Then* automate, last. If you have not had to add back at least ten percent of the process afterwards because you went too far, you did not delete enough.

Most teams skip straight to step five and automate a broken process, so now they have a faster broken process. That is the win they bought. Before you automate anything, ask whether the step should exist at all.

Deleting process sounds reckless, and it is, unless you have the safety nets in place: automated tests catching the regressions you would otherwise catch by hand, type checking and linters covering a class of review effort, small changes that are cheap to review and easy to roll back, and a Ship-Show-Ask routing pattern so not every change pays the same gate cost. With those in place, deleting process is the highest-leverage move available to you.

### Knowledge Stays Stuck

The third place the constraint shows up is at the team boundary. You have got your data connected and your process is in shape, and you still find that one or two engineers are dramatically faster with AI while the rest of the team is not. The wins are real and exist at the individual level, they just do not transfer. The patterns, the prompts, the workflows, the small tricks that ten-times someone's output stay locked in their head, or worse, locked in their personal chat history.

Until the team has those patterns, the team does not benefit. The constraint has just shifted from "we do not have AI" to "we do not share AI."

The first instinct teams have is to create a channel: `#ai-tips`, a Notion page, an "AI Wins" wiki. It does not work; the posts go in, nobody reads them. What works is active surfacing: getting the patterns onto people's screens whether they asked for them or not. A client of mine had an engineer who had built a brilliant little query-builder tool using AI. Nobody else on the team knew it existed until he demoed it in a sprint review, and by the end of the week half the team were using it. The channel is the archive; the demo is the surface.

The layer above demos is *skills*: short markdown files that codify how a particular thing is done at this particular company, that can be loaded by anyone's AI to get the benefit. The Perplexity team make this point well in a recent piece on how they design skills internally: you only need a skill when the agent will get the task wrong without special context, or where the behaviour has to be extremely consistent across runs. Writing a skill that restates things the model already knows (their example: a sequence of git commands the model can already execute correctly) is good documentation and a poor skill[^perplexity][^skillbench]. Skills only earn their keep when they contain something the public training set does not have: your company's tone of voice, your team's idiosyncratic conventions, the specific shape of your internal APIs, the way you do code review here.

This is where I am putting most of my building energy at the moment, because there are not good tools yet for managing skills as a shared organisational asset, propagating them across teams, and letting non-technical people contribute. GitHub is not the right shape for this: skills are not code, and they should not be managed with diffs and pull requests. I have a tool called [Airskills](https://airskills.ai) that I demoed briefly at the end of the session. It is currently free, very early, and people are signing up faster than I can keep up with. If you have a team and you are wrestling with skill propagation, give it a try and tell me what is missing.

## Keep Tweaking

The answer to "what do I do once I have fixed these three constraints?" is that the constraint will have moved again. Fix data, and process is now the slowest part. Fix process, and knowledge is now the slowest part. Fix knowledge, and you might find that pricing, or product definition, or something nobody had thought about is now the slowest part. The job is to notice where the constraint went this week and fix it there. If that sounds exhausting, it is the work of running a team. AI just makes the speed at which the constraint moves quite a lot faster than it used to be.

## Q&A Worth Surfacing

**On pull requests.** I am not a fan. PRs are an artefact GitHub invented, and a lot of teams import them without questioning whether they need them. I run almost everything on trunk-based development. I will sometimes open a PR to run the CI, but it lives for less than an hour. If you want someone to review your code, open a PR and have the conversation, but do not make it the default. This is the kind of process step the SpaceX move asks you to question.

**On reading specs versus reading code.** We are not at the point where the spec is a higher abstraction than the code in the way C was over assembly, and we are still responsible for the code being shipped. My own pattern: write a short spec as a bookmark for the conversation you are having about what to build, let the agent implement it, then read the code. If the change is small enough, reviewing the code is cheap; if you cannot get to "small enough", that is itself the constraint you need to fix.

**On small commits being out of date now that AI can write big ones.** Small changes are how you manage risk and blast radius, and they are not out of date. AIs are capable of making lots of small changes in a row, and mine do. The argument that big PRs make sense because AI can write them quickly confuses generation speed with verification speed. The verification side does not get faster the way generation does, which is what David Crawshaw at Tailscale identified as the principal-agent problem in AI-assisted development.

**On QA and end-to-end tests.** AI is good at writing end-to-end tests. If you have no end-to-end coverage today, get AI to write some, and you have a high-leverage place to start. The bottleneck in QA is rarely "we need more tests written"; it is usually the human effort of running through scenarios. AI can help you build a test plan and then check the output against it.

**On open-source contributions.** We are heading for a shift. Open-source projects are getting flooded with low-quality AI-generated PRs and are closing them automatically. The model that probably works better in the long run is what I have been calling *incorporation*: contributors submit very good issues with all the context around the problem, and you point your own agent at the issue to write the solution. You incorporate the *idea* rather than accepting the *code*. That is roughly what Airskills does for skills, and it will likely be how a lot of open source ends up working.

## Key Takeaway

AI does not fix a team, it moves the constraint. Your job as a technical leader is to notice where the constraint moved to and fix the system at that point, not to deploy AI. Three places to look first: whether the AI can see your data, whether the work is piling up at handoffs, and whether the wins of your best AI user are reaching the rest of the team.

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
