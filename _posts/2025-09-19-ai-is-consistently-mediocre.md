---
layout: post
title: "AI Is Consistently Mediocre. That's Why It's Valuable."
date: 2025-09-19 09:00:00 +0000
categories:
- ai
- productivity
- development
---

I discovered something counterintuitive while building [Kaijo](/kaijo/), my AI judging platform. AIs are consistently inconsistent. Humans are inconsistently inconsistent. This fundamental difference changes everything about how we should deploy AI in our organisations.

Most companies deploy AI expecting immediate competence but get consistency instead. Then they feel disappointed when it makes predictable mistakes rather than brilliant insights. We have the progression backwards.

<!--more-->

## The Framework

After months of building AI evaluation systems and watching teams struggle with AI implementation, I created this framework to explain what I was seeing:

![AI vs Human Progression Framework](/assets/img/ai-vs-human-progression.png)
*AI reaches consistency quickly through prompting, but competence slowly through model improvements. Humans reach competence quickly through training, but consistency slowly through practice.*

The matrix reveals two distinct paths. Humans move from inconsistent incompetence to inconsistent competence relatively quickly through training. We can have flashes of brilliance early on, like when learning an instrument. But maintaining that performance consistently over time requires extensive practice.

AI follows the opposite trajectory. Through better prompting and larger models, AI achieves consistency remarkably quickly. It starts fresh with every prompt, maintaining the same baseline energy and attention. But reaching true competence takes much longer.

This explains so many failed AI implementations I have witnessed.

## The Hidden Advantages of Consistency

Understanding AI's consistency reveals several counterintuitive advantages that most deployments miss. These are not the flashy capabilities shown in demos, but the mundane strengths that deliver real value.

### Consistent Quality, Not Identical Output

When I say AI is consistently inconsistent, I do not mean it produces identical outputs. I mean it maintains a consistent quality level. An AI with a 15% error rate will maintain that 15% error rate whether processing its first item or its thousandth. A human might start at 5% errors but drift to 40% by Friday afternoon.

Consider expense processing. I do not need a brilliant expense processor. I need a mediocre expense processor that never gets tired. An AI that correctly categorises 85% of expenses consistently beats a human who starts at 95% accuracy but drops to 60% after two hours of mind-numbing receipt scanning.

This consistent mediocrity becomes powerful at scale. When converting large datasets or scoring hundreds of candidates, uniform error rates are actually preferable to variable human performance. You can plan for consistent 15% errors. You cannot plan for human variability that ranges from 5% to 40% depending on coffee levels, time of day, or proximity to the weekend.

This connects directly to Daniel Kahneman's research in ["Thinking, Fast and Slow"](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow){:target="_blank"} about noise in human judgment. He found that expert evaluators show alarming variability - the same person evaluating the same case at different times gives different answers. AI eliminates this temporal noise, even if it cannot eliminate all bias.

### The Fresh Context Advantage

One of AI's most underappreciated capabilities emerged clearly in my coding work. When I finish implementing a feature, I cannot objectively evaluate my own code. My brain carries all the context, assumptions, and justifications that led to my implementation choices. I cannot unknow what I know.

An AI starts completely fresh. It can evaluate my code changes with no recent bias, seeing them as a new developer would. While it cannot eliminate all biases from its training, it absolutely can eliminate the specific contextual biases that cloud my judgment immediately after writing code.

This ["reset and refine" principle](/coding-with-ai/#the-power-of-reset-and-refine) extends beyond code review. Any task requiring fresh perspective benefits from AI's ability to start without recent context. Legal document review, content editing, data validation - wherever human familiarity breeds blindness, AI's consistent freshness provides value.

### The Exhaustion Asymmetry

Working with AI reveals a fundamental asymmetry that explains why many teams burn out on AI tools. The AI brings fresh energy to every interaction. It approaches prompt 100 with the same enthusiasm as prompt 1. Meanwhile, I am exhausted by prompt 20.

This creates a unique cognitive strain. With human colleagues, natural rhythms emerge. We both get tired. We take breaks. Energy ebbs and flows in understood patterns. With AI, I am the only one who needs rest. The AI keeps barrelling forward with fresh context every 20 minutes while I desperately need coffee.

Some tasks suit this asymmetry perfectly. Overnight data processing, systematic content review, automated testing - anywhere human exhaustion traditionally limited throughput. But for collaborative creative work requiring sustained human judgment, the exhaustion asymmetry becomes a limiting factor.

## Why We Deploy AI Wrong

The progression framework explains most AI deployment failures I have observed. Companies see demos of AI competence and expect to buy competence off the shelf. Instead, they get consistency. Then they complain the AI makes too many mistakes, not recognising they have purchased the wrong capability for their needs.

Take customer service. Companies deploy chatbots expecting competent problem-solving. Customers encounter consistent mediocrity instead. The chatbot reliably provides 60% accurate responses while customers expect the 90% accuracy a skilled human provides (at least when that human is fresh and motivated).

But flip the use case. Deploy that same chatbot for initial ticket triage and classification - a task where consistent 85% accuracy beats variable human performance - and suddenly the AI delivers value. The key is matching AI's consistency strength to tasks where consistency matters more than peak competence.

## The Discipline Gap

Perhaps the most personally challenging insight from this framework is recognising my own limitations. I am not a naturally consistent person. I have learned some discipline in some areas with years of practice. Yet the AI applies my own documented principles more consistently than I do.

When I write documentation about coding standards or architectural patterns, I might follow them 70% of the time. Various factors - rushing, distraction, assumption that "this case is different" - lead to inconsistency. The AI, reading those same standards, applies them 95% of the time. It becomes more disciplined about my own rules than I am.

This is humbling but powerful. The AI becomes an accountability partner, consistently applying the standards I set in my more thoughtful moments. It catches me when I try to cut corners. It reminds me of my own best practices. It enforces the discipline I aspire to but struggle to maintain.

There is another crucial realisation here. Some tasks I will never be brilliant at. I will only ever achieve consistent mediocrity. Data entry. Expense categorisation. Routine administrative work. The AI is already good at that consistent mediocrity right now. This means I do not have to do these tasks at all. I can focus entirely on work where human judgment, creativity, and inconsistent brilliance actually matter.

## Practical Applications

Understanding the progression framework transforms how we deploy AI. The delegation matrix below shows exactly where to invest AI effort based on consistency and competence requirements:

![How to Delegate Tasks to AI](/assets/img/How To Delegate Tasks To AI.png)
*Match AI capabilities to task requirements: invest where AI performs well independently, reserve complex tasks for human-AI collaboration.*

This framework reveals four distinct deployment strategies:

**Invest Here - AI Can Perform Well Independently**: Tasks requiring most consistency but least competence. Data processing, routine content moderation, systematic quality checks, compliance verification. AI delivers reliable value with minimal human oversight. These become your first AI implementations.

A recent large-scale study demonstrates this perfectly: AI voice recruiters evaluating 70,000 customer service applicants in the Philippines achieved 12% more job offers, 18% more candidate starts, and 17% higher retention than human recruiters, while also reducing gender discrimination.[^1] The AI maintained consistent evaluation criteria that human recruiters struggled to apply uniformly across thousands of interviews.

[^1]: Cowgill, B. & Xie, T. (2024). "Can Large Language Models Transform HR? Evidence from a Field Experiment." Available at SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5395709. Via [Ethan Mollick's analysis](https://www.linkedin.com/posts/emollick_pretty-big-finding-for-ai-in-hr-in-an-experiment-activity-7363232783395098624-8_vz/){:target="_blank"}.

**Marginal Value - Delete or Quickly Outsource**: Tasks requiring least consistency and least competence. Administrative busywork, simple data entry, basic categorisation. Neither humans nor AI should spend significant time here. Eliminate these tasks entirely or outsource cheaply.

**Creativity - Talented Humans Assisted by AI Tools**: Tasks requiring least consistency but most competence. Strategic planning, creative problem-solving, novel architecture decisions. Humans lead with AI providing research, analysis, and implementation support. The human provides insight; AI provides execution.

**The Future - Reserve for Humans, Monitor AI Progress**: Tasks requiring both high consistency and high competence. Complex customer service, medical diagnosis, financial planning. Currently human-only domains where AI serves as research assistant. Monitor AI advancement in these areas for future opportunities.

## The Charlie Chaplin Problem

![Modern Times - Charlie Chaplin](/assets/img/modern-times-chaplin.jpg)
*How many jobs today will look like this to our grandchildren?*

Charlie Chaplin's [Modern Times](https://en.wikipedia.org/wiki/Modern_Times_(film)){:target="_blank"} depicted the dehumanising nature of repetitive industrial work. A human reduced to a cog in a machine, performing the same motion endlessly. We now celebrate that these jobs are disappearing. Humans should not be forced into machine-like consistency. But at the time, this automation created massive social upheaval, much like when these factory jobs were first introduced and people fled the fields to the factories in search of work.

The same pattern emerges in software development. Traditional junior developer tasks involved repetitive work that built competence through practice. Format code to standards. Write unit tests. Fix simple bugs. These tasks provided learning opportunities while delivering value. But these are exactly the tasks where AI's consistency excels.

In my exploration of [coding with AI](/coding-with-ai/), I discovered how AI's consistency helps maintain coding standards and catch errors human reviewers miss when tired. But the progression framework suggests even deeper changes. If AI handles the consistent but mundane work, juniors must jump directly to higher-order thinking. Strategic planning. Architecture decisions. Understanding user needs. Skills that traditionally came after years of groundwork.

Where does that leave inexperienced workers? The optimistic view suggests juniors will leap directly to more strategic, creative work. Paired with AI, they might achieve outcomes previously requiring years of experience. The pessimistic view worries we are removing the bottom rungs of the career ladder. Without foundational practice, will juniors develop the intuition senior roles require? This requires completely rethinking [how we develop talent](/ai-new-dawn-of-software-craft/).

### A New Form of Leverage

Historically, inexperienced workers had only their time to offer. They could not compete with experienced workers on quality, but they could compete on cost and availability. AI fundamentally changes this equation.

An inexperienced worker paired with AI can now achieve consistency similar to an experienced worker. Not the same competence - the experienced worker still excels at complex judgment. But for tasks where consistency matters more than peak performance, the inexperienced-plus-AI combination becomes competitive much sooner in their career.

This accelerates the traditional learning curve. Instead of spending years building consistency through repetition, juniors can focus immediately on developing judgment, creativity, and strategic thinking. They can catch up to senior-level impact in months rather than years.

This could be profoundly democratising. Geographic location, educational background, years of experience - these matter less when AI provides consistent execution. A motivated beginner with good AI tools can compete with established players in ways previously impossible.

### What Companies Miss

The fatal mistake companies make is stopping junior hiring because "AI is more consistent anyway." They see AI handling routine tasks better than inexperienced humans and conclude they no longer need entry-level workers.

This completely misses the point. Humans, even inexperienced ones, have flashes of brilliant competence. Creative insights. Novel connections. Moments of genuine innovation. When you pair those human sparks with AI's relentless consistency, you get something neither could achieve alone.

A junior developer might have one brilliant architectural insight per week. Without AI, they struggle to implement it consistently. With AI handling the routine implementation, that one insight can transform into production-ready code. The junior provides the creative leap; AI provides the disciplined execution. Together, they outperform either alone.

But here's the deeper mistake: if you restrict people to narrow job descriptions, you will never see that brilliant competence. The future demands humans work across roles, spotting connections and opportunities that span departments. Let AI stick to the job descriptions. Humans are [moving to manager work, not maker work](/webinar-how-not-to-screw-up-your-ai-rollout/) - orchestrating, connecting, and directing rather than executing within narrow bounds.

### The Coming Disruption

If companies will not give inexperienced workers a chance, those workers will create new companies that will.

Armed with AI tools that provide consistency, motivated beginners can bootstrap businesses that previously required teams of experienced professionals. A solo founder with AI can maintain consistent quality across marketing, development, customer service, and operations. Not excellent quality, but consistent quality. And for many customers, consistency beats occasional excellence.

We are already seeing this. Solo developers shipping products that previously required entire teams. Small agencies competing with established consultancies. Individual creators building media empires. AI provides the consistency that enables scale without headcount, though [the infrastructure for truly autonomous agents is not quite ready yet](/independent-coding-agents-tools-arent-ready/).

This is not about AI replacing workers. It is about AI enabling workers who lack traditional credentials or experience to compete anyway. The progression framework suggests this is not a temporary arbitrage opportunity but a fundamental shift in how work gets done.

## Conclusion

Understanding that AI provides consistency before competence, while humans achieve competence before consistency, changes everything about deployment strategy. Stop expecting AI to be brilliant. Start expecting AI to be boringly reliable.

For organisations, this means restructuring work around consistency needs versus competence needs. Deploy AI where uniform mediocrity beats variable excellence. Reserve humans for situations requiring judgment, creativity, and the ability to recognise when rules do not apply.

For individuals, especially those early in their careers, AI offers unprecedented leverage. You do not need years of experience to achieve consistent output. You need discipline to manage AI effectively and judgment to know when consistency suffices.

The companies that understand this framework will build fundamentally different organisations. They will separate consistency work from competence work. They will pair inexperienced workers with AI for leverage. They will focus human development on judgment and meta-skills rather than execution.

Most importantly, they will recognise that the question is not whether AI can replace human competence. The question is when consistency matters more than competence. Answer that correctly, and AI becomes a powerful ally. Answer it wrong, and AI becomes expensive disappointment.

The future belongs not to those who achieve perfect human-AI collaboration, but to those who understand which tasks benefit from AI's consistent mediocrity versus human inconsistent brilliance. The framework is simple. The implications are profound. The organisations that grasp this distinction will thrive. Those that do not will wonder why their expensive AI initiatives keep failing to deliver value.

