---
layout: default
title: A simple, durable framework for all search systems
parent: Modeling & Intelligence
---

*[← Back to Modeling & Intelligence](README.md)*

---

# **A simple, durable framework for all search systems**

You can think of *all* search engines as falling into **four major families**, each with clear strengths and weaknesses:

---

## **1) Lexical / Sparse Search**

This includes:

* BM25 (Elastic, Lucene, Pyserini, Vespa)
* TF-IDF
* Keyword matching with analyzers, tokenizers

**How it works:**
Documents → tokens → inverted index → match based on exact words.

### **Understanding Analyzers and Tokenizers**

**The Core Pipeline:**
```
Raw Text → Analyzer → Tokens → Inverted Index
           ↓
        [Tokenizer + Filters]
```

**What is a Tokenizer?**

A tokenizer breaks text into individual tokens (terms). It's the first step in analysis.

**Common Tokenizer Types:**

1. **Standard Tokenizer** (most common)
   - Splits on whitespace and punctuation
   - `"Hello, world!"` → `["Hello", "world"]`
   - Handles Unicode, emails, URLs intelligently

2. **Whitespace Tokenizer**
   - Splits only on whitespace
   - `"Hello, world!"` → `["Hello,", "world!"]`
   - Keeps punctuation attached

3. **N-gram Tokenizer**
   - Creates overlapping character sequences
   - `"search"` with n=3 → `["sea", "ear", "arc", "rch"]`
   - Great for partial matching, typo tolerance

4. **Keyword Tokenizer**
   - Treats entire input as single token
   - `"product-code-123"` → `["product-code-123"]`
   - Used for exact match fields (IDs, codes)

**What is an Analyzer?**

An analyzer is a **pipeline** that combines:
1. **Character filters** (pre-processing)
2. **Tokenizer** (splitting)
3. **Token filters** (post-processing)

**Example Analyzer Pipeline:**

```
Input: "The QUICK brown fox's running!"

↓ Character Filter (HTML strip, mapping)
"The QUICK brown fox's running!"

↓ Tokenizer (Standard)
["The", "QUICK", "brown", "fox's", "running"]

↓ Token Filters
   - Lowercase: ["the", "quick", "brown", "fox's", "running"]
   - Stop words: ["quick", "brown", "fox's", "running"]
   - Stemmer: ["quick", "brown", "fox", "run"]

Final tokens: ["quick", "brown", "fox", "run"]
```

**Common Token Filters:**

- **Lowercase**: `"HELLO"` → `"hello"`
- **Stop words**: Remove `"the", "a", "an", "is"`
- **Stemming**: `"running"` → `"run"`, `"mice"` → `"mouse"`
- **Synonyms**: `"quick"` → `["quick", "fast", "rapid"]`
- **ASCII folding**: `"café"` → `"cafe"`
- **Edge n-gram**: `"search"` → `["s", "se", "sea", "sear", "searc", "search"]`

**Why This Matters for Search:**

**Example 1: Product codes**
```
Analyzer: Keyword (no tokenization)
Input: "SKU-2024-A1"
Token: ["SKU-2024-A1"]
→ Only exact match works
```

**Example 2: Natural language**
```
Analyzer: Standard + lowercase + stemming
Input: "Running shoes for kids"
Tokens: ["run", "shoe", "kid"]
→ Matches "run", "running", "runner", "shoes", "child", "children"
```

**Example 3: Partial matching (autocomplete)**
```
Analyzer: Edge n-gram (min=2, max=10)
Input: "elasticsearch"
Tokens: ["el", "ela", "elas", "elast", "elasti", "elastic", "elastics", "elasticse", "elasticsea", "elasticsear"]
→ Matches any prefix query
```

**Practical Impact:**

| Query | Standard Analyzer | Keyword Analyzer | Edge N-gram |
|-------|------------------|------------------|-------------|
| `"iPhone"` | Matches "iphone", "IPHONE" | Only "iPhone" | Matches "iP", "iPh", "iPhone" |
| `"running shoes"` | `["run", "shoe"]` | `["running shoes"]` | Multiple prefixes |
| `"SKU-123-A"` | `["SKU", "123", "A"]` | `["SKU-123-A"]` | `["S", "SK", "SKU", ...]` |

**When to Use What:**

- **Standard analyzer**: General text search (documents, descriptions)
- **Keyword analyzer**: Exact match fields (IDs, codes, tags)
- **N-gram analyzers**: Autocomplete, typo tolerance
- **Custom analyzer**: Domain-specific (medical terms, code, legal)

**Strengths:**

* Excellent for precision
* Excellent for domain-specific vocabulary (codes, part numbers)
* Supports filters/structured queries well
* Deterministic and easy to control
* Analyzers highly customizable for domain needs

**Weaknesses:**

* Fails when user does not know exact terminology
* No semantic understanding
* Over-stemming can hurt precision
* Synonym expansion increases index size

**Typical use cases:**

* Legal, compliance, finance documents (exact terminology matters)
* Engineering specs, materials codes (product IDs, part numbers)
* Log search, monitoring (structured data, timestamps)
* E-commerce (SKUs, brands with exact names)
* Code search (function names, variable names)

**Tech examples:**
Elastic, OpenSearch, Vespa, Lucene, Whoosh (toy)

---

## **2) Dense Vector / Semantic Search**

This includes:

* SentenceTransformers + FAISS
* Weaviate, Pinecone, Qdrant (vector DBs)
* OpenAI embeddings search
* Vespa hybrid ANN
* Elastic dense_vector kNN

**How it works:**
Documents → embeddings model → vectors → approximate nearest neighbors search.

**Strengths:**

* Handles paraphrases and synonyms
* Works with natural-language questions
* Great for “find something like this” tasks

**Weaknesses:**

* Harder to control (less exact matching)
* Can retrieve on-topic-but-wrong items
* Requires embeddings that fit the domain

**Typical use cases:**

* RAG retrieval
* Support / FAQ semantic matching
* Document similarity, clustering
* Code search (with code embeddings)

**Tech examples:**
FAISS, HNSWLib, Qdrant, Weaviate, Pinecone

---

## **3) Hybrid Search**

This includes:

* Elastic RRF hybrid
* Weaviate’s `hybrid()`
* Qdrant sparse+dense hybrid
* Vespa rank-profiles

**How it works:**
Combine sparse BM25 score + dense vector score.

**Strengths:**

* Best of both worlds
* Very robust across query styles
* Most common modern RAG setups

**Weaknesses:**

* Requires tuning (e.g., alpha weight)
* More computationally expensive

**Typical use cases:**

* Technical manuals where exact terms matter
* Long documents, semi-structured text
* Enterprise search / AI assistants
* Most agentic LLM systems

**Tech examples:**
Elastic, Weaviate, Qdrant, Vespa

---

## **4) Semantic Reasoning / LLM-Augmented Search**

This includes:

* Query rewriting (e.g., “expand this to better keywords”)
* LLM rerankers (Cross-Encoder, ColBERT, OpenAI rerank endpoint)
* Multi-hop LLM reasoning
* Metadata synthesis

**How it works:**
Search → LLM improves → re-ranks → selects → reasons over results.

**Strengths:**

* Best relevance quality
* Best multi-step reasoning
* Handles ambiguous or poorly phrased queries
* Produces explanations, not just matches

**Weaknesses:**

* Slowest
* Requires cost awareness
* Needs guardrails

**Typical use cases:**

* RAG over long documents
* Policy reasoning, compliance assistants
* Customer support chatbots
* Retrieval that needs “understanding,” not just similarity

**Tech examples:**
OpenAI Rerank, Cohere Rerank, ColBERT, ReAct agents, DSPy

---

# **Putting it together visually (conceptually)**

Here’s the simplest mental model:

```
            |  EXACT MATCH  |  SEMANTIC MATCH  |  MULTI-HOP / REASONING  
-----------------------------------------------------------------------
Sparse      |    Strong     |     Weak         |     None
Dense       |    Weak       |     Strong       |     None
Hybrid      |    Strong     |     Strong       |     None
LLM-based   |    Medium     |     Strongest    |     Strongest
```

This is the map you can use in interviews when someone asks:

* "How would you design a search system for X?"
* "When would you choose Elasticsearch vs a vector DB?"
* "Why do hybrid approaches outperform single-mode ones?"
* "How would you build a RAG pipeline for technical documentation?"

And you respond by framing the answer in terms of these four families.

---

# **Mapping search technologies to real applications**

Let’s add a few concrete “bridge” examples so your intuition grows.

### **1) Regulatory / legal text search**

* exact codes matter = sparse
* synonyms & NL queries = dense
* best setup = **hybrid + LLM re-ranker**

### **2) Engineering manuals or construction specifications**

* sparse: matches exact materials
* dense: handles “summarize electrical safety requirements”
* best setup = **hybrid + chunking + reranking**

### **3) Customer support**

* dense works well for FAQs
* LLM reranker boosts quality
* best setup = **dense + rerank**

### **4) Log search / observability**

* sparse dominates
* best setup = **Elastic BM25**

### **5) Image/text multimodal retrieval**

* embeddings dominate
* best setup = **dense** vectors from CLIP or similar models

---

# **Summary**

This framework provides a mental model for all search technologies. Understanding the four families (lexical, dense, hybrid, LLM-augmented) and how analyzers/tokenizers work in lexical search enables you to:

- Design appropriate search architectures for different use cases
- Understand trade-offs between precision and recall
- Choose the right technology stack (Elastic vs. vector DB vs. hybrid)
- Optimize search quality through proper analyzer configuration
