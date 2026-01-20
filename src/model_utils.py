from sklearn.ensemble import RandomForestRegressor

def build_rf_model(params=None):
    """Create Random Forest model with default parameters."""
    return RandomForestRegressor(
        n_estimators=300,
        random_state=42
    )
