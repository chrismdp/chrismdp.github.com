---
layout: post
title: "The Job Is Not To Build"
date: 2024-12-01 21:00:00
categories:
- business
- product
- startup
- sol trader
- cto
---

Startup CTOs or founding developers are the first technical people in the business. It is natural to think your job is to write code and build software. This is backwards.

Your first job is not to build software. Your role is to use your technical expertise to help the startup figure out fast if you have a valid solution to a compelling problem, and then a valid product for a big enough market.

You might do this through building software, but you might not need to.

Here is a story of how I did this wrong, and how you can do it right.

<!--more-->

## Building the wrong thing

When I created [Sol Trader](https://store.steampowered.com/app/396680) between 2012 and 2016, I made the game I always wanted to play. I [released early](/sol-trader-now-in-alpha/), determined to get feedback. I waved away much of the early feedback because they had not understood what I was making. The product was not finished yet. I knew what I wanted to build.  

I used [KISSmetrics](https://kissmetrics.io) to add lots of analytics and events, so I could track what players were doing. These metrics told me that players would play for a while, and get bored. This did not matter. I was missing key features. Once those were in place, the players would come back. I knew what I wanted to build.

I spent thousands of hours building a carefully designed, well architected game complete with a custom C++ engine that compiled in a few seconds. It was glorious.

On release, I got negative feedback. The game received a torrent of blunt Steam reviews, stating similar issues to early feedback I had received. I discovered that, outside a small niche, not enough people wanted to play it.

At that point I was worried. My response was to build more. I released many patches. These made a small difference, but did not move the needle.

The problem was not that I did not talk to customers, or look at engagement metrics. The problem was that I did not listen.

Eventually I realised I had made the wrong game. I had jumped to building the game of my dreams, without truly understanding the gap that my game might fill in people's lives. That is fine if game development is a hobby, but I wanted to make it a business. I did not think through whether I had the right product for a big enough market.

I had no idea that the first job is not to build.

To explore this further, time to look at why we are here in the first place.

## Why startups exist

Startups exist to find a solution to a problem someone has, and then to build a product around it. Ideally that problem is not being addressed well for a certain group of people, and there is a chance to improve the lives of those people in a way that makes money.

Essentially, there need to be:

1. **enough customers out there**[^1], that
2. **you are able to reach** with a
3. **big enough problem** that is
5. **worth them paying you to solve it** that
4. **you are capable of solving.**[^2]

Answering these questions is the only thing that matters at first. Once the team has figured out the answers you have a business. Simple, but difficult. This process will take months or years.

Your job is to use your skills to help the team figure out these five things. Here is what you can do to help.

## Identify the bigger problem

Join customer research calls. Deeply understand the challenges your customers face. Fall in love with the problems they have. Solutions are fleeting, problems are eternal.

Do not delegate this to a product manager or the CEO, however competent they are. This is especially true if you are a co-founder. Seeing a problem first hand will elicit sparks of technical insight. Bring that insight to team discussions. Enlighten your team on what is possible.

Only you really know what software is capable of. Everyone else in the team is likely to have assumptions about what can or cannot be done.

This will help the team see a bigger problem than the first one in front of you. The problem that is really worth solving.

Help your team dream bigger.

## Demonstrate what is possible

If necessary, build prototypes to prove out what can be done. Demonstrate fast what is possible. Learn quickly about what is high risk and what cannot be done.

We did this at [Cherrypick](https://cherrypick.co) with our AI enabled meal planning feature. It was difficult to convince the rest of the business that it could work, so I spent a few hours sticking together a prototype to demonstrate what it could do. The impact was high, and it moved to production.

You will never be as small or be able to move as fast as you can right now. This is a strength. Use it to try a lot of things very quickly. Remember, [code is a liability](/your-code-is-a-liability). Do not build more than you must.

Sometimes founders do not take on the problem they really want to solve—because they cannot envisage a solution. You can help with that. The art of the possible lies with you.

Demo to potential customers. Listen to what they say to you and iterate. Ask them to commit to paying for you to solve this for them, and then build the proper solution in response. Regularly review what they are telling you in case you need to change direction. State hypotheses in advance and hold them lightly.

## Help the team reach people

Set up simple systems to manage your customer funnel. Use simple cheap tools to start, and stay low tech until you have figured out what you want.

If you are selling to businesses, a simple sales funnel can be a Google Sheet, or even a Slides doc, or perhaps a Notion page. If you are doing direct sales or customer outreach, help set up a simple CRM. As a technical person, you are good at information flow. Use your knowledge to keep the team efficient.

Be careful not to collect too many SaaS services. These add up over time and before you know it your pipeline is expensive to support and difficult to unpick. Buy in just enough, and make the rest work with what you already have.

If you are selling direct to consumers, you may assume you are trying to reach lots of people at first, and you need tools to do this. Again this is backwards. At first you are trying to understand who to reach, and how many of them there are. You can still start with very simple tools that do not scale.

At [Cherrypick](https://cherrypick.co) in the early days we used a shared Google Sheet to track all of our customer development questionnaires, and recorded the calls via Google Meet. As our customer numbers increased to tens of thousands, then hundreds of thousands of people, we moved our surveys to [Typeform](https://typeform.com/) and [Maze](https://maze.design/), and our analysis to [BigQuery](https://cloud.google.com/bigquery). We built simple processes for identifying good people to speak to, and kept the spreadsheets for video interviews.

Technical people are good at managing complexity. Use these skills to figure out what works for your stage and reduce wherever you can.

## Coding envy

If you feel you are not using your coding skills, it is time for a moment of self-reflection. If you prefer to code all day, you might be in the wrong job.

Startup technical work is not just coding. It is learning; it is communicating the art of the possible.

Your skills come in when you have to understand whether or not to build, or when to build. Nobody else can tell whether a system needs creating to solve the problem, or how much needs to be built now.

Put the editor down for now. Learn, demonstrate and enable. When you do this, you are not just adding to your team's effectiveness. You are multiplying it.

---

[^1]: Reminder: if you are not charging your users, they are not your customers. Customers are people that pay you money directly.

[^2]: There is a fantastic expanded version of this idea in [The Growth Equation](https://www.amazon.co.uk/dp/1068746106?psc=1&smid=A3P5ROKL5A1OLE&ref_=chk_typ_imgToDp). Disclaimer: the author Andy is a friend of mine, but the book is still great.

