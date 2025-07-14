---
layout: post
title: "Beyond the Demo: Building LLM Applications That Actually Ship"
date: 2025-07-09 10:00:00 +0000
image: /assets/img/google-cloud-llm-talk.jpg
image_portrait: false
categories:
- ai
- talk
- engineering
- llm
event_name: "Google Cloud Summit 2025"
venue: "London"
talk_date: 2025-07-09
talk_url: "https://cloudonair.withgoogle.com/events/london-summit-25/speakers"
talk_title: "Imagine What's Next: Imagine What's Possible"
---

Every team building with LLMs faces the same crushing moment. The demo works perfectly. Stakeholders are impressed. Then you deploy to production and watch it fall apart. What worked flawlessly with test data breaks in ways you never imagined. The carefully crafted system that seemed so promising becomes a source of constant firefighting.

I recently spoke at Google Cloud Summit with [Gunisha Vig](https://www.linkedin.com/in/gunisha-vig-18b950a8/?originalSubdomain=uk) about how to build LLM applications that actually make it to production. Not proof of concepts. Not investor demos. Real systems serving real customers every day.

<!--more-->

The energy in the room was palpable. Investment seems to be on the up, and budget strings are being loosened. There was a genuine excitement from partners and customers alike about the possibilities ahead. When I asked how many had tried AI, perhaps 80 out of 200 hands went up. When I asked how many had AI in production, that number dropped to maybe 4.

This gap perfectly illustrates the challenge. Lots of people are putting a toe in the water with AI, building small proofs of concept. Very few are swimming in the deep end of production systems. My talk was about bridging that gap.

## The Four Questions That Determine Success

Standing in front of a room full of technical leaders, I outlined the four critical questions every team must answer before touching any code. Miss any of these, and you are building an expensive demo, not a product.

**Do you need an LLM?** Most teams start here last. They get excited about the technology and look for places to apply it. This is backwards. At Cherrypick, we had a meal generator since 2023. It worked, but customers wanted more personalisation and explanations for our choices. Traditional approaches would have required complex rule engines or massive manual effort. LLMs gave us natural language explanations that felt personal. That is a problem worth solving with an LLM. [Read the full case study](/case-studies/gpt-meal-generator) to see how we built it.

**What interface matches how users want to work?** Chat is just a construct. It is not the only way to use LLMs. At their core, LLMs are completion engines, and there are far better ways to leverage them. We pre-generate rejection suggestions for our meal plans. Customers get one-tap options instead of having to chat. The LLM works behind the scenes, creating personalised choices without forcing users into conversations. This approach eliminates typing fatigue while maintaining all the personalisation benefits.

**Can you afford it?** We experimented with WhatsApp grocery shopping. It was fun and quick, but required hundreds of LLM calls per shop. The economics destroyed our margins. A chatbot grocery assistant would have eroded our entire profit margin. In contrast, our meal generator requires just a few calls per plan. The limited number of plans each customer generates weekly makes it viable. Do this maths before you build, not after.

**Can you handle the randomness?** LLMs are inherently unpredictable. We learned to work with this, not against it. Instead of sending our full recipe database and hoping the model picks safe options, we only send recipes the customer can actually eat. More tokens, but reliable results. No risk of suggesting meals that could harm someone.

## Building an Evaluation System That Works

The most uncomfortable truth about LLMs is that you cannot test them like regular code. The outputs are not deterministic. You need a completely different approach.

We built a multi-layered evaluation framework that caught issues before they reached customers. First, automated validation checked JSON structure and verified recipe IDs against our context. When generations failed, the system automatically retried. We accept a 25% failure rate because the speed and cost remain acceptable with retries.

The second layer involved expert review. Our Head of Food Sophie assessed sample plans for quality and nutritional balance. She checked flavour combinations and weekly meal variety. Automated checks cannot catch everything. Human expertise remains essential.

Every evaluation became training data. We stored prompt versions, tracked success metrics, and refined continuously. Using Liquid templates for prompts let us test variations systematically. Same data, different prompts, measurable results.

Our next phase will be using LLMs to evaluate LLMs. With thousands of generated plans and their evaluations, we can train models to assess quality and even suggest prompt improvements. The system will begin to optimise itself.

Learning from all this evaluation work, I am building [Kaijo](https://kaijo.ai) to help teams automate this entire process. Instead of manually managing prompts and evaluations, Kaijo handles the complexity of prompt engineering automatically. It continuously evaluates and optimises your AI functions based on the examples you provide.

## Why Most LLM Projects Fail

During the Q&A, someone asked why so many LLM projects never ship. The answer is simple: teams treat them like traditional software projects.

Traditional software is deterministic. You write tests, they pass, you ship. LLMs require probabilistic thinking. You need evaluation frameworks, not unit tests. You need to design for failure, not assume success. You need to constrain the problem space, not give the model unlimited freedom.

I shared our grocery chatbot failure as an example. It worked brilliantly in demos. Customers loved the interaction. But the economics were impossible. Hundreds of API calls per shopping session meant we would lose money on every order. We killed it before launch because we did the maths.

The meal generator succeeded because we learned from that failure. We designed for economical operation from day one. We chose an interface that minimised API calls. We built evaluation systems before we needed them. We shipped something sustainable.

## Results That Matter

The numbers speak for themselves. Customers now change their meal plans 30% less often. They use generated plans in their baskets 14% more. These are not vanity metrics. They directly impact customer satisfaction and business revenue.

But the hidden success is what we built along the way. The evaluation infrastructure became reusable for future AI features. The prompt templating system accelerated experimentation. The team gained confidence working with non-deterministic systems. These foundations matter more than any single feature.

## A Quick Demo That Sparked Discussion

To illustrate how quickly you can prototype with the right tools, I showed the audience something I had built just before the talk. Using BigQuery and some basic LLM integration, I created a natural language BI tool that let non-technical users query our data.

![BigQuery BI Demo](/assets/img/bi-demo-chat.gif)

Google Cloud have been a fantastic partner to Cherrypick over the years, and their infrastructure made experiments like this possible. The combination of BigQuery's power and LLMs' natural language capabilities opens interesting possibilities. But possibilities are not products.

## Starting Your Journey

If you are building with LLMs, start with these principles:

**First, validate the problem genuinely needs LLM capabilities.** Can you explain why traditional approaches fail? If not, use traditional approaches.

**Second, design interfaces that match user behaviour.** Chat is not the default. Find what works for your specific use case.

**Third, calculate costs upfront.** Build spreadsheets. Run scenarios. Know your unit economics before writing code.

**Fourth, embrace non-deterministic outputs.** Build evaluation systems. Design for failure. Constrain the problem space.

**Finally, ship something.** A working system in production teaches you more than any number of prototypes. Start small, measure everything, iterate based on data.

The room left with a clear message. Building LLM applications that ship requires different thinking. Not better prompts. Not newer models. Different thinking about problems, interfaces, costs, and quality. Master those, and you can build the future.

For teams ready to move beyond demos, the path is clear. Stop treating LLMs like magic. Start treating them like tools with specific strengths and limitations. Build systems that leverage those strengths while mitigating the limitations. Ship something real. Learn from production. Iterate based on evidence.

That is how you build LLM applications that actually ship.
