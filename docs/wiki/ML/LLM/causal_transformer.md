---
layout: page
title: Causal Transformer
author: Yifei Zhu
comments: true
tags:
  - AI
  - Transformer
  - ML
  - LLM
---
A **Causal Transformer** is a variant of the Transformer architecture designed for **autoregressive (sequential)** tasks, where each token can only attend to **past and current** positions, not to **future** ones. This restriction is enforced by a **causal attention mask**, which blocks attention to later tokens.

### Key Features

- **Unidirectional attention:** Each position ( i ) attends only to tokens ( \leq i ).
    
- **Autoregressive generation:** Ideal for tasks like text generation and next-token prediction.
    
- **Parallel training, sequential inference:** Training can be parallelized, but generation proceeds token by token.
    

### Difference from Standard (Bidirectional) Transformers

Ordinary Transformers, such as those used in BERT, employ **bidirectional attention**, allowing each token to attend to all others in the sequence. This enables richer contextual understanding but prevents autoregressive generation.

|Aspect|**Causal Transformer (e.g., GPT)**|**Bidirectional Transformer (e.g., BERT)**|
|:--|:--|:--|
|**Attention Direction**|Unidirectional (causal mask)|Bidirectional|
|**Context Access**|Past and current tokens only|All tokens (past + future)|
|**Main Use Case**|Text generation, prediction|Understanding, classification|
|**Training Objective**|Next-token prediction|Masked language modeling|
|**Inference Style**|Sequential (token by token)|Non-sequential (full context)|
