---
layout: page
title: SHAP Analysis
author: Yifei Zhu
comments: true
tags:
  - ML
  - Algo
---

**SHAP (SHapley Additive exPlanations)** is a unified framework for interpreting machine-learning model predictions.  
It is based on **Shapley values** from cooperative game theory, which provide a principled way to distribute a model’s prediction among individual input features.

SHAP answers a simple question:

> _How much does each feature contribute to increasing or decreasing the prediction compared with a baseline?_

By treating each feature as a “player” in a cooperative game, SHAP assigns each feature an importance value that satisfies fairness properties such as additivity, consistency, and symmetry.

---

## Why SHAP?

SHAP is widely used because it:

- Works with many model types (tree-based models, linear models, neural networks).
    
- Provides **local explanations** (per-sample) and **global explanations** (overall feature importance).
    
- Offers intuitive visualizations such as summary plots, force plots, dependence plots, and waterfall plots.
    
- Ensures mathematically consistent attributions.
    

---

## SHAP Components

### 1. **Explainers**

Different explainers support different model types:

- **TreeExplainer** — optimized for Random Forest, XGBoost, LightGBM, CatBoost.
    
- **KernelExplainer** — model-agnostic, uses a sampling-based approximation.
    
- **DeepExplainer / GradientExplainer** — for neural networks.
    

### 2. **SHAP Values**

For a given instance ( x ), SHAP computes the contribution of each feature ( i ) as:

$$
\phi_i = \sum_{S \subseteq F \setminus {i}}  
\frac{|S|!(|F|-|S|-1)!}{|F|!}  
\big[f(S \cup {i}) - f(S)\big]  
$$

This represents the marginal contribution of feature ( i ) averaged over all possible subsets ( S ).

---

## Common SHAP Plots

SHAP provides a set of visualization tools that help interpret both **global** (dataset-level) and **local** (instance-level) model behaviors. These plots make it easier to understand how features contribute to predictions and how they interact with each other. The most commonly used SHAP plots include:

---

### 1. Summary Plot (Global Overview)

The **SHAP summary plot** is the most widely used visualization. It shows:

- **Overall feature importance** (sorted by mean absolute SHAP value)
    
- **Effect direction** (positive or negative impact on prediction)
    
- **Feature value distribution** (color-coded, usually from low to high)
    

This plot combines importance ranking and feature effect patterns in one chart, making it ideal as a first step in SHAP analyses.

---

### 2. Bar Plot (Global Feature Importance)

The **bar plot** displays the mean absolute SHAP value for each feature, sorted from most to least important.  
It provides a simple, clean view of global importance, without showing detailed variation within each feature.

Use this plot when you want a straightforward ranking of features.

---

### 3. Dependence Plot (Feature Interaction)

The **SHAP dependence plot** shows how the SHAP value of one feature varies with its feature value.  
It also reveals **feature interactions** by coloring each point with the value of a second feature.

This plot answers questions such as:

- “Does the effect of this feature increase monotonically?”
    
- “Which feature interacts strongly with it?”
    

---

### 4. Force Plot (Local Explanation)

The **force plot** provides a per-sample explanation that visualizes how each feature pushes the prediction up or down relative to the expected value.

- Red arrows push the prediction higher.
    
- Blue arrows push the prediction lower.
    
- The sum of contributions equals the final model output.
    

Good for explaining individual decisions (e.g., credit scoring).

---

### 5. Waterfall Plot (Local Decomposition)

The **waterfall plot** gives a step-by-step breakdown of a single instance’s prediction:

- Starts from the model’s baseline (expected value)
    
- Sequentially adds each feature's SHAP contribution
    
- Ends at the final prediction
    

It is more readable than the force plot when many features are involved.

---

## 6. Decision Plot (Local or Global Path Visualization)

The **decision plot** shows how each feature cumulatively contributes to predictions:

- Can visualize one or many samples simultaneously
    
- Shows curves representing prediction paths across features
    
- Highlights consistent and divergent behaviors
    

Useful for understanding how models differentiate groups of samples.
