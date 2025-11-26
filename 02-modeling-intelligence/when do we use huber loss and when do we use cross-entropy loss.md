---
layout: default
title: 1. Start with the nature of the target (CSAT)
parent: Modeling & Intelligence
---

*[← Back to Modeling & Intelligence](README.md)*

---

# **1. Start with the nature of the target (CSAT)**

CSAT can be treated in two ways:

### **A. As a numeric score**

1 → 5, or 1.0 → 5.0
Then your model is doing **regression**.

### **B. As discrete classes**

1 star, 2 stars, 3 stars, etc.
Then your model is doing **classification**.

Your loss function must match the “shape” of the problem.

This is the source of 90% of confusion.

---

# **2. Cross-entropy loss (CE)**

**Use CE when CSAT is treated as classification.**

If you say “I want the model to output 1/2/3/4/5 as categories with probabilities,”
then CE is the natural choice.

### Why CE?

* It teaches the model to produce a probability distribution over classes.
* It penalizes incorrect predictions *by probability mass*, not by numeric distance.
* Predicting “3” when ground truth is “4” is considered **fully wrong**, same as predicting “1.”

### CE strengths

* Great when categories are discrete and unordered.
* Works extremely well with softmax heads.
* Stable training.

### CE weaknesses for CSAT

* It **ignores ordinal structure** — 5 is closer to 4 than to 1, but the loss treats them the same.
* Misclassifying by 1 point vs 4 points yields identical loss.
* It may lead to overfitting on mode (e.g., predicting 4 all the time).

In customer satisfaction tasks that have natural ordering, CE sometimes wastes information.

---

# **3. Huber loss (smooth L1)**

**Use Huber if you treat CSAT as a numerical regression.**

Huber loss blends:

* L2 loss for small errors (smooth)
* L1 loss for large errors (robust to outliers)

### Why Huber?

CSAT tends to be noisy and subjective.
Huber:

* reduces the effect of occasional extreme labels
* stabilizes gradient updates
* behaves nicely if your predictions fall within a reasonable band
* respects *distance* (predicting 4 when true is 5 is not as bad as predicting 1)

### Huber strengths

* Perfect for ordinal numeric outcomes.
* Smooth gradient near correct regions.
* Resilient to mislabeled or noisy data.
* Encourages predictions that match true magnitude.

### Huber weaknesses

* Doesn’t give probability distributions.
* Harder to use for ranking or multi-class reporting workflows.
* You need to decide on the δ parameter (threshold between L1 and L2 regions).

---

# **4. What changes when these losses sit on RoBERTa/Longformer?**

You’re not modifying the backbone — you’re modifying the **head** and how it learns.

### With cross-entropy:

* Add a softmax classification head
* Model learns discrete categories
* Outputs: `[p1, p2, p3, p4, p5]` probabilities
* Loss encourages *correct class selection*, not closeness

### With Huber:

* Add a regression head (usually a single linear neuron)
* Model outputs a single real value
* Loss encourages *numerical accuracy* and distance minimization
* Predictions can be fractional: 4.18, 3.92, etc.

In practice:

* CE → predictions look like “class 4”
* Huber → predictions look like “4.21”

For business use (especially trending analysis), **Huber often produces more stable insights** because fractional CSAT preserves variance.

---

# **5. Which one is better for CSAT modeling?**

Here’s the deeper truth:
Most CSAT tasks contain **ordinal + continuous** characteristics.
Users’ ratings are subjective but numerically meaningful.

### So:

*If you care about precision, nuance, and trends → **Huber**.*
*If you care about classification accuracy or thresholds → **Cross-entropy**.*

### More nuanced perspective

**Cross-entropy is a categorical worldview:**
CSAT 4 is fundamentally different from CSAT 3.

**Huber is a continuous worldview:**
CSAT 4 is just one more than CSAT 3, and the model should reflect that.

For your CSAT prediction task — especially if you’re building something like PORS or resolution scoring — **Huber is typically closer to the true nature of satisfaction** because satisfaction is not categorical noise; it moves smoothly.

---

# **6. The one-paragraph distillation**

Cross-entropy thinks of CSAT as a bucket you fall into — either correct or incorrect — and completely ignores how far off you were.
Huber thinks of CSAT as a number on a continuum — and penalizes you more the farther you are from the correct value, while still resisting outliers.
So choosing between them is choosing between a discrete vs. continuous worldview for how humans express satisfaction.
