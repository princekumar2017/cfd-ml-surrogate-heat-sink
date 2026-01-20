# Machine Learning–Accelerated Heat Transfer Prediction  
### CFD + Random Forest Surrogate Modeling for Porous Wavy Channels (Heat Sink Applications)

## Overview
This repository demonstrates a **machine-learning surrogate modeling framework**
trained on high-fidelity CFD simulations of **laminar forced convection in a
wavy channel with a porous slab**.

The objective is to rapidly predict:
- **Average Nusselt number (Nū)**
- **Pressure drop (ΔP)**

across a wide parametric space, enabling:
- Design exploration
- Optimization studies
- Reduced CFD computational cost

> ⚠️ **Note:** Raw simulation data and trained models are intentionally excluded
> to protect unpublished research results.

---

## Physics & Modeling Background
- 2D sinusoidal channel geometry
- Partially porous slab (Brinkman–Forchheimer model)
- Constant heat flux boundary condition
- Steady-state laminar flow

**Governing parameters**
- Reynolds number (Re)
- Prandtl number (Pr)
- Darcy number (Da)
- Porosity (ε)
- Slab thickness (Hp)
- Wave amplitude (a)
- Wavelength (Lw)

---

## Machine Learning Approach
- Model: **Random Forest Regressor**
- Inputs:  
  `Re, Pr, Da, ε, Hp, a, Lw`
- Outputs:  
  `Nū`, `ΔP`
- Dataset size: ~4600 samples (long-form expansion)
- Train/test split: 80% / 20%

---

## Key Results
- **Nū prediction:**  
  R2=0.9990, MAE=0.0709, RMSE=0.3306
- **ΔP (Pa) prediction:**  
  R2=1.0000, MAE=0.6545, RMSE=2.0924

Parity plots demonstrate excellent agreement between
CFD ground truth and ML predictions.

<p align="center">
  <img src="figures/parity_Nuavg.png" width="45%">
  <img src="figures/parity_DelP.png" width="45%">
</p>

---

## Repository Structure
```text
src/          → Core ML pipeline (dataset build, training, evaluation)
notebooks/    → Demonstration notebook (sanitized)
figures/      → Selected publication-quality plots
