---
layout: page
title: Smith–Waterman Algorithm
author: Yifei Zhu
comments: true
tags:
  - ML
  - Algo
---
# Smith–Waterman Algorithm

The **Smith–Waterman algorithm** is a **dynamic programming** method for **local sequence alignment** — finding the most similar regions between two biological sequences (DNA, RNA, or proteins). It was developed by **Temple F. Smith** and **Michael S. Waterman** in 1981.

## Overview

Unlike the **Needleman–Wunsch** algorithm, which aligns sequences globally from end to end, **Smith–Waterman** focuses only on the **best-matching subsequences**. This makes it ideal when the sequences share only partial similarity.

## How It Works

The algorithm constructs a scoring matrix to compute the optimal local alignment:

1. **Initialization:**  
    The first row and column are set to zero (allowing local alignment to start anywhere).
    
2. **Scoring rule:**  
    For sequences `A` and `B`, each cell `H(i, j)` is computed as:
    
    ```
    H(i, j) = max(
        0,
        H(i-1, j-1) + match_or_mismatch_score,
        H(i-1, j) - gap_penalty,
        H(i, j-1) - gap_penalty
    )
    ```
    
    The zero ensures scores never go negative, which enables local (not global) alignment.
    
3. **Traceback:**  
    Start from the highest-scoring cell and move diagonally, up, or left until a cell with score 0 is reached.  
    The traced path gives the **best local alignment**.
    

## Example

Consider two short DNA sequences:

```
A = G A C T
B = G A C
```

Scoring scheme: Match = +2, Mismatch = –1, Gap = –2.  
The resulting scoring matrix (partial view):

| | |G|A|C|
|---|---|---|---|---|
||0|0|0|0|
|G|0|2|0|0|
|A|0|0|4|2|
|C|0|0|2|6|
|T|0|0|0|4|

The **maximum score (6)** corresponds to the local alignment:

```
A: G A C
B: G A C
```

## Pseudocode

```python
def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-2):
    m, n = len(seq1), len(seq2)
    H = [[0]*(n+1) for _ in range(m+1)]
    max_score, max_pos = 0, (0, 0)

    for i in range(1, m+1):
        for j in range(1, n+1):
            score_diag = H[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            score_up = H[i-1][j] + gap
            score_left = H[i][j-1] + gap
            H[i][j] = max(0, score_diag, score_up, score_left)

            if H[i][j] > max_score:
                max_score, max_pos = H[i][j], (i, j)

    return max_score, max_pos
```

## Key Features

- **Local alignment:** Finds the most similar region, not the entire sequence.
    
- **Dynamic programming:** Guarantees optimal alignment.
    
- **Accurate but slow:** O(mn) time complexity.
    

## Applications

- Detecting conserved motifs or protein domains
    
- Finding homologous genes
    
- Analyzing sequencing data in bioinformatics
    