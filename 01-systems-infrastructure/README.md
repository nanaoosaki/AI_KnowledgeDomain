---
layout: default
title: Systems & Infrastructure
nav_order: 3
permalink: /systems
---

# Systems & Infrastructure
{: .no_toc }

*The Engineering Spine*
{: .fs-6 .fw-300 }

> How modern AI systems are built, deployed, and scaled—from data pipelines to production inference

## Domain Overview

The gap between "model works in notebook" and "system serves millions of users" is where most AI projects fail. This domain covers the engineering foundations for building production AI systems.

## Core Capabilities

- **Data Engineering**: Pipelines, versioning, quality, lineage
- **ML Operations**: Training workflows, experiment tracking, model versioning
- **Deployment**: Serving strategies, containerization, orchestration
- **Inference Optimization**: Latency, throughput, cost trade-offs
- **Monitoring & Observability**: Performance tracking, drift detection, debugging
- **Infrastructure**: Cloud platforms, distributed computing, resource management
- **Storage Systems**: Vector databases, feature stores, model registries

## Knowledge Map

### Foundational Concepts
*Core understanding required for all AI systems work*

- [ ] ML Pipeline Architecture
- [ ] Model Versioning & Experiment Tracking
- [ ] Containerization & Orchestration Basics
- [ ] Cloud Compute Economics
- [ ] Data Versioning & Lineage
 
### Intermediate Topics
*Applied techniques for production systems*

- [ ] Inference Serving Patterns
- [ ] Vector Database Selection & Optimization
- [ ] Model Monitoring & Drift Detection
- [ ] A/B Testing Infrastructure
- [ ] Feature Engineering at Scale
- [ ] Cost Optimization Strategies

### Advanced Topics
*Specialized expertise for complex systems*

- [ ] Distributed Training Architectures
- [ ] Real-time Inference Optimization
- [ ] Multi-Model Serving & Routing
- [ ] Custom ML Hardware (GPUs, TPUs, inference accelerators)
- [ ] Edge Deployment Strategies
- [ ] Auto-scaling & Resource Allocation

## Learning Path

**If you're starting out** → Begin with core concepts, set up a simple MLOps pipeline

**If you're building production systems** → Focus on monitoring and cost optimization

**If you're scaling to millions** → Dive into performance and reliability topics

## Key Resources

### Papers
- [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) - Sculley et al., 2015
- [Machine Learning: The High-Interest Credit Card of Technical Debt](https://research.google/pubs/pub43146/) - Google Research

### Tools & Frameworks
- **Orchestration**: Airflow, Prefect, Dagster, Metaflow
- **Experiment Tracking**: Weights & Biases, MLflow, Neptune
- **Serving**: Ray Serve, BentoML, TorchServe, TensorFlow Serving
- **Vector DBs**: Pinecone, Weaviate, Milvus, Qdrant, Chroma
- **Platforms**: AWS SageMaker, GCP Vertex AI, Azure ML, Databricks

### Engineering Blogs
- [Netflix Tech Blog](https://netflixtechblog.com/) - ML infrastructure at scale
- [Uber Engineering](https://eng.uber.com/) - Michelangelo platform
- [Airbnb Engineering](https://medium.com/airbnb-engineering) - ML platform evolution

## Current State (October 2025)

**Major trends**:
- Shift from model-centric to data-centric infrastructure
- Vector databases becoming standard infrastructure layer
- LLM inference optimization (quantization, speculative decoding)
- Rise of multi-modal serving requirements
- Cost optimization increasingly critical as models scale

**Fast-changing**: Specific tools, cloud pricing, inference optimizations  
**Slow-changing**: Pipeline design patterns, monitoring principles, cost modeling approaches

---

## Knowledge Articles

### Core Topics

- [1. Why different attention mechanisms exist](different%20attention%20mechanisms%20and%20their%20uses.md)
- [Evole From Applied Ml Scientist To Applied Dl And Ai Scientist](evole%20from%20applied%20ML%20scientist%20to%20applied%20DL%20and%20AI%20scientist.md)
- [**1. Hugging Face is *not* scikit-learn**](how%20to%20go%20from%20scikit%20learn%20to%20transformers.md)
- [✅ What we recommended you do](how%20to%20train%20your%20own%20transformer%20locally.md)
- [A More Expressive Foundation for Your AI Knowledge Domain](how%20tranformers%20and%20LLMs%20run-%20the%20layer%20and%20who%20provides%20them.md)
- [🌱 1. At the programming-language level](imperative%20vs%20declarative)
- [1. BERT: Architecturally limited for the modern era](why%20T5%20and%20BART%20are%20less%20known.md)

---

*Explore specific topics using the Knowledge Articles section above*

