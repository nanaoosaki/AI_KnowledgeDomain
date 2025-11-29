---
layout: default
title: Modeling & Intelligence
nav_order: 4
has_children: true
permalink: /modeling
---

# Modeling & Intelligence
{: .no_toc }

*The Cognitive Layer*
{: .fs-6 .fw-300 }

> How models reason, generalize, and fail—both traditional ML and modern LLMs

## Domain Overview

Understanding model behavior is fundamental to AI leadership. You don't need to implement every algorithm, but you must understand the trade-offs each implies and when to apply them.

## Core Capabilities

- **Model Selection**: Choosing the right approach for the problem
- **Representation Learning**: Embeddings, feature learning, transfer learning
- **Fine-tuning & Adaptation**: Customizing pre-trained models efficiently
- **Retrieval & Search**: Dense retrieval, hybrid search, ranking
- **Alignment & Safety**: RLHF, constitutional AI, red-teaming
- **Interpretability**: Understanding model decisions and failures
- **Evaluation**: Rigorous assessment of capabilities and limitations
- **Uncertainty Quantification**: Knowing when models don't know

## Knowledge Map

### Foundational Concepts
*Core understanding for working with models*

- [ ] Embeddings & Vector Representations
- [ ] Transfer Learning Fundamentals
- [ ] Attention Mechanisms & Transformers
- [ ] Language Model Scaling Laws
- [ ] Evaluation Metrics & Benchmarks
- [ ] Bias & Fairness Fundamentals

### Intermediate Topics
*Applied techniques for real-world systems*

- [ ] Fine-tuning Strategies (LoRA, QLoRA, PEFT)
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Prompt Engineering & Optimization
- [ ] Model Compression & Quantization
- [ ] Chain-of-Thought & Reasoning
- [ ] Embedding Model Selection
- [ ] Multi-modal Models
- [ ] Model Debugging & Failure Analysis

### Advanced Topics
*Specialized expertise for cutting-edge applications*

- [ ] Alignment Techniques (RLHF, DPO, Constitutional AI)
- [ ] Model Interpretability Methods
- [ ] Uncertainty Estimation in Neural Networks
- [ ] Few-shot & Zero-shot Learning
- [ ] Model Merging & Mixture of Experts
- [ ] Agentic Systems & Tool Use
- [ ] Adversarial Robustness
- [ ] Custom Architecture Design

## Learning Path

**If you're starting out** → Focus on embeddings, transformers, and evaluation fundamentals

**If you're building LLM applications** → Master RAG, fine-tuning, and prompt engineering

**If you're doing research/innovation** → Explore alignment, interpretability, and advanced architectures

## Key Resources

### Papers - Foundational
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Vaswani et al., 2017
- [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) - Devlin et al., 2018
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) - Brown et al., 2020 (GPT-3)

### Papers - Recent Advances
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) - Hu et al., 2021
- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) - Bai et al., 2022
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) - Lewis et al., 2020

### Courses & Tutorials
- [Hugging Face NLP Course](https://huggingface.co/course) - Practical transformer usage
- [Stanford CS224N](http://web.stanford.edu/class/cs224n/) - NLP with Deep Learning
- [Fast.ai](https://www.fast.ai/) - Practical deep learning

### Implementation Resources
- [Hugging Face Transformers](https://github.com/huggingface/transformers) - Pre-trained models
- [LangChain](https://github.com/langchain-ai/langchain) - LLM application framework
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified LLM API

## Current State (October 2025)

**Major trends**:
- Continued scaling of foundation models
- Efficient fine-tuning techniques (LoRA variants, merging)
- RAG architectures maturing and specializing
- Multi-modal models becoming standard
- Agentic systems and tool use emerging
- Open models approaching closed model quality

**Fast-changing**: Model architectures, benchmark rankings, specific techniques  
**Slow-changing**: Evaluation principles, probabilistic reasoning, attention mechanisms, transfer learning concepts

## Key Trade-offs in Practice

| Decision | Trade-off |
|----------|-----------|
| Fine-tuning vs. RAG | Latency/cost vs. freshness/flexibility |
| Larger vs. smaller model | Capability vs. cost/latency |
| Closed vs. open source | Quality/ease vs. control/cost |
| General vs. specialized | Versatility vs. task performance |

---

## Knowledge Articles

### Core Topics

- [1. Single-turn inference (API call)](how%20a%20chatbot%20experience%20different%20from%20API%20call.md)
- [1. The intuition first](how%20BERT%20next%20sentence%20prediction%20different%20from%20GPT%20next%20token%20prediction.md)
- [How To Set Up Remote Gpu And Local Notebook For Fine Tuning Pretrained Model](how%20to%20set%20up%20remote%20GPU%20and%20local%20notebook%20for%20fine-tuning%20pretrained%20model.md)
- [Scaling Law And Parameter Size](scaling%20law%20and%20parameter%20size.md)
- [🌟 1. What these tokens are called](summary%20of%20all%20the%20special%20tokens%20in%20language%20model.md)
- [A simple, durable framework for all search systems](the%20search%20landscape.md)
- [🌱 First: What actually changes between tasks?](what%20does%20it%20mean%20to%20train%20transfomer%20using%20your%20own%20corpus%20or%20dataset%20with%20labels.md)
- [1. Why tokenization matters](what%20happends%20during%20inference%20when%20interacting%20with%20SOTA%20models%20through%20chatbot.md)
- [1. More text ≠ easier classification](what%20makes%20resolution%20classification%20a%20much%20harder%20text%20classification%20task.md)
- [1. Start with the nature of the target (CSAT)](when%20do%20we%20use%20huber%20loss%20and%20when%20do%20we%20use%20cross-entropy%20loss.md)
- [1. Why tokenization matters](why%20tokenization%20matters%20and%20how%20to%20choose%20your%20method.md)

---

*Explore specific topics using the Knowledge Articles section above*

