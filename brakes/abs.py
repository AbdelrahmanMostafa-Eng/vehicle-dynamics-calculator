#abs.py

"""

Module for simulating Anti-Lock Braking System (ABS) behavior in Formula 1.
Models wheel slip ratio and brake modulation to prevent lock-up.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class ABSModel:
    slip_optimal: float   # Optimal slip ratio (~0.15 for racing tires)
    modulation_gain: float  # How aggressively ABS reduces brake force

    def brake_force(self, slip_ratio: float, max_brake_force: float) -> float:
        """Return effective brake force based on slip ratio."""
        if slip_ratio <= self.slip_optimal:
            return max_brake_force
        else:
            reduction = self.modulation_gain * (slip_ratio - self.slip_optimal)
            return max_brake_force * max(0.0, 1 - reduction)


# Example usage and plotting

if __name__ == "__main__":
    abs_model = ABSModel(slip_optimal=0.15, modulation_gain=2.0)
    slip_ratios = np.linspace(0, 0.4, 50)
    forces = [abs_model.brake_force(s, 8000) for s in slip_ratios]

    print("ABS Example:")
    for s in [0.1, 0.2, 0.3]:
        print(f"Slip Ratio {s:.2f} → Brake Force = {abs_model.brake_force(s, 8000):.1f} N")

    plt.plot(slip_ratios*100, forces, label="Brake Force vs Slip Ratio")
    plt.axvline(abs_model.slip_optimal*100, color="red", linestyle="--", label="Optimal Slip")
    plt.xlabel("Slip Ratio (%)")
    plt.ylabel("Brake Force (N)")
    plt.title("ABS Brake Modulation")
    plt.legend()
    plt.show()
