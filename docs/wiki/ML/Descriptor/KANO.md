---
layout: page
title: KANO
author: Yifei Zhu
comments: true
tags:
  - ML
  - Python
  - Descriptor
---
**K**nowledge graph-enhanced molecular contr**A**stive learning with fu**N**ctional pr**O**mpt (**KANO**)

**Firstly**, we construct a Chemical Element Knowledge Graph (ElementKG) based on the Periodic Table and Wikipedia pages to summarize the class hierarchy, relations and chemical attributes of elements and functional groups.

**Second**, we propose an element-guided graph augmentation in contrastive-based pre-training to capture deeper associations inside molecular graphs.

**Third**, to bridge the gap between the pre-training <u>contrastive tasks</u> ([[contrastive_learning]]) and downstream molecular property prediction tasks, we propose functional prompts to evoke the downstream task-related knowledge acquired by the pre-trained model.

![[Pasted image 20251018170801.png]]


### Ref
- Github: https://github.com/HICAI-ZJU/KANO.git

```Bash
# requirements
python          3.7
torch           1.13.1
rdkit           2018.09.3
numpy           1.20.3
gensim          4.2.0
nltk            3.4.5
owl2vec-star    0.2.1
Owlready2       0.37
torch-scatter   2.0.9
```

- Environ. Sci. Technol. 2025, 59, 18, 9298–9311, https://doi.org/10.1021/acs.est.4c14193