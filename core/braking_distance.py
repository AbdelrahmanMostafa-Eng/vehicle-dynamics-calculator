# braking_distance.py

"""

Module for calculating braking distance in Formula 1.
Uses deceleration from braking force and vehicle mass.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class BrakingDistanceModel:
    mass: float        # kg
    mu: float          # friction coefficient
    g: float = 9.81    # gravity (m/s²)

    def braking_distance(self, v0: float) -> float:
        """Calculate braking distance from initial speed v0 (m/s)."""
        decel = self.mu * self.g
        return (v0**2) / (2 * decel)


# Example usage and plotting

if __name__ == "__main__":
    model = BrakingDistanceModel(mass=800, mu=1.6)
    speeds = np.linspace(50, 300, 50)  # km/h
    speeds_ms = speeds / 3.6
    distances = [model.braking_distance(v) for v in speeds_ms]

    print("Braking Distance Example:")
    for v in [100, 200, 300]:
        print(f"Speed {v} km/h → Distance = {model.braking_distance(v/3.6):.1f} m")

    plt.plot(speeds, distances, color="blue")
    plt.xlabel("Initial Speed (km/h)")
    plt.ylabel("Braking Distance (m)")
    plt.title("Braking Distance vs Speed")
    plt.show()
