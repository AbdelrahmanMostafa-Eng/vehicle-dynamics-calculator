# tire_dynamics.py

"""

Module for modeling tire forces in Formula 1.
Includes lateral and longitudinal force generation.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class TireDynamicsModel:
    cornering_stiffness: float  # N/rad
    friction_coeff: float       # μ
    load: float                 # N

    def lateral_force(self, slip_angle: float) -> float:
        """Return lateral force (N) at given slip angle (rad)."""
        return min(self.cornering_stiffness * slip_angle, self.friction_coeff * self.load)

    def longitudinal_force(self, slip_ratio: float) -> float:
        """Return longitudinal force (N) at given slip ratio."""
        return min(self.friction_coeff * self.load * slip_ratio, self.friction_coeff * self.load)


# Example usage and plotting

if __name__ == "__main__":
    model = TireDynamicsModel(cornering_stiffness=80000, friction_coeff=1.7, load=3000)
    angles = np.linspace(0, 0.2, 50)
    forces_lat = [model.lateral_force(a) for a in angles]

    slips = np.linspace(0, 0.3, 50)
    forces_long = [model.longitudinal_force(s) for s in slips]

    print("Tire Dynamics Example:")
    print(f"Lateral Force at 0.1 rad → {model.lateral_force(0.1):.1f} N")
    print(f"Longitudinal Force at 0.2 slip → {model.longitudinal_force(0.2):.1f} N")

    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.plot(angles, forces_lat, color="red")
    plt.xlabel("Slip Angle (rad)")
    plt.ylabel("Lateral Force (N)")
    plt.title("Lateral Force vs Slip Angle")

    plt.subplot(1,2,2)
    plt.plot(slips, forces_long, color="green")
    plt.xlabel("Slip Ratio")
    plt.ylabel("Longitudinal Force (N)")
    plt.title("Longitudinal Force vs Slip Ratio")

    plt.tight_layout()
    plt.show()
