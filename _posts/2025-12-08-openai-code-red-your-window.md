---
layout: post
title: "OpenAI's Code Red Is Your Window"
date: 2025-12-08 09:00:00 +0000
image: /assets/img/openai-code-red.png
infographic: /assets/img/openai-code-red-infographic.jpg
categories:
- ai
- strategy
- business
---

Sam Altman declared "code red" at OpenAI last week, marshalling resources to improve ChatGPT as Gemini 3 and Claude Opus 4.5 gain ground. The company is delaying advertising, health agents, shopping agents, and the Pulse personal assistant to focus on catching up on benchmarks.[^code-red]

I have been trying to understand OpenAI's strategy for a while now, and the code red makes it harder, not easier. But that confusion is actually good news if you are building products with AI.

<!--more-->

## The Strategic Puzzle

Every technology company eventually decides: are you a product business using technology to create great user experiences, or are you a platform business building infrastructure others depend on?

Apple chose product. They control hardware, software, and services to deliver experiences competitors cannot match. Amazon chose platform. AWS serves competitors because infrastructure revenue matters more than protecting retail margins.

OpenAI appears to be choosing both. ChatGPT with 800 million weekly users suggests a product business. The API serving developers worldwide suggests a platform business. AgentKit commoditising agent prototyping suggests a platform play.[^agentkit] Atlas browser suggests a product play.[^atlas] Health agents, shopping agents, advertising, hardware with Jony Ive... the list keeps growing.

The code red response to Gemini 3 is revealing. If OpenAI were primarily a product business, they would respond by doubling down on user experience, personalisation, workflow integration. The things that create switching costs regardless of which model sits underneath.

Instead, they delayed the product initiatives to focus on benchmark performance. That is what a model business does. But models commoditise. Benchmark leadership is temporary by definition. You cannot win a commoditisation race by running faster.

I am not saying they are wrong. I am saying the only strategy I can see is "do everything and bet on AI eventually solving it," and that matters for anyone building in this space.

## The Bitter Lesson Bet

There is an implicit bet behind OpenAI's approach. The "bitter lesson" in AI research holds that general methods leveraging computation ultimately outperform approaches that leverage human knowledge.[^bitter-lesson] Scale and compute solve problems better than clever engineering.

Applied to products, the bet is that making the model good enough will magically improve the product experience, that a sufficiently capable model removes the need for careful product design, that AGI solves the UX problem.

That is a big bet. It might even be right eventually. But "eventually" could be years.

## Why This Bet Differs From Apple

Apple's hardware has never been the best on specs. The original Macintosh was underpowered compared to IBM PCs. The iPhone launched without 3G, copy-paste, or third-party apps. Today, Android phones routinely beat iPhones on processor benchmarks, camera megapixels, and RAM. It has never mattered.

Apple won because they built better products, not better components. The experience of using a Mac or iPhone exceeded what spec sheets could capture. Customers pay a premium for that integration, not for benchmark leadership. You accept that components commoditise and compete on the layer above: the experience of using the thing.

OpenAI is doing the opposite. They declared code red to chase Gemini 3 on benchmarks. That is component thinking, not product thinking.

But there is a deeper problem with applying the Apple playbook to AI. Apple's vertical integration succeeds because each layer is stable enough to build upon. The iPhone hardware changes annually in predictable ways. iOS provides consistent APIs. Developers invest knowing the foundation will not shift beneath them.

OpenAI's stack has no stable layer. Models improve unpredictably. Capabilities emerge without warning. The product experience built on GPT-4 differs fundamentally from what GPT-5 enables. Each model generation potentially obsoletes the product assumptions above it.

When Apple improves the A-series chip, iPhone apps get faster. When OpenAI improves their models, ChatGPT might need complete redesign. The tight integration that benefits Apple creates fragility for OpenAI.

This explains why ChatGPT's user experience remains uneven despite massive investment. They are building a product on foundations that shift every few months. And perhaps why they are betting on the bitter lesson rather than doubling down on product craft.

## Your Window

OpenAI is spread across model benchmarks, agent tooling, browsers, health, shopping, advertising, and hardware. They cannot focus on your specific product vertical because they are trying to do everything.

That means you can do what they cannot: build the compelling user experience for your specific domain, solve the particular problems your customers face, do the hard product work that creates genuine switching costs.

As I explored when [analysing AgentKit's impact](/openai-devday-where-value-lives-in-ai-agent-tooling/), commoditising prototyping actually creates the market for production tools. OpenAI makes it easy to start. You make it work for real.

The same pattern applies to products. OpenAI provides increasingly capable building blocks. You assemble them into something that solves a real problem better than a general-purpose assistant ever could.

Stop waiting for the magical agent that solves everything. Current AI capabilities are extraordinary, and the gap is thoughtful product design that applies those capabilities to specific problems, not capability itself. Your product focus beats their scattered attention.

The window will not stay open forever. Eventually, capabilities might reach the point where general solutions outcompete specific ones. But we are not there yet, and betting your company on "eventually" is not a strategy.

OpenAI's identity crisis is your opening.


[^code-red]: Details from [Fortune's coverage](https://fortune.com/2025/12/02/sam-altman-declares-code-red-google-gemini-ceo-sundar-pichai/){:target="_blank"} of Altman's internal memo.

[^agentkit]: See my analysis of [where value lives in AI agent tooling](/openai-devday-where-value-lives-in-ai-agent-tooling/) for how AgentKit commoditises prototyping whilst creating the market for production tools.

[^atlas]: I explored the browser play in [Who wants a browser?](/who-wants-a-browser/) - browsers are transitional technology for agent integration, not the endgame.

[^bitter-lesson]: Rich Sutton's 2019 essay [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html){:target="_blank"} argues that 70 years of AI research shows general methods leveraging computation beat hand-crafted approaches. Chess, Go, speech recognition, computer vision - breakthrough progress came from scaling search and learning, not encoding expert knowledge. I explored [what this means for testing frontier models](/how-to-react-to-a-new-frontier-model/#the-bitter-lesson-for-frontier-model-testing) when Gemini 3 launched.
