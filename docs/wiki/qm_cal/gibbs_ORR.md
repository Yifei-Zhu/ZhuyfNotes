---
layout: page
title: Gibbs Free Energy Calculation for O₂ to H₂O₂ Reaction
author: Yifei Zhu
comments: true
tags:
 - QM Calculation
 - Gaussian
 - Physical Chemistry
---
This wiki provides a concise guide on calculating the Gibbs free energy (ΔG) for the reaction where O₂ is reduced to H₂O₂ via a 2-electron oxygen reduction reaction (ORR) pathway on a catalyst surface (*). The process is key to understanding catalyst efficiency in producing H₂O₂.

---

## **Reaction Pathway**

The ORR pathway involves these steps:

1. O₂(g) → *O₂: O₂ adsorbs onto the catalyst.
2. \*O₂ + H⁺ + e⁻ → \*OOH: Proton-electron transfer forms *OOH.
3. \*OOH + H⁺ + e⁻ → \*HOOH: Another transfer forms *HOOH (adsorbed H₂O₂).
4. \*HOOH → H₂O₂(l) + \*: H₂O₂ desorbs into liquid phase.

---

## **Calculating ΔG**

### **General Formula**

For each step:

$$
\Delta G = \Delta E + \Delta \text{ZPE} - T \times \Delta S
$$

- **ΔE**: Electronic energy change (from DFT).
- **ΔZPE**: Zero-point energy change.
- **T × ΔS**: Entropy contribution (T = 298.15 K).

Proton-electron steps use the computational hydrogen electrode (CHE) model: $G(\text{H}^+ + \text{e}^-) = \frac{1}{2} G(\text{H}_2)$ at U = 0 V, pH = 0.

### **Step-by-Step ΔG**

1. O₂(g) → *O₂:
   $\Delta G_1 = G(*\text{O}_2) - G(*) - G(\text{O}_2\text{(g)})$
2. \*O₂ + H⁺ + e⁻ → *OOH:
   $\Delta G_2 = G(*\text{OOH}) - G(*\text{O}_2) - \frac{1}{2} G(\text{H}_2)$
3. \*OOH + H⁺ + e⁻ → *HOOH:
   $\Delta G_3 = G(*\text{HOOH}) - G(*\text{OOH}) - \frac{1}{2} G(\text{H}_2)$
4. \*HOOH → H₂O₂(l) + *:
   $\Delta G_4 = G(*) + G(\text{H}_2\text{O}_2\text{(l)}) - G(*\text{HOOH})$

### **Other Considerations**
#### **$\Delta G_U$: Electrode Potential**
$\Delta G_U = -n \times e \times U$

- $n$: Number of electrons (1 per proton-electron step).
- $U$: Electrode potential (V vs. SHE).

Set $U = 0$ V for baseline; adjust as needed.

#### **$\Delta G_{\text{pH}}$: pH Effect**
$\Delta G_{\text{pH}} = 0.0592 \times \text{pH} \, \text{(eV)}$

- pH = 0 (acidic): $\Delta G_{\text{pH}} = 0$.
- Adjust for other pH values (e.g., pH = 7 → 0.414 eV).

#### **Entropy ($S$) Calculation**
If you calculate $ΔG$ using Gaussian, the $G$ can be obtained directly. Otherwise, you might need to calculate $ΔG$ with $ΔS$.

- **Adsorbed Species**: From frequency analysis (e.g., VASP):
  1. Vibrational factor: $x_i = \frac{100 \times c \times h \times \nu_i}{k_B \times T}$.
  2. Partition function: $p f_i = \frac{x_i}{e^{x_i} - 1} - \log(1 - e^{-x_i})$.
  3. Total entropy: $S = \frac{R \times \sum p f_i}{1000 \times 96.485}$ (eV/K).
- **Gas Phase (O₂, H₂, H₂O₂)**: Use Gaussian 16 (6-311G* basis) to calculate vibrational, rotational, and translational contributions.

### **Free Energy Diagram**

- Reference: O₂(g) + * = 0 eV.
- Plot: *O₂ (ΔG₁), *OOH (ΔG₁ + ΔG₂), *HOOH (ΔG₁ + ΔG₂ + ΔG₃), H₂O₂(l) + * (ΔG₁ + ΔG₂ + ΔG₃ + ΔG₄).

---

## **Key Points to Note**

- **O₂(g) Correction**: DFT underestimates O₂(g) stability. Use:$$
  G(\text{O}_2\text{(g)}) = 2G(\text{H}_2\text{O}) - 2G(\text{H}_2) + 4.92 \, \text{eV}
  $$
- **H₂O₂(l) Adjustment**: Convert $G(\text{H}_2\text{O}_2\text{(g)}) $ to liquid phase:
  $G(\text{H}_2\text{O}_2\text{(l)}) = G(\text{H}_2\text{O}_2\text{(g)}) - 0.28 \, \text{eV}$
- **Adsorption Sites**: Optimize *O₂, *OOH, *HOOH configurations for stability.
- **Consistency**: Use identical DFT settings for all species.
- **Corrections**: Include ZPE, entropy, $ \Delta G_U $, and $ \Delta G_{\text{pH}} $ if needed.

---

## **Summary**

Accurate ΔG calculation for O₂ to H₂O₂ requires precise energy terms, gas-phase corrections, and consistent methods. These steps enable a reliable free energy diagram for evaluating ORR catalysts.
