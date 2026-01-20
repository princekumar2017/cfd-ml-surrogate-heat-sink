import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from plotting_utils import parity_plot, residual_hist

DATASET_FILE = "outputs/ML_dataset_clean_long.xlsx"

MODEL_NU_FILE = "outputs/RF_Nuavg_model.pkl"
MODEL_DP_FILE = "outputs/RF_DelP_model.pkl"

PARITY_DATA_FILE = "outputs/test_predictions_parity_data.xlsx"

def report(y_true, y_pred, name):
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"{name}: R2={r2:.4f}, MAE={mae:.4f}, RMSE={rmse:.4f}")

def train_models():
    # Load dataset created by build_dataset.py
    df = pd.read_excel(DATASET_FILE, engine="openpyxl")

    features = ["Re","Pr","Da","epsi","Hp_mm","a_mm","Lw_mm"]
    X = df[features].copy()
    y_nu = df["Nuavg"].copy()
    y_dp = df["DelP_Pa"].copy()

    # One split for both targets
    X_train, X_test, ynu_train, ynu_test, ydp_train, ydp_test = train_test_split(
        X, y_nu, y_dp, test_size=0.2, random_state=42
    )

    # Models
    rf_nu = RandomForestRegressor(
        n_estimators=600,
        max_depth=None,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )

    rf_dp = RandomForestRegressor(
        n_estimators=600,
        max_depth=None,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )

    rf_nu.fit(X_train, ynu_train)
    rf_dp.fit(X_train, ydp_train)

    ynu_pred = rf_nu.predict(X_test)
    ydp_pred = rf_dp.predict(X_test)

    print("\nMODEL PERFORMANCE (test set)")
    report(ynu_test, ynu_pred, "Nuavg")
    report(ydp_test, ydp_pred, "DelP (Pa)")

    # Save models
    os.makedirs("outputs", exist_ok=True)
    joblib.dump(rf_nu, MODEL_NU_FILE)
    joblib.dump(rf_dp, MODEL_DP_FILE)
    print("\nSaved:", MODEL_NU_FILE, ",", MODEL_DP_FILE)

    # Plots (save into figures/)
    os.makedirs("figures", exist_ok=True)
    parity_plot(ynu_test.values, ynu_pred, "Parity Plot: Nuavg", "figures/parity_Nuavg.png")
    parity_plot(ydp_test.values, ydp_pred, "Parity Plot: ΔP (Pa)", "figures/parity_DelP.png")

    # Optional residual histograms (helpful)
    residual_hist(ynu_test.values, ynu_pred, "Residuals: Nuavg", "figures/residuals_Nuavg.png")
    residual_hist(ydp_test.values, ydp_pred, "Residuals: ΔP (Pa)", "figures/residuals_DelP.png")

    # Export test predictions (for MATLAB or paper)
    out = X_test.copy()
    out["Nuavg_true"] = ynu_test.values
    out["Nuavg_pred"] = ynu_pred
    out["DelP_true"] = ydp_test.values
    out["DelP_pred"] = ydp_pred

    out.to_excel(PARITY_DATA_FILE, index=False)
    print("\nSaved:", PARITY_DATA_FILE)

if __name__ == "__main__":
    train_models()

