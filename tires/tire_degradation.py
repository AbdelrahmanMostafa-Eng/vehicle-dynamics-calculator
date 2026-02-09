#tire_degradation.py

"""

Module for modeling tire degradation in Formula 1.
Includes wear progression and its effect on grip.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class TireDegradationModel:
    base_mu: float       # initial friction coefficient
    wear_rate: float     # degradation per lap

    def grip(self, lap: int) -> float:
        """Return grip coefficient at given lap."""
        return max(0.5, self.base_mu - self.wear_rate * lap)


# Example usage and plotting

if __name__ == "__main__":
    model = TireDegradationModel(base_mu=1.8, wear_rate=0.02)
    laps = np.arange(1, 50)
    grip_values = [model.grip(l) for l in laps]

    print("Tire Degradation Example:")
    print(f"Grip at Lap 10 → {model.grip(10):.2f}")
    print(f"Grip at Lap 30 → {model.grip(30):.2f}")

    plt.plot(laps, grip_values, color="blue")
    plt.xlabel("Lap Number")
    plt.ylabel("Grip Coefficient (μ)")
    plt.title("Tire Grip vs Laps")
    plt.show()
