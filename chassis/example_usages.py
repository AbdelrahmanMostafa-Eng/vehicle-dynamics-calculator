#example_usages.py

"""

Integration demo for chassis modules:
- geometry.py
- suspension.py

"""

import numpy as np
import matplotlib.pyplot as plt
from geometry import ChassisGeometry
from suspension import SuspensionModel

# === Geometry System ===
geometry = ChassisGeometry(track_width=1.6, cg_height=0.35, suspension_arm_angle=10, wheelbase=3.6)
roll_center = geometry.roll_center_height()
anti_dive = geometry.anti_dive_percentage(caster_angle=6)
anti_squat = geometry.anti_squat_percentage(swing_arm_angle=8)

# === Suspension System ===
suspension = SuspensionModel(spring_rate=60000, damping_coeff=4500, unsprung_mass=40, sprung_mass=300)
nat_freq = suspension.natural_frequency()
damp_ratio = suspension.damping_ratio()
load_transfer = suspension.load_transfer(lateral_accel=3.0, cg_height=0.35, track_width=1.6)

# === Print Sample Outputs ===
print("=== Chassis Integration Example ===")
print(f"Roll Center Height → {roll_center:.3f} m")
print(f"Anti-Dive (caster=6°) → {anti_dive:.1f} %")
print(f"Anti-Squat (swing=8°) → {anti_squat:.1f} %")
print(f"Natural Frequency → {nat_freq:.2f} Hz")
print(f"Damping Ratio → {damp_ratio:.3f}")
print(f"Load Transfer at 3g lateral → {load_transfer:.1f} N")

# === Plotting ===
plt.figure(figsize=(12, 6))

# Roll Center vs Suspension Arm Angle
angles = np.linspace(0, 15, 50)
roll_centers = [ChassisGeometry(1.6, 0.35, a, 3.6).roll_center_height() for a in angles]
plt.subplot(1, 2, 1)
plt.plot(angles, roll_centers, color="blue")
plt.xlabel("Suspension Arm Angle (°)")
plt.ylabel("Roll Center Height (m)")
plt.title("Roll Center vs Suspension Arm Angle")

# Load Transfer vs Lateral Acceleration
accel = np.linspace(0, 5, 50)  # g
transfers = [suspension.load_transfer(a, 0.35, 1.6) for a in accel]
plt.subplot(1, 2, 2)
plt.plot(accel, transfers, color="red")
plt.xlabel("Lateral Acceleration (g)")
plt.ylabel("Load Transfer (N)")
plt.title("Suspension Load Transfer vs Lateral Acceleration")

plt.tight_layout()
plt.show()
