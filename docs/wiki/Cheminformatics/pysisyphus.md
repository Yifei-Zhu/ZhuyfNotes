---
layout: page
title: Chemistry Python Library
author: Yifei Zhu
comments: true
tags:
  - Cheminformatics
  - Python
---

## Get redundant internal coordinates from XYZ

### Command Line
```bash
pysistrj --internals input.xyz
```

### Python

```python
  def get_ric_list_from_xyz(input_xyz):
    """Get redundant internal coordinates with stable order.
	Inputs:
		input_xyz: target xyz file with single geometry
    Returns:
        ric_dict: a dict of RIC
    """
    ric_dict = defaultdict(list)
    geom = geom_loader(input_xyz, coord_type="redund")
    typed_prims = geom.internal.typed_prims

    type_map = {0: "bond", 1: "bend", 2: "dihedral"}

    seen = set()
    for tp in typed_prims:
        typ = tp[0].name
        atoms = tuple(sorted(tp[1:]))
        if atoms not in seen:
            seen.add(atoms)
            ric_dict[typ].append(atoms)

    for typ in ric_dict:
        ric_dict[typ].sort()

    return dict(ric_dict)
    
def get_coord_from_tuple(input_xyz, atom_indices):
	"""Get Cartesian coords of atoms in atom_indeices
	Input:
		input_xyz: XYF file of target mol
		atom_indices: tuple of atom indeices, e.g. (2,10), (3,10,11,13)
	return:
		a dict of Cartesian coords
	"""
    coord_dict={}
    geom = geom_loader(input_xyz)
    coords3d = geom.coords3d
    for i in atom_indices:
        atom = geom.atoms[i]
        x, y, z = coords3d[i]
        coord_dict[i] = [atom,x,y,z]
    return coord_dict

```

**Package**

> Here, I wrote a package that generates redundant internal coordinates from a molecular geometry file using pysisyphus.  https://gitee.com/Zhu-Yifei_1998/get_ric
> 2025.11.11

