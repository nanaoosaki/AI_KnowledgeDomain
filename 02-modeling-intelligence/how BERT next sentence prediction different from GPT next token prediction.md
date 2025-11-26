---
layout: default
title: 1. The intuition first
parent: Modeling & Intelligence
---

*[← Back to Modeling & Intelligence](README.md)*

---

# **1. The intuition first**

**BERT’s NSP**
→ A *classification task* about whether two sentences belong together.
→ It is **not** predicting text.
→ It is **not** generative.

**GPT’s next-token prediction (autoregressive LM)**
→ A *prediction task* over the next word/piece of text.
→ It is **how the model learns the entire distribution of language**.
→ It is fully generative.

These are fundamentally different worlds.

---

# **2. What BERT’s NSP actually does**

BERT was trained with two objectives:

### **(1) Masked Language Modeling (MLM)**

Predict missing tokens:

```
The cat sat on the [MASK].
```

### **(2) Next Sentence Prediction (NSP)**

Given two segments A and B:

```
A = The cat sat on the mat.
B = The dog barked loudly.
```

The model must classify:

```
Is B the actual next sentence after A?  (Yes/No)
```

It’s a binary classification task.
**The output is just: “IsNext” or “NotNext.”**

### Why they added NSP

At the time, researchers believed:

* it would teach discourse relationships
* it would help BERT understand paragraph-level coherence
* it would improve performance on QA and NLI tasks

Later research showed NSP barely helps and may even hurt.

RoBERTa removed NSP entirely and got *better* results.

---

# **3. What GPT does (next-token prediction)**

GPT has one objective:

### **Predict the next token in the sequence.**

```
Input:  The cat sat on the
Output: next token = "mat"
```

But because the model sees trillions of tokens over time, it learns to:

* continue text
* plan long sequences
* maintain coherence
* imitate reasoning
* generate paragraphs
* follow instructions once fine-tuned

This is because NTP forces GPT to model:

* syntax
* semantics
* discourse
* long-range dependencies
* world knowledge
* pragmatic language use
* planning and continuation

Everything emerges from the single goal:
**“given context, predict the next token.”**

---

# **4. Why NSP ≠ NTP**

| Aspect                 | BERT NSP                        | GPT Next Token Prediction             |
| ---------------------- | ------------------------------- | ------------------------------------- |
| **Type of Task**       | Classification (Yes/No)         | Prediction (token distribution)       |
| **Output**             | Binary label                    | Vocabulary probability distribution   |
| **Model Training**     | Non-generative                  | Fully generative                      |
| **Goal**               | Coherence between two sentences | Learn full language distribution      |
| **Emergent Abilities** | None beyond NLU                 | Reasoning, creativity, code, planning |
| **Context Flow**       | Bidirectional attention         | Left-to-right causal attention        |
| **Use Case**           | Understanding tasks             | Generation + reasoning tasks          |

NSP teaches almost nothing about text generation.
NTP teaches everything about how language behaves.

---

# **5. The deeper structural difference: Encoder vs Decoder**

### BERT (Encoder-only)

* Uses bidirectional self-attention
* Looks at the whole sentence at once
* Learns *representations*
* Cannot naturally generate text

### GPT (Decoder-only)

* Uses causal self-attention
* Processes text left → right
* Naturally produces continuation
* Scaling leads to emergent abilities

So even without NSP, an encoder cannot do next-token prediction properly because its architecture is not autoregressive.

---

# **6. A simple analogy**

**NSP is like asking:**
“Do these two puzzle pieces fit next to each other?”

**Next-token prediction is like saying:**
“Given the puzzle so far, what’s the next piece?”
And continually generating the puzzle itself.

One is a judgment.
The other is an act of creation.

---

# **7. Why GPT-style models dominate today**

Because next-token prediction:

* scales beautifully
* creates coherent long outputs
* forces the model to learn world knowledge
* supports reasoning-like behaviors
* allows instruction tuning and RLHF
* enables agents, copilots, and conversational systems

NSP cannot produce any of these emergent behaviors.

---

# **8. One-paragraph summary**

BERT's next sentence prediction is a simple binary classification task meant to teach whether one sentence logically follows another, while GPT's next-token prediction is a generative modeling task in which the model learns to predict the next piece of text in a sequence. NSP teaches *coherence recognition*, but NTP teaches the entire *structure of language*, enabling generation, reasoning, and emergent intelligence. That's why GPT-style models have become the backbone of modern AI.
