---
layout: post
title: "Stop Saving Tokens. Start Writing Scripts."
date: 2026-06-05 07:00:00 +0000
permalink: /stop-saving-tokens-start-writing-scripts/
categories:
- ai
- engineering
image: /assets/img/stop-saving-tokens-start-writing-scripts-motif.jpg
infographic: /assets/img/stop-saving-tokens-start-writing-scripts-infographic.jpg
---

The most powerful thing about a Large Language Model is what sets it apart from any other regular task a computer might perform. Computers normally do something exactly the same way every time (the correct term for this is "deterministic"): give it the same input and you get the same output, with no judgement involved. A Large Language Model is the opposite (it is "non-deterministic"). You can hand it fuzzy, open-ended work that you could never have written a program for, and it will make a decent attempt.

This is amazing for work that requires nuance: it can spot trends, make judgement calls, and be creative. But that flexibility also means it is fallible and unreliable.

Is there a way to get the best of both worlds?

Adding a bit of old-fashioned programming back in makes things more powerful still: it gives your LLM a better framework for making reliable decisions. It also saves tokens, a [big topic](/webinar-escape-the-great-ai-lock-in/) at the moment.

<!--more-->

## Prompt Diets Do Not Work

Plenty of people are trying to get that bill down with prompt tricks. Caveman mode, if you have not come across it yet, strips everything back to terse, grunt-like instructions and asks for equally terse output.[^2] Fewer words in, fewer words out, smaller bill.

It works at the margin. The trouble is that the expensive part of an agent is rarely the words you typed, but the model thinking through the same problem again, writing the same helper again, and rediscovering the same structure it worked out yesterday. You cannot diet your way out of repeated work. You have to remove the work.

People treat the prompt as the most obvious cost because it is the part they can see and edit. The real spend is in everything the model does after it reads the prompt, and the cheapest way to cut that is to stop asking it to redo things it has already done well once.

## Simpler Beats Clever

I have been round this loop before, in both senses. A couple of years ago the fashionable answer to orchestrating AI was the workflow: a graph of boxes and arrows in something like n8n, each node a step you wired together by hand. I built one for my newsletter. It took weeks and broke at two o'clock every Monday. Building something that brittle to manage the AI was exactly the work the AI should have been doing for me.

Then the loops won. Geoffrey Huntley's Ralph loops[^1] showed that a model good enough to read its own previous work does not need an elaborate state machine wrapped around it. You point it at a pile of tasks and let it run. I made that case at length in [my AI Engineer Europe workshop earlier this year](/ralph-loops-aie-europe/) and in [my post on why your orchestrator is too clever](/your-agent-orchestrator-is-too-clever/): simpler methods plus a better model beat hand-built complexity almost every time. I have packaged my own Ralph-style loop into a skill you can install and run yourself.[^3]

So it might sound odd to say that workflows are coming back. They are, in a smaller and sharper form than the graphs I abandoned. Determinism is returning as scripts that live inside skills, and as orchestration scripts that drive agents.

## Let It Write The Script Once

<img src="/assets/img/stop-saving-tokens-start-writing-scripts-comic.jpg" alt="Sam, in his gilet with a coffee mug, tells a sceptical arms-crossed Charlie: I did not get the agents to write scripts, I just run a loop a thousand times in parallel and pick the best result. Charlie asks what his monthly spend is. Sam, proud: 43,794 dollars, cool huh? Behind them, glum suited financiers reluctantly hand sacks of cash to delighted robots." style="width: 45%; float: right; margin: 0 0 1rem 1.5rem;" />

Agents are good at writing scripts. Give a model a clear, repeatable job and it will produce tidy, deterministic code that does the same thing every time. The mistake is letting it do that on every run. Ask it once, keep the script, and from then on the skill calls the script instead of generating it again.

You are reading a worked example. Every post on this site goes through a skill called slop-check that scans for the tics of AI writing: false dichotomies, weasel words, choppy three-word sentences, the dreaded em dash. None of that detection needs a language model: it is a short bash script that greps for about a dozen patterns and prints the lines that match. The skill wraps that script with the part that does need a brain, reading the flagged lines and deciding which are genuinely slop and which are fine in context.

The pattern matching is deterministic, so it lives in the script, where it runs in milliseconds and costs nothing. The judgement is not deterministic, so it stays in the prompt. If I made the model rediscover those dozen patterns every time it checked a draft, I would pay tokens for worse and less consistent results. A kept script does ask for one discipline in return: a test or a check, so that when the job changes it fails loudly instead of quietly doing the wrong thing. The balance between scripts and prompting inside a skill is a delicate one.

The same shape is all over my setup. My home skill has a script that knows how to talk to Home Assistant, so the model never has to work out an API just to turn off a light. There are off-the-shelf versions of that now, things like Hermes, but I wrote mine before they existed and it still earns its place. I use scripts to produce content, to pull data, and sometimes to spawn a sub-agent at exactly the right moment. The skill holds the judgement about when and why, and the script holds the how.

## Skills Are The Glue

Skills are how this stays manageable. A skill is a small, named parcel of capability: a bit of prompt that carries the judgement, plus the scripts it leans on for the repeatable parts. Loose on their own, the scripts would be a drawer of utilities you forget you own. Wrapped in a skill, they become something the model reaches for at the right moment, with instructions for how to use them and when to leave them alone. I have written before about [why skills are Claude Code's secret weapon](/skills-are-claude-codes-secret-weapon/) and [what belongs in your AI knowledge base](/what-to-put-in-your-ai-knowledge-base/): the skill is the unit where prompt and script meet.

## Workflows Come Back, Smaller

The newest piece arrived this week. The latest Claude Code, running on Opus 4.8, ships a feature called Workflows: a way to orchestrate agents from a script. You write plain JavaScript that spawns sub-agents, fans them out in parallel, pipelines them through stages, and collects structured results. The control flow is deterministic. The loops, the branching, and the order of operations are fixed in code. What happens inside each step is still an agent doing agent things.

This is the same trick as the slop script, one level up: rather than trusting a single skill to choreograph a complicated fan-out correctly on every run, you write the choreography down once and let it run the same way every time, with the model supplying the intelligence at each node instead of the structure. When I have a repeatable job that wants five agents arranged in a particular shape, a workflow gives me that shape for nothing, and I stop paying the model to reinvent the plan each time. The infographic and comic on this page came out of one of these workflows, several agents running in parallel while I got on with other things. The feature is Claude's, though the idea underneath belongs to no one vendor: any agent runtime that can call a script gets the same split between deterministic code and judgement, whether that is Claude Code, Codex, or a Gemini command line.

## The Double Dovetail

Step back and the shape is a set of nesting dolls. First we had workflows: pure structure, no intelligence. Then skills and agent loops: intelligence with very little structure. Now the two are folding into each other. Skills sit inside workflows, where a deterministic harness calls intelligent steps. Workflows, in the form of scripts, sit inside skills, where an intelligent step calls deterministic code. My slop-check is the small version of this: a script, which is a workflow in miniature, living inside a skill, while that same skill can be one node inside a larger production workflow. Determinism and judgement keep swapping places depending on which layer you are looking at, and that is worth designing on purpose.

<img src="/assets/img/stop-saving-tokens-start-writing-scripts-infographic.jpg" alt="The Double Dovetail infographic: four stages showing determinism and AI-agency nesting into each other. One, Workflows, pure structure shown as gears. Two, Skills, intelligence shown as a glowing loop. Three, Skills within Workflows, loops nested inside an angular bracket. Four, Workflows within Skills, a gear and a code window nested inside one loop." style="max-width: 100%; display: block; margin: 1.5rem auto;" />

None of this would matter much if tokens were free. For a single developer working alone they almost are, because the right thing to optimise is your own time, so let the loops run and burn the compute. At team and company scale the maths change. Token spend becomes a real line in the budget, and the work that gets repeated thousands of times a day is where the money quietly leaks out. Picture a small glue script that a workflow calls two thousand times a day. Once that work lives in a script, the model stops reasoning its way back to the same thirty lines of helper on every one of those runs. The saving is the same work, removed two thousand times over, not a few percent shaved off a prompt. Costs have [already fallen enormously](/doing-real-work-with-ai-just-became-150x-cheaper/), and cheaper models keep arriving that handle deterministic glue work at a fraction of the price of the frontier. Reaching for one of those where it fits saves more than any prompt trick. The honest catch is that at company scale this only compounds if those scripts are shared and trusted, rather than rebuilt from scratch by every engineer. Coordinating that across a whole team is a harder problem, and one I will come back to.

Every script you write once is work the model never does again. Where caveman mode trims the sentence, scripts inside skills, and skills inside workflows, remove the whole paragraph you were otherwise going to pay to have rewritten every single day.

The cheapest token is the one you never spend. You get there by letting the AI write the script once, and keeping it.

[^1]: Geoffrey Huntley [introduced Ralph loops](https://ghuntley.com/ralph/){:target="_blank"} in July 2025.

[^2]: The term comes from a [Claude Code skill by Julius Brussee](https://github.com/JuliusBrussee/caveman){:target="_blank"}, whose tagline is "why use many token when few token do trick". A [careful analysis of it](https://alexriosme.substack.com/p/there-is-a-reason-that-caveman-is){:target="_blank"} found that most of the saving comes from a single "answer concisely" instruction, and that the trick never touches the reasoning the model does before it replies, which is exactly where the cost sits.

[^3]: It is published on [airskills](https://airskills.ai/chrismdp/ralph){:target="_blank"}; install it with `airskills add chrismdp/ralph`.
