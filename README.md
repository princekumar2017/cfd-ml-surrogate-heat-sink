# Machine Learning–Accelerated Thermo-hydrulic Prediction  
### CFD + Random Forest Surrogate Modeling for Thermal System Design

## Project Summary
This project demonstrates an **end-to-end engineering workflow** that combines
**high-fidelity CFD simulations** with **machine learning surrogate models** to
predict thermal and hydraulic performance in complex internal flow geometries.

The framework enables **fast, accurate predictions** of:
- **Average Nusselt number (Nū)** → heat transfer performance
- **Pressure drop (ΔP)** → pumping power penalty

for **porous wavy channel configurations**, representative of:
- Heat sinks
- Compact heat exchangers
- Electronics and battery thermal management systems

---

## Why This Matters (Industry Perspective)
Traditional CFD parametric studies are:
- Computationally expensive
- Slow for design iteration
- Difficult to integrate into optimization loops

This project shows how **ML surrogate models** can:
- Replace thousands of CFD runs during design exploration
- Enable real-time performance prediction
- Support optimization and decision-making workflows
- Preserve physical trends learned from CFD

---

## Engineering & Physics Background
- 2D sinusoidal wavy channel
- Partially porous slab region
- Brinkman–Forchheimer porous flow model
- Constant heat flux boundary condition
- Steady, laminar forced convection

**Key design variables**
- Reynolds number (Re)
- Prandtl number (Pr)
- Darcy number (Da)
- Porosity (ε)
- Porous slab thickness (Hp)
- Wave amplitude (a)
- Wavelength (Lw)

---

## CFD Dataset Overview
- **768 fully converged CFD simulations**
- Each simulation represents a unique operating condition:
  - Re × Pr × Da × ε × Hp
- Each CFD case is expanded across multiple geometry variants:
  - Different wave amplitudes and wavelengths

**Final ML dataset**
- Long-form dataset created from CFD results
- **4608 labeled samples** used for training
- All samples are physically valid (no failed or incomplete cases)

---

## Machine Learning Implementation
- Algorithm: **Random Forest Regressor**
- Input features:  
  `Re, Pr, Da, ε, Hp, a, Lw`
- Outputs:  
  `Average Nusselt number (Nū)`  
  `Pressure drop (ΔP)`
- Train/test split: **80% / 20%**
- Separate regression models for thermal and hydraulic performance

This approach captures:
- Strong nonlinear interactions
- Geometry–flow coupling effects
- Porous media impacts on heat transfer and pressure loss

---

## Model Performance
- **Nū prediction accuracy:**  
  **R² = 0.9990**, MAE = 0.0709, RMSE = 0.3306
- **ΔP prediction accuracy:**  
  **R² = 1.0000**, MAE = 0.6545 Pa, RMSE = 2.0924 Pa

Parity plots show excellent agreement between CFD results and ML predictions.

<p align="center">
  <img src="figures/parity_Nuavg.png" width="45%">
  <img src="figures/parity_DelP.png" width="45%">
</p>

---

## Technical Skills Demonstrated
- CFD-based thermal–fluid modeling
- Porous media flow and heat transfer
- Parametric simulation design
- Data engineering from simulation outputs
- Supervised machine learning for regression
- Model validation and performance assessment
- Python (NumPy, pandas, scikit-learn, matplotlib)
- Reproducible and modular code structure

---

## Repository Structure
```text
src/          → Dataset construction, ML training, evaluation scripts
figures/      → Publication-quality plots (parity, residuals)
