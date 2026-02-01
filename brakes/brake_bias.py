#brake_bias.py

"""

Module for calculating brake bias distribution in Formula 1.
Models front/rear brake force split and its effect on stability.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class BrakeBiasModel:
    bias_front: float  # Fraction of braking force on front axle (0–1)

    def distribution(self, total_force: float) -> tuple:
        """Return front and rear brake forces."""
        f_front = total_force * self.bias_front
        f_rear = total_force * (1 - self.bias_front)
        return f_front, f_rear


# Example usage

if __name__ == "__main__":
    model = BrakeBiasModel(bias_front=0.58)
    total_force = 12000  # N
    biases = np.linspace(0.4, 0.7, 50)
    front_forces = [BrakeBiasModel(b).distribution(total_force)[0] for b in biases]
    rear_forces = [BrakeBiasModel(b).distribution(total_force)[1] for b in biases]

    print("Brake Bias Example:")
    for b in [0.5, 0.6]:
        f_front, f_rear = BrakeBiasModel(b).distribution(total_force)
        print(f"Bias {b:.2f} → Front = {f_front:.1f} N, Rear = {f_rear:.1f} N")

    plt.plot(biases*100, front_forces, label="Front Brake Force")
    plt.plot(biases*100, rear_forces, label="Rear Brake Force")
    plt.xlabel("Brake Bias (%) Front")
    plt.ylabel("Brake Force (N)")
    plt.title("Brake Bias Distribution")
    plt.legend()
    plt.show()
