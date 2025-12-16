---
layout: post
title: "See Three Kings Of Inference Spar"
date: 2025-12-15 10:00:00 +0000
image: /assets/img/three-kings-spar.png
categories:
- ai
- productivity
---

I was writing [a complex article](/chatgpt-is-terraforming-earth/) about solar energy, China's manufacturing acceleration, AI power demands, and synthetic fuel production. The topic spanned economics, geopolitics, technology, and climate policy. Any single model would give me a plausible synthesis, but I had no way to know what I was missing.

So I tried something different. I ran the same prompt through Claude, Gemini, and ChatGPT simultaneously.

Each model returned a substantially different response, not just different words but different conceptual frames, different emphases, and different blind spots. That is when I realised the distinction. For facts, use Gemini Deep Research. For insights and novel angles on a problem, run multiple models and pit them against each other. They think differently, and running all three gives me frames I would never reach with just one.

<!--more-->

## The prompt

I opened Claude, Gemini, and ChatGPT in separate windows and pasted the same prompt into each:

> Research what is happening in solar and put it together with China accelerating, the power needs of AI, how it will transform the world (a la Terraform Industries creating natural gas from air), and come up with a compelling argument for a blog post outline with sources.

The prompt was deliberately broad. I wanted to see how each model would structure the argument, which connections it would draw, and what sources it would surface. A narrow prompt would constrain the responses too much to reveal their different thinking styles.

## Anonymise

I labelled the three responses Model A, Model B, and Model C, removing any indication of which AI produced which output. Knowing which model wrote something brings assumptions about that model, and anonymising forces evaluation of the actual work rather than preconceptions about the tool.

I copied all three outputs into a single document with just the A/B/C labels.

## Compare blind

I gave the anonymised outputs to ChatGPT 5.2 and asked it to produce a comparison table rating each for factual accuracy, insightfulness, clarity of conclusion, novel insight, systems thinking, and source hygiene.

The comparison table gave me an immediate sense of relative strengths. One output scored highest on insightfulness and systems thinking. Another scored highest on source hygiene and argument discipline. The third scored highest on breadth but lower on factual reliability.

## Fact-check

I asked ChatGPT 5.2 to fact-check all three responses against current web sources, marking each major claim as supported, partially supported, or unverifiable.[^1]

[^1]: Ethan Mollick has [noted](https://www.linkedin.com/posts/emollick_i-have-found-gpt-52-thinking-to-be-a-surprisingly-activity-7406432277490053120-YFCP){:target="_blank"} that GPT-5.2 Thinking is "a surprisingly deep second-opinion/fact checker" that can find and gently correct errors requiring research to verify, including checking dates against source code on GitHub.

The most impressive-looking output, the one with the most statistics and the most confident tone, contained a clear date error. It confused May 2024 with May 2025 when citing a statistic about Chinese solar panel installations.[^2] Several other ultra-specific numbers could not be verified against the sources cited.

[^2]: Date confusion is a classic Claude failure mode. It often cites events from the wrong year with complete confidence.

The most editorially cautious output was ChatGPT 5.2, the same model I used as the fact-checker. It qualified its claims, acknowledged uncertainty, and had the highest factual accuracy. Almost every concrete number checked out.

[Confidence and correctness are not the same thing](/ai-is-consistently-mediocre/). The model that sounded most authoritative was the least reliable on verification.

## Select frames

Based on the evaluation and fact-check, I selected two of the three outputs to use as my foundation, picking the strongest elements from each rather than declaring a single winner.

One gave me a brilliant conceptual frame: the idea of AI data centres as "anchor tenants" that fund massive solar overbuild, creating surplus cheap electricity that enables synthetic fuel production. This systems-level insight was worth more than any individual statistic.

The other gave me editorial discipline: careful claims, explicit sourcing, a section anticipating objections, and numbers I could trust. This became my factual backbone.

I discarded the third output's structure entirely, though I kept a few of its statistics after independent verification.

## Synthesise

I gave the two strongest outputs to my "Writing AI" project in Claude Opus 4.5. This project knows exactly how I structure arguments and how I write. Opus 4.5 is still the best model for writing, and it synthesised Gemini's conceptual frame with ChatGPT's factual discipline into a draft that sounded like me.

Then I asked it to [interview me about the results](/ai-feeding-on-itself/). The synthesis was missing my perspective, my take on what mattered most. By asking it to question me, I could add the angles only I could provide: which implications felt most urgent, which objections I had encountered in real conversations, which parts of the argument I found most compelling and why.

## Edit

The draft needed refinement. I had a back-and-forth conversation with Opus 4.5, pointing out things I did not like and asking for specific improvements. Some sections felt too abstract, others needed sharper transitions, and the conclusion needed more punch.

Then I ran a slop-checking agent in Claude Code. This agent scans for common AI writing patterns: "Here's the thing" constructions, preachy second-person lecturing, triplet sentence patterns, scaffolding phrases like "This is crucial." Rather than catching each one manually, the agent flags them all and fixes them in one pass. I [continually improve this prompt](/webinar-advanced-prompting/#the-prompt-cycle) as I discover new patterns to avoid.

## Visuals

Once I had my draft, I gave it to a custom Gemini gem I have built for creating infographics. Gemini produced a visual showing the solar-AI-synthetic fuel loop described in the article.

Then I asked it to extract just the globe element from that infographic. I wanted a cleaner motif for the article header, something that suggested the global scale without the full diagram's complexity. Gemini isolated the element and gave me a standalone image.

The overhead is perhaps 20 minutes beyond what single-model research would take. The improvement in output quality, and the reduction in confident errors, is substantial.

## The verdict

These assessments are a snapshot. [Models move fast](/three-coding-agents-head-to-head/), and what wins today may lose next month. When a new frontier model drops, I [run it through this same process](/how-to-react-to-a-new-frontier-model/) to see where it fits. But the pattern of distinct strengths has held across every comparison I have run.

**Claude was the most thorough but the slowest.** It produced the longest output with the most statistics and the most comprehensive source list. It also took noticeably longer to generate. The problem was overconfidence: several specific claims could not be verified, and one date was simply wrong. Claude's strength is breadth and synthesis. Its weakness is presenting uncertain information with the same confidence as verified facts.

**Gemini had the best conceptual framing.** Its output was shorter and had fewer citations, but it gave me the single most valuable insight: the "anchor tenant" framing for how AI data centres could fund solar infrastructure. Gemini thinks in systems and causal chains. Its weakness is that it sometimes presents heuristics and mental models as though they were established facts. The claim about needing to overbuild solar 3-5x for 24/7 operation is a useful heuristic, not a universal rule.

**ChatGPT had the best editorial discipline.** It produced the most publishable-ready structure: clear thesis, explicit sourcing, a section anticipating objections, and claims that almost all checked out on verification. It was the most cautious about what it asserted as fact versus what it framed as analysis. Its weakness is that it was less novel. The conceptual contribution was solid but not surprising.

If I had to pick one model for research, I would struggle. Claude gives me breadth I cannot get elsewhere but needs heavy fact-checking. Gemini gives me insights I would not reach myself but needs grounding in evidence. ChatGPT gives me reliability but less spark.

Running all three and synthesising the best of each gives me something none of them can produce alone.

<img src="/assets/img/three-kings-spar-infographic.jpg" alt="Three Kings of Inference workflow infographic" style="width: 50%;" />
