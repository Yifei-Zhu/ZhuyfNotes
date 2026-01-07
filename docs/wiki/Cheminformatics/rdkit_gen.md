---
layout: page
title: RDKit Conformer Generation
author: Yifei Zhu
comments: true
tags:
  - Python
  - RDKit
  - Cheminformatics
---
RDKit provides several methods for generating 3D molecular conformations (conformers) from 2D or SMILES representations. These conformers represent different possible spatial arrangements of a molecule’s atoms that satisfy its bonding and geometric constraints.

---

## 1. Overview

Conformer generation in RDKit involves **embedding** atoms in 3D space followed by **geometry optimization**.  
The general workflow is:

1. Convert a molecule (e.g., from SMILES) to an RDKit `Mol` object.
    
2. Use an embedding algorithm (e.g., `EmbedMolecule()` or `EmbedMultipleConfs()`) to generate one or more 3D conformers.
    
3. Optionally refine the geometries using force-field minimization (`UFF`, `MMFF`).
    

---

## 2. Embedding Methods

### 2.1 Distance Geometry (DG)

The **classical embedding** in RDKit is based on **distance geometry (DG)**.  
It constructs a **distance bounds matrix** based on atomic connectivity and stereochemical constraints, then **embeds** the molecule in 3D space by solving for coordinates consistent with these bounds.

**Example:**

```python
from rdkit import Chem
from rdkit.Chem import AllChem

mol = Chem.MolFromSmiles("CCO")
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol)  # Classical distance geometry
```

While simple, classical DG embeddings can produce unrealistic conformations, especially for flexible or large molecules, because it doesn’t encode chemical knowledge such as torsional preferences or ring strain.

---

## 3. ETKDG Method

### 3.1 What is ETKDG?

**ETKDG (Experimental-Torsion Knowledge Distance Geometry)** is an improved algorithm that combines **experimental torsional angle preferences** and **knowledge-based geometric constraints** with distance geometry.  
It was developed to produce more **realistic, low-energy conformations** that better match experimentally observed structures.

### 3.2 Evolution of ETKDG

| Version     | Description                                                                                  |
| ----------- | -------------------------------------------------------------------------------------------- |
| **ETDG**    | Adds **experimental torsion-angle distributions** to DG.                                     |
| **ETKDG**   | Further includes **basic knowledge-based corrections** (e.g., preferred ring conformations). |
| **ETKDGv2** | Improves ring sampling and reproduces crystallographic geometries more accurately.           |
| **ETKDGv3** | Introduces refined covalent geometry parameters and enhanced distance constraints.           |

### 3.3 Usage Example

```python
from rdkit import Chem
from rdkit.Chem import AllChem

mol = Chem.MolFromSmiles("CCO")
mol = Chem.AddHs(mol)

# Generate multiple ETKDG conformers
params = AllChem.ETKDGv3()
conf_ids = AllChem.EmbedMultipleConfs(mol, numConfs=10, params=params)
```

### 3.4 Advantages

- Produces **experimentally realistic** conformations
    
- Captures **torsional preferences** and **ring strain**
    
- More robust for **flexible or macrocyclic** molecules
    
- Can be combined with force-field minimization for further refinement
    

---

## 4. Force Field Optimization

After embedding, RDKit allows conformer refinement using **molecular mechanics force fields**:

```python
from rdkit.Chem import AllChem

for conf_id in conf_ids:
    AllChem.UFFOptimizeMoleculeConfs(mol, confId=conf_id)
	# or
	AllChem.MMFFOptimizeMoleculeConfs(mol, confId=conf_id)

```

Both **UFF** and **MMFF94** force fields are supported.  
This step improves geometric consistency and helps identify the **lowest-energy conformer**.

---

## 5. Summary

|Method|Key Feature|Realism|Typical Use|
|---|---|---|---|
|**DG**|Classical distance geometry|Low|Simple, fast generation|
|**ETDG**|Adds experimental torsions|Medium|Improved torsional accuracy|
|**ETKDG**|Combines torsions + knowledge-based constraints|High|Default for realistic conformers|
|**ETKDGv3**|Latest refinement with better covalent geometry|Very High|Best choice for general use|

---

## References

- Riniker, S.; Landrum, G. A. _J. Chem. Inf. Model._ **2015**, _55_(12), 2562–2574.  
    _Better Informed Distance Geometry: Using What We Know To Improve Conformation Generation._
    
- Wang, S.; Witek, J.; Landrum, G. A.; Riniker, S. _J. Chem. Inf. Model._ **2020**, _60_(4), 2044–2058.  
    _Improved Conformer Generation for Small Rings and Macrocycles._
    
