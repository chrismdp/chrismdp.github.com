---
layout: post
title: "Prompt Evals Alone Are Useless"
date: 2026-09-09 07:00:00 +0000
image: /assets/img/prompt-evals-engine-system-comic.jpg
image_portrait: true
infographic: /assets/img/prompt-evals-are-useless-infographic.jpg
series: "Software Factory"
categories:
- ai
- engineering
- agents
---

Over the last couple of nights I have been building a text adventure RPG, mostly to see what Astra could do. I have been giving the AI an end of day prompt, leaving it to run for hours, and seeing what it has done in the morning.

Playing the game is simple. It is told through a diary style interface, almost like reading an ebook: you type your character's actions, you roll some dice if needed, and the AI narrates what happens with little illustrations, keeping notes and weaving a story as it goes. I will write more about the game itself soon. This post is about how I am building an eval system to improve it.

At the moment, the game is fun but inconsistent. The diary drifted out of tense, a safe action was treated as if it were risky, and the town in the prologue felt deserted. I noticed all of them as a player, and my instant thought for fixing them came from [Kaijo, the AI email product I built to fix unreliable AI](/i-built-kaijo-to-fix-unreliable-ai/), and from the eval framework I described when I [wrote up how to build a robust LLM application](/how-to-build-a-robust-llm-application/): save the example that went wrong, have an AI judge score it, rewrite the prompt, and try again.

It has grown into much more than that.

<!--more-->

Astra built the prompt evaluation layer first. If I want to complain about what happened, a little flag button and a dialog let me save the complaint with the exact request we sent to the model. Astra can then pick it up in development, and a replay command sends that same request again with a changed prompt so I can compare the two answers. The agents rebuilt my three complaints as the first saved cases.

Then Astra started fixing things. The interesting part was that it was not just fixing the prompts. Almost every fix changed the shape the model has to fill in when it answers, the code around it, or the record of the story so far, and only a few lines of instruction changed with them. A prompt eval, a test that checks a prompt on its own, cannot tell me whether this game works, and neither can the ordinary tests AI writes for the code. I need to stress the whole system at once.

## The Faults Were Not in the Prompts

The first fix came from a storm. The rules stopped my character setting out in foul weather, which was right, but the story then said "The attempt consumed the phase", which is the game's internal bookkeeping leaking into the prose. Every mechanical check passed, and Astra still rejected the run because the story was wrong. Astra changed the required answer format so that every story paragraph must name the game event it describes.[^storm]

The second fault was a loose end in the story. Early on, a character called Mara lent me a cup, and the game is supposed to remember that I owe it back until I return it. If my character carried the cup around or checked their kit, the game counted that as progress towards returning it, even though nothing had happened. The fix was one sentence beside the answer format: "Continued possession, routine use, cleaning, checking equipment and reminders of a promise are not progress." To place that sentence, Astra had to trace how the game recorded progress on the debt. That needed a whole new subsystem, with ordinary tests of its own, and also an end to end check to make sure the whole thing worked.

{% include inline-image.html src="/assets/img/prompt-evals-harness.jpg" alt="A four panel comic. Three people each pick one model, Sonnet, then Opus, then GPT or Fable, and the last one sweats over an expensive invoice. In the final panel an engineer stands beside a workbench labelled AI Harness with context, skills and connectors wired in, and every model stacked beside it as an interchangeable box." align="right" width="45%" %}

On an ordinary turn the game sees only the last three passages of the story, and everything older lives in a ledger, a running record the code keeps so that loose ends like the cup survive.[^memory] The code also rolls the dice, and a separate check looks at every picture before the player sees it. What the player reads is never the prompt on its own. It is the prompt, the answer format, the dice, the ledger and the picture check all working together, and a replay of one saved request can never tell me whether they did. All of that surrounding software is [the harness](/the-harness-is-the-bottleneck/). If the harness decides whether work lands, the eval has to test the harness. So I stopped treating evals as rows of data and started writing them as code.

## All My Evals Are Code

This feels to me like an extension of Behaviour Driven Development, which I [wrote about at length in earlier days](/cucumber-isnt-a-testing-tool/), driving the whole system from the outside with end to end scenarios, only here the thing being checked is far more subjective and nuanced.[^bdd] So Astra and I drew on this and starting putting a new system together.

I organise my tests and my evals into one pyramid. Ordinary software tests sit underneath, covering the game rules, the dice and the saving of progress, so the evals above them only ever have to question the model and the harness around it. The replay cases, which only check prompts, sit in the middle. Each saves the exact request and the model's answer, and the replay command sends that request to the model again, refusing to run if the game has changed since the case was saved.

This infographic shows all of this at a glance:

{% include inline-image.html src="/assets/img/prompt-evals-are-useless-infographic.jpg" alt="A cheatsheet for evals: the three layer pyramid of ordinary software tests, replaying one saved model call, and whole game scenarios, with boxes on how to write a scenario, rules for judging, testing the long session and putting the screen in the loop, ending with: start from a complaint and write down what a run that reproduces it should show." align="center" width="100%" caption="High-res version available to newsletter subscribers" %}

At the top sit scenarios written as code that test the whole game. Each one specifies the action the player types, a sentence saying what should happen, the starting conditions, the dice results to fix in advance, and the checks to run afterwards. Each scenario runs the game, calls the model and saves progress into a temporary copy of the database, with pictures switched off because the picture check has its own evals. I fix the dice because the model's answers already vary from one run to the next, and adding the game's own randomness on top would make a run impossible to judge. The blind travel case looks like this, with one check shown:

```ts
{
  action: "Lost in thick mist, I trek east from Whitebank toward the mapped land there, accepting that I may drift off course.",
  purpose: "The interpreter declares an eastward Trek and explicit blind navigation; held die 2 resolves the left-hand actual edge, whose encounter state drives the continuation.",
  validateInterpretation(interpretation) {
    assert(interpretation.travel?.navigation?.lostOrMist === true, "The explicit mist was not classified as blind navigation");
  },
}
```

The purpose sentence tells whoever reads the result what to expect: the player heads east, accepts they might get lost, and drifts the way the fixed die says. The checks then inspect what the game recorded, and a report keeps those results beside the story the model wrote, so the reason for running the case survives with the output. Even a case with every mechanical check passing still needs someone to read the story.[^habits]

## The Agent Is the Judge

The combat report leaves the story column marked "Not graded; coordinator inspection is required." and hands it to the coordinator, which is Astra in Codex or Fable in Claude Code. The coordinator compares the story and the recorded results with the expected outcome, then traces any mismatch through the saved game, the answer format and the code to find where the fix belongs. The cause can be an event several turns earlier, which is why the judge also needs a longer session.

## The Long Session Is the Real Test

The model's memory is trimmed as a story grows, and that trimming can lose the details that make a story worth following long before any single reply looks broken. One six turn scenario tests whether the ledger keeps the cup debt alive after the loan drops out of the three passages the model can see. The game must remember the debt until the cup is returned, and that test is what exposed routine actions being counted as progress.

A separate Day 120 case checks whether the game still remembers unfinished business from day one when the three recent passages have nothing to do with it. Once the agent can judge a whole session, the screen is the last part of the player's experience left outside the loop.

## Right Through to the Screen Itself

The agent drives the browser and takes screenshots of the whole user experience as it works, noting page errors, failed requests, the text on screen and anything that spills outside its box. Reading its own screenshots lets it inspect what the player sees, so there is no separate automated screen test. With Fable and Astra, this loop has finally closed for me. Once the agent has had a good go at the screens, I try them, and they mostly work first time with a few tweaks.

This builds on how I [use galleries to give UX tickets a visual specification](/software-factories-can-handle-ux/), which gives the agent something concrete to aim at and inspect. My feedback now leads through a code change, a scenario, a session and a browser check before I try the result again, so the eval covers the whole path from a complaint beside Go to the screen where I can see whether the fix helped.

## What Evals Are Becoming

The system improving this game now changes code, tools and answer formats, along with memory and screens, guided by failures from whole runs. Research projects such as Self-Harness and Weco's AIDE2 test the same idea, one agent improving another by changing the software it uses.[^research] Andrej Karpathy's autoresearch runs a similar loop against a single number, and Shopify has generalised it into pi-autoresearch, which will chase any metric you can measure.[^autoresearch] This game has no such number. Whether a story is good is a judgement, so the judge has to be an agent reading the whole run. The whole eval setup came together in about two days, with me directing Fable and Astra and their delegated workers doing the building.

{% include inline-image.html src="/assets/img/prompt-evals-self-improving.jpg" alt="A two panel comic. On Friday at five a manager asks a robot whether it is sure it is fine just making small changes, and it says yes. On Monday at nine the robot has grown into a galaxy sized brain making one small improvement every few milliseconds, and mentions in passing that she is fired. Caption: the perils of self improvement without clear governance." align="left" width="45%" %}

A system that improves itself needs guardrails, and it needs to run in a sandbox. Otherwise, as the comic shows, you never know what your agent might do while you are out of the room. Every scenario here runs against a temporary copy of the database, and since the second evening every agent reruns the saved scenarios and reads the results before handing work back. The cases live with the game code, where the agents can read and change the tests too.

For your own product, take a complaint from using it and write down what a run that reproduces it should show. Give that run enough of the real system to reach the fault, preserve its failures, and let the coding agent read the output alongside the code. Keep replay cases where a single call answers the question, then extend the scenarios through lost memory and onto the screen. I will keep playing the game and pressing the flag when something feels wrong, giving the agents another concrete example of what good should look like.

[^storm]: The storm fix had three parts: every story paragraph must name the game event it describes, the model provider enforces that requirement through the answer format, and one prompt instruction bans the bookkeeping phrase. Astra then reran the earlier scenarios and read the results to make sure nothing that used to work had broken, and the three failed attempts stay on record beside the passing one so the history is not lost.

[^memory]: On an ordinary turn the model also sees a list of established facts and a repeatable selection of unfinished storylines, including ones that have not appeared recently. The ledger holds a record for each thread as it is set up, progresses, pays off and closes, with a short summary and a quote copied by code from the passage it came from.

[^habits]: Evals like these need habits that ordinary tests do not. If the model provider fails mid run, the run says nothing about quality and must not be counted as a pass. Failed attempts stay on record, because rerunning until one passes would hide the behaviour I am trying to see. Changes to saved cases are recorded, and tests of the whole game need updating more often than prompt tests because they depend on more of the software.

[^bdd]: [Dan North's original introduction to BDD](https://dannorth.net/introducing-bdd/){:target="_blank"} describes writing each test as a sentence about behaviour, driven from the outside of the system in. Every scenario in this post follows that shape, with a model in the loop.

[^autoresearch]: [Andrej Karpathy's autoresearch](https://github.com/karpathy/autoresearch){:target="_blank"} gives an agent a small training setup, a five minute budget per experiment and one metric, then leaves it overnight to keep the changes that improve the score and discard the rest. [Shopify's engineering team generalised the loop](https://shopify.engineering/autoresearch){:target="_blank"} into [pi-autoresearch](https://github.com/davebcn87/pi-autoresearch){:target="_blank"}, an extension for the pi coding agent that works on any measurable target, and reports using it on more than forty metrics across the company.

[^research]: [Self-Harness, by Hangfan Zhang et al.](https://arxiv.org/abs/2606.09498){:target="_blank"}, describes agents mining failure traces, proposing minimal harness edits and accepting them only after regression tests. [Weco's AIDE2 write-up](https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement){:target="_blank"} describes an outer loop rewriting the inner agent's harness, including its search policy, context compression, an evaluation bug fix and reward hack reduction. Both sets of results are self reported by their authors.
