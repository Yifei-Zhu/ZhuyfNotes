---
layout: page
title: In-Context Learning
author: Yifei Zhu
comments: true
tags:
  - ML
  - LLM
---
# In-Context Learning (ICL)

**In-Context Learning (ICL)** refers to the ability of large language models (LLMs) to learn and perform new tasks from examples provided directly within the input prompt — without updating their model parameters. Instead of traditional training or fine-tuning, the model “learns” from context.

## How It Works

In ICL, a user provides **a few examples** (input–output pairs) or **instructions** in the prompt. The model then infers the underlying pattern or task and applies it to unseen inputs in the same session.  
For example:

```
Translate English to French:
English: apple → French: pomme
English: cat → French: chat
English: dog → French:
```

The model continues the pattern by outputting “chien.”

## Key Features

- **No parameter updates** – Learning happens dynamically during inference.
    
- **Few-shot or zero-shot** – The model can generalize from a few or even no examples.
    
- **Prompt-dependent** – Performance depends heavily on the structure and quality of the prompt.
    

## Comparison with Other Learning Paradigms

- **Fine-tuning:** Adjusts model parameters on task-specific data, requiring retraining and computational resources. In contrast, ICL learns “on the fly” during inference.
    
- **Retrieval-Augmented Learning:** Incorporates external knowledge from a database or document store to improve responses, while ICL relies solely on the examples given in the prompt.
    
