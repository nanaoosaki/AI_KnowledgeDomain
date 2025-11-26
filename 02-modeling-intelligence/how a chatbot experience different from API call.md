---
layout: default
title: 1. Single-turn inference (API call)
parent: Modeling & Intelligence
---

*[← Back to Modeling & Intelligence](README.md)*

---

# **1. Single-turn inference (API call)**

In this mode, the model sees **only one request** and produces **one response**.

> You send text → model responds → done.

The pipeline is:

```
text → tokenization → embeddings → transformer → output tokens → text
```

There is no “memory,” no history, no accumulation of knowledge across calls.
Each request is a brand new universe.

---

# **2. Multi-turn chatbot (ChatGPT-like systems)**

Multi-turn chat adds something extra:

### **There is a “conversation manager” outside the model.**

The LLM itself has no memory between turns.
It cannot recall previous messages unless they’re included in the next input.

So the platform (ChatGPT, Claude, etc.) handles memory with a simple mechanism:

### **Every time you send a message, the system sends your whole conversation history back into the model.**

Literally:

```
User: Hi
Assistant: Hello!
User: What did I ask before?
→ The system sends:

[
  {role: system, content: "..."},
  {role: user, content: "Hi"},
  {role: assistant, content: "Hello!"},
  {role: user, content: "What did I ask before?"}
]

→ All concatenated and fed to the model as the next prompt.
```

The model “remembers” only because **the system repeats the past messages to it**.

This is the key insight:

> **Chatbots don’t have memory. They have context. And the context is rebuilt every turn.**

---

# **3. Multi-turn = single-turn repeated with more text**

When you chat with ChatGPT, each turn is still a **single inference pass**.

The only difference is:
Instead of sending one user message, the system appends:

* system prompt
* conversation history
* your latest message

The model sees the *entire sequence* and then generates one answer.

Technically:

```
First message: context = [system + user]
Second message: context = [system + user + assistant + user]
Third message: context = [system + user + assistant + user + assistant + user]
...
```

It keeps growing until it hits the **context window limit** (8k, 32k, 128k, etc.).

---

# **4. So what happens when the conversation gets long?**

Two things:

### A. The oldest messages get **dropped or summarized**

Platforms do one of:

* drop oldest turns
* summarize previous turns with an LLM
* compress representation using smaller models
* store memory outside the model and re-inject relevant pieces

### B. Attention cost increases

The model must attend to a longer token sequence:

* 1k tokens → easy
* 40k tokens → huge memory + compute
* 200k tokens → specialized inference optimizations

This is why ultra-long-context models (GPT-4o, Claude 3.5, Gemini 2.0) are so impactful.

---

# **5. Difference between “stateless” and “stateful” API usage**

Typical API usage is **stateless**:

You explicitly include history yourself:

```json
{
  "messages": [
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello!"},
    {"role": "user", "content": "What did I ask before?"}
  ]
}
```

But some platforms let you:

### **Option A: Use a session token**

which lets the server store the history for you
(but still, the model cannot recall; the server re-feeds it).

### **Option B: Provide your own memory module**

RAG, vector memory, summarization, pointer networks, etc.

Even then: the LLM never keeps memory; you do.

---

# **6. Why multi-turn chat feels different from single-turn inference**

Because multi-turn:

* carries **implicit goals**
* accumulates **conversational norms**
* builds **local context**
* enables **coreference resolution** (“he”, “it”, “that thing earlier”)
* allows **user preference encoding**
* supports **task decomposition**

These are not new abilities.
The model is just reacting to a **longer prompt**, over and over.

This is why prompting improves as you go:
each turn enriches the prompt.

---

# **7. Summary in a single flowing paragraph**

When you use ChatGPT in chat mode, the system takes your conversation history, tokenizes it, embeds it, and feeds it as one long prompt into the model at every turn. The LLM does not remember previous turns — it simply reprocesses the whole conversation each time, using attention across the sequence to produce the next token. Multi-turn chat is essentially repeated single-turn inference with accumulating context, until the context window fills and the system starts summarizing or truncating. That's why chat feels interactive and continuous even though the LLM itself is stateless.
