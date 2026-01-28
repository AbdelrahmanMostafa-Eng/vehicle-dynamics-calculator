#plotting.py

"""
Generic plotting utilities
"""

import matplotlib.pyplot as plt

def plot_series(x, y, xlabel: str, ylabel: str, title: str, label: str = None):
    """
    Plot a simple line series.
    """
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker="o", label=label if label else ylabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if label:
        plt.legend()
    plt.grid(True)
    plt.show()


def plot_bar(x, y, xlabel: str, ylabel: str, title: str, label: str = None):
    """
    Plot a simple bar chart.
    """
    plt.figure(figsize=(8, 4))
    plt.bar(x, y, label=label if label else ylabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if label:
        plt.legend()
    plt.show()


# Example usage
if __name__ == "__main__":
    laps = [1, 2, 3, 4, 5]
    times = [81.5, 82.0, 81.8, 82.3, 81.7]

    plot_series(laps, times, xlabel="Lap", ylabel="Time [s]", title="Lap Times", label="Lap time")

    fuel = [2.5, 2.6, 2.4, 2.7, 2.5]
    plot_bar(laps, fuel, xlabel="Lap", ylabel="Fuel [kg]", title="Fuel Usage", label="Fuel used")
