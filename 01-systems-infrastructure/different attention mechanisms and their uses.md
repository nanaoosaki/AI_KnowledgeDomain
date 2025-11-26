*[← Back to Systems & Infrastructure](README.md)*

---

# **1. Why different attention mechanisms exist**

Standard self-attention is powerful but expensive:

**Cost = O(n²)**
(n = sequence length)

For long documents, code, transcripts, or multi-modal inputs, that cost becomes impossible to scale.
So researchers developed different attention patterns to solve different pain points:

* reduce computational cost
* expand context window
* bias attention toward important tokens
* improve efficiency on long text
* encode order and structure better

Each mechanism reflects a *design choice* to solve a specific limitation.

---

# **2. Core Attention Mechanisms (with models)**

## **A. Full Self-Attention (vanilla Transformer)**

**Models:**

* Original Transformer (Vaswani, 2017)
* BERT
* RoBERTa
* GPT-1/2/3
* Most encoder-decoder models

**What it does:**
Every token attends to *all* other tokens.

**Why:**
Maximal flexibility and expressiveness.

**Downside:**
O(n²) cost → limited to short sequences (512–2048 tokens historically).

---

## **B. Causal Attention (autoregressive / GPT-style)**

**Models:**

* GPT series
* LLaMA / Mistral / Qwen
* Claude
* Gemini / GPT-4o
* Almost all modern LLMs

**What it does:**
Each token only attends to previous tokens (left-to-right).

**Why:**
Enables next-token prediction for generation.

**Downside:**
Still O(n²); long sequences remain expensive.

---

## **C. Sparse Attention**

Tokens attend only to a structured subset of positions.

### **Models:**

* **Longformer** – sliding window + global tokens
* **BigBird** – random + local + global
* **Reformer** – locality-sensitive hashing
* **Sparse Transformer** (OpenAI)

### **Why:**

Cuts cost from O(n²) to **O(n)** or **O(n log n)**.

### **Where it used:**

* long documents
* transcripts
* scientific papers
* legal text

Sparse attention was the first wave of “long-context” innovation.

---

## **D. Local Attention (fixed window)**

A token attends only to its neighbors.

### **Models:**

* Longformer (local component)
* Transformer-XL (segment recurrence + local attention)
* GPT-J / GPT-NeoX (early long-context)
* ConvFormer-style hybrids

### **Why:**

Local structure captures most dependencies in long documents, reducing memory use.

**Downside:**
Loses global understanding unless combined with special tokens.

---

## **E. Global Attention (special tokens)**

Some tokens get full attention (like CLS in BERT), others only local.

### **Models:**

* Longformer
* BigBird
* LED (Longformer Encoder-Decoder)

**Why:**
Allows important tokens to aggregate global info and keep long-range reasoning.

---

## **F. Memory-Augmented Attention**

Adds memory slots or recurrence.

### **Models:**

* Transformer-XL
* Compressive Transformer
* RMT (Recurrent Memory Transformer)
* Retro (DeepMind retrieval transformer)

**Why:**
Extend context *beyond* window limits through learned memory.

---

## **G. Linear / Kernelized Attention**

Approximates softmax attention to reduce cost to **O(n)**.

### **Models:**

* Performers
* LinearTransformer
* Synthesizer
* LambdaNetworks
* Hyena (convolution-inspired)

**Why:**
Massive speedups; theoretical scalability.

**Downside:**
Sometimes loses accuracy compared to softmax.

---

## **H. Attention with External Retrieval (RAG-style)**

Not really a new attention type — but a new **architecture wrapper**.

### **Models:**

* RETRO (DeepMind)
* RAG (Facebook)
* GPT-4’s “Search and Index” features
* Gemini 1.5’s retrieval integration

**Why:**
Effectively infinite context by pulling relevant chunks from a database.

---

## **I. Multi-Query Attention (MQA)**

Each attention head shares keys and values (faster KV-cache).

### **Models:**

* PaLM
* GPT-3.5/4
* Mistral
* Llama-3
* Qwen-2

**Why:**
Huge inference speed gain, especially for long outputs.

---

## **J. Grouped-Query Attention (GQA)**

Middle ground between multi-head and multi-query.

### **Models:**

* GPT-4
* LLaMA-2/3
* Mistral
* Many 2024–2025 models

**Why:**
Better quality than MQA, still fast.

---

## **K. FlashAttention (Algorithmic optimization)**

Not a new pattern — a new *implementation*.

### **Models:**

* Almost all modern models use FlashAttention 2 or 3
* GPT-4o, Claude 3, Gemini 2
* Open-source long-context variants

**Why:**
Reduces memory usage and speeds up true softmax attention.

---

## **L. Mixture-of-Depth / MoE Attention Routing**

Routing attention or FFN layers through expert networks.

### **Models:**

* Mixtral (8x7B)
* DeepSeek V2/MoE models
* Google Switch-Transformer

**Why:**
Scales model capacity without scaling compute proportionally.

---

# **3. A clean summary table**

| Attention Type                    | Models                | Why It Exists              | Cost                        |
| --------------------------------- | --------------------- | -------------------------- | --------------------------- |
| **Full Self-Attention**           | BERT, GPT-2           | Maximum flexibility        | O(n²)                       |
| **Causal Attention**              | GPT family            | Autoregressive generation  | O(n²)                       |
| **Sparse Attention**              | Longformer, BigBird   | Long documents             | O(n)                        |
| **Local Attention**               | Transformer-XL        | Efficient long context     | O(n)                        |
| **Global Attention**              | Longformer            | Key tokens aggregate info  | Mixed                       |
| **Memory-Based**                  | Transformer-XL, RETRO | Beyond context window      | Variable                    |
| **Linear Attention**              | Performers            | Fast approximate attention | O(n)                        |
| **MQA/GQA**                       | GPT-4, Llama-3        | Faster inference           | O(n²) but smaller constants |
| **FlashAttention**                | Modern LLMs           | Efficient implementation   | O(n²) but memory-efficient  |
| **Retrieval-Augmented Attention** | RAG, RETRO            | Scalable external memory   | External lookup             |

---

# **4. Why the field evolved this way**

In one sentence:

**Attention mechanisms evolved to solve scaling problems — compute, memory, context length, and reasoning complexity.**

Full attention is extremely expressive but too expensive.
Long-sequence tasks require approximations.
Inference-time efficiency requires smarter KV-caching.
Massive-scale training pushes toward MQA/GQA and FlashAttention.

Every variant is a tradeoff between:

* quality
* speed
* memory
* context length

No single mechanism is universally “best.”

---

# **5. Short, polished explanation for your site**

Transformers began with full self-attention, where every token attends to every other token, but this becomes too expensive for long documents. To address this, researchers created new variants such as causal attention for autoregressive models, sparse and local attention for long-context efficiency, global attention for document-level reasoning, linear attention for scalability, and memory-based attention for beyond-window context. Modern models combine these techniques — often with multi-query or grouped-query attention and FlashAttention — to balance speed, accuracy, and context length. Each attention type exists to solve a specific bottleneck in scaling or reasoning.
