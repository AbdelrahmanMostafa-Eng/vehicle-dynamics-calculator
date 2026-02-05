#example_usages.py

"""

Integration demo for environment modules:
- altitude.py
- track_grip.py
- weather.py

"""

import numpy as np
import matplotlib.pyplot as plt
from altitude import AltitudeModel
from track_grip import TrackGripModel
from weather import WeatherModel

# === Altitude ===
alt_model = AltitudeModel()
altitudes = np.linspace(0, 3000, 50)
densities = [alt_model.air_density(h) for h in altitudes]

# === Track Grip ===
grip_model = TrackGripModel(base_mu=1.4, rubber_gain=0.01, wet_penalty=0.4)
laps = np.arange(0, 50)
grip_dry = [grip_model.grip(l, wet=False) for l in laps]
grip_wet = [grip_model.grip(l, wet=True) for l in laps]

# === Weather ===
weather_model = WeatherModel(ambient_temp=30, humidity=60, rain_intensity=0.3)
rain_levels = np.linspace(0, 1, 50)
grip_mods = [WeatherModel(30, 60, r).grip_modifier() for r in rain_levels]

# === Print Sample Outputs ===
print("=== Environment Integration Example ===")
print(f"Air Density at 1000 m → {alt_model.air_density(1000):.3f} kg/m³")
print(f"Grip after 10 laps (dry) → {grip_model.grip(10, False):.2f}")
print(f"Grip after 10 laps (wet) → {grip_model.grip(10, True):.2f}")
print(f"Track Temp → {weather_model.track_temp():.1f} °C")
print(f"Grip Modifier (rain=0.3) → {weather_model.grip_modifier():.2f}")

# === Plotting ===
plt.figure(figsize=(12, 8))

# Altitude
plt.subplot(2, 2, 1)
plt.plot(altitudes, densities, color="blue")
plt.xlabel("Altitude (m)")
plt.ylabel("Air Density (kg/m³)")
plt.title("Air Density vs Altitude")

# Track Grip
plt.subplot(2, 2, 2)
plt.plot(laps, grip_dry, label="Dry Track")
plt.plot(laps, grip_wet, label="Wet Track", linestyle="--")
plt.xlabel("Laps")
plt.ylabel("Grip Coefficient (μ)")
plt.title("Track Grip Evolution")
plt.legend()

# Weather Grip Modifier
plt.subplot(2, 2, 3)
plt.plot(rain_levels*100, grip_mods, color="purple")
plt.xlabel("Rain Intensity (%)")
plt.ylabel("Grip Modifier")
plt.title("Grip Modifier vs Rain Intensity")

plt.tight_layout()
plt.show()
