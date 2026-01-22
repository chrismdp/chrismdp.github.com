---
layout: post
title: "Advanced Prompting: How to Put AI to Work"
date: 2025-10-02 14:00:00 +0100
image: /assets/img/advanced-prompting-webinar.png
series: "AI In Action Webinars"
categories:
- ai
- webinar
- productivity
---

On 2nd October, I gave a webinar about advanced prompting techniques that transform AI from a frustrating chatbot into a genuinely useful work tool. Whilst 90% of people now use AI at work, only 40% of companies have actually purchased AI subscriptions. This gap reveals a fundamental problem: most people are using AI poorly, producing what Harvard Business Review calls "work slop", output that looks professional but meaningfully advances nothing.

The difference between effective and ineffective AI use is not the tool you choose. It is understanding what AI actually is and how to give it exactly the right context to produce useful results.

<!--more-->

## What AI Actually Does

Large language models do one thing: they predict the next word in a sequence. That is it. They are not databases. They are not search engines. They are prediction engines trained on vast amounts of text to figure out what word most likely comes next.

When you type "the cat sat quietly purring on the", the model examines every word it knows and calculates probability. "Dog"? Unlikely. "Banana"? Definitely not. "Mat"? Yes, that fits. The model generates that token because it was the statistically most likely thing based on everything it has seen before.

This simple mechanism powers everything ChatGPT, Claude, and Gemini do. They cannot tell fact from fiction. They only predict what sounds plausible based on their training data.

Understanding this changes how you use AI. If you ask it to "complete the sentence: Apple's Q2 2035 results were", it might generate science fiction rather than facts because it cannot distinguish future speculation from past reporting. Modern AI tools work around this with additional systems, like web search integration, but the core model remains a prediction engine.

## The Context Problem

Every AI interaction involves layers you control and layers you do not:

**You control:**
- Your prompt (the message you type)
- The conversation history (previous messages in the chat)
- Custom instructions (system prompts in gems, custom GPTs, or Claude projects)
- Knowledge files (PDFs, docs, or other reference materials you provide)

**You do not control:**
- The underlying training data
- The base system prompt (instructions telling AI to be helpful, avoid harm, etc.)
- The reward training (how the model was taught to respond to certain types of questions)

The challenge is giving AI just enough context to produce good results without overwhelming it with irrelevant information. Too little context produces bland, generic output. Too much context causes confusion and hallucination, as the model cannot determine what matters most.

Just like a team with 10 priorities has no priorities, an AI with 1,000 pieces of context cannot figure out what actually matters.

## The Power of Questions

The single most important technique I have learned is this: ask AI to ask you questions.

The magic phrase is simple:

> "Ask me one question at a time to help me think through [whatever problem you are facing]."

This works for anything. Marketing strategies. Difficult conversations with your CEO. Technical problems. Project planning. Even meta-questions like "how to get the most out of this webinar".

I emphasise "one question at a time" because AI tends to generate 10 questions at once. By question four, your brain is overwhelmed and you are no longer thinking clearly. One question forces you to engage deeply with each answer.

What happens is remarkable. The AI asks a question. You answer. It uses your answer to ask a better follow-up question. Then another. Then another. Before you know it, you have figured out the answer to your own problem.

This is not outsourcing your thinking to AI. This is using AI to augment your thinking. You provide the knowledge and judgement. AI provides the structured questioning that helps you articulate what you already know but have not yet organised.

When I demonstrated this with a teacup marketing strategy, the AI immediately started probing: Who is the target customer? Why would they want teacups? What style? Within three questions, I had gone from a vague idea to something specific: novelty teacups for 20-year-old men who want to drink beer ironically from movie-quote mugs.

At the end of this process, ask AI to summarise everything you discussed. You now have a structured brief you can paste into a new chat or share with colleagues.

## Meta-Prompting: Teaching AI How to Think

Beyond asking questions about specific problems, you can ask AI to help you write better prompts. This is meta-prompting: getting AI to prompt AI.

Instead of struggling to create the perfect marketing strategy prompt yourself, ask:

> "Ask me one question at a time to help me come up with a really good specific prompt for creating marketing strategies."

The AI will interview you about your goals, target audience, constraints, and output preferences. Then it will write a comprehensive prompt template you can reuse.

I did this live during the webinar. After answering a few questions about targeting college students with revenue growth goals and wanting markdown output broken down by social media platform, Gemini generated a complete prompt structure I could use repeatedly.

The key is being specific about what you want and how you want it formatted. AI is a predictor, not a mind reader. If you leave gaps in your requirements, it will make things up. If you specify exactly what you need, including output format, it has much less room to hallucinate.

This is particularly powerful because you can take that generated prompt, paste it into a new chat, and immediately get results in exactly the format you specified.

## The Prompt Cycle

Effective prompting is iterative. Here is the workflow I use for any repeatable task:

**Start with context.** If you have organisational information that applies broadly, company values, brand colours, writing style, put it in a Google Doc. Do not use too much. Just enough to get started.

**Use meta-prompting.** Ask AI to interview you and create a basic prompt. Do not spend too much time perfecting this. Get something workable quickly.

**Try it.** Test your prompt on a specific task. See how it does.

**Decide quickly.** If the output is 80% good, continue refining within that chat. If it is less than 80% good or makes fundamental mistakes, throw it away and start over with an improved prompt.

This is counterintuitive. People see all that generated content and think, "I cannot waste all that work." But it did not take hours. It took seconds. It is much faster to retry with a better prompt than to spend an hour arguing with AI to fix output from a bad prompt.

Never argue with AI. If you find yourself going back and forth saying "no, that is not quite right", stop. The conversation history is polluting the context. Just like telling someone "do not think about elephants" makes them think about elephants, telling AI repeatedly what not to do fills its context with exactly the wrong information.

Throw it away. Refine your prompt. Start fresh.

**Update your rules.** When you finally get good output, ask: "What did you wish you knew at the start that would have helped you do a better job first time?"

AI will suggest improvements to your prompt. Add those. Next time, your results will be 1% better. Do this daily for three months and you will have an incredibly powerful, refined prompt.

## Custom AI: Making It Repeatable

Once you have a prompt that works, it becomes tedious to paste instructions into every new chat. This is where custom GPTs, Claude projects, and Gemini gems become invaluable.

These tools let you save system instructions, reference documents, and context that applies every time you use that particular AI. Instead of repasting your marketing strategy prompt, you create a "Marketing Strategist" gem with all the instructions baked in. Every new chat starts with those rules already loaded.

You can share these with colleagues. In Gemini, gems work like Google Docs. You can share them as view-only or editable. Your team can benefit from all the prompt refinement work you have done.

Different workflows work for different teams. You might create a shared gem that everyone can edit collaboratively, continuously improving it together. Or you might have a platform team that creates read-only gems for consistent outputs across the organisation.

I demonstrated this with "Sally", my social media manager gem. It contains multiple Google Docs with brand context, tone guidelines, and step-by-step instructions for different content types. When I tell it "write a LinkedIn post about cats and AI", it knows exactly how to structure the post, what hooks to try, and what format to use.

Sally was not created in one session. It is the result of months of iterative refinement using the prompt cycle. Each time I used it, I asked what would have made it better, then updated the instructions. Now it produces consistently good starting points for social content.

## The Techniques in Practice

These techniques are distinct but most powerful when combined:

**Questions** help you extract knowledge from your own brain without overwhelming AI with context you have not yet organised.

**Meta-prompting** teaches AI how to approach problems systematically rather than just answering individual questions.

**The prompt cycle** creates a feedback loop of continuous improvement.

**Custom AI** makes proven prompts repeatable and shareable across your team.

The webinar format meant I could demonstrate this live. When I asked Gemini to help me think through a teacup marketing strategy one question at a time, the iterative questioning immediately surfaced insights I had not consciously considered. When I used meta-prompting to create a marketing strategy template, the resulting prompt was more comprehensive than I would have written myself.

These are not theoretical techniques. They are practical tools that work today with whatever AI you already use.

## What to Try This Week

Pick something bothering you at work. A difficult decision. A project you are stuck on. A conversation you are dreading.

Open your preferred AI and type:

> "Ask me one question at a time to help me think through [your problem]."

Answer two or three questions. See where it takes you.

If you find it useful, try meta-prompting next. Ask AI to help you create a reusable prompt for a task you do repeatedly. Test it. Refine it. Save it as a custom GPT, gem, or Claude project.

The goal is not to have AI do your thinking. The goal is to have AI help you think more clearly about problems you already understand but have not yet articulated.

Start small. One question. One problem. One prompt. The insights will guide everything that comes next.

## Tools and Resources

- [ChatGPT](https://chat.openai.com){:target="_blank"} - Best all-rounder for most tasks
- [Claude](https://claude.ai){:target="_blank"} - Best for writing and content creation
- [Gemini](https://gemini.google.com){:target="_blank"} - Best for research and deep dives with Google Search integration
- [Wispr Flow](https://wisprflow.ai/r?CHRIS104) - Dictation tools that make answering AI questions much faster (that's a referral link but I'd recommend it even if it didn't give me free months - it's that good!)
- [AI fundamentals training](/training/) - Comprehensive training on using AI effectively in technical teams
