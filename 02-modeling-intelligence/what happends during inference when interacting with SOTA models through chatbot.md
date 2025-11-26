---
layout: default
title: 1. Why tokenization matters
parent: Modeling & Intelligence
---

*[← Back to Modeling & Intelligence](README.md)*

---

# **1. Why tokenization matters**

Before we list methods, it helps to feel the underlying problem:

*Computers operate on bytes.
Language operates on words, morphemes, or characters.
Tokenization is the bridge.*

A tokenizer defines the “alphabet” the model uses to think.
A bad tokenizer → longer sequences, higher cost, fractured words, messy learning.
A good tokenizer → compact representation, stable patterns, smooth learning.

---

# **2. The major tokenization methods (modern era)**

## **A. WordPiece (BERT family)**

**Used by:** BERT, RoBERTa, DistilBERT, ALBERT, DeBERTa

WordPiece builds tokens based on **frequency statistics**:
start with characters → merge common subwords → produce vocabulary.

Pros:

* balances readability and model efficiency
* handles unknown words reasonably well
* stable for multilingual settings

Cons:

* vocabulary fixed at training time
* OOV (out-of-vocabulary) issues still appear, though mitigated
* merges sometimes counterintuitive (“playing” → “play” + “##ing”)
* not byte-level → needs normalization rules

Why models use it:
It was the best available when BERT launched; the ecosystem built around it.

---

## **B. BPE — Byte Pair Encoding (GPT-2, old LLMs)**

**Used by:** GPT-2, GPT-3, early GPT-4 variants, many older models

Core idea: merge the most frequent **character pairs** to create a vocabulary.

Pros:

* simple
* effective for many languages
* compact sequences
* works well with Latin-alphabet languages

Cons:

* struggles with Unicode (Asian languages, emoji)
* requires normalization rules (NFKC, lowercasing, etc.)
* merges can produce very long tokens for rare words

Why used historically:
OpenAI and others wanted a fast, simple method that produced short sequences for English-heavy datasets.

---

## **C. Unigram LM Tokenizer (SentencePiece)**

**Used by:** T5, ALBERT, XLNet, UL2, PaLM, Flan models

Key idea: model keeps a **probabilistic vocabulary** and selects tokens that best “explain” the text.

Pros:

* handles multilingual text gracefully
* no dependency on whitespace (can tokenize raw text)
* flexible and often produces cleaner segmentation
* good for structured prompts (prefix tasks, text-to-text)

Cons:

* slightly slower
* vocabulary training is more complex
* can produce surprising token boundaries

Why used by T5 and many Google models:
Its ability to tokenize **raw text without preprocessing** is a big win.

---

## **D. Byte-level BPE (GPT-4, GPT-4o, Claude, Llama, Mistral, Qwen)**

This is the modern standard.

**Used by:**

* GPT-4 / GPT-4o
* Claude 3
* Llama 2 / 3
* Mistral / Mixtral
* Qwen 1.5 / 2
* DeepSeek family

Core idea: operate **directly on bytes**, not characters.
No Unicode rules, no normalization headaches.
Everything is representable.

Pros:

* perfect coverage of all languages, emoji, code
* robust to typos and weird unicode characters
* simpler pipeline, fewer encoding errors
* excellent for multimodal data
* especially good for code models

Cons:

* token boundaries are less intuitive
* token count may explode for languages like Chinese/Japanese compared to specialized tokenizers
* sometimes breaks semantic units into “uglier” chunks

Why it dominates today:
It removes an entire class of encoding bugs and is incredibly robust across global datasets.

---

## **E. Character-level tokenization (rare today)**

Very few models use this anymore except specialized ones.

Pros:

* complete flexibility
* perfect robustness
* small vocabulary

Cons:

* sequences extremely long → inefficient
* poor semantic modeling unless scaled massively
* impractical for LLMs

Used by:

* some early RNN/CNN models
* experimental or tiny architectures
* certain multimodal models

---

## **F. Word-level tokenization (obsolete)**

Not used anymore — too rigid, too many OOV issues.

---

# **3. Comparison Table**

| Method              | Examples                            | Strengths                       | Weaknesses                                    |
| ------------------- | ----------------------------------- | ------------------------------- | --------------------------------------------- |
| **WordPiece**       | BERT, RoBERTa                       | good subwords, stable           | poor for unicode, fixed vocabulary            |
| **BPE**             | GPT-2, GPT-3                        | simple, efficient               | unicode issues, requires normalization        |
| **Unigram LM**      | T5, ALBERT                          | multilingual, raw text          | slower, probabilistic                         |
| **Byte-level BPE**  | GPT-4, Claude, Llama, Qwen, Mistral | robust, unicode-safe, universal | unintuitive chunks, long token counts for CJK |
| **Character-level** | rare                                | perfect coverage                | very inefficient                              |
| **Word-level**      | obsolete                            | readable                        | crippling OOV issues                          |

---

# **4. What major models use and why**

### **BERT / RoBERTa / DeBERTa / ALBERT**

Use **WordPiece** or variations of it.
Reason: historical lineage + good subword properties.

### **T5 / UL2 / PaLM / Flan models**

Use **SentencePiece Unigram LM**.
Reason: multilingual, clean preprocessing, flexible text-to-text tasks.

### **GPT-4 / GPT-4o / GPT-4 Turbo**

Use **byte-level BPE**.
Reason: robustness across languages + code + mistakes + multimodal noise.

### **Llama 2 / 3**

**Byte-level BPE**.
Reason: open, multilingual, modern standard.

### **Mistral, Mixtral**

**Byte-level BPE**.
Reason: easiest to train at scale, reproducible.

### **Qwen, DeepSeek**

**Byte-level** or **byte-level BPE**.
Reason: unifies Chinese + English + code cleanly without special handling.

---

# **5. Why models transitioned toward byte-level tokenization**

Modern LLMs need to:

* process multiple languages
* handle emoji
* work with raw logs
* understand source code
* parse messy user inputs
* avoid normalization bugs
* be trainable at 100B+ token scales with minimal preprocessing

Byte-level tokenization makes all of this **trivially safe**.

Unicode fragmentation issues simply disappear.
