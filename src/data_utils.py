import pandas as pd

# Raw files (kept private)
NU_FILE = "data_private/Nuavg.xlsx"
DP_FILE = "data_private/DelP.xlsx"

# Output dataset (safe to publish AFTER anonymization, but by default keep in outputs/)
OUT_FILE = "outputs/ML_dataset_clean_long.xlsx"

def build_dataset():
    # Read Excel (no headers)
    nu_raw = pd.read_excel(NU_FILE, header=None, engine="openpyxl")
    dp_raw = pd.read_excel(DP_FILE, header=None, engine="openpyxl")

    # Enforce exactly 768 rows (no silent dropping beyond this)
    nu_raw = nu_raw.iloc[:768, :].copy()
    dp_raw = dp_raw.iloc[:768, :].copy()

    print("Nuavg raw shape:", nu_raw.shape)
    print("DelP raw shape :", dp_raw.shape)

    # Inputs: columns 1–5 (0–4 in pandas)
    X_base = nu_raw.iloc[:, 0:5].copy()
    X_base.columns = ["Re", "Pr", "Da", "epsi", "Hp_mm"]

    for c in X_base.columns:
        X_base[c] = pd.to_numeric(X_base[c], errors="coerce")

    # Output mapping (convert 1-based -> 0-based indices)
    # Nuavg.xlsx: col 5..10 => indices 4..9
    # DelP.xlsx : col 8,11,14,17,20,23 => indices 7,10,13,16,19,22
    cases = [
        # (nu_col0, dp_col0, a_mm, Lw_mm)
        (5-1,  8-1,  0.0, 0.0),  # a=0,  Lw N/A
        (6-1, 11-1,  0.1, 4.0),
        (7-1, 14-1,  0.1, 5.0),
        (8-1, 17-1,  0.2, 4.0),
        (9-1, 20-1,  0.2, 5.0),
        (10-1, 23-1, 0.3, 4.0),
    ]

    rows = []
    for nu_c, dp_c, a_mm, Lw_mm in cases:
        tmp = X_base.copy()
        tmp["a_mm"] = a_mm
        tmp["Lw_mm"] = Lw_mm

        tmp["Nuavg"] = pd.to_numeric(nu_raw.iloc[:, nu_c], errors="coerce")
        tmp["DelP_Pa"] = pd.to_numeric(dp_raw.iloc[:, dp_c], errors="coerce")

        rows.append(tmp)

    df = pd.concat(rows, ignore_index=True)

    print("\nCombined long dataset (before drop):", df.shape)
    print("Missing Nuavg count:", df["Nuavg"].isna().sum())
    print("Missing DelP count :", df["DelP_Pa"].isna().sum())

    # Drop rows where outputs missing (keep full valid set)
    df_clean = df.dropna(
        subset=["Re","Pr","Da","epsi","Hp_mm","a_mm","Lw_mm","Nuavg","DelP_Pa"]
    ).reset_index(drop=True)

    print("Clean dataset (after drop):", df_clean.shape)

    # Save
    import os
    os.makedirs("outputs", exist_ok=True)
    df_clean.to_excel(OUT_FILE, index=False)
    print("\nSaved:", OUT_FILE)

    return df_clean

if __name__ == "__main__":
    build_dataset()
