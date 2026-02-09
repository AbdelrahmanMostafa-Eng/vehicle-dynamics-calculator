#tire_heat.py

"""

Module for modeling tire heat buildup in Formula 1.
Includes heating from friction and cooling effects.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class TireHeatModel:
    mass: float           # kg
    specific_heat: float  # J/(kg*K)
    cooling_coeff: float  # cooling rate
    ambient_temp: float   # °C

    def temp_change(self, friction_power: float, duration: float, temp: float) -> float:
        """Return new tire temperature after given duration (s)."""
        heat_gain = (friction_power * duration) / (self.mass * self.specific_heat)
        cooling = self.cooling_coeff * (temp - self.ambient_temp) * duration
        return temp + heat_gain - cooling


# Example usage and plotting

if __name__ == "__main__":
    model = TireHeatModel(mass=20, specific_heat=1800, cooling_coeff=0.02, ambient_temp=25)
    time = np.linspace(0, 60, 100)
    temps = []
    temp = 80
    for t in time:
        friction_power = 5000 if 10 < t < 30 else 0
        temp = model.temp_change(friction_power, 0.6, temp)
        temps.append(temp)

    print("Tire Heat Example:")
    print(f"Final Temp after 60s → {temps[-1]:.1f} °C")

    plt.plot(time, temps, color="orange")
    plt.xlabel("Time (s)")
    plt.ylabel("Tire Temperature (°C)")
    plt.title("Tire Temperature Evolution")
    plt.show()
