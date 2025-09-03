---
layout: post
title: "Writing and Thinking with AI: Why Repositories Beat Chatbots"
date: 2025-08-29 00:00:00 +0000
image: /assets/img/writing-thinking-ai-repositories-vs-chatbots.png
categories:
- ai
- writing
- knowledge-management
- productivity
---

The absolute best way to do AI-assisted writing right now is not through chat interfaces. It is repositories.

After months of experimenting with different approaches to AI-powered writing and knowledge management, I have discovered something counterintuitive: the most powerful way to work with AI is not through polished chat interfaces like Claude.ai or ChatGPT. It is by treating your writing projects as living repositories that grow smarter over time.

This shift from disposable conversations to persistent, context-rich workspaces has transformed how I write, research, and organise knowledge. The difference is not just incremental. It is a fundamental reimagining of what AI collaboration can be.

<!--more-->

## The Problem with Chat Interfaces vs The Repository Approach

Traditional AI chat interfaces feel impressive at first. You type a question, get an instant response, and move on. But this interaction model has fundamental limitations when it comes to serious knowledge work.

Yes, many chat UIs now offer "projects" where you can save conversations and upload documents. Claude.ai has projects. ChatGPT has custom GPTs and memory. But these are still fundamentally chat-first interfaces with bolted-on persistence. The context is limited, the organisation is weak, and you are still trapped in a conversational paradigm that does not match how complex knowledge work actually happens.

More critically, these systems do not grow naturally over time. Custom GPTs and projects are static configurations that are difficult to evolve. You cannot easily get the AI to edit its own instructions, refine its understanding of your preferences, or adapt its behaviour based on what it learns from working with you. The knowledge remains frozen in its initial form rather than becoming a living, evolving system.

Every conversation starts from scratch. Even with projects, the AI has limited understanding of your broader work, your evolving needs, or the connections between different pieces of information. You find yourself repeating context, explaining your preferences, and managing dozens of separate conversations. The context is fragmented across projects and chats rather than unified in a single workspace.

For one-off questions, this works fine. But for complex projects that evolve over weeks or months, it becomes actively counterproductive. You spend more time providing context than getting value[^prompting].

**The repository approach changes everything.** Instead of ephemeral conversations, I treat each major project as a Git repository. Whether it is my Obsidian knowledge vault or this blog, the project lives in a structured directory with its own history, documentation, and growing context.

Claude Code is particularly well suited for this repository approach. It was designed to handle large amounts of text, with built-in tools for searching through files with grep, finding patterns with glob, and reading entire directory structures. Unlike other AI tools that struggle with context windows, Claude Code can navigate through hundreds of files, understanding not just their content but their relationships and history.

This creates a fundamentally different dynamic. Instead of explaining my writing style every time, the AI learns from my existing work. Instead of starting conversations from zero, it builds on accumulated knowledge. The repository becomes a shared workspace where both human and AI understanding compound over time.

Here are a couple of examples of how I'm using this approach.

## Example 1: The Knowledge Vault

**The Knowledge Vault** is my [Obsidian](https://obsidian.md){:target="_blank"} repository containing all my research notes, saved articles from the Internet, journal entries, and interconnected ideas[^obsidian]. It serves as my external brain, a structured collection of everything I am thinking about and working on.

When I open my knowledge vault in Claude Code, it immediately understands the scope of my thinking. It can connect ideas across different notes and articles, creating unexpected insights from seemingly unrelated information. It surfaces forgotten commitments buried in meeting notes that I would have otherwise missed. 

The AI suggests improvements based on my writing patterns, understanding not just what I write but how I structure arguments and develop ideas. It helps organise information in ways that align with how I think, rather than imposing rigid categorisation systems. Most importantly, it can reference previous work when answering new questions, building on accumulated knowledge rather than starting fresh each time.

This persistent context creates a virtuous cycle. The more I work within these repositories, the better the AI becomes at understanding my needs and preferences. It learns not just from our current conversation, but from the entire history of the project. This is exactly the kind of context management that makes [building robust LLM applications](/how-to-build-a-robust-llm-application/) possible: deep understanding rather than shallow pattern matching.

### Living the Science Fiction Future

In 1992, Kim Stanley Robinson wrote about an AI research assistant that reads everything and connects ideas across an entire knowledge base. In his [Mars Trilogy](https://www.kimstanleyrobinson.info/content/mars-trilogy)[^mars], the character Jon Boone uses an AI system that surfaces insights he might have missed. It felt like distant science fiction at the time.

Yet here I am in 2025, living that reality every day.

My notes have evolved from a scattered collection into a living system. The AI does not just search. It understands. It finds connections I have missed, surfaces forgotten commitments, and builds a semantic map of my thinking.

Here is exactly how it works: I maintain my knowledge vault as a markdown repository in [Obsidian](https://obsidian.md){:target="_blank"}. When I open this vault in Claude Code and ask for a review, it reads through everything, understanding every note and connection. It spots tasks in meeting notes and suggests adding them to my todo lists. It reviews my periodic notes and helps me reflect on themes and progress. It processes links I share, creating smart summaries that it can reference later when answering broader questions about the repository.

The power is not just in searching. That would be merely a fancy keyword search. It is in how the AI builds a deep understanding of my knowledge graph. It sees relationships between ideas, builds context over time, and actively helps organise information in ways that align with how I think[^graphrag].

### The Monday Morning Strategy Session

Every Monday begins with a structured "Strategy Session" - a focused session that sets the week's direction by combining calendar awareness, goal alignment, and realistic capacity planning within my knowledge vault repository.

<div class='float-right ml-8 mb-6 w-1/2 max-w-md pl-4'>
<img alt='CLAUDE.md Daily and Weekly Routine' src='/assets/img/claude-md-daily-weekly-routine.png' class='rounded-lg'>
<span class='text-sm italic'>To get the high-res version of this guide <a href="https://chrismdp.com" target="_blank">sign up to my newsletter</a>.</span>
</div>

The four-step process starts with context review, checking calendar for upcoming meetings and deadlines whilst reviewing current month and quarter goals stored in the vault. I ask AI to ask me questions about what I want to achieve and how I have reflected on the previous week's review. Reality assessment follows, honestly evaluating energy levels, health, and unexpected demands documented in daily notes. Strategic alignment connects immediate tasks to bigger picture business objectives using the interconnected note system. Finally, energy-aware prioritisation schedules demanding creative work for high-energy periods and routine admin for low-energy slots.

Rather than creating impossible schedules, the method acknowledges real constraints like illness, urgent client issues, and competing priorities. This builds sustainable momentum instead of setting up for failure. When facing choices between building features or talking to customers, the strategy consistently prioritises customer conversations. A single webinar becomes both content delivery and market research.

Unpleasant but necessary tasks get strict time limits. This prevents them consuming the entire week whilst ensuring professional handling. The plan explicitly schedules demanding work for peak energy periods and routine tasks for low-energy times, treating attention as a finite strategic resource.

The method works because it treats energy and attention as finite strategic resources rather than unlimited inputs, whilst maintaining laser focus on revenue-generating activities that serve genuine market needs.

### The Review System

The knowledge vault includes an automated review system that transforms daily observations into structured, interconnected knowledge. This review system lives in a few paragraphs in CLAUDE.md and operates on multiple levels:

**Daily Notes** serve as raw capture of thoughts, meetings, observations, and activities. These feed into **Topic/Project Notes** which become organised knowledge repositories for specific subjects like people, companies, projects, and concepts. **Periodic Notes** at weekly, monthly, and quarterly levels track progress and themes.

The weekly review cycle processes 20-30 files, reading through all daily notes and extracting relevant information to move into appropriate topic notes. It maintains context by reading existing topic content first, then updates rather than duplicates knowledge. The system automatically creates wikilinks for all dates, people, companies, and projects, ensuring bidirectional connectivity throughout the knowledge graph.

What makes this powerful is the interactive reflection component. The AI asks strategic questions one at a time based on the week's events, waiting for responses rather than making assumptions. It incorporates answers directly into the weekly review with timestamped reflections, capturing not just what happened but how I felt about it.

When reviews cross month or quarter boundaries, the system automatically triggers comprehensive period closures, reading all notes from the completed period to create holistic summaries. At week starts, it reviews previous period progress to suggest ambitious but realistic goals aligned with longer-term objectives.

This creates a living knowledge base that grows more valuable over time, rather than just an archive of past events.

## Example 2: The Blog Repository

**The Blog Repository** is the [Jekyll](https://jekyllrb.com){:target="_blank"} site you are reading now[^jekyll]. It contains published articles, drafts in progress, images, and all the technical infrastructure for publishing content. But it also serves as the hub for all my marketing efforts and strategic thinking about content.

### Writing Articles

My blog writing process has evolved to leverage this repository-based approach completely. The AI has immediate access to my previous posts, writing guidelines in CLAUDE.md, and established voice patterns.

First, I brain dump everything into Claude Code while the blog repository is open. Random thoughts, half-formed opinions, struggles, and insights, all captured through voice dictation using Wispr Flow[^wispr-flow]. Unlike working with a fresh chat interface, the AI can immediately draw connections to my other work, suggest relevant links to previous articles, and propose structures that fit my established patterns.

The editing process becomes collaborative in ways that feel impossible with traditional chat interfaces. I go through paragraph by paragraph, but the AI can reference my CLAUDE.md style guide, understand my typical argument patterns, and maintain consistency with my voice across the entire body of work. These style guides become living documents that evolve with my practice, similar to how I maintain architectural patterns when [coding with AI](/coding-with-ai/).

Every time I go through the process of writing an article or doing a review, I am constantly updating and tweaking my rules files. Whenever the AI makes a mistake, I treat it like feedback to an employee. I explain what went wrong, why it matters, and how to do better next time. Then I update the relevant CLAUDE.md or role file so the same mistake does not happen again. This creates a genuine learning system rather than static instructions.

The repository contains detailed guidelines about tone of voice: direct and conversational, confident but not arrogant, no contractions, specific technical advice for my target audience of CTOs and engineering leaders. It knows to link implicitly within sentences rather than using "check out this post" style linking. It understands my preference for British English throughout.

This very post was written using this method. The AI did not just help with individual paragraphs. It helped structure the entire argument while understanding how it fits into my broader thinking about AI tools and development practices.

### Social Roles

The blog repository includes a `_roles` directory with specialised AI personas for different types of content. The most sophisticated persona I've developed is Sally, my social media manager, who lives in `_roles/sally-social-media-manager/` with detailed instructions for LinkedIn posts, carousels, and newsletters.

Sally's role files contain specific voice and tone standards, content structure requirements, and crucially, performance data from actual posts. She knows that awareness posts with economics and cost shock are my top performers, that personal mistake stories massively outperform authority-based content (people clearly like to see me fail!) and that specific numbers are essential in high-performing posts.

Her instructions include optimal content structure for LinkedIn, specific hook requirements, and detailed formatting guidelines that drive performance[^sally]. She knows to use emojis for structure instead of markdown headers, avoid hashtags, and follow engagement patterns based on real data.

When I need to create social media content, I can invoke Sally by referencing her role files. She understands my voice, knows which content patterns perform best based on actual data, and follows specific formatting requirements. This eliminates the repetitive context-setting that plagues chat-based workflows.

### Marketing Hub

The blog repository has evolved into the central hub for all my marketing efforts. It contains not just published content, but marketing strategy documents, content calendars, performance analysis, and integration points with other systems.

Every piece of marketing content connects back to the core repository. Blog posts link to each other, social media content references articles, newsletter content draws from both. The AI can see these connections and suggest how new content fits into the broader marketing ecosystem.

The repository includes templates for different content types, guidelines for each marketing channel, and historical performance data that helps inform content strategy. When planning new content, the AI can review what has worked before, identify gaps in coverage, and suggest topics that align with proven successful patterns.

This centralised approach means marketing decisions are informed by the full context of previous efforts, brand guidelines, and strategic objectives rather than isolated creative decisions.

## Improvements: Making It Even Better

### Enhanced Search with LEANN

Recently, I have been experimenting with [LEANN](https://github.com/anthropics/leann-server) to add embedded search directly within these repositories. This creates an even more powerful combination: the contextual understanding of repository-based AI work enhanced by semantic search across the entire knowledge base.

LEANN indexes my repositories and provides natural language search that understands concepts rather than just keywords[^leann]. This builds a semantic index of all my content that Claude Code can query instantly via MCP.

When combined with Claude Code's full repository context, this creates something approaching the AI research assistant Robinson envisioned decades ago - all I need is to add voice... Claude Code can use LEANN to find related articles when I am writing, identify patterns across years of writing, and surface connections I had forgotten existed.

The workflow is seamless: I can ask broad questions about themes across my entire knowledge base, then drill down into specific documents or ideas, all while maintaining the rich context that makes AI collaboration effective. Claude Code's native tools combined with LEANN's semantic search create a knowledge system that genuinely augments thinking rather than just retrieving information.

### Connecting the Two Repositories

One improvement I am experimenting with is connecting the knowledge vault and blog repository so they can inform each other. The knowledge vault contains my private thinking and research, while the blog repository focuses on public content and marketing. Finding ways to let them communicate could unlock powerful synergies.

The challenge is doing this without leaking personal notes into public marketing content, or overwhelming the AI with too much context. I need to train carefully, go slowly, and experiment with different approaches to selective context sharing.

The goal would be letting the blog repository draw insights from the knowledge vault when appropriate, while maintaining clear boundaries around private information. This could help surface research that should become public content, or identify themes from private thinking that could inform marketing strategy.

This remains experimental, but the potential is significant: a unified knowledge system that respects privacy boundaries while maximising the value of accumulated thinking.

### Taking It Online: The Coder Integration

The next evolution involves taking these repositories online using [Coder](https://coder.com){:target="_blank"} workspaces. Instead of being limited to local computation, I can spin up fully isolated development environments that still maintain access to my complete project context.

This solves several problems: I can work from any device, scale computational resources as needed, and experiment with more advanced AI integrations without affecting my local setup. The repositories remain the source of truth, but the execution environment becomes flexible and scalable. As AI costs continue to plummet (we are seeing [150x cost reductions](/doing-real-work-with-ai-just-became-150x-cheaper/) in just months) these cloud-based workflows become increasingly viable.

The integration is still experimental. I wrote about the current limitations in [Independent Coding Agents: The Tools Aren't Ready](/independent-coding-agents-tools-arent-ready/). But the trajectory is clear. We are moving toward fully autonomous development environments that maintain rich, persistent context across all our knowledge work.

## Getting Started

If you want to experiment with repository-based AI work, start simple:

Choose one ongoing project and create a dedicated repository for it. Include documentation about your goals, preferences, and patterns. Add a CLAUDE.md file that explains how you want AI to interact with the project.

Start small conversations within this context, letting the AI learn from your existing work rather than starting from scratch each time. Notice how the quality of collaboration improves as the shared context grows.

The goal is not to replace all AI interactions with repositories, but to identify the knowledge work that benefits from persistent context and intentionally structure those projects for AI collaboration.

## The Future of Knowledge Work

Repository-based AI collaboration points toward a future where our knowledge systems become genuine thinking partners. Not just tools for capturing information, but active participants in making sense of complexity.

This approach has implications far beyond writing blog posts. It represents a fundamentally different model for knowledge work in the age of AI. Traditional productivity systems assume human cognition as the bottleneck. We create systems for capturing and organising information because our brains cannot hold it all. But when AI can understand and connect vast amounts of information, the bottleneck shifts from memory to context management.

The challenge becomes not just capturing information, but creating systems where AI can understand the relationships, priorities, and patterns that make that information useful. Repositories provide this structure. They create persistent contexts where both human and AI understanding can compound over time.

Repository-based AI work requires more upfront setup than firing up a chat interface. You need to think about information architecture, maintain consistent documentation, and invest time in creating the context that makes AI collaboration effective. You need to keep updating the rules. The cognitive overhead is different. Instead of quick, disposable interactions, you are building systems intended to evolve over months or years.

But for serious knowledge work, writing that matters, research that compounds, creative projects that evolve, the investment pays dividends. The AI becomes genuinely helpful rather than merely impressive.

We are still early in this transition. The tools are evolving rapidly, the best practices are still emerging, and many of the most interesting possibilities remain unexplored. But the core insight feels robust: the most powerful AI collaboration happens not in ephemeral conversations, but in persistent contexts that grow smarter over time.

The future of knowledge work is not human versus AI, or even human plus AI. It is human and AI working together in shared spaces designed for understanding to compound. Repositories are just the beginning.


[^mars]: I'd _highly_ recommend reading the Mars Trilogy if you are interested in hard science fiction and an optimistic view of the future. The trilogy (Red Mars, Green Mars, Blue Mars) follows the colonisation and terraforming of Mars over nearly two centuries. It's remarkable not just for its scientific plausibility, but for how it explores the social, political and psychological implications of space colonisation. The invention of the AI assistant that appears in the books, along with other uses of AI, was remarkably prescient about how we might use AI to augment our thinking and research capabilities.

[^leann]: I keep my LEANN index updated with the command: `leann build blog-vault --force --embedding-mode openai --embedding-model text-embedding-3-small --docs *`. The `--force` flag rebuilds the entire index, while the embedding model choice balances cost and quality. You can experiment with different OpenAI embedding models depending on your needs and budget.

[^sally]: Sally's LinkedIn specifications include 1,250-3,000 characters with 14+ short paragraphs for optimal engagement, hook requirements with a strict 62/0/50 character format (62 chars first line, blank line, 50 chars third line), and performance data showing that awareness posts with specific economics outperform educational content 3-5x. The role files contain actual metrics from hundreds of posts, making content decisions data-driven rather than intuitive.

[^jekyll]: I have been using Jekyll for [about 15 years](/jekyll) to run this site. The longevity means the repository contains a substantial history of content, writing evolution, and established patterns that provide rich context for AI collaboration.

[^obsidian]: I have been using this Obsidian repository for about three years to capture all my notes, so it already had a pretty good set of context when I started experimenting with AI-assisted knowledge management. The accumulated notes, connections, and patterns gave the AI substantial foundation to work from rather than starting with an empty vault.

[^graphrag]: This approach to understanding connections between pieces of knowledge is similar to what I explored in [Graph RAG: The Future is Relationships](/graph-rag/), where the focus shifts from isolated information retrieval to understanding how knowledge interconnects. Traditional RAG systems retrieve relevant documents, but Graph RAG understands the relationships between concepts, creating a more nuanced and contextual understanding of information.

[^wispr-flow]: [Wispr Flow](https://wisprflow.ai/r?CHRIS104) is an excellent voice-to-text app that transforms spoken thoughts into well-structured text. This is a referral link, but I would recommend Wispr Flow regardless because it genuinely enhances AI-assisted workflows by bridging the gap between brain dumping and structured thinking.
[^prompting]: As I explored in [Prompting Sucks (And What We Can Do About It)](/beyond-prompting/), the fundamental problem with prompting is that it is brittle, repetitive, and endlessly frustrating. You end up spending more time crafting the perfect prompt than actually getting work done, and the AI never remembers your preferences from one conversation to the next.
