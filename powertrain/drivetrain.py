#drivetrain.py

"""

Module for modeling drivetrain efficiency and wheel torque in Formula 1.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class DrivetrainModel:
    gear_ratios: list       # list of gear ratios
    final_drive: float      # final drive ratio
    efficiency: float       # drivetrain efficiency (0–1)

    def wheel_torque(self, engine_torque: float, gear: int) -> float:
        """Return wheel torque (Nm) for given gear."""
        ratio = self.gear_ratios[gear-1] * self.final_drive
        return engine_torque * ratio * self.efficiency


# Example usage and visualization

if __name__ == "__main__":
    drivetrain = DrivetrainModel(gear_ratios=[3.5, 2.2, 1.6, 1.2, 1.0], final_drive=3.0, efficiency=0.9)
    engine_torque = 700
    gears = range(1, 6)
    torques = [drivetrain.wheel_torque(engine_torque, g) for g in gears]

    print("Drivetrain Example:")
    for g in gears:
        print(f"Gear {g} → Wheel Torque = {drivetrain.wheel_torque(engine_torque, g):.1f} Nm")

    plt.bar(gears, torques, color="blue")
    plt.xlabel("Gear")
    plt.ylabel("Wheel Torque (Nm)")
    plt.title("Wheel Torque vs Gear")
    plt.show()
