#example_usages.py

"""

Integration demo for aerodynamic modules:
- downforce.py
- drag.py
- ground_effect.py
- lift_balance.py

"""

import numpy as np
import matplotlib.pyplot as plt
from downforce import WingElement
from drag import DragModel
from ground_effect import GroundEffectModel
from lift_balance import AeroBalanceModel

rho = 1.225
velocities = np.linspace(50, 350, 50)  # km/h
velocities_ms = velocities / 3.6

# Downforce
front_wing = WingElement(area=1.5, base_cl=2.0, aoa_sensitivity=0.05, drs_effect=0.25)
rear_wing = WingElement(area=2.0, base_cl=2.5, aoa_sensitivity=0.04, drs_effect=0.35)
df_front = [front_wing.downforce(v, aoa_deg=5, rho=rho, drs_active=False) for v in velocities_ms]
df_rear_drs = [rear_wing.downforce(v, aoa_deg=10, rho=rho, drs_active=True) for v in velocities_ms]

# Drag
drag_model = DragModel(frontal_area=1.6, cd_base=0.9, cl_total=3.5, aspect_ratio=5.0, cooling_drag=50)
drag_forces = [drag_model.drag_force(v, rho) for v in velocities_ms]

# Ground Effect
ground_effect = GroundEffectModel(base_cl=4.0, decay_rate=15, rake_sensitivity=0.02, stall_threshold=0.05)
ride_heights = np.linspace(0.01, 0.1, 20)
cl_ground = [ground_effect.cl(h, rake_deg=2.0) for h in ride_heights]

# Lift Balance
aero_balance = AeroBalanceModel(front_cl=2.0, rear_cl=2.5, front_area=1.5, rear_area=2.0, wheelbase=3.6)
cop_positions = [aero_balance.center_of_pressure(v, rho) for v in velocities_ms]

# Print sample outputs
print("=== Aero Integration Example ===")
print(f"Front Wing Downforce at 200 km/h → {front_wing.downforce(200/3.6, 5, rho):.1f} N")
print(f"Rear Wing Downforce with DRS at 300 km/h → {rear_wing.downforce(300/3.6, 10, rho, True):.1f} N")
print(f"Drag Force at 250 km/h → {drag_model.drag_force(250/3.6, rho):.1f} N")
print(f"Cl at 30 mm ride height → {ground_effect.cl(0.03, 2.0):.3f}")
print(f"CoP at 300 km/h → {aero_balance.center_of_pressure(300/3.6, rho):.2f} m")

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(velocities, df_front, label="Front Wing")
plt.plot(velocities, df_rear_drs, label="Rear Wing (DRS)")
plt.xlabel("Velocity (km/h)")
plt.ylabel("Downforce (N)")
plt.title("Downforce vs Speed")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(velocities, drag_forces, color="red")
plt.xlabel("Velocity (km/h)")
plt.ylabel("Drag Force (N)")
plt.title("Drag vs Speed")

plt.subplot(2, 2, 3)
plt.plot(ride_heights*1000, cl_ground, color="green")
plt.xlabel("Ride Height (mm)")
plt.ylabel("Cl")
plt.title("Ground Effect vs Ride Height")

plt.subplot(2, 2, 4)
plt.plot(velocities, cop_positions, color="purple")
plt.xlabel("Velocity (km/h)")
plt.ylabel("CoP (m from front axle)")
plt.title("Center of Pressure vs Speed")

plt.tight_layout()
plt.show()
