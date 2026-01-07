---
layout: page
title: Nested Cross-Validation
author: Yifei Zhu
comments: true
tags:
  - ML
  - Algo
---
**Nested Cross-Validation (Nested CV)** is a robust evaluation strategy used to estimate the generalization performance of machine-learning models when hyperparameter tuning is involved.  
Traditional cross-validation may lead to overly optimistic scores because hyperparameters are selected using the same data on which performance is evaluated. Nested CV solves this by introducing two loops:

- **Outer loop**: Splits the dataset into training/testing folds to estimate generalization performance.
    
- **Inner loop**: Performs hyperparameter tuning (e.g., grid search or Bayesian optimization) using only the training folds of the outer loop.
    

By keeping model selection (inner loop) and model assessment (outer loop) strictly separated, nested CV provides an unbiased estimate of true performance.

---

## Workflow

1. Split data using an **outer K-fold CV**.
    
2. For each outer training fold:
    
    - Run **inner K-fold CV** to tune hyperparameters.
        
    - Train a final model using the best hyperparameters on the entire inner-training set.
        
3. Evaluate performance on the untouched outer test fold.
    
4. Average outer-loop scores → unbiased estimate.
    

---

## Example (scikit-learn)

```python
from sklearn.datasets import load_boston
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
import numpy as np

# Dataset
X, y = load_boston(return_X_y=True)

# Outer CV for unbiased evaluation
outer_cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Hyperparameter grid for inner CV
param_grid = {"alpha": [0.1, 1, 10, 100]}

outer_scores = []

for train_idx, test_idx in outer_cv.split(X):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    # Inner CV + hyperparameter tuning
    model = Ridge()
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=3,              # inner fold
        scoring='neg_mean_squared_error'
    )
    grid_search.fit(X_train, y_train)

    # Evaluate on outer test fold
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    outer_scores.append(mse)

print("Outer CV MSE:", outer_scores)
print("Mean MSE:", np.mean(outer_scores))
```
