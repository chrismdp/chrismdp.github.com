---
layout: post
title: "Webinar: Are We Behind in AI?"
date: 2026-01-08 14:00:00 +0000
series: "AI In Action Webinars"
categories:
- ai
- webinar
- leadership
image: /assets/img/am-i-behind-in-ai-webinar.jpg
---

On 8th January 2026, I gave a webinar tackling a question that preoccupies every technical leader I speak to: am I behind in AI? The data is confusing. Gartner says 88% of organisations have not realised significant value from AI tools. [^1] Stanford says productivity gains of 14% to 66% are possible when AI is done right. [^2] [^3] Some early adopters are struggling whilst late starters are thriving, and something strange is happening.

The short answer is no, you have not missed the boat. But the longer answer requires examining what we mean by AI, who we are talking about, and how we measure progress.

<!--more-->

## Why You Have Not Missed the Boat

The psychological phenomenon of feeling behind comes from a happy accident. When OpenAI put a chat window in front of GPT and released it expecting modest academic interest, it captured the business imagination overnight. Suddenly everyone felt like they were missing out.

But AI has existed as a field for decades: symbolic AI gave us rules-based systems, machine learning brought statistical approaches like regression, deep learning introduced neural networks, and generative AI is simply the latest development rather than a sudden revolution. The progress has been reasonably steady, and what changed was accessibility. The visceral usefulness of a chat interface made AI feel immediate in a way that building logistic regression models never did.

That accessibility triggered panic. Organisations rushed to put AI into products, then discovered chatbots could be convinced to sell cars for a dollar. They retreated to internal tools, hit problems there too, and finally realised they should have started with personal productivity. The sensible route through AI adoption moves through three stages: start with personal productivity to understand what the tools can actually do, then build internal tools where mistakes are contained, and only then expose AI in products to the wider world where the stakes are highest.

Organisations that already have strong data infrastructure and machine learning models in production have many of the raw ingredients for success. But generative AI offers unique tools that help latecomers catch up quickly. It handles messy data at scale remarkably well, so if you have not touched AI before, you can still move fast.

## Where People Actually Stand

A study last year found that 31% of people in organisations are actively sabotaging their AI rollouts. Among Gen Z workers, that rises to 41%. [^4] Far from passive resistance, this represents deliberate obstruction. Understanding [how not to screw up your AI rollout](/webinar-how-not-to-screw-up-your-ai-rollout/) means addressing this human element first. The rise of generative AI is as much a people problem as a technical one, perhaps more so.

Most people progress through predictable stages when using AI personally. They start using it like advanced Google, asking for facts or translations. Then they discover they can ask it to interview them, to help them think through problems by asking questions one at a time. That leap [beyond autocomplete](/ai-for-rest-of-us-beyond-autocomplete/) transforms AI from a tool into a [thinking partner](/writing-and-thinking-with-ai-why-repositories-beat-chatbots/). Beyond that, people customise with GPTs or give it repeatable rules. The most advanced users string whole workflows together. Yet 80% to 90% of people I speak to are still at the first stage. If you have moved beyond using AI like Google, you are already ahead.

Coders move at a different speed because their tools have evolved rapidly. Many started with autocomplete, found it unhelpful, and gave up. Inline assist was better, but the real benefits come from [learning to code with AI properly](/coding-with-ai/). The significant shift came around December 2024 when agent mode in tools like Cursor became genuinely useful, powered by models like Claude 3.5 Sonnet. [Claude Code](/claude-code-is-for-everything/) pushed things further still, removing the need for a coding editor entirely. And now orchestrators like Gas Town and Ralph Mode push into territory where agents work with increasing autonomy.

If you are still writing most of the code yourself, you are behind the cutting edge. Personally, I write about 1% of the code I ship these days. I still read and review every PR, and that remains important, but the days of developers writing most of their code are numbered. If you are experimenting with agent mode, you are roughly where many coders are at. If you are using cloud-based orchestrators with high autonomy, you are at the bleeding edge. Most people are not there yet.

## Readiness Matters More Than Adoption

Many leaders measure adoption by asking how many people are using AI, but readiness is the more important question: are we set up for AI to succeed? One report showed that 77% of employees take AI training when offered, but only 42% know how to identify where AI could improve their work. [^5] They are taking the training but cannot apply it, which points to a readiness problem rather than an adoption problem.

Consider a quadrant with adoption on one axis and readiness on the other.

![Readiness vs Adoption quadrant showing four zones: Sweet Spot (high readiness, low adoption), Peak Performance (high readiness, high adoption), Fix Foundations (low readiness, low adoption), and Danger Zone (low readiness, high adoption)](/assets/img/readiness-adoption-quadrant.png)

High adoption with high readiness is peak performance: AI use grows and flourishes under proper supervision, like a well-tended plant. That is where the 14% to 66% productivity gains live. High readiness with low adoption is the sweet spot for investment: the path ahead is clear, train your team and get running. Low adoption with low readiness means you need to fix foundations first: get out the toolbox and the blueprints, then use AI to pay down technical debt. You do not need many collaborators. If it fails, you have not affected system behaviour. If it succeeds, you improve the codebase for both humans and AI. The existing tests tell you if it worked.

The danger zone is high adoption with low readiness: running hard on a treadmill, going nowhere. This is characterised by poor testing, unclear compliance, and undocumented processes, and when AI proliferates without these quality controls, instability rises, progress slows, and data exfiltrates.

For production coding teams, readiness means great DORA metrics with quick test suites that have good coverage, deploying multiple times a day, and everyone confident to change code. This is [the XP renaissance](/ai-new-dawn-of-software-craft/) many of us have been advocating for years. If your code is hard for humans to work with, it will be hard for AI too. For non-production coding teams like data scientists and analysts, readiness means data in accessible formats where AI can run queries successfully, good experiment management, and proper versioning. For non-technical teams, readiness means rigorous, repeatable, well-documented processes. If people operate in a fuzzy way, just getting things done without clear workflows, AI cannot identify which parts to automate. Document the processes first, then look for automation opportunities.

Whether you are behind depends on your team, your readiness, and your organisational bottleneck. That bottleneck is rarely coding speed. I talk to companies where developers race ahead with AI whilst nothing gets done faster. Cloud bills rise, vendor invoices pile up, but outcomes stay flat. [Coding was never the constraint](/why-ai-fast-teams-still-ship-slowly/). If you are here asking whether you are behind, you probably are not. The people who are behind think AI is a fad that will pass. It will not.

## What to Do Next

Prioritise readiness over adoption. Well-documented processes, good testing, and accessible data are the foundations that determine whether AI amplifies your organisation or destabilises it. Measure readiness before measuring how many people have subscriptions.

Then ask yourself where you sit on the personal AI adoption curve. If you are still using it like Google, asking for facts and translations, try asking it to interview you about a problem you are wrestling with. Say: "Ask me one question at a time to help me understand why this project is stuck." That single shift from answer-getter to thinking partner is where the most significant benefits begin.

## Tools and Resources

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code){:target="_blank"}: Agent-based coding assistant that works without an IDE. See my post on [using Claude Code for thinking and writing](/claude-code-is-for-everything/).
- [Gas Town](https://github.com/sjalq/gas-town){:target="_blank"}: Experimental orchestrator for high-autonomy agent workflows by Steven Jay
- [Ralph Mode](https://github.com/sjalq/ralph-mode){:target="_blank"}: Plugin that runs Claude Code in a loop for continuous task completion
- [AI Leader Accelerator](/ai-leader-accelerator/): Eight-week cohort course for senior technical leaders working through AI adoption

[^1]: [Gartner Survey Shows 88% of HR Leaders Say Their Organizations Have Not Realized Significant Business Value from AI Tools](https://www.gartner.com/en/newsroom/press-releases/2025-10-28-gartner-survey-shows-88-percent-of-hr-leaders-say-their-organizations-have-not-realized-significant-business-value-from-ai-tools){:target="_blank"}, Gartner, 2025.
[^2]: [Stanford and MIT study: A.I. boosted worker productivity by 14%](https://www.cnbc.com/2023/04/25/stanford-and-mit-study-ai-boosted-worker-productivity-by-14percent.html){:target="_blank"}, April 2023. This study predates the current generation of AI tools and likely understates current productivity gains.
[^3]: [AI Improves Employee Productivity by 66%](https://www.nngroup.com/articles/ai-tools-productivity-gains/){:target="_blank"}, Nielsen Norman Group meta-analysis of studies from Stanford, MIT, and Microsoft Research.
[^4]: [31% of Employees Are Sabotaging Your Gen AI Strategy](https://www.cio.com/article/4022953/31-of-employees-are-sabotaging-your-gen-ai-strategy.html){:target="_blank"}, Writer AI Survey, March 2025. The survey polled 800 C-suite executives and 800 employees. Reasons include job fears, dissatisfaction with AI tools, and concerns about quality.
[^5]: Same Gartner survey, 2025. The study of 2,986 employees also found that 65% are excited to use AI for work, and those in AI-relevant roles save an average of 1.5 hours per day.
