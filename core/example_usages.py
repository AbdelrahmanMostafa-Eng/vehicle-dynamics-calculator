#example_usages.py

"""

Integration demo for core modules:
- braking_distance.py
- lateral_acceleration.py
- limits.py
- weight_transfer.py

"""

import numpy as np
import matplotlib.pyplot as plt
from braking_distance import BrakingDistanceModel
from lateral_acceleration import LateralAccelerationModel
from limits import GripCircleModel
from weight_transfer import WeightTransferModel

# === Braking Distance ===
brake_model = BrakingDistanceModel(mass=800, mu=1.6)
speeds = np.linspace(50, 300, 50)  # km/h
speeds_ms = speeds / 3.6
distances = [brake_model.braking_distance(v) for v in speeds_ms]

# === Lateral Acceleration ===
lat_model = LateralAccelerationModel(mu=1.8, mass=800, downforce=15000)
downforces = np.linspace(0, 40000, 50)
accels = [LateralAccelerationModel(1.8, 800, df).max_lat_accel()/9.81 for df in downforces]

# === Grip Circle ===
grip_model = GripCircleModel(mu=1.6, mass=800)
accel_long, accel_lat = grip_model.limit_curve()

# === Weight Transfer ===
wt_model = WeightTransferModel(mass=800, cg_height=0.35, wheelbase=3.6, track_width=1.6)
accels_long = np.linspace(-10, 10, 50)
transfers_long = [wt_model.longitudinal_transfer(a) for a in accels_long]
accels_lat = np.linspace(0, 15, 50)
transfers_lat = [wt_model.lateral_transfer(a) for a in accels_lat]

# === Print Sample Outputs ===
print("=== Core Integration Example ===")
print(f"Braking Distance at 200 km/h → {brake_model.braking_distance(200/3.6):.1f} m")
print(f"Max Lateral Accel with 15kN downforce → {lat_model.max_lat_accel()/9.81:.2f} g")
print(f"Grip Circle Max Longitudinal Accel → {max(accel_long):.2f} m/s²")
print(f"Grip Circle Max Lateral Accel → {max(accel_lat):.2f} m/s²")
print(f"Longitudinal Transfer at 5 m/s² → {wt_model.longitudinal_transfer(5):.1f} N")
print(f"Lateral Transfer at 10 m/s² → {wt_model.lateral_transfer(10):.1f} N")

# === Plotting ===
plt.figure(figsize=(12, 10))

# Braking Distance
plt.subplot(2, 2, 1)
plt.plot(speeds, distances, color="blue")
plt.xlabel("Initial Speed (km/h)")
plt.ylabel("Braking Distance (m)")
plt.title("Braking Distance vs Speed")

# Lateral Acceleration
plt.subplot(2, 2, 2)
plt.plot(downforces/1000, accels, color="red")
plt.xlabel("Downforce (kN)")
plt.ylabel("Max Lateral Acceleration (g)")
plt.title("Lateral Acceleration vs Downforce")

# Grip Circle
plt.subplot(2, 2, 3)
plt.plot(accel_long, accel_lat, label="Grip Circle")
plt.plot(accel_long, -accel_lat, label="Grip Circle (negative)")
plt.xlabel("Longitudinal Acceleration (m/s²)")
plt.ylabel("Lateral Acceleration (m/s²)")
plt.title("Friction Ellipse (Grip Circle)")
plt.legend()
plt.axis("equal")

# Weight Transfer
plt.subplot(2, 2, 4)
plt.plot(accels_long, transfers_long, label="Longitudinal Transfer", color="green")
plt.plot(accels_lat, transfers_lat, label="Lateral Transfer", color="orange")
plt.xlabel("Acceleration (m/s²)")
plt.ylabel("Weight Transfer (N)")
plt.title("Weight Transfer")
plt.legend()

plt.tight_layout()
plt.show()
