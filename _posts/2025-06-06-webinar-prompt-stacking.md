---
layout: post
title: "Master Prompt Stacking: The Secret to Making AI Code Like You Do"
date: 2025-06-06 14:00:00 +0000
image: /assets/img/stop-ai-agents-breaking-your-code.png
image_portrait: true
series: "AI In Action Webinars"
categories:
- ai
- engineering
- webinar
- cursor
---

After months of fighting with inconsistent AI coding results, I discovered something that changed how I work with tools like Cursor. The problem was not my prompts. The problem was that I had no idea what else was being fed into the AI alongside my requests.

During a recent webinar, I walked through this discovery with a group of engineers who were facing the same frustrations. What we uncovered was both obvious and surprising: AI coding tools are far more complex than they appear on the surface.

<!--more-->

## The Hidden Layers I Never Knew Existed

I used to think that when I typed something into Cursor, my request went straight to the AI. I was wrong. What actually happens is far more complex.

Every request includes training data from the entire internet. System prompts I cannot see. Tool specific instructions. Agent prompts. My workspace configuration. Then, finally, my actual request gets added to the end of this massive context.

This explained why my results felt so unpredictable. I was trying to influence an outcome while being unaware of most of the inputs.

The breakthrough came when someone leaked Cursor's internal prompting structure during the webinar. We could see exactly where user rules get inserted into the prompt stack. This was revelation for participants who had been wondering why their instructions worked inconsistently.

## What I Learned About .cursor Rule Files

The solution turned out to be simpler than I expected. Cursor allows you to insert your own rules into the prompt stack at a specific, predictable point. Not at the beginning where they get overridden, not at the end where they get ignored, but right where they can actually influence the output.

I shared my own blog writing setup as an example. Under my `.cursor` folder, I keep rule files that define how I want content written. One file contains my writing style, extracted by analysing dozens of my own posts. Another has templates for specific content types. They reference each other, creating a modular system.

What surprised me was how much this simplified my workflow. Instead of typing "write in my style" every time, the style rules are automatically included. Instead of repeatedly explaining my blog post format, the template is always there. The AI learned my patterns once and now applies them consistently.

## How This Applied to Real Coding Projects

The writing example was just the beginning. When I showed my Kaijo codebase during the webinar, the real impact became clear. This Next.js application had accumulated rules for everything that kept going wrong. Cursor forgetting to use pnpm instead of npm. Getting Shadcn component names wrong. Trying to edit generated files instead of regenerating them.

Each rule file solved a specific recurring problem. Some I wrote myself after hitting the same issue repeatedly. Others came from the community. Supabase, for example, published official rules for integrating with their platform, solving dozens of gotchas in one import.

What resonated with participants was how this mirrors principles we already know. We do not write monolithic code files. We create modules, separate concerns, build composable systems. The same approach works for AI instructions.

## A Question That Exposed a Deeper Problem

Jim Downing asked something that had been bothering me too: how do you get AI to follow test driven development? He struggled to make Cursor actually run tests instead of just assuming the code was correct.

This highlighted something I had not considered before. The AI was trained on millions of code examples, but how many of those followed TDD? How many included the step of running tests before committing? The training data reflects how developers actually work, not how we think they should work.

I had to be honest: prompt stacking cannot completely fix this. But it does help. By explicitly including testing rules in your stack, you increase the probability of getting the behaviour you want. Not certainty, but a meaningful improvement over hoping the AI will just know what to do.

## What I Learned About Building Prompt Stacks

The session was not just theory. I live coded improvements to a cheat sheet generator, demonstrating how to diagnose when prompts are not working and how to fix them.

The process reminded me of debugging code. When something goes wrong, you isolate the issue. You ask the AI to explain what it understood. You get it to rewrite your request more clearly. Then you extract the patterns into reusable rules.

One participant asked about evaluation: how do you know if a prompt change actually improved things versus just random variation? I had to give an honest answer: you often do not know from a single example. You need to try it multiple times, see if it consistently helps, and be willing to discard rules that do not prove their worth.

## What This Revealed About Team Dynamics

The implications went beyond individual productivity. When teams share rule files, they create a shared understanding of how to work with AI. Junior developers inherit the accumulated wisdom of seniors. Team conventions get enforced automatically. Knowledge becomes code.

I have watched teams transform their AI adoption by treating prompt rules like they treat code. Version control them. Review them. Refactor them. Share them. The same engineering disciplines that make code maintainable make AI interactions predictable.

Several participants mentioned disappointing experiences with random prompt collections from the internet. This made sense to me. A prompt written for Cursor in July 2024 is largely useless now. The tools evolved. The models improved. You cannot copy and paste your way to AI productivity any more than you can copy and paste your way to good software.

## My Recommendation: Start Small, Think Modular

If you want to try prompt stacking, I recommend starting with your biggest pain point. What do you find yourself typing repeatedly? What does the AI consistently get wrong? Write a rule for that one thing.

Test it manually first. Include the rule explicitly in your chat and see if it helps. Once you gain confidence, set it to auto include for relevant files. Build up your library gradually.

Most importantly, think modularly. Do not create one massive rules file with everything. Create focused rules that do one thing well. Let them reference each other. Build a system, not a monolith.

## What I Took Away From the Session

By the end of the webinar, participants were already planning their prompt architectures. Some wanted to codify their company's coding standards. Others saw opportunities to capture domain knowledge. Everyone recognised that prompt stacking was not just about making AI work better, but about making it work consistently.

The tools will keep evolving. New models will emerge. But the principle of managing context thoughtfully, of building systems rather than hoping for magic, will remain valuable. 

I think we are moving from the era of prompt engineering as art to prompt engineering as engineering. The transition feels overdue.

This approach has changed how I work with AI tools. Instead of fighting unpredictability, I now have systems that help me get consistent results. The investment in building these rule files pays dividends every time I start a new project.