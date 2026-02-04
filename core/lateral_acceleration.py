# lateral_acceleration.py

"""

Module for calculating maximum lateral acceleration in Formula 1.
Uses tire friction and downforce contribution.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class LateralAccelerationModel:
    mu: float          # tire-road friction coefficient
    mass: float        # kg
    downforce: float   # N

    def max_lat_accel(self) -> float:
        """Return maximum lateral acceleration (m/s²)."""
        normal_force = self.mass * 9.81 + self.downforce
        return (self.mu * normal_force) / self.mass


# Example usage and plotting

if __name__ == "__main__":
    model = LateralAccelerationModel(mu=1.8, mass=800, downforce=15000)
    downforces = np.linspace(0, 40000, 50)
    accels = [LateralAccelerationModel(1.8, 800, df).max_lat_accel()/9.81 for df in downforces]

    print("Lateral Acceleration Example:")
    print(f"Max Lateral Accel with 15kN downforce → {model.max_lat_accel()/9.81:.2f} g")

    plt.plot(downforces/1000, accels, color="red")
    plt.xlabel("Downforce (kN)")
    plt.ylabel("Max Lateral Acceleration (g)")
    plt.title("Lateral Acceleration vs Downforce")
    plt.show()
