#example_usages.py

"""

Integration demo for powertrain modules:
- drivetrain.py
- engine.py
- ers.py

"""

import numpy as np
import matplotlib.pyplot as plt
from drivetrain import DrivetrainModel
from engine import EngineModel
from ers import ERSModel

# === Engine ===
engine = EngineModel(max_power=750, max_rpm=15000, torque_peak=800)
rpms = np.linspace(5000, 15000, 100)
torques = [engine.torque_curve(r) for r in rpms]
powers = [engine.power_curve(r) for r in rpms]

# === Drivetrain ===
drivetrain = DrivetrainModel(gear_ratios=[3.5, 2.2, 1.6, 1.2, 1.0], final_drive=3.0, efficiency=0.9)
engine_torque = 700
gears = range(1, 6)
wheel_torques = [drivetrain.wheel_torque(engine_torque, g) for g in gears]

# === ERS ===
ers = ERSModel(capacity=4000, efficiency=0.7, deploy_rate=120)
braking_events = np.linspace(0, 6000, 50)
harvested = [ers.harvest(e) for e in braking_events]

times = np.linspace(0, 40, 50)
deployed = [ers.deploy(t) for t in times]

# === Print Sample Outputs ===
print("=== Powertrain Integration Example ===")
print(f"Torque at 8000 RPM → {engine.torque_curve(8000):.1f} Nm")
print(f"Power at 12000 RPM → {engine.power_curve(12000):.1f} kW")
print(f"Wheel Torque in Gear 3 → {drivetrain.wheel_torque(engine_torque, 3):.1f} Nm")
print(f"ERS Harvest from 3000 kJ braking → {ers.harvest(3000):.1f} kJ")
print(f"ERS Deploy over 20s → {ers.deploy(20):.1f} kJ")

# === Plotting ===
plt.figure(figsize=(12, 10))

# Engine Torque & Power
plt.subplot(2, 2, 1)
plt.plot(rpms, torques, label="Torque Curve")
plt.plot(rpms, powers, label="Power Curve")
plt.xlabel("Engine Speed (RPM)")
plt.ylabel("Torque (Nm) / Power (kW)")
plt.title("Engine Torque & Power Curve")
plt.legend()

# Drivetrain Wheel Torque
plt.subplot(2, 2, 2)
plt.bar(gears, wheel_torques, color="blue")
plt.xlabel("Gear")
plt.ylabel("Wheel Torque (Nm)")
plt.title("Wheel Torque vs Gear")

# ERS Harvesting
plt.subplot(2, 2, 3)
plt.plot(braking_events, harvested, color="green")
plt.xlabel("Braking Energy (kJ)")
plt.ylabel("Harvested Energy (kJ)")
plt.title("ERS Harvesting")

# ERS Deployment
plt.subplot(2, 2, 4)
plt.plot(times, deployed, color="orange")
plt.xlabel("Deployment Duration (s)")
plt.ylabel("Deployed Energy (kJ)")
plt.title("ERS Deployment")

plt.tight_layout()
plt.show()
