#ground_effect.py

"""

Module for modeling ground effect in Formula 1.
Captures ride height sensitivity, rake effects, and diffuser stall behavior.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class GroundEffectModel:
    base_cl: float
    decay_rate: float
    rake_sensitivity: float
    stall_threshold: float

    def cl(self, ride_height: float, rake_deg: float) -> float:
        """Calculate lift coefficient based on ride height and rake angle."""
        if ride_height > self.stall_threshold:
            return 0.0  # diffuser stalls
        decay = np.exp(-self.decay_rate * ride_height)
        rake_effect = self.rake_sensitivity * rake_deg
        return self.base_cl * decay + rake_effect


# Example usage

if __name__ == "__main__":
    model = GroundEffectModel(base_cl=4.0, decay_rate=15, rake_sensitivity=0.02, stall_threshold=0.05)

    ride_heights = np.linspace(0.01, 0.1, 50)  # meters
    cl_values = [model.cl(h, rake_deg=2.0) for h in ride_heights]

    # Print default outputs
    print("Ground Effect Example:")
    for h in [0.01, 0.03, 0.05, 0.08]:
        print(f"Ride Height {h*1000:.0f} mm → Cl = {model.cl(h, rake_deg=2.0):.3f}")

    # Plot
    plt.plot(ride_heights*1000, cl_values, color="green")
    plt.xlabel("Ride Height (mm)")
    plt.ylabel("Lift Coefficient (Cl)")
    plt.title("Ground Effect Cl vs Ride Height")
    plt.show()
