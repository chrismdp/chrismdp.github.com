---
layout: post
title: "How To Use Claude Code Skills"
date: 2026-01-25 09:00:00 +0000
series: "Where AI Lives"
categories:
- ai
- development
- productivity
image: /assets/img/claude-code-skills-motif.jpg
infographic: /assets/img/claude-code-skills-infographic.jpg
---

Skills are Claude Code's secret weapon, but most people never create any because they do not see the value. Once you understand what skills can do, you start building a small, carefully curated set that represents how you actually work, refined over time as you discover what saves you effort and what gets in the way.

Start with "pattern thinking", and it comes naturally once you look for it. After every task, ask yourself what is reusable here and what would help you next time. Coders learn this instinct through years of extracting common functionality into libraries and modules, but the skill transfers to anyone willing to notice their own repetition. When you find yourself explaining the same preferences to Claude Code twice, that repetition is a signal: you have a skill waiting to be written.

<!--more-->

## What Is a Skill?

A skill is a reusable prompt that Claude Code can load when needed.[^docs] Think of it as a set of instructions you would otherwise repeat every time you start a particular kind of task. Instead of explaining your writing style from scratch, you load a skill that already contains your preferences. Instead of describing how you want code structured, you load a skill that encodes your conventions.

Each skill lives in its own directory with a `SKILL.md` file as the entrypoint. The file has two parts: YAML frontmatter that tells Claude when to use the skill, and markdown content with the instructions Claude follows when the skill is active. You can invoke a skill directly with `/skill-name`, or let Claude load it automatically when it matches what you are doing.

The power is in the loading. Skills only take up context when they are active, so you can have dozens of them without cluttering every conversation. Claude Code reads the skill description and decides when to invoke it based on what you are doing. This is why clear descriptions matter so much: a vague skill gets ignored.

[^docs]: The official documentation at [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills){:target="_blank"} covers the full technical specification, including frontmatter options, tool restrictions, and subagent integration.

## Start Simple

The best way to understand skills is to create one, and the best first skill is capturing your tone of voice for writing. Do not start with something complex like a multi-step workflow or an agent that coordinates external APIs. Start with something you can verify immediately: does the output sound like me or not?

Think about what you find yourself repeating when you write. Maybe you always want British English spelling, or you prefer short paragraphs, or you have a list of phrases you never want to see. Write these preferences down in a markdown file, give it a clear description that tells Claude when to load it, and you have your first skill. That single skill will teach you more about the concept than any tutorial, because you will see immediately whether Claude follows your instructions and how to refine them when it does not.

The skill itself is just a text file with no magic syntax or special commands. It is instructions written for another entity that happens to be very good at following instructions, and the quality of your output depends entirely on how clearly you articulate what you want.

## Separate Your Concerns

Coders learn early to separate concerns: keep different responsibilities in different places so each piece can be loaded, tested, and changed independently. This principle applies directly to skills.

I have two writing skills that could easily be one, but separating them makes each more useful. My writing style skill describes what good looks like: paragraph length, heading style, voice, and the kind of examples I tend to use. Claude loads this before drafting anything. My slop check skill describes what to avoid: AI phrases like "here is the thing", structural patterns like false dichotomies, and rhythms that become robotic when you read them aloud. Claude loads this after the draft exists.

Why separate them? Because sometimes I only need one. When I am editing existing content, I do not need the writing style skill cluttering context with guidance about structure and flow. I just need the slop check to catch AI patterns. When I am brainstorming and want Claude to write freely, I might load the style skill but skip the slop check until later. Keeping them separate means I load only what the current task requires, which keeps context clean and responses focused.

This is a pattern worth stealing. Whenever you find yourself building a skill that does two distinct things at two distinct times, consider splitting it. Each skill becomes simpler, easier to refine, and more flexible about when it gets used.

## Include Scripts and Supporting Files

Skills can do more than provide instructions. Each skill is a directory, so you can include scripts, templates, examples, and reference documentation alongside your `SKILL.md`. Claude reads the main file and loads supporting files only when needed, keeping context efficient.

I have a skill that generates images using Gemini's API. The skill directory contains both the prompt template and the script that calls the API. When I ask Claude Code to create an infographic, it loads the skill, runs the script, and shows me the results. The structure looks like this:

```
gemini-images/
├── SKILL.md           # Main instructions
├── templates/
│   └── infographic.md # Prompt template
└── generate.sh        # Script Claude executes
```

I did not write the script myself. I pasted in the API documentation and asked Claude Code to build it, having it ask me questions as it went. I needed to know roughly how API keys work, but that was about it. The script lives inside the skill directory and only loads when needed, keeping my normal context clean.

You can also create agents within your skills by adding `context: fork` to the frontmatter. These run in isolated subagents that coordinate multiple steps without cluttering your main conversation. My [morning routine skill](/webinar-claude-code-thinking/), for example, reads my calendar, checks my goals, asks me questions about how I am feeling, and writes a journal entry. All of this is encoded in a skill that I invoke with a single command.

## Source Control Your Skills

Skills become more valuable over time. Each refinement makes them better at capturing how you work. Treat them like any other important document: put them in source control, commit changes with meaningful messages, and back them up.

I keep my skills in a dedicated folder that gets synced across machines. Personal skills live in `~/.claude/skills/` and are available across all your projects. Project skills live in `.claude/skills/` and stay with that codebase. When I improve a skill on my laptop, it is available on my desktop. When I try something that does not work, I can revert. The version history becomes a record of how my workflow has evolved.

This also makes skills portable. I can share a skill with someone else by sending them a file. They can read it, understand what it does, and adapt it for their own work. Source control is not just backup: it is documentation. This approach to [treating your work as repositories rather than chat conversations](/writing-and-thinking-with-ai-why-repositories-beat-chatbots/) is what makes AI collaboration compound over time.

## Build Your Own

Do not import too many skills from others, because skills represent how you work rather than how someone else works. Their preferences are not your preferences, their workflow is not your workflow, and the value of a skill comes from it matching your thinking precisely. Looking at examples helps you understand what is possible and how other people structure their instructions, but the skills you actually use every day need to be ones you wrote yourself.

I would also not use a skill unless I knew what was in it. A skill has access to whatever Claude Code has access to, which means it can read files, run commands, and make changes to your codebase. You should understand what a skill does before you let it loose on your work, and the easiest way to understand it is to have written it in the first place.

## Clear Descriptions Matter

Your AI picks up skills based on their descriptions. A vague description means the skill gets ignored when it should be loaded, or loaded when it should not be. Be specific about when a skill should activate.

Bad description: "Writing help"

Good description: "Load before writing any blog post, LinkedIn post, or newsletter. Contains Chris's tone of voice, paragraph structure preferences, and British English spelling conventions."

The description is for Claude Code, not for you. Write it as if you were explaining to a colleague when they should use this particular set of instructions.

You can also control who invokes a skill. Add `disable-model-invocation: true` to your frontmatter if you want a skill that only you can trigger, like a deploy script. Add `user-invocable: false` for background knowledge that Claude should use but users should not invoke directly. These controls prevent skills from running at the wrong time or being invoked accidentally.

## Pattern Thinking

The people who use Claude Code best are pattern thinkers who keep asking how they can reuse what they just built. Developers learn this through years of [building abstractions](/coding-with-ai/), extracting common parts into functions and modules every time they write similar code twice. That instinct for noticing repetition and eliminating it transfers directly to skills.

When you give Claude Code the same context repeatedly, explain the same preferences across multiple conversations, or correct the same mistakes over and over, you are looking at a skill waiting to be created. The goal is to [automate the routine parts of your work](/unlocking-real-leverage-with-ai-delegation/) so you can focus on the parts that are different each time, which tend to be the interesting parts. Skills handle the repetitive setup, the consistent preferences, and the guardrails you always want in place, leaving you free to think about the actual problem you are trying to solve.

## Getting Started

Create your first skill this week by picking something simple like your tone of voice, your formatting preferences, or a checklist you always follow. Write it down in a `SKILL.md` file, give it a clear description that tells Claude when to load it, and save it in `~/.claude/skills/` so it is available across all your projects.

Use the skill for a few days and notice what is missing, what is wrong, and what could be better. Refine it based on what you learn, commit your changes, and keep iterating. That refinement is the start of building a system that grows with you, where each improvement makes Claude more useful for your specific workflow.

The best skills are simple ones you use every day that save you time on repetitive tasks. Skills let you teach an AI your patterns through carefully crafted instructions rather than through training data, and that teaching compounds over time as your skill library grows.
