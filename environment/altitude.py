#altitude.py

"""

Module for modeling the effect of altitude on air density and vehicle performance.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class AltitudeModel:
    temp0: float = 288.15   # Sea-level standard temperature (K)
    pressure0: float = 101325  # Sea-level pressure (Pa)
    lapse_rate: float = 0.0065 # Temperature lapse rate (K/m)
    R: float = 287.05       # Specific gas constant for dry air (J/kg*K)
    g: float = 9.81         # Gravity (m/s²)

    def air_density(self, altitude: float) -> float:
        """Return air density (kg/m³) at given altitude (m)."""
        temp = self.temp0 - self.lapse_rate * altitude
        pressure = self.pressure0 * (temp / self.temp0) ** (self.g / (self.R * self.lapse_rate))
        return pressure / (self.R * temp)


# Example usage and plotting

if __name__ == "__main__":
    model = AltitudeModel()
    altitudes = np.linspace(0, 3000, 50)
    densities = [model.air_density(h) for h in altitudes]

    print("Altitude Example:")
    for h in [0, 1000, 2000]:
        print(f"Altitude {h} m → Air Density = {model.air_density(h):.3f} kg/m³")

    plt.plot(altitudes, densities, color="blue")
    plt.xlabel("Altitude (m)")
    plt.ylabel("Air Density (kg/m³)")
    plt.title("Air Density vs Altitude")
    plt.show()
