#brake_migration.py

"""

Module for modeling brake migration in Formula 1.
Brake migration shifts braking force from rear to front as pedal pressure increases.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class BrakeMigrationModel:
    base_bias: float       # initial rear bias fraction
    migration_rate: float  # rate of migration per unit pedal pressure

    def bias(self, pedal_pressure: float) -> float:
        """Return rear brake bias fraction at given pedal pressure (0–1)."""
        return max(0.0, self.base_bias - self.migration_rate * pedal_pressure)


# Example usage and plotting

if __name__ == "__main__":
    model = BrakeMigrationModel(base_bias=0.55, migration_rate=0.2)
    pressures = np.linspace(0, 1, 50)
    biases = [model.bias(p) for p in pressures]

    print("Brake Migration Example:")
    for p in [0.2, 0.5, 0.8]:
        print(f"Pedal Pressure {p:.1f} → Rear Bias = {model.bias(p):.2f}")

    plt.plot(pressures*100, biases, color="blue")
    plt.xlabel("Pedal Pressure (%)")
    plt.ylabel("Rear Brake Bias Fraction")
    plt.title("Brake Migration vs Pedal Pressure")
    plt.show()
