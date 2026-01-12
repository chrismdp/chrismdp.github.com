---
layout: post
title: "AI: The New Dawn of Software Craft"
date: 2025-05-12 01:03:15 +0100
categories:
- ai
- development
- architecture
- craftsmanship
---

AI is not the death knell for the software crafting movement. With the right architectural constraints, it might just be the catalyst for its rebirth.

The idea that AI could enable a new era of software quality and pride in craft is not as far-fetched as it sounds. I have seen the debate shift from fear of replacement to excitement about new possibilities. The industry is at a crossroads, and the choices we make now will define the next generation of software.

But there is a real danger: most AI coding assistants today do not embody the best practices of our craft. They generate code at speed, but almost never write tests unless explicitly told to. This is not a minor oversight. It is a fundamental flaw that risks undermining the very quality and maintainability we seek. If we do not demand better, we risk letting AI amplify our worst habits rather than our best.

This is the moment to ask whether AI will force us to rediscover what software crafting[^terms] truly means in the AI age.

<!--more-->

[^terms]: I use the term "software craft" to refer to the [software craftsmanship movement](https://manifesto.softwarecraftsmanship.org/) that emerged from the Agile Manifesto and was formalised in the Software Craftsmanship Manifesto of 2009. The movement emphasises well-crafted software, steady value delivery, professional community, and productive partnerships. I prefer the terms "crafting" and "craft" to avoid gender assumptions.

## The Software Craft Agent: A New Premise

AI can be more than a code monkey. Imagine an agent guided by rigorous, off-the-shelf architectural patterns, not just churning out code but building with intent and discipline. If you give AI a really tight architecture, it might produce whole systems more autonomously, and with a level of quality that rivals the best human teams.

This is not a theoretical exercise. Research shows AI thrives in environments where patterns are discernible and constraints are explicit.[^2] I have seen teams where a single early architectural decision made the difference between chaos and clarity[^microservices].

The foundation for a renaissance in software craftsmanship is a strong architecture that lets both humans and machines do their best work.

[^microservices]: At a previous startup, I chose microservices too early and allowed too many languages to proliferate without having a large enough team to require that level of autonomy. This was a mistake and harmed our efficiency.

## The Renaissance We Need

The software industry is at a crossroads. AI coding assistants have led to a surge in productivity, but also a risk of amplifying complexity and technical debt. Without robust architectural oversight, AI-generated code can introduce service duplication, unwanted dependencies, and an uncontrolled sprawl of microservices.[^3]

The answer is not to shun AI, but to pair it with rigorous architectural patterns that act as guardrails. By constraining AI within proven architectural frameworks, we can elevate the quality of the systems it produces. The craftsperson agent is not a replacement for human expertise, but a force multiplier, allowing us to focus on higher-order aspects of design, intent, and user experience.

## Testing and Patterns: The Foundation of AI-Driven Development

Testing remains the backbone of quality in software development. Despite less than one percent of developers using Test Driven Development (TDD) in practice, the rise of AI makes rigorous, test-first approaches more important than ever. AI can generate code rapidly, but without tests, there is no guarantee of correctness, reliability, or maintainability.[^8]

The uncomfortable truth is that unless you explicitly ask for it, coding agents rarely provide tests by default. They tend to write code in the way most developers do: without tests, because that is what the vast majority of code in the wild looks like, and that is what they are trained on. This is a significant gap, and it is holding us back. We should be demanding more from our tools. Why are we accepting agents that cut corners, when we know that test-first and great practices are what make teams truly fast and resilient?

Perhaps the solution is to build this discipline in at the agent level. Imagine a software craft agent that produces well-tested code as the default, not the exception. If this becomes the norm, teams could move much faster over time, with quality and confidence built in from the start. In theory, this approach could become a clear competitive advantage. But it will not happen unless we insist on it.

The renaissance in software craftsmanship will not come from AI alone. It will emerge from a renewed commitment to practices like TDD, continuous integration, and architectural fitness functions. The best results occur when AI is guided by clear, testable requirements and a strong architectural vision. I have observed teams that treat testing as an afterthought struggle with quality and maintainability, while the best teams treat tests as first-class citizens. We must make this the default expectation for our AI tools, not a rare exception.

Patterns serve as the shared language between human and machine. They provide a predictable framework that AI can leverage to understand the roles of different system parts and their interactions.[^4] For example, in an MVC architecture, AI can focus on generating or modifying code for the View component, knowing exactly how it should interact with the Model and Controller.

AI requires structure to excel. The modularity and explicit interfaces provided by these patterns create bounded contexts where it can operate with greater efficacy and precision. I have found this approach valuable [in my own code already](/coding-with-ai).

## Trust, Transparency, and the Human-AI Partnership

Trust is the linchpin of effective AI adoption. Developers need to trust that AI-generated code is not only functional, but also readable, secure, and aligned with architectural principles.[^10] This requires transparency and explainability. AI must be able to show its reasoning, justify its decisions, and provide clear, actionable feedback.

There are limits, of course. AI still struggles with high-level planning, abstraction, and nuanced reasoning over long-term system evolution.[^2] It can hallucinate, generate unsound designs, or introduce subtle bugs. I have seen AI generate code that looked perfect but failed in subtle ways. The lesson is clear: trust, but verify. Human oversight is essential, especially as AI becomes more capable.

The future is not AI versus human, but AI and human in partnership. The most successful teams will be those that embrace the "centaur" model: human architects providing strategic direction, critical evaluation, and contextual understanding, while AI handles the labour-intensive analysis, generation, and verification tasks.[^9]

This partnership is already transforming workflows. Documentation, for example, is no longer a neglected afterthought. With AI, documentation becomes a living, dynamic part of the codebase, continuously updated and aligned with the system's evolution.[^2] I have worked in environments where documentation was always out of date, and with AI, [I have seen it become a living part of the system](/coding-with-ai), always current and always useful. This is a game changer for teams and for the craft.

## The Virtuous Cycle: How Good Architecture Makes AI Better (and Vice Versa)

A well-defined initial architecture acts as an important enabler for AI tools. It provides the structure and clarity that AI needs to interpret, generate, and modify code effectively.[^11] In turn, AI can help maintain architectural integrity, detect drift, and automate compliance checking. This creates a virtuous cycle: good architecture makes AI more effective, and AI helps preserve and enhance architectural quality over time.

This is not just theory. Case studies already show that AI-driven compliance checking can reduce analysis time from weeks to minutes, while identifying thousands of issues and violations.[^12]

When architecture and AI work together, the result is a system that is easier to maintain, scale, and evolve.

This is the future of software craftsmanship.

## The Real Challenge: Training the Next Generation

If AI handles the routine coding tasks, how will junior developers develop the intuition and expertise needed for higher-level work? The answer may lie in pairing[^coding-with-ai], mentorship, and a renewed focus on architectural thinking, complexity recognition, and product intuition. The job was [never just about writing code](/the-job-is-not-to-build). It was about solving problems within constraints, understanding what to build and why, and making intentional design decisions.

I have mentored junior developers who learned more from pairing and architectural discussions than from any amount of solo coding. The next generation will need these skills more than ever, as AI takes over the routine work.

## Takeaways: The Path Forward

AI is not the end of software craftsmanship. It is the beginning of a new era, where the craftsperson agent, guided by rigorous architecture, can produce systems of unprecedented quality and reliability. The renaissance will not come from AI alone, but from the partnership between human expertise and machine precision.

But this partnership will only succeed if we demand more from our tools. We must not settle for AI that cuts corners or skips the disciplines that underpin real speed and quality. Ask your agent for tests, or use an agent that produces well crafted code by default. Insist on test-first, insist on great practices, and let us raise the bar for what AI can and should deliver.

And above all, remember that the true value of software craftsmanship lies not in the code itself, but in the clarity of thought, intent, and design that underpins it.

Thanks to Rob Bowley for comments on a previous version of this post.

---
[^1]: See the original discussion on LinkedIn: [LinkedIn comment](https://www.linkedin.com/feed/update/urn:li:activity:7314173057340702721?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7314173057340702721%2C7314210179871367169%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287314210179871367169%2Curn%3Ali%3Aactivity%3A7314173057340702721%29). This is the original social media thread that inspired the premise of this post, discussing whether AI can be constrained by architecture to produce high-quality systems autonomously.
[^2]: [Artificial Intelligence for Software Architecture: Literature Review and the Road Ahead](https://arxiv.org/html/2504.04334v1). A comprehensive academic survey of the current state and future directions of AI in software architecture, including capabilities, challenges, and open research questions. Also cited for its discussion of AI's role in dynamic documentation, architectural knowledge management, and the current limitations of AI in high-level architectural reasoning and planning.
[^3]: [Rethinking architecture in the age of AI: Findings from our latest research report](https://vfunction.com/blog/rethinking-architecture-in-the-age-of-ai/). This industry report explores the risks and opportunities of AI-driven development, especially the dangers of architectural drift and technical debt without strong architectural guardrails.
[^4]: [Software Architecture Patterns: What Are the Types and Which Is the ...](https://www.turing.com/blog/software-architecture-patterns-types). An accessible overview of major software architecture patterns, their principles, and their impact on system qualities like scalability and maintainability.
[^6]: [The Evolution and Future of Microservices Architecture with AI-Driven Enhancements](https://digitalcommons.lindenwood.edu/cgi/viewcontent.cgi?article=1725&context=faculty-research-papers). This paper examines how microservices architectures are evolving, particularly with the integration of AI-driven tools and techniques.
[^7]: See [Rigorous System Design - ResearchGate](https://www.researchgate.net/publication/266659438_Rigorous_System_Design): a foundational research article on the principles of rigorous system design, including separation of concerns, component-based construction, and correctness-by-construction.
[^8]: [AI-Driven Innovations in Software Engineering: A Review of Current Practices and Future Directions](https://www.mdpi.com/2076-3417/15/3/1344). A peer-reviewed paper on how AI is transforming software engineering, with a focus on productivity, code quality, and the importance of testing and verification.
[^9]: [The Role of AI in Software Architecture: Trends and Innovations](https://www.imaginarycloud.com/blog/ai-in-software-architecture). A practitioner-focused article summarising the latest trends in AI for software architecture, including the "centaur" model of human-AI collaboration.
[^10]: [AI Software Engineer: Programming with Trust - arXiv](https://arxiv.org/html/2502.13767). This paper explores the challenges of trust, explainability, and verification in AI-generated code and architectural decisions.
[^11]: [The Use of AI in Software Architecture - Neueda](https://neueda.com/insights/ai-in-software-architecture/). An industry insight piece on how AI is being used for architectural compliance, governance, and continuous validation in real-world organisations.
[^12]: [Enabling AI to assess code for compliance against software architecture design principles](https://www.turnberrysolutions.com/case-study/enabling-ai-to-assess-code-for-compliance-against-software-architecture-design-principles/). A case study showing how AI tools can automate architectural compliance checking, dramatically reducing analysis time and improving code quality.