#brake_thermal.py

"""

Module for modeling brake thermal behavior in Formula 1.
Captures heat generation from braking and cooling over time.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class BrakeThermalModel:
    mass: float          # Brake disc mass (kg)
    specific_heat: float # J/(kg*K)
    cooling_coeff: float # Cooling rate constant
    ambient_temp: float  # Ambient temperature (°C)

    def temp_change(self, brake_power: float, duration: float, temp_current: float) -> float:
        """Calculate new brake temperature after braking event."""
        heat_in = brake_power * duration
        delta_temp = heat_in / (self.mass * self.specific_heat)
        temp_new = temp_current + delta_temp
        # Apply cooling
        temp_new -= self.cooling_coeff * (temp_new - self.ambient_temp) * duration
        return temp_new


# Example usage and plotting

if __name__ == "__main__":
    model = BrakeThermalModel(mass=5.0, specific_heat=500, cooling_coeff=0.02, ambient_temp=25)
    time = np.linspace(0, 20, 100)  # seconds
    temps = []
    temp = 200  # initial brake temp (°C)

    for t in time:
        brake_power = 30000 if 5 < t < 7 else 0  # simulate braking event
        temp = model.temp_change(brake_power, 0.2, temp)
        temps.append(temp)

    print("Brake Thermal Example:")
    print(f"Final Brake Temperature after 20s → {temps[-1]:.1f} °C")

    plt.plot(time, temps, color="orange")
    plt.xlabel("Time (s)")
    plt.ylabel("Brake Temperature (°C)")
    plt.title("Brake Thermal Behavior")
    plt.show()
