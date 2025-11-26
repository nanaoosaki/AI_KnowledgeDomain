---
layout: default
title: **1. Hugging Face is *not* scikit-learn**
parent: Systems & Infrastructure
---

*[← Back to Systems & Infrastructure](README.md)*

---

# **1. Hugging Face is *not* scikit-learn**

Scikit-learn is a **full ML toolkit** containing algorithms (SVMs, logistic regression, trees, clustering, etc.) plus utilities.

Hugging Face is different:

* It doesn’t implement Transformers “from scratch.”
* It doesn’t own the deep learning algorithms.
* It is mainly:

  * a high-level **model interface**
  * a huge **model hub**
  * helper utilities for loading/training
  * tokenizers
  * datasets

The *actual* Transformer computation still depends on either **PyTorch**, **TensorFlow**, or **JAX**.

So HF = “wrapper + ecosystem,” not the underlying engine.

---

# **2. Other major libraries/frameworks for training Transformers**

Here are the major alternatives — many used professionally at very large scale.

---

## **A. Native Deep Learning Frameworks**

These are the “true engines” that implement attention, gradients, tensors, etc.

### **1. PyTorch**

*Most widely used for Transformer research + training.*
Many labs (Meta, OpenAI, Mistral, Stability) rely heavily on it.

Pros: great flexibility, ecosystem, community
Cons: more boilerplate than HF if writing Transformer code manually

### **2. TensorFlow / Keras**

Still used at scale inside Google.

Pros: built-in distributed training tools
Cons: waning popularity outside Google, less ergonomic than PyTorch

### **3. JAX**

Used by Google (e.g., T5, PaLM) and DeepMind.

Pros:

* super fast XLA compilation
* ideal for mega-scale training
* pure functional style

Cons:

* not beginner-friendly
* smaller community
* requires TPU/Cloud setup for best performance

**If you wanted to build a transformer “from the ground up”, you’d probably use PyTorch, JAX, or TensorFlow — not Hugging Face.**

---

## **B. Training/Finetuning Toolkits (beyond HF)**

These sit *above* PyTorch/JAX, offering distributed training, optimization, and efficiency.

### **1. DeepSpeed (Microsoft)**

Used for training very large models (like BLOOM, GPT-NeoX).

* 3D parallelism
* ZeRO optimization
* memory sharding

Great for massive-scale training.

---

### **2. Megatron-LM (NVIDIA)**

Industrial-grade library for GPT-like model training.

* tensor parallelism
* pipeline parallelism
* large-scale pretraining infrastructure
* heavily optimized for NVIDIA GPUs

Used for Megatron-Turing NLG, MosaicML models.

---

### **3. Fairseq (Meta)**

Facebook’s research codebase where many original Transformer ideas developed.

Models that used Fairseq:

* BART
* RoBERTa
* wav2vec
* various translation models

---

### **4. OpenNMT**

Open-source neural machine translation toolkit.

* Python & C++ versions
* used by academic NLP groups
* supports Transformer training

---

### **5. Trax (Google)**

Used historically for early transformer experiments.

Not as popular today.

---

### **6. AllenNLP**

Academic research toolkit.

Good for NLP pipelines, experiments, structured prediction.

---

### **7. MosaicML Composer**

Training efficiency toolkit.

Provides:

* speed-ups
* optimized training loops
* LLM training recipes

Powerful for organizations building large models from scratch.

---

# **3. Inference-Specific Libraries (not training)**

These are specialized for **running** transformers, not training them.

### **1. vLLM**

State-of-the-art for fast LLM serving.

* Paged Attention
* very high throughput
* used in many production stacks

### **2. TensorRT-LLM (NVIDIA)**

Highly optimized for NVIDIA GPU inference.

### **3. GGML / llama.cpp**

Fast CPU inference for quantized LLMs.

---

# **4. Specialized High-Level Libraries (beyond HF Transformers)**

### **1. Haystack**

NLP pipelines, RAG, document QA.

### **2. spaCy (with transformer pipeline)**

NLP tasks using transformer encoders under the hood.

---

# **5. Where Hugging Face fits into this landscape**

### **Hugging Face provides:**

* easy loading of 100k+ pretrained models
* high-level training abstractions (`Trainer`)
* tokenizers
* datasets
* pipelines (quick inference)

### **But it depends on:**

* PyTorch
* TensorFlow
* JAX

for the **actual math**.

### **An analogy:**

* **PyTorch/TensorFlow/JAX** = the engine
* **Transformers library (HF)** = the dashboard
* **Model Hub** = the garage with pre-built cars
* **DeepSpeed/Megatron** = turbochargers and factory equipment for building huge engines

---

# **6. So is Hugging Face like scikit-learn?**

**Not really.**
Scikit-learn *implements* algorithms.
Hugging Face *wraps* algorithms implemented in PyTorch/JAX/TF.

HF is a:

✔ model loader
✔ API layer
✔ tokenizer framework
✔ training helper
✔ huge model ecosystem

…but not a standalone training framework.

In modern ML architecture terms, it is a **convenience layer**, not the kernel.

---

# **7. One-paragraph summary for your site**

Other than Hugging Face's Transformers library, you can train transformer models using deep learning frameworks like PyTorch, TensorFlow, and JAX as the core engines, along with large-scale toolkits such as DeepSpeed, Megatron-LM, Fairseq, and MosaicML Composer for distributed training and efficiency. Hugging Face is not equivalent to scikit-learn; instead of being a place where all algorithms live, it is a high-level interface, model hub, and tooling ecosystem built on top of real deep learning frameworks that do the actual mathematical computation.
