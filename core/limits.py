#limits.py

"""

Module for calculating performance limits in Formula 1.
Includes combined grip circle (friction ellipse) for braking and cornering.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class GripCircleModel:
    mu: float    # friction coefficient
    mass: float  # kg

    def limit_curve(self, n_points: int = 100):
        """Return arrays of longitudinal vs lateral acceleration limits."""
        accel_long = np.linspace(-self.mu*9.81, self.mu*9.81, n_points)
        accel_lat = np.sqrt((self.mu*9.81)**2 - accel_long**2)
        return accel_long, accel_lat


# Example usage and plotting

if __name__ == "__main__":
    model = GripCircleModel(mu=1.6, mass=800)
    accel_long, accel_lat = model.limit_curve()

    print("Grip Circle Example:")
    print(f"Max Longitudinal Accel → {max(accel_long):.2f} m/s²")
    print(f"Max Lateral Accel → {max(accel_lat):.2f} m/s²")

    plt.plot(accel_long, accel_lat, label="Grip Circle")
    plt.plot(accel_long, -accel_lat, label="Grip Circle (negative)")
    plt.xlabel("Longitudinal Acceleration (m/s²)")
    plt.ylabel("Lateral Acceleration (m/s²)")
    plt.title("Friction Ellipse (Grip Circle)")
    plt.legend()
    plt.axis("equal")
    plt.show()
