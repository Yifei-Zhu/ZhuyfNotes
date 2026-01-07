---
layout: page
title: Sequence Packing
author: Yifei Zhu
comments: true
tags:
  - AI
  - Transformer
  - ML
  - LLM
---

**Sequence packing** is a technique used in Transformer-based models to **efficiently batch variable-length sequences** without wasting computation on padding tokens.  
Instead of padding each sequence to a fixed maximum length, multiple shorter sequences are **concatenated** into a single continuous sequence (or “pack”) within the same batch element, separated by special boundary tokens.  
This approach significantly improves **GPU utilization** and reduces **training time** for large-scale language models.

### Longest-Pack-First Histogram Packing (Krell et al., 2021)

The **Longest-Pack-First (Histogram Packing)** algorithm, proposed by Krell et al. (2021), is an efficient heuristic for packing sequences of different lengths into fixed-size blocks. This method was widely adopted in training large autoregressive models (e.g., GPT-like architectures).

#### Key Idea

- Treat sequence lengths as items to fit into bins of fixed capacity (the model’s maximum sequence length).
    
- Sort all sequences by length in **descending order**.
    
- Iteratively assign each sequence to the “best-fitting” existing bin (pack) that can still accommodate it; if none fit, open a new bin.
    
- The **histogram-based optimization** step groups sequences with similar lengths to minimize wasted space.
    

### Example: Longest-Pack-First Histogram Packing

#### Pseudocode

```python
# Inputs:
# sequences = list of sequence lengths
# max_len = maximum sequence length per pack

sequences.sort(reverse=True)        # Step 1: sort by length (longest first)
packs = []                          # list of current bins

for seq_len in sequences:           # Step 2: greedy packing
    placed = False
    for pack in packs:
        if sum(pack) + seq_len <= max_len:
            pack.append(seq_len)
            placed = True
            break
    if not placed:
        packs.append([seq_len])     # Step 3: open new pack if none fit
```

This produces a set of efficiently filled “packs,” each containing one or more sequences whose total length does not exceed `max_len`.

#### Visual Example

Suppose `max_len = 10`, and we have sequences with lengths `[9, 8, 3, 3, 2, 2]`:

|Step|Current Packs|Explanation|
|---|---|---|
|1|[9]|9 starts a new pack|
|2|[9], [8]|8 starts a new pack|
|3|[9], [8, 2]|3 doesn’t fit in [9], fits in [8] → total 10|
|4|[9, 2], [8, 2], [3, 3]|Remaining 3,3,2 fill remaining gaps|

Final packing: **[9,2] [8,2] [3,3]**, using 3 packs instead of 6 — almost no wasted space.
