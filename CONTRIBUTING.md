---
layout: default
title: Contributing
nav_order: 8
---

# Contributing to AI Knowledge Domain

## Content Philosophy

This knowledge base values **depth, discernment, and deliberate thinking**. Every entry should be:

1. **Substantive**: Adds genuine insight, not surface-level description
2. **Referenced**: Cites papers, implementations, or credible sources
3. **Opinionated**: Includes reasoned perspectives and trade-offs
4. **Concise**: Every word earns its place; no AI-generated fluff
5. **Connected**: Links to related concepts across the knowledge graph

## Entry Template

Use this template for new knowledge entries:

```markdown
# [Concept Name]

> One-sentence description of the concept and why it matters

## Context

Why does this concept exist? What problem does it solve?

## Technical Depth

Core explanation with sufficient detail for a senior practitioner:
- Key mechanisms or components
- How it works under the hood
- Mathematical formulation (if applicable)
- Code examples or pseudocode (if applicable)

## Trade-offs & Failure Modes

What are the limitations? When does this approach break down?

- **Strengths**: Where this excels
- **Weaknesses**: Where this fails or struggles
- **Gotchas**: Non-obvious pitfalls from experience

## Real-World Application

How is this used in production systems?

- Concrete use cases
- Implementation considerations
- Scale and performance characteristics

## References

### Primary Sources
- [Paper/Article Title](link) - Author, Year
- [Implementation/Repo](link) - Organization

### Related Concepts
- [[Related Concept 1]] - connection description
- [[Related Concept 2]] - connection description

## Personal Insights

Your own observations, opinions, or lessons learned:

> "Quote or key insight from experience"

**Opinion**: Your reasoned perspective on this concept

**Experience**: Specific situations where you've seen this work or fail

---

**Tags**: `tag1`, `tag2`, `tag3`  
**Domain**: Systems | Modeling | Product | People | Meta-Learning  
**Level**: Foundational | Intermediate | Advanced  
**Last Updated**: YYYY-MM-DD
```

## File Organization

### Naming Convention

- Use lowercase with hyphens: `transformer-architecture.md`
- Be descriptive but concise: `rag-retrieval-optimization.md`
- Avoid dates in filenames (use git history)

### Folder Structure

```
domain-folder/
├── README.md                 # Domain overview and learning path
├── foundational/             # Core concepts
├── intermediate/             # Applied techniques
├── advanced/                 # Specialized topics
└── resources.md             # Curated external resources
```

## Quality Checklist

Before adding content, verify:

- [ ] **Cited sources**: At least 2-3 credible references
- [ ] **No fluff**: Every paragraph adds value
- [ ] **Technical accuracy**: Claims are verifiable
- [ ] **Practical relevance**: Clear connection to real systems
- [ ] **Personal insight**: Includes reasoned opinion or experience
- [ ] **Cross-links**: Connected to ≥2 related concepts
- [ ] **Proper formatting**: Follows markdown standards
- [ ] **No AI generation**: Written/heavily edited by human

## Writing Style

**Do**:
- Write in clear, direct language
- Use technical terms precisely
- Include concrete examples
- Acknowledge uncertainty or debate
- Share failure modes and gotchas

**Don't**:
- Use marketing language or hype
- Make unsupported claims
- Dump AI-generated content
- Write generic summaries
- Avoid technical depth

## Example: Good vs. Bad

### ❌ Bad Entry

> "RAG is a powerful technique that combines retrieval with generation. It's widely used in modern AI systems and provides better results. Many companies use RAG for chatbots."

*Problem: Generic, unsupported claims, no depth, no references*

### ✓ Good Entry

> "RAG addresses LLM hallucination by grounding generation in retrieved context, but introduces latency/cost trade-offs that require careful optimization.
>
> **Core mechanism**: Given query q, retrieve top-k documents D from vector store, then condition LLM generation on {q, D}. The retrieval step adds 50-200ms latency depending on index size and distance metric.
>
> **Trade-off**: Better factual accuracy vs. increased cost and latency. In production, we've seen 30-40% reduction in hallucination but 2-3x increase in inference cost.
>
> **Reference**: [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), Lewis et al., 2020"

*Why good: Specific mechanism, quantified trade-offs, cited source, practical insight*

## Contribution Process

1. **Explore existing content**: Check if topic already covered
2. **Use template**: Follow the entry template above
3. **Write in your own voice**: Personal insights encouraged
4. **Add references**: Cite papers, repos, blog posts
5. **Cross-link**: Connect to related concepts
6. **Self-review**: Use quality checklist
7. **Commit with clear message**: `Add: [concept name] - [one line summary]`

## Maintenance

This is a **living knowledge base**. Content should be:

- **Updated** when new research changes understanding
- **Refined** when better examples or explanations emerge
- **Pruned** when concepts become obsolete
- **Reorganized** as the knowledge graph evolves

---

*Building knowledge, one deliberate insight at a time.*

