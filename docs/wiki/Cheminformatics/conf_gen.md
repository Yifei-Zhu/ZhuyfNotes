---
layout: page
title: Conformer Generation Tools
author: Yifei Zhu
comments: true
tags:
  - Cheminformatics
  - Python
---
## Open-Source v.s. Commercial
### Open-Source Tools

- Balloon
- Confab
- Conforge
- FROG2
- Moltiverse
- CONFORGE
- BCL::Conf
- Multiconf-DOCK
- OpenBabel
- RDKit

### Commercial Tools:

- CAESAR
- ConfGen
- Conformator
- COSMOS
- ForceGen
- OMEGA
- iCon
- CREST
- Molecular Operating Environment (MOE) LowModeMD
- MOE Stochastic and MOE Conformation Import


## Rule-/Knowledge-based

- iCon
- Omega
- CAESAR
- Confab
- ConfGen
- FROG2
- Conformator
- COSMOS
- BCL::Conf
- CONFORGE


## Molclus

REF: http://www.keinsci.com/research/molclus.html

- Molclus自带的genmer程序结合Molclus：用于分子团簇或原子团簇构型搜索，使用简便。对于分子团簇搜索这通常是首选。唯一局限性是对分子的构象考虑不够充分，因为genmer将分子当成刚性来堆积，因此不适合单分子柔性很强的情况（这种情况适合后面说的做动力学程序结合molclus）。相关介绍和示例看《genmer：生成团簇初始构型结合molclus做团簇结构搜索的超便捷工具》（[http://bbs.keinsci.com/thread-2369-1-1.html](http://bbs.keinsci.com/thread-2369-1-1.html)）
- Molclus自带的gentor程序结合Molclus：用于分子构象搜索。使用简便，但不支持环状区域构象搜索（环状区域是指诸如环己烷这样有多种构象的环状区域）。对于可旋转的键不很多的分子的构象搜索这是首选，可控性最强。相关介绍和示例看《gentor：扫描方式做分子构象搜索的便捷工具》（[http://bbs.keinsci.com/thread-2388-1-1.html](http://bbs.keinsci.com/thread-2388-1-1.html)）
- 第三方的Confab或Frog2构象生成程序结合Molclus：用于分子构象搜索。使用最为傻瓜化，但不支持环状区域构象搜索、不支持普通有机分子以外的情况。相关介绍和示例看《将Confab或Frog2与Molclus联用对有机体系做构象搜索》[http://bbs.keinsci.com/thread-20063-1-1.html](http://bbs.keinsci.com/thread-20063-1-1.html)）
- xtb程序跑动力学轨迹结合Molclus：普适性极强，用于构象搜索、原子/分子团簇构型搜索皆可，使用容易。但由于模拟时间长度有限，有动力学采样不充分导致遗漏构型/构象的风险（风险随动力学模拟时间增长而减小）。相关介绍和示例看《使用Molclus结合xtb做的动力学模拟对瑞德西韦(Remdesivir)做构象搜索》（[http://bbs.keinsci.com/thread-16255-1-1.html](http://bbs.keinsci.com/thread-16255-1-1.html)）
- GROMACS等经典力场分子动力学程序结合Molclus：用于分子团簇搜索和分子构象搜索。使用稍繁琐，因为得创建拓扑文件，且被动力学模拟的体系必须有恰当的力场，好处是动力学模拟耗时极低，因此动力学采样不充分导致遗漏构型/构象的风险很小。相关介绍和示例看《使用molclus程序做团簇构型搜索和分子构象搜索》（[http://bbs.keinsci.com/thread-577-1-1.html](http://bbs.keinsci.com/thread-577-1-1.html)）。
  


