---
layout: default
title: 🌱 First: What actually changes between tasks?
parent: Modeling & Intelligence
---

*[← Back to Modeling & Intelligence](README.md)*

---

# 🌱 First: What actually changes between tasks?

Inside a transformer, **almost nothing changes in the main body**:

* Embeddings stay the same
* Attention layers stay the same
* Hidden states behave the same

**The only part that changes is the model head** — the final layer that turns hidden states into predictions.

Everything else (embeddings → layers → hidden states) is shared.

Think of the transformer as “understanding text,” and the head as “deciding how to use that understanding.”

---

# 🎯 Two scenarios: Classification vs Regression

## **1. Classification (e.g., sentiment: positive/negative)**

Labels: categories
Head type: **Classification head**
Loss function: **Cross-entropy**

### How layers are used:

1. **Transformer layers** process the sentence and produce hidden states.
2. **[CLS] hidden state** (or pooled output) represents the whole sentence.
3. The **classification head** maps this vector → logits for each class.

Example:

Hidden state (768 dimensions) → linear layer → [logit_pos, logit_neg]

Then softmax converts logits into probabilities.

### Why this matters:

The model is learning to **separate categories**.
Your labels are discrete *classes*, not numeric magnitudes.

---

## **2. Regression (e.g., CSAT score 1–5)**

Labels: numeric values
Head type: **Regression head**
Loss function: **MSE (mean squared error)** or **MAE**

### How layers are used:

1. Transformer produces a hidden state vector (same as classification).
2. Regression head maps the 768-dim vector → **one number**.

Example:

Hidden state → linear layer → predicted score (float, e.g., 3.8)

### Why this matters:

The output is treated as a continuous variable, even if your labels are 1, 2, 3, 4, 5.

You’re teaching the model:
**“Higher numbers mean stronger/more positive sentiment.”**

This preserves *ordinal meaning* that classification would destroy.

---

# 🧩 Where does CSAT 1–5 fit?

Your CSAT values are **discrete**, but they represent **ordered magnitude**.
That makes them **ordinal regression**.

Two approaches are valid:

---

## **Option A — Treat CSAT as Regression (recommended)**

The model predicts a **continuous number**, then you round to 1–5.

This works well because:

* 5 should be “more positive” than 4
* 3 should be more neutral than 1 or 5
* The model can learn distance between labels

**Why?**
Regression preserves the **ordinal relationship** between values.

The head:

```
hidden_state → linear → float (e.g., 3.74)
```

Loss function: MSE.

---

## **Option B — Treat CSAT as 5-Class Classification**

The model predicts **one of 5 categories**.

This can work but has drawbacks:

* Model cannot understand that 5 is “close” to 4 — they become unrelated classes
* “Mistaking 5 for 4” is penalized as heavily as “mistaking 5 for 1”

**When to use:**
Only if your CSAT labels behave more like *categories* than a smooth scale.

---

# 🧠 Putting it together — how each layer plays its role in both tasks

Below is a concise comparison of how the same internal layers behave:

| Stage                   | What happens (same in both tasks)         | How it differs for classification vs regression |
| ----------------------- | ----------------------------------------- | ----------------------------------------------- |
| **Embeddings**          | Convert tokens → vectors                  | identical                                       |
| **Transformer layers**  | Capture context, semantics, relationships | identical                                       |
| **Hidden states**       | Internal representation of meaning        | identical                                       |
| **Head**                | Converts hidden state → output            | 👇 different                                    |
| **Classification head** | Hidden state → logits → softmax           | multi-class categories                          |
| **Regression head**     | Hidden state → float                      | continuous output                               |
| **Loss function**       | drives learning                           | CE for classification; MSE for regression       |

The *head* and *loss* are the only differences.

---

# 🌟 Summary in one sentence

**A transformer always produces hidden states; the model head decides whether those states map to categories (classification) or to a number (regression), and your loss function enforces the right behavior.**
