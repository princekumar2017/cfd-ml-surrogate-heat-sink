import numpy as np
import matplotlib.pyplot as plt

def parity_plot(y_true, y_pred, title, filename):
    y_true = np.asarray(y_true).ravel()
    y_pred = np.asarray(y_pred).ravel()

    plt.figure()
    plt.scatter(y_true, y_pred, s=12)
    y_min = float(min(y_true.min(), y_pred.min()))
    y_max = float(max(y_true.max(), y_pred.max()))
    plt.plot([y_min, y_max], [y_min, y_max])
    plt.xlabel("True")
    plt.ylabel("Predicted")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print("Saved:", filename)

def residual_hist(y_true, y_pred, title, filename, bins=40):
    y_true = np.asarray(y_true).ravel()
    y_pred = np.asarray(y_pred).ravel()
    resid = y_pred - y_true

    plt.figure()
    plt.hist(resid, bins=bins)
    plt.xlabel("Residual (Pred - True)")
    plt.ylabel("Count")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print("Saved:", filename)

