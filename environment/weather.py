#weather.py

"""

Module for modeling weather effects on vehicle dynamics.
Includes temperature, humidity, and rain intensity impacts.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class WeatherModel:
    ambient_temp: float   # °C
    humidity: float       # %
    rain_intensity: float # 0–1 scale

    def track_temp(self) -> float:
        """Estimate track temperature (°C)."""
        return self.ambient_temp + 10 * (1 - self.humidity/100)

    def grip_modifier(self) -> float:
        """Return grip modifier based on rain intensity."""
        return max(0.3, 1 - self.rain_intensity)


# Example usage and visualization

if __name__ == "__main__":
    model = WeatherModel(ambient_temp=30, humidity=60, rain_intensity=0.3)
    rain_levels = np.linspace(0, 1, 50)
    grip_mods = [WeatherModel(30, 60, r).grip_modifier() for r in rain_levels]

    print("Weather Example:")
    print(f"Track Temp → {model.track_temp():.1f} °C")
    print(f"Grip Modifier (rain=0.3) → {model.grip_modifier():.2f}")

    plt.plot(rain_levels*100, grip_mods, color="purple")
    plt.xlabel("Rain Intensity (%)")
    plt.ylabel("Grip Modifier")
    plt.title("Grip Modifier vs Rain Intensity")
    plt.show()
