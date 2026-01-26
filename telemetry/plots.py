#plots.py

"""
Standalone telemetry visualization
"""

import random
import matplotlib.pyplot as plt

# ---------------- Telemetry generator ----------------
def generate_lap_data(laps: int, lap_distance: float) -> list:
    """
    Generate synthetic telemetry data for multiple laps.
    """
    data = []
    for lap in range(1, laps + 1):
        avg_speed = random.uniform(60, 70)  # m/s
        lap_time = lap_distance / avg_speed
        fuel_used = random.uniform(2.3, 2.7)  # kg
        tire_wear = random.uniform(0.01, 0.03) * lap

        data.append({
            "lap": lap,
            "avg_speed": avg_speed,
            "lap_time": lap_time,
            "fuel_used": fuel_used,
            "tire_wear": tire_wear
        })
    return data


# ---------------- Plot functions ----------------
def plot_lap_times(telemetry: list):
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


# ---------------- Example run ----------------
if __name__ == "__main__":
    telemetry = generate_lap_data(10, lap_distance=5300)

    plot_lap_times(telemetry)
    plot_fuel_usage(telemetry)
    plot_tire_wear(telemetry)
