---
layout: page
title: "Case Study: GPT Meal Generator"
permalink: /case-studies/gpt-meal-generator
excerpt: "How we built a production LLM system that reduced plan changes by 30% and increased basket usage by 14%"
---

<img src="/assets/img/meal-generator.jpg" alt="Meal Generator" class="float-right rounded-lg ml-6 mb-6 w-1/2 max-w-md"/>

## The Challenge

Cherrypick had operated a basic meal generator since early 2023. Customers could select how many meals they wanted for the week, and the system would generate a plan. They could reject meals and ask for alternatives, but there was no way to specify preferences or understand the reasoning behind recipe selections.

Customer feedback was clear: they wanted more personalisation and explanations for why certain recipes were chosen. The existing system felt rigid and opaque, leading to frequent plan changes and lower engagement with the generated meal plans.

This presented a perfect opportunity to explore how LLMs could add genuine value beyond the typical chatbot implementations flooding the market.

## The Solution

We built a production LLM system that creates truly personalised meal plans with natural language explanations. The breakthrough was recognising that this was not a chat problem but a completion problem.

Instead of forcing customers into lengthy conversations, we designed an interface where meal plans generate with one click. Customers can then refine their plans using LLM-generated rejection options that feel customised and natural. This approach eliminated conversation fatigue while maintaining the personalisation benefits of LLMs.

The system excels at tasks that uniquely benefit from LLM capabilities: understanding dietary preferences, combining compatible recipes, and generating natural explanations for choices. These were problems that would have been difficult to solve effectively with traditional programming approaches.

<img src="/assets/img/meal-generator-3.jpg" alt="Meal Generator Interface" class="float-right rounded-lg ml-6 mb-6 w-1/2 max-w-md"/>

## Technical Implementation

The implementation required careful consideration of both technical and business constraints. We calculated costs upfront, understanding that consumer applications with large user bases and small margins cannot sustain expensive LLM interactions.

Our meal generator requires only a few LLM calls per plan generation, compared to the dozens of messages typical in chat sessions. This made the system financially viable where other approaches would have eroded profit margins entirely.

Quality control became paramount given the unpredictable nature of LLMs. We built a multi-layered evaluation system starting with automated validation of JSON structure and recipe ID verification against provided context. This prevented hallucinated recipes from reaching customers.

Expert review formed the second evaluation layer. Cherrypick's Head of Food Sophie assesses generated plans for nutritional balance and flavour combinations, ensuring meals work well together throughout the week. These evaluations became training data for continuous improvement.

Context curation proved crucial for reliable results. Rather than sending the model our full recipe database and risking dangerous selections, we only provide recipes the customer can actually eat. This approach uses more tokens but delivers consistent, safe results.

## Results

The system delivered measurable business impact that validated our approach. Customers began changing their meal plans 30% less frequently, indicating they were more satisfied with the initial recommendations. More importantly, basket usage of meal plans increased by 14%, demonstrating that customers found the personalised plans more actionable and appealing.

<img src="/assets/img/meal-generator-reject.jpg" alt="Meal Generator Rejection Interface" class="float-right rounded-lg ml-6 mb-6 w-1/2 max-w-md"/>

These improvements came from a production-ready system serving real customers daily. The multi-layered evaluation framework proved its worth during launch, catching quality issues before they reached users. Despite initial concerns about LLM costs, the system operates comfortably within budget constraints thanks to careful interface design.

Beyond the meal generator itself, we shipped major additional features including a health scores system while maintaining high delivery standards. The evaluation infrastructure we built became reusable for future AI features, creating lasting value beyond this single project.

<div style="clear: both;"></div>

<!-- TFC Testimonial Section -->
<section class="py-20 bg-brand-deep-turquoise">
  <div class="max-w-4xl mx-auto px-6">
    <div class="bg-white rounded-lg p-8">
      <div class="flex items-center mb-4">
        <a href="https://www.linkedin.com/in/tomfostercarter/" target="_blank" style='text-decoration: none' class="flex items-center">
          <img src="/assets/img/testimonials/tfc.jpeg" alt="Tom Foster Carter" class="w-16 h-16 rounded-full mr-4 object-cover">
          <div>
            <div class="text-lg font-semibold text-brand-black">Tom Foster Carter</div>
            <div class="text-sm text-brand-black/70">CEO, Cherrypick</div>
          </div>
        </a>
      </div>
      <div class="flex text-yellow-500 mb-4 space-x-1">
        <span>⭐</span><span>⭐</span><span>⭐</span><span>⭐</span><span>⭐</span>
      </div>
      <p class="text-brand-black italic mb-4">
        "Chris helped us build a production LLM meal generator that achieved a 30% reduction in plan changes and 14% increase in basket usage. His expertise in AI systems allowed us to ship major new features including health scores while maintaining high quality delivery."
      </p>
    </div>
  </div>
</section>

## Key Learnings

The success came from treating this as a product challenge first, then finding the right technical implementation. We learned that LLMs excel when applied to problems that genuinely benefit from their unique capabilities. Natural language explanations and dietary preference understanding were perfect fits, but we would never use LLMs for simple categorisation tasks.

Interface design proved more important than the underlying technology. Our guided approach with LLM-generated options delivered superior results compared to chatbot interfaces. Users received personalisation benefits without conversation fatigue, creating a sustainable interaction model.

Building evaluation frameworks from day one prevented quality disasters and enabled confident model comparisons. This upfront investment paid dividends during scaling, allowing us to iterate quickly while maintaining reliability.

Perhaps most importantly, we learned to work with LLM limitations rather than fight them. Careful context curation eliminated dangerous outputs while preserving the flexibility that makes these systems valuable. The key was designing constraints that enhanced reliability without sacrificing the core benefits.

## The Impact

This case study demonstrates how to build LLM applications that actually work in production. Too many AI projects become investor demos rather than shipped products.

The key was treating this as a product challenge first, then finding the right technical implementation. The result was a system that improved customer experience while operating within business constraints.

**Want similar results for your team?** Chris can help you identify where LLMs add real value and build systems that work in production, not just in demos.

<div class="bg-white rounded-lg p-8 text-center mt-12 border border-brand-light-blue/20">
  <h3 class="text-2xl font-heading font-bold text-brand-black mb-4">Ready to build production AI systems?</h3>
  <p class="text-brand-black/80 mb-6">Get the same systematic approach that delivered these results. Fill in the form to get started:</p>
  <div class="rm-area-embed-services"></div>
</div>
