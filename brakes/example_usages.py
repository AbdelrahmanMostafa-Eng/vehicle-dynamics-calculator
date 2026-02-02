#example_usages.py

"""

Integration demo for braking modules:
- abs.py
- brake_bias.py
- brake_thermal.py

"""

import numpy as np
import matplotlib.pyplot as plt
from abs import ABSModel
from brake_bias import BrakeBiasModel
from brake_thermal import BrakeThermalModel

# ABS
abs_model = ABSModel(slip_optimal=0.15, modulation_gain=2.0)
slip_ratios = np.linspace(0, 0.4, 50)
forces = [abs_model.brake_force(s, 8000) for s in slip_ratios]

# Brake Bias
biases = np.linspace(0.4, 0.7, 50)
total_force = 12000
front_forces = [BrakeBiasModel(b).distribution(total_force)[0] for b in biases]
rear_forces = [BrakeBiasModel(b).distribution(total_force)[1] for b in biases]

# Brake Thermal
thermal_model = BrakeThermalModel(mass=5.0, specific_heat=500, cooling_coeff=0.02, ambient_temp=25)
time = np.linspace(0, 20, 100)
temps = []
temp = 200
for t in time:
    brake_power = 30000 if 5 < t < 7 else 0
    temp = thermal_model.temp_change(brake_power, 0.2, temp)
    temps.append(temp)

# Print sample outputs
print("=== Brakes Integration Example ===")
print(f"ABS Force at slip=0.2 → {abs_model.brake_force(0.2, 8000):.1f} N")
print(f"Brake Bias 0.6 → Front={BrakeBiasModel(0.6).distribution(total_force)[0]:.1f} N, Rear={BrakeBiasModel(0.6).distribution(total_force)[1]:.1f} N")
print(f"Final Brake Temp after 20s → {temps[-1]:.1f} °C")

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(slip_ratios*100, forces, label="ABS Force")
plt.axvline(abs_model.slip_optimal*100, color="red", linestyle="--", label="Optimal Slip")
plt.xlabel("Slip Ratio (%)")
plt.ylabel("Brake Force (N)")
plt.title("ABS Modulation")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(biases*100, front_forces, label="Front Force")
plt.plot(biases*100, rear_forces, label="Rear Force")
plt.xlabel("Brake Bias (% Front)")
plt.ylabel("Brake Force (N)")
plt.title("Brake Bias Distribution")
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(time, temps, color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Brake Temp (°C)")
plt.title("Brake Thermal Behavior")

plt.tight_layout()
plt.show()
