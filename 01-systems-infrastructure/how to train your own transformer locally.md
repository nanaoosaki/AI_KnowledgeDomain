---
layout: default
title: ✅ What we recommended you do
parent: Systems & Infrastructure
---

*[← Back to Systems & Infrastructure](README.md)*

---

## ✅ What we recommended you do

1. Identify your GPU architecture: you have a NVIDIA GeForce RTX 5060 Ti, which uses the Blackwell micro-architecture (compute capability `sm_120`).
2. Understand the compatibility issue: the version of PyTorch you initially installed supported CUDA architectures up to around `sm_90`, but **not** `sm_120`. This mismatch caused the “no kernel image available for execution on the device” error. ([PyTorch Forums][1])
3. Uninstall the incompatible PyTorch version and install (or plan to install) a build that supports CUDA 12.8+ (or the corresponding binary) **and** includes kernel support for `sm_120` (Blackwell).
4. Verify after installation by running code like:

   ```python
   import torch
   print(torch.__version__)
   print(torch.cuda.get_arch_list())
   ```

   to ensure `sm_120` appears.
5. Once that’s confirmed, run your Transformers pipeline with `device=0` (or appropriate GPU) and everything should work with GPU acceleration instead of falling back to CPU.

---

## 🔍 Why it worked (the underlying mechanics)

* The GPU you have has a newer architecture (`sm_120`) which requires specific compiled kernels in the deep‐learning backend (PyTorch) to run GPU code.
* When you first installed a “cu126” build (CUDA 12.6) of PyTorch, although CUDA runtime and driver were present, the build did *not* include those compiled kernels for `sm_120`. Hence the backend recognized your GPU but could not execute any GPU kernels.
* By moving to a build that supports “CUDA 12.8+” and/or explicitly includes Blackwell kernel support, you aligned **three layers**:

  * **Hardware** (your RTX 5060 Ti, `sm_120`)
  * **CUDA runtime / driver** (you had CUDA 12.9, driver 576.88)
  * **Deep-learning framework build** (PyTorch binary compiled for newer architecture)
* When these layers align, the deep‐learning framework detects the GPU and can dispatch kernels to it, enabling actual GPU execution instead of fallback or error.

---

## 🧠 Key takeaway

Matching the right **framework build** (PyTorch + correct CUDA version + architecture support) is just as important as having a capable GPU. Having a "new GPU" alone isn't enough—if the deep-learning binary doesn't know how to talk to that architecture (in this case `sm_120`), GPU acceleration won't run.
