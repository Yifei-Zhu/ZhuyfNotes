---
layout: page
title: Contrastive Learning
author: Yifei Zhu
comments: true
tags:
  - ML
  - LLM
---

# Contrastive Learning

**Contrastive learning** is a self-supervised learning approach that trains models to distinguish between similar (positive) and dissimilar (negative) data samples. Instead of relying on explicit labels, it learns by comparing pairs of inputs and encouraging the model to bring representations of similar samples closer together while pushing apart those of different samples.

### Core Idea

The central idea is to **learn a representation space** where semantic similarity is reflected by proximity. Typically, a _contrastive loss function_ (such as InfoNCE or NT-Xent) is used to measure how well the model separates positive pairs from negatives.

> "Learn by comparison: similar samples should have similar representations, while dissimilar samples should have distinct representations."

### Typical Workflow

1. **Sample Preparation**: Take input data and create multiple views through data augmentation
2. **Positive Pairs**: Different augmented views of the same sample
3. **Negative Pairs**: Views from different samples
4. **Learning Objective**: Maximize similarity for positive pairs, minimize similarity for negative pairs

### Applications

Contrastive learning has been successfully applied in:

- **Computer vision** (e.g., SimCLR, MoCo for image representations)
- **Natural language processing** (e.g., SimCSE for sentence embeddings)
- **Molecular and materials modeling**, where it helps learn chemical representations from unlabeled data.