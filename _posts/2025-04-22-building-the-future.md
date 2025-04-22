---
title: "Building the Future"
date: 2025-04-22 09:00:00 +0100
categories:
- ai
- product
- business
---

![A diagram of the future of AI agents](/assets/img/building-the-future.jpeg)

Something has been on my mind for months. The rapid evolution of AI agents has opened up possibilities I cannot ignore.

We are witnessing the emergence of semi autonomous agents that will fundamentally reshape how we work and communicate. The opportunities in this space are extraordinary. I am diving deeper into this world of AI agent development and product creation.

**My newsletter is evolving.** Instead of dispensing tips from a position of authority, I invite you on a journey of discovery. I will document my experiences building with AI, how to apply my tech experience in a new world, and navigating the inevitable struggles and setbacks.

Read on for several key areas I am exploring.

<!--more-->

## Beyond Prompting

The limitations of prompting as a primary interface for AI systems are becoming increasingly apparent. As I explored [in my previous post](/beyond-prompting), prompting is fundamentally broken as an approach to working with AI. It is brittle, model-specific, and endlessly repetitive.

The solution lies not in getting better at prompting, but in moving beyond it entirely. We need to develop higher-level abstractions that hide complexity while preserving control over what matters. This evolution mirrors the progression from machine code to high-level programming languages in traditional software development.

The emergence of frameworks like DSPy and Langchain are early attempts at this, though none have yet provided a complete solution. The right abstractions will make prompting as obsolete as punch cards, allowing us to focus on what truly matters: the inputs, outputs, and evaluation metrics that define our applications.

I have lots more ideas on this topic. I will be writing more about it very soon.

## Agent Communication and Rollback

The emergence of protocols like A2A and MCP raises questions about the future of multi-agent systems. These standardised communication frameworks are onnly a starting point, but they will shape how agents interact and collaborate at least short term. We must understand what new capabilities these protocols will enable and how they will evolve.

The new workflow with AI agents is taking shape. Customers want AI decisions to be reversible and trackable, and to be able to reset to previous checkpoints on demand. This presents unique challenges. The traditional Git source control model (itself only 20 years old) may translate well from code to the results of agent actions, but it may not suffice. We need to consider whether to adapt existing version control systems or create entirely new ones. 

Branching strategies must also account for multiple collaborating agents. The concept of "undo" takes on new meaning in an autonomous context. What about actions with side effects that are not reversible, like sending an email? How do you recover? How do we manage the complexity of coordinating multiple agents which might need to undo state changes? This is already hard for humans, requiring flexibility and adaptability. How can we systemise these interactions?

Universal interfaces will become crucial for tracking and managing collective agent actions. New chat interfaces may be necessary to coordinate complex human-agent interactions effectively.

## Beyond RAG: The Next Generation of Knowledge for Personalised Agents

Building agents that truly understand their users requires sophisticated knowledge management. We must determine whether agents should share knowledge or maintain separate knowledge bases. Enabling meaningful cross-domain conversations presents its own set of challenges.

Selective memory management could optimise agent capabilities, but implementation details remain unclear. Current RAG implementations need advancement, but the path forward is uncertain. Graph based RAG may offer solutions, but alternative approaches could prove more effective.

The development of custom communication protocols by agents themselves raises important questions about risk management and control. We must carefully consider the implications of allowing agents to evolve their own communication methods[^2027].

[^2027]: The [AI 2027 report](https://ai-2027.com) highlights a critical concern about the opacity of advanced AI systems. As we build increasingly sophisticated agents, we risk creating systems whose inner workings we cannot fully understand or control. Without proper transparency and interpretability, we may find ourselves relying on systems that make decisions we cannot explain or verify and which could develop sophisticated methods to evade alignment beyond our understanding. We must build systems that maintain human oversight and understanding even as they grow more capable.

## The Vision

My hypothesis is simple: by sharing this journey openly, documenting both successes and failures, we can learn together how to build meaningful products in the age of AI. The questions I am exploring feel fundamental to our future.

If you are interested in following this journey more closely, subscribe to my newsletter. You will get weekly field notes of what I am learning and building with AI, complete with raw insights and lessons learned.

The future of work is being reshaped before our eyes. I want to be part of that transformation. Will you join me? 

<img src="/assets/img/ai-portal.jpeg" alt="Join me on my AI journey" style='border-radius: 12px; margin:0 0 24px 0; width:50%'/>