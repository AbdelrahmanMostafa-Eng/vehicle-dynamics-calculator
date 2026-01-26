#plots.py

"""
Telemetry visualization with matplotlib
"""

import matplotlib.pyplot as plt

def plot_lap_times(telemetry: list):
    """
    Plot lap times across laps.
    """
    laps = [d["lap"] for d in telemetry]
    times = [d["lap_time"] for d in telemetry]

    plt.figure(figsize=(8, 4))
    plt.plot(laps, times, marker="o", label="Lap time [s]")
    plt.xlabel("Lap")
    plt.ylabel("Time [s]")
    plt.title("Lap Times")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_fuel_usage(telemetry: list):
    """
    Plot fuel usage per lap.
    """
    laps = [d["lap"] for d in telemetry]
    fuel = [d["fuel_used"] for d in telemetry]

    plt.figure(figsize=(8, 4))
    plt.bar(laps, fuel, label="Fuel used [kg]")
    plt.xlabel("Lap")
    plt.ylabel("Fuel [kg]")
    plt.title("Fuel Usage per Lap")
    plt.legend()
    plt.show()


def plot_tire_wear(telemetry: list):
    """
    Plot tire wear progression.
    """
    laps = [d["lap"] for d in telemetry]
    wear = [d["tire_wear"] for d in telemetry]

    plt.figure(figsize=(8, 4))
    plt.plot(laps, wear, marker="x", color="red", label="Tire wear [-]")
    plt.xlabel("Lap")
    plt.ylabel("Wear")
    plt.title("Tire Wear Progression")
    plt.legend()
    plt.grid(True)
    plt.show()


# Example usage
if __name__ == "__main__":
    from generator import generate_lap_data
    telemetry = generate_lap_data(10, lap_distance=5300)

    plot_lap_times(telemetry)
    plot_fuel_usage(telemetry)
    plot_tire_wear(telemetry)
