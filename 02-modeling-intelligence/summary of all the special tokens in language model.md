---
layout: default
title: 🌟 1. What these tokens are called
parent: Modeling & Intelligence
---

*[← Back to Modeling & Intelligence](README.md)*

---

# 🌟 **1. What these tokens are called**

They are called **special tokens**.

Special tokens tell the model about structure rather than meaning.

Examples include:

* **Mask token**: `<mask>` or `[MASK]`
* **Start-of-sequence**: `<s>` or `[CLS]` or `<BOS>`
* **End-of-sequence**: `</s>` or `[SEP]` or `<EOS>`
* **Padding token**: `<pad>` or `[PAD]`
* **Unknown token**: `<unk>` or `[UNK]`

Every model family decides its own conventions.

---

# 🌟 **2. Why different models use different styles**

## **BERT-based models (BERT, DistilBERT, etc.)**

Use **square brackets**, uppercase:

* `[CLS]`
* `[SEP]`
* `[MASK]`
* `[PAD]`
* `[UNK]`

This matches how the original BERT paper defined them.

---

## **RoBERTa-based models (RoBERTa, DistilRoBERTa)**

Use **angle brackets**, lowercase:

* `<s>`
* `</s>`
* `<mask>`
* `<pad>`
* `<unk>`

This is inherited from the **SentencePiece** tokenizer and Facebook’s RoBERTa conventions.

Your model is **DistilRoBERTa**, so:

* Correct mask token is **`<mask>`**
* NOT `[MASK]`

That’s why your pipeline rejected your input.

---

## **GPT-style models**

Use a totally different scheme:

* No explicit mask token (because GPT is autoregressive).
* Usually no `[CLS]` or `[SEP]`.
* Sometimes `<|endoftext|>` or `<|bos|>`.

---

# 🌟 **3. Should you use uppercase or lowercase?**

Always use the one defined by the tokenizer:

```python
print(tokenizer.mask_token)
print(tokenizer.eos_token)
print(tokenizer.bos_token)
print(tokenizer.cls_token)
print(tokenizer.sep_token)
```

Whatever prints out is what you should use.

For DistilRoBERTa, you’ll typically see:

* `mask_token = '<mask>'`
* `cls_token = '<s>'` (yes, `<s>` serves as CLS)
* `sep_token = '</s>'`
* `eos_token = '</s>'`  (same as SEP)
* `bos_token = '<s>'`

---

# 🌟 **4. Why the format matters**

Because the tokenizer splits text based on its learned vocabulary.

* If your model expects `<mask>` but you insert `[MASK]`,
  it won’t recognize the token → error.

* If your model expects `[CLS]` but you insert `<s>`,
  the meaning is lost → weird results.

---

# 🌟 **5. What to call these tokens in general?**

You can call them:

* **special tokens**
* **meta tokens**
* **control tokens**
* **structural tokens**

But “special tokens” is the standard term.

---

# 🌟 **6. Quick Summary Table**

| Model Family                | Mask Token          | Start Token     | End Token  | Format                     |
| --------------------------- | ------------------- | --------------- | ---------- | -------------------------- |
| **BERT**                    | `[MASK]`            | `[CLS]`         | `[SEP]`    | square brackets, uppercase |
| **RoBERTa / DistilRoBERTa** | `<mask>`            | `<s>`           | `</s>`     | angle brackets, lowercase  |
| **GPT-2/3**                 | *none*              | `<bos>`         | `<endoftext>` | custom control tokens   |
| **T5**                      | `<extra_id_0>` etc. | `<pad>`         | `</s>`     | angle brackets             |
