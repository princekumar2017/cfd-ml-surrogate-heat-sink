# CFD–ML Surrogate Modeling of Porous Wavy Channels (Heat Sink)

This repository presents a CFD-informed machine learning framework to predict
average Nusselt number (Nu_avg) and pressure drop (ΔP) in porous wavy channels
governed by Brinkman–Forchheimer flow with constant wall heat flux.

The surrogate models are trained using high-fidelity COMSOL Multiphysics
simulations and enable rapid performance prediction without re-running CFD.

---

## 🔬 Physics and Numerical Model

- Flow model: Brinkman–Forchheimer porous media model
- Energy model: Conjugate heat transfer with constant heat flux
- Geometry: 2D wavy channel with porous slab
- Solver: Fully coupled stationary solver (COMSOL)

---

## 📥 Input Parameters

| Symbol | Description | Range |
|------|------------|-------|
| Re | Reynolds number | 25 – 500 |
| Pr | Prandtl number | 3 – 50 |
| Da | Darcy number | 1e−3 – 1e−6 |
| ε | Porosity | 0.70 – 0.85 |
| Hp | Slab thickness (mm) | 0.1 – 0.3 |
| a | Wave amplitude (mm) | 0 – 0.3 |
| Lw | Wavelength (mm) | 4, 5 |

---

## 📤 Output Quantities

- Average Nusselt number (Nu_avg)
- Pressure drop (ΔP) in Pa

---

## 📊 Dataset

- 768 operating conditions
- 6 geometrical configurations
- Total samples: **4608**
- Cleaned and reshaped to long format

Dataset file: data/ML_dataset_clean_long.xlsx

---

## 🤖 Machine Learning Models

- Algorithm: Random Forest Regressor
- Separate models for Nu_avg and ΔP
- Features: Re, Pr, Da, ε, Hp, a, Lw

### Model performance (test set)

| Quantity | R² | MAE | RMSE |
|--------|----|-----|------|
| Nu_avg | 0.999 | 0.071 | 0.331 |
| ΔP (Pa) | 1.000 | 0.655 | 2.09 |

Trained models:
    models/RF_Nuavg_model.pkl (Average Nusselt number:- Heat transfer)
    models/RF_DelP_model.pkl  (Pressure drop:- Pumping power)

---

## 📈 Key Results

- Excellent agreement between CFD and ML predictions
- High accuracy across full parameter space
- Strong interpretability via feature importance

Figures available in: figures/

---

## ✅ Validation Strategy

15 independent CFD cases spanning:
- Low / high Re
- Low / high Pr
- Low / high Da
- Multiple geometries

Used for independent ML validation.

---

## 🧪 How to Run

1. Clone the repository
2. Create Python environment
3. Run notebooks in order:
    notebooks/01_build_dataset.ipynb
    notebooks/02_train_models.ipynb
    notebooks/03_evaluate_plots.ipynb
    notebooks/04_predict_new_cases.ipynb

---

## 📌 Applications

- Rapid design screening
- Surrogate modeling for optimization
- CFD + ML integration for thermal systems

---

## 📜 License

MIT License

---

## 👤 Author

**Prince Kumar**  
CFD | Heat Sink | Battery modeling | Machine Learning

