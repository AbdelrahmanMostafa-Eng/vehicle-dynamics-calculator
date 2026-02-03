#example_usages.py

"""

Integration demo for control modules:
- brake_migration.py
- engine_maps.py
- traction_control.py

"""

import numpy as np
import matplotlib.pyplot as plt
from brake_migration import BrakeMigrationModel
from engine_maps import EngineMap
from traction_control import TractionControlModel

# === Brake Migration ===
migration_model = BrakeMigrationModel(base_bias=0.55, migration_rate=0.2)
pressures = np.linspace(0, 1, 50)
biases = [migration_model.bias(p) for p in pressures]

# === Engine Maps ===
engine = EngineMap(max_torque=800, efficiency_peak=11000, fuel_rate_base=0.5)
rpms = np.linspace(8000, 15000, 100)
torques = [engine.torque(r) for r in rpms]
fuel_rates = [engine.fuel_rate(r, throttle=0.8) for r in rpms]

# === Traction Control ===
tc_model = TractionControlModel(slip_threshold=0.12, reduction_gain=3.0)
slip_ratios = np.linspace(0, 0.3, 50)
tc_torques = [tc_model.adjusted_torque(s, 700) for s in slip_ratios]

# === Print Sample Outputs ===
print("=== Control Integration Example ===")
print(f"Rear Bias at 50% pedal → {migration_model.bias(0.5):.2f}")
print(f"Torque at 11000 RPM → {engine.torque(11000):.1f} Nm")
print(f"Fuel Rate at 12000 RPM, 80% throttle → {engine.fuel_rate(12000, 0.8):.2f} g/s")
print(f"Adjusted Torque at slip=0.2 → {tc_model.adjusted_torque(0.2, 700):.1f} Nm")

# === Plotting ===
plt.figure(figsize=(12, 8))

# Brake Migration
plt.subplot(2, 2, 1)
plt.plot(pressures*100, biases, color="blue")
plt.xlabel("Pedal Pressure (%)")
plt.ylabel("Rear Brake Bias Fraction")
plt.title("Brake Migration vs Pedal Pressure")

# Engine Torque
plt.subplot(2, 2, 2)
plt.plot(rpms, torques, label="Torque Curve")
plt.plot(rpms, fuel_rates, label="Fuel Rate (80% throttle)")
plt.xlabel("Engine Speed (RPM)")
plt.ylabel("Torque (Nm) / Fuel Rate (g/s)")
plt.title("Engine Torque & Fuel Map")
plt.legend()

# Traction Control
plt.subplot(2, 2, 3)
plt.plot(slip_ratios*100, tc_torques, color="red")
plt.axvline(tc_model.slip_threshold*100, color="black", linestyle="--", label="Slip Threshold")
plt.xlabel("Slip Ratio (%)")
plt.ylabel("Adjusted Torque (Nm)")
plt.title("Traction Control Torque Reduction")
plt.legend()

plt.tight_layout()
plt.show()
