import matplotlib.pyplot as plt

def parity_plot(y_true, y_pred, label):
    plt.scatter(y_true, y_pred, alpha=0.5)
    plt.plot([min(y_true), max(y_true)],
             [min(y_true), max(y_true)], 'k--')
    plt.xlabel("CFD")
    plt.ylabel("ML")
    plt.title(label)
    plt.show()
