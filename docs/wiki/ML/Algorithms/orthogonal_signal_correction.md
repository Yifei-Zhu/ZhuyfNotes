---
layout: page
title: Orthogonal Signal Correction
author: Yifei Zhu
comments: true
tags:
  - ML
  - Preprocessing
  - Algo
---
**Orthogonal Signal Correction (OSC)** is a preprocessing technique used in chemometrics and spectroscopy to remove systematic variations from the data matrix $\mathbf{X}$ that are orthogonal to the response variable $\mathbf{Y}$, enhancing model interpretability and prediction, especially in Partial Least Squares (PLS) regression.

## Overview

OSC removes variations in $\mathbf{X}$ (e.g., spectral data, $n \times p$) unrelated to $\mathbf{Y}$ (e.g., concentrations, $n \times m$), such as noise or environmental effects, producing a corrected matrix $\mathbf{X}_{\text{OSC}}$.

## Mathematical Principles

### Algorithm

1. **Preprocess**: Center  and $\mathbf{Y}$.
2. **Initialize $\mathbf{w}$**: Compute via PCA or PLS.
3. **Orthogonalize $\mathbf{w}$**:  
    $$
    \mathbf{w}_{\text{ortho}} = \mathbf{w} - \mathbf{Y} (\mathbf{Y}^T \mathbf{Y})^{-1} \mathbf{Y}^T \mathbf{w}  
    $$
    Normalize $\mathbf{w}_{\text{ortho}}$.
4. **Compute Score**: $\mathbf{t} = \mathbf{X} \mathbf{w}_{\text{ortho}}$, normalize $\mathbf{t}$.
5. **Compute Loading**: $\mathbf{p} = \frac{\mathbf{X}^T \mathbf{t}}{\mathbf{t}^T \mathbf{t}}$.
6. **Remove Component**: $\mathbf{X} = \mathbf{X} - \mathbf{t} \mathbf{p}^T$.
7. **Iterate**: Repeat for $k$ components.
8. **Output**: $\mathbf{X}_{\text{OSC}} = \mathbf{X} - \sum_{i=1}^k \mathbf{t}_i \mathbf{p}_i^T$.

## Orthogonalization Formula Derivation

To ensure $\mathbf{w}_{\text{ortho}}$ is orthogonal to $\mathbf{Y}$ $(\mathbf{Y}^T \mathbf{w}_{\text{ortho}} = 0)$:  
$$
\mathbf{w}_{\text{ortho}} = \mathbf{w} - \mathbf{Y} \mathbf{c}  
$$ 
Solve for $\mathbf{c}$:  
$$  
\mathbf{Y}^T (\mathbf{w} - \mathbf{Y} \mathbf{c}) = 0 \implies \mathbf{Y}^T \mathbf{Y} \mathbf{c} = \mathbf{Y}^T \mathbf{w} \implies \mathbf{c} = (\mathbf{Y}^T \mathbf{Y})^{-1} \mathbf{Y}^T \mathbf{w}  
$$  
Thus:  
$$ 
\mathbf{w}_{\text{ortho}} = \mathbf{w} - \mathbf{Y} (\mathbf{Y}^T \mathbf{Y})^{-1} \mathbf{Y}^T \mathbf{w}  
$$
**Verification**:  
$$  
\mathbf{Y}^T \mathbf{w}_{\text{ortho}} = \mathbf{Y}^T \mathbf{w} - \mathbf{Y}^T \mathbf{Y} (\mathbf{Y}^T \mathbf{Y})^{-1} \mathbf{Y}^T \mathbf{w} = \mathbf{Y}^T \mathbf{w} - \mathbf{Y}^T \mathbf{w} = 0  
$$ 
For single response ((m=1)):  
$$
\mathbf{w}_{\text{ortho}} = \mathbf{w} - \frac{\mathbf{Y} (\mathbf{Y}^T \mathbf{w})}{\mathbf{Y}^T \mathbf{Y}}  
$$


## Conclusion

OSC removes $\mathbf{Y}$-orthogonal variations from $\mathbf{X}$ using the key formula $\mathbf{w}_{\text{ortho}} = \mathbf{w} - \mathbf{Y} (\mathbf{Y}^T \mathbf{Y})^{-1} \mathbf{Y}^T \mathbf{w}$, ensuring robust preprocessing for multivariate analysis.