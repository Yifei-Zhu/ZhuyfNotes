---
layout: page
title: Tanimoto Coefficient and Dice Coefficient
author: Yifei Zhu
comments: true
tags:
  - ML
  - Algo
---

The **Tanimoto coefficient** and **Dice coefficient** are two related measures used to quantify the **similarity between two sets** or **binary vectors**. They are widely used in **cheminformatics**, **machine learning**, and **information retrieval** to compare molecular fingerprints or feature sets.

---

## Tanimoto Coefficient

The **Tanimoto coefficient** (also called the **Jaccard index**) measures the ratio of shared features to total unique features between two sets ( A ) and ( B ).

$$T(A, B) = \frac{|A \cap B|}{|A \cup B|} = \frac{c}{a + b - c}$$  

where:

- ( a ) = number of bits set in fingerprint A
    
- ( b ) = number of bits set in fingerprint B
    
- ( c ) = number of bits set in both A and B
    

**Range:** 0 to 1

- 1 → identical fingerprints
    
- 0 → no overlap
    

**Example:**  
If A = {1, 2, 3, 4} and B = {3, 4, 5}, then  
$$T = \frac{2}{5} = 0.4    $$

---

## Dice Coefficient

The **Dice coefficient** (or **Sørensen–Dice index**) emphasizes shared features slightly more than Tanimoto:

$$D(A, B) = \frac{2|A \cap B|}{|A| + |B|} = \frac{2c}{a + b}  $$


**Range:** 0 to 1

- 1 → identical sets
    
- 0 → no overlap
    

**Example:**  
Using the same sets as above,  
$$
D = \frac{2 \times 2}{4 + 3} = \frac{4}{7} \approx 0.57  
$$

---

## Comparison

| Property   | Tanimoto                                   | Dice                           |
| ---------- | ------------------------------------------ | ------------------------------ |
| Formula    | $c / (a + b - c)$                          | $2c / (a + b)$                 |
| Emphasis   | Balanced                                   | Rewards overlap slightly more  |
| Range      | 0–1                                        | 0–1                            |
| Common Use | Molecular fingerprints (RDKit, Open Babel) | Image segmentation, clustering |

---

## Applications

- **Cheminformatics:** Measuring molecular similarity using fingerprints (e.g., ECFP).
    
- **Machine learning:** Comparing binary feature vectors.
    
- **Information retrieval:** Ranking documents or data points by similarity.
    
