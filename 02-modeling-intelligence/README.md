# Modeling & Intelligence
*The Cognitive Layer*

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

*Explore specific topics in the folders above or start with [Embeddings & Vector Representations](foundational/embeddings-vectors.md)*

