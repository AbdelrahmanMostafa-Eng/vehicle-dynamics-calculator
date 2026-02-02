#suspension.py

"""

Module for modeling suspension dynamics in Formula 1.
Includes spring stiffness, damping ratio, and wheel load transfer.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class SuspensionModel:
    spring_rate: float     # N/m
    damping_coeff: float   # Ns/m
    unsprung_mass: float   # kg
    sprung_mass: float     # kg

    def natural_frequency(self) -> float:
        """Calculate suspension natural frequency (Hz)."""
        return np.sqrt(self.spring_rate / self.sprung_mass) / (2 * np.pi)

    def damping_ratio(self) -> float:
        """Calculate damping ratio (dimensionless)."""
        critical_damping = 2 * np.sqrt(self.spring_rate * self.sprung_mass)
        return self.damping_coeff / critical_damping

    def load_transfer(self, lateral_accel: float, cg_height: float, track_width: float) -> float:
        """Calculate lateral load transfer (N)."""
        return (lateral_accel * self.sprung_mass * 9.81 * cg_height) / track_width

# Example usage

if __name__ == "__main__":
    suspension = SuspensionModel(spring_rate=60000, damping_coeff=4500, unsprung_mass=40, sprung_mass=300)

    print("Suspension Example:")
    print(f"Natural Frequency → {suspension.natural_frequency():.2f} Hz")
    print(f"Damping Ratio → {suspension.damping_ratio():.3f}")
    print(f"Load Transfer at 3g lateral → {suspension.load_transfer(3.0, 0.35, 1.6):.1f} N")

    accel = np.linspace(0, 5, 50)  # g
    transfers = [suspension.load_transfer(a, 0.35, 1.6) for a in accel]

    plt.plot(accel, transfers, color="red")
    plt.xlabel("Lateral Acceleration (g)")
    plt.ylabel("Load Transfer (N)")
    plt.title("Suspension Load Transfer vs Lateral Acceleration")
    plt.show()
