---
layout: post
title: "What To Put In Your AI Knowledge Base"
permalink: /what-to-put-in-your-ai-knowledge-base/
date: 2026-05-01 07:00:00 +0000
series: "Claude Code for Leaders"
categories:
  - ai
  - productivity
  - leadership
image: /assets/img/ai-knowledge-base-cauldron.jpg
infographic: /assets/img/ai-knowledge-base-infographic.jpg
published: true
---

The folder is ready. You have had a few conversations with Claude and saved some notes, as described in the [first part of this series](https://chrismdp.com/build-an-ai-knowledge-base-from-scratch/). Now you are staring at it and wondering what the point is if all you are putting in is manual meeting notes.

Manual meeting notes are a fine start, and after a few weeks they do become useful: you can ask Claude what you decided in March, or what the reasoning was behind a particular choice, and get a real answer drawn from your own notes. But the folder gets interesting when you start adding the things you are already reading and listening to, and the recordings you are already making, processed in a way that makes each new source compound on everything already there.

<!--more-->

## The compounding idea

When you save an article to read later, you create a pile that grows and stays flat. When you extract the useful insight and place it next to a related thought you already noted from a meeting last month, you create a concept with two sources of evidence and a connection to your current thinking. The knowledge compounds.

Andrej Karpathy, who built the Autopilot team at Tesla, described this as the "LLM wiki" pattern.[^1] You extract the useful parts of each source once and let them merge into a growing knowledge base, rather than storing raw documents and hoping the AI retrieves the right thing on every query. Every source enriches what was already there.

After a month of adding sources this way, when you ask your folder a question, the answer draws on your meetings, the articles you have been reading, and the podcast you listened to last week, all organised by concept rather than by date.

## Where everything came from

When the folder grows, you will lose track of who said what. A line you paraphrased from an interview, a paragraph that came from an article, a thought that was originally yours: six weeks in, they all read the same. The fix is **provenance**[^2]: every note carries the trail of where it came from. Treat this as a first-class rule.

### Ideas have authors, and you owe them credit

When you reuse an idea (in a board meeting, a blog post, a conversation) you should be able to credit the person who put it there. If your folder does not record where each thought came from, you cannot give credit, and you cannot check whether you have remembered the source accurately.

### Without provenance, the folder is just a confident liar

You will forget in a "did I think this or did I read this" way, not the simple "what was that called again" way. The folder is meant to remember for you. If it loses provenance, it becomes a more confident stand-in for your imperfect memory, and you are worse off than before.

Every note carries the source URL, author, and date in its frontmatter, and those fields get updated when the note is enriched by a new source. The folder lives on your machine; nothing leaves it except the source you point Claude at when you ask. Six weeks later, the folder will tell you exactly where each idea came from, and so will you.

## A worked example

Here is what this looked like in my own folder this morning. I processed one newsletter, [AINews's "Agents for Everything Else"](https://www.latent.space/p/ainews-agents-for-everything-else){:target="_blank"}, by pasting the URL into Claude Code, and five minutes later the folder had moved. Two existing concept notes picked up new paragraphs: *Coding Agent Behaviors Are the Template for General Knowledge Work Agents* (started a few days earlier from a piece in *Every*) gained a section on OpenAI's "Codex for Work" launch, and *Agent-Native Software Design - The Best UX Is No UX* gained a confirmation paragraph from a swyx talk. Two new concept notes were created: *Agents Save Yak Shaves - The Non-Coding Value Claim* and *Harness-Centric Engineering Replaces Model Benchmarks as Agent Quality Metric*.

<details style="margin-bottom: 2rem;">
<summary><strong>What one of those notes actually looks like</strong></summary>
<pre><code>---
type: concept
first_mentioned: 2026-05-01
source_link: building-ai-engineer-with-ai
source_url: https://www.youtube.com/watch?v=zepu8Kk6FBQ
source_author: swyx
---

One underappreciated benefit of AI agents is that they save
yak shaves — the distracting, often non-technical tasks that
disrupt deep work. swyx argues this is where agents provide
their biggest productivity gain, not in the primary coding or
creative task itself.

The concrete example: his team expected a design iteration to
take weeks. By adding Devin as an agent layer, the gap between
design and implementation collapsed. The biggest win wasn't
speed on the main task — it was eliminating the friction of
handoff and the cognitive cost of context switching.

This reframes where to look for agent ROI. Instead of measuring
how much faster agents write code, measure how much time is
reclaimed from the surrounding logistics, tooling, and integration
work that teams tolerate because they can't easily delegate it
to a human.

## Related Thoughts

- Coding Agent Behaviors Are the Template for General Knowledge
  Work Agents
- AI Is Still Searching For a Home
- Briefing Cycle - From Prompt Cycle to Autonomous Agent Delegation

## References

- swyx talk "Building AI Engineer with AI", 2026-05-01
- Captured 2026-05-01 from AINews newsletter processing
</code></pre>
</details>

That was five minutes of processing for two existing ideas enriched and two new ideas filed. The newsletter sits archived in case I want to re-read the original, but the value lives in the notes rather than the source.

The skill I use for this is open: [`/capture`](https://airskills.ai/chrismdp/capture){:target="_blank"}. Run `npx airskills add chrismdp/capture` in your project to install it as a `/capture` command in Claude Code. Point it at a URL, a transcript, or a rough note and it does the rest.

The rest of this post walks through the source types that feed the folder (meeting transcripts, links, video) and what changes after a month of doing it.

## Transcripts

Manual notes capture what you remembered to write down; a transcript captures everything that was said. The folder benefits from both.

Use whatever your existing meeting tool gives you. Zoom, Google Meet, and Teams now generate transcripts automatically, and that is enough to get going. For reference, the specific stack I run: [Fathom](https://fathom.video/){:target="_blank"} for meetings I do not control (it joins as a guest, transcribes, and emails a summary I can then drop into the folder), Google Meet's built-in transcript for meetings I run myself, and voice notes for the in-between thoughts like a debrief on the walk home or an idea on a station platform. The voice notes go through my own capture pipeline at [voice-inbox](https://github.com/chrismdp/voice-inbox){:target="_blank"} so anything I record on my phone lands in the folder ready to process.

If you have a recording of a meeting, a talk you gave, a podcast interview, or a training session, give Claude the transcript. Tell it to "pull out the key decisions, insights, and action items, and add them to my notes folder". Claude reads the transcript, extracts what matters, and files it where it belongs: a decision about hiring lands next to your existing notes on team structure, a customer insight joins the product direction notes, and an action you committed to becomes a note of its own.

For talks and training sessions you deliver, a recording is all you need; Claude Code can process the transcript and pull out the themes, decisions, and insights that came up. A 90-minute session becomes a set of connected notes in a few minutes, ready to inform the next one.

## Links you would otherwise lose

You are already reading articles, newsletters, reports, and LinkedIn posts online, and most of them disappear the moment you close the tab. The "read it later" queue grows and never empties.

When you read something worth keeping, copy the URL and tell Claude Code: "Save this link and pull out what is useful: [URL]". I have packaged this into a [`/capture`](https://airskills.ai/chrismdp/capture){:target="_blank"} skill so I do not retype the prompt every time. Claude fetches the article, extracts the ideas that matter, and merges them into your notes. If you already have a note about the topic, Claude adds to it; if not, it creates one. The article gets archived in full so you can re-read it later, but the knowledge from it is now searchable and connected to everything else.

You save the knowledge from articles immediately and let the raw sources live quietly in the background, so the folder grows instead of the reading queue.

Say you come across a useful piece about how AI tools handle long documents. You already have notes from a conversation with your team about which tools to adopt. Processed through Claude Code, the article's insights land next to your team conversation, and a note called "How AI handles context" now carries both sources. A month later, preparing for a tooling decision, that note is there.

## YouTube and video

YouTube has locked down most of the obvious paths to a transcript, so Claude Code cannot reliably fetch one on its own. The way I do it is by hand: open the video, hit "show transcript" under the description, copy the text, paste it into Claude Code, and ask it to extract what is worth keeping. It is slower than the link or transcript flow, but it works on every video.

Automation is possible but takes work. The [`/capture`](https://airskills.ai/chrismdp/capture){:target="_blank"} skill routes YouTube URLs through Gemini's video understanding to pull a transcript directly, which avoids the manual paste. The manual route is fine if this is a once-a-week habit rather than a daily one.

YouTube carries useful thinking that rarely gets captured: conference talks by founders, research presentations, industry interviews. Processing one good talk a week compounds in a way that passive watching never does.

## After a month

After a month of adding sources this way, you have concept notes rather than files called "meeting-notes-monday.md" and "article-from-last-week.md". The notes are titled by idea: "AI adoption in engineering teams", "Team structure thinking", "Customer interview themes".

Each concept note has history: it started from one conversation, was enriched by a podcast, updated after a customer interview, and is connected by links to related ideas. When you ask Claude "what have I been thinking about headcount this quarter?", it reads the concept note that already compiles everything relevant.

You do not organise any of this yourself, file things, or maintain a hierarchy. You keep adding sources and asking Claude to extract and merge, and the structure emerges from the content.

## The question that pays off

Once a week, or whenever you are preparing for something important, ask the folder a direct question.

<div style="border-left: 4px solid #0292b7; padding: 0.5rem 1rem; color: #0292b7; margin: 1.5rem 0;" markdown="1">

"Given everything I have noted about our product direction, what are the themes I keep returning to?"

"I have a board meeting on Monday about team structure. What have I already thought through, and what is still open?"

"What customer insights have I collected this month, and do they point anywhere consistent?"

</div>

These questions are only as good as what is in the folder, and after a month of adding sources they start to pay off. You get answers drawn from your own thinking, the articles you have been reading, and the podcasts you have been listening to, organised by concept rather than by date.

A leader's second brain in 2026 is a plain text folder you feed with real sources and ask real questions of, where the knowledge is yours, organised by your thinking, and grows every time you add something new.

## What comes next

The next part of this series is about Skills: small, repeatable workflows you can build on top of the folder so the things you do every week get a little easier and a little more reliable each time. This is where the knowledge base becomes a system rather than a notebook, climbing the same ladder engineers climb when they harden their work: do it once, write it down, turn it into a script, add evals, lift the floor.

After that, projects. How I run real work (proposals, training engagements, client deliverables) out of the same folder. I do this in plain Markdown, but the same shape works in Linear, Notion, or any tool that gives you a place to think out loud and track decisions over time.

Until then, save the link when you read something useful, add a note when a meeting matters, and paste the transcript when you watch something worth keeping. The folder compounds from there.

This is a personal practice. A team's shared knowledge base is a different question, and a different post when it is ready.

[^1]: Andrej Karpathy's [LLM wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f){:target="_blank"}: instead of retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki. Knowledge is compiled once and kept current, not re-derived on every query.
[^2]: *Provenance*, the chain of custody and origin of an object, is the word archivists, museum curators, and (more recently) data scientists have always used for this. The [W3C PROV standard](https://www.w3.org/TR/prov-overview/){:target="_blank"} formalises it for digital data. It transfers cleanly to ideas: track where each insight came from, the way an art dealer tracks a painting.
