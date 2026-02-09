#example_usages.py

"""

Integration demo for tire modules:
- tire_degradation.py
- tire_dynamics.py
- tire_heat.py

"""

import numpy as np
import matplotlib.pyplot as plt
from tire_degradation import TireDegradationModel
from tire_dynamics import TireDynamicsModel
from tire_heat import TireHeatModel

# === Tire Degradation ===
deg_model = TireDegradationModel(base_mu=1.8, wear_rate=0.02)
laps = np.arange(1, 50)
grip_values = [deg_model.grip(l) for l in laps]

# === Tire Dynamics ===
dyn_model = TireDynamicsModel(cornering_stiffness=80000, friction_coeff=1.7, load=3000)
angles = np.linspace(0, 0.2, 50)
forces_lat = [dyn_model.lateral_force(a) for a in angles]
slips = np.linspace(0, 0.3, 50)
forces_long = [dyn_model.longitudinal_force(s) for s in slips]

# === Tire Heat ===
heat_model = TireHeatModel(mass=20, specific_heat=1800, cooling_coeff=0.02, ambient_temp=25)
time = np.linspace(0, 60, 100)
temps = []
temp = 80
for t in time:
    friction_power = 5000 if 10 < t < 30 else 0
    temp = heat_model.temp_change(friction_power, 0.6, temp)
    temps.append(temp)

# === Print Sample Outputs ===
print("=== Tires Integration Example ===")
print(f"Grip at Lap 10 → {deg_model.grip(10):.2f}")
print(f"Lateral Force at 0.1 rad → {dyn_model.lateral_force(0.1):.1f} N")
print(f"Longitudinal Force at 0.2 slip → {dyn_model.longitudinal_force(0.2):.1f} N")
print(f"Final Temp after 60s → {temps[-1]:.1f} °C")

# === Plotting ===
plt.figure(figsize=(12, 10))

# Tire Degradation
plt.subplot(2, 2, 1)
plt.plot(laps, grip_values, color="blue")
plt.xlabel("Lap Number")
plt.ylabel("Grip Coefficient (μ)")
plt.title("Tire Grip vs Laps")

# Tire Dynamics - Lateral Force
plt.subplot(2, 2, 2)
plt.plot(angles, forces_lat, color="red")
plt.xlabel("Slip Angle (rad)")
plt.ylabel("Lateral Force (N)")
plt.title("Lateral Force vs Slip Angle")

# Tire Dynamics - Longitudinal Force
plt.subplot(2, 2, 3)
plt.plot(slips, forces_long, color="green")
plt.xlabel("Slip Ratio")
plt.ylabel("Longitudinal Force (N)")
plt.title("Longitudinal Force vs Slip Ratio")

# Tire Heat
plt.subplot(2, 2, 4)
plt.plot(time, temps, color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Tire Temperature (°C)")
plt.title("Tire Temperature Evolution")

plt.tight_layout()
plt.show()
