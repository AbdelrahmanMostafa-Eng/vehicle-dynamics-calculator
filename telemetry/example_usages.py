#example_usages.py

"""
example_usage_telemetry.py
---------------------------
Integration demo for telemetry modules:
- generator.py
- plots.py
"""

import matplotlib.pyplot as plt
from generator import TelemetryGenerator
from plots import TelemetryPlots

# === Telemetry Generation ===
gen = TelemetryGenerator(lap_time=90.0, max_speed=320)
time, speed, throttle, brake, gear = gen.generate()

# === Print Sample Outputs ===
print("=== Telemetry Integration Example ===")
print(f"Lap Time → {gen.lap_time:.1f} s")
print(f"Max Speed → {max(speed):.1f} km/h")
print(f"Sample Gear Trace → {gear[:10]}")

# === Plotting ===
plt.figure(figsize=(12, 8))

# Speed Trace
plt.subplot(3, 1, 1)
plt.plot(time, speed, color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Speed (km/h)")
plt.title("Speed Trace")

# Driver Inputs
plt.subplot(3, 1, 2)
plt.plot(time, throttle, label="Throttle", color="green")
plt.plot(time, brake, label="Brake", color="red")
plt.xlabel("Time (s)")
plt.ylabel("Input Level")
plt.title("Driver Inputs")
plt.legend()

# Gear Trace
plt.subplot(3, 1, 3)
plt.step(time, gear, where="post", color="purple")
plt.xlabel("Time (s)")
plt.ylabel("Gear")
plt.title("Gear Trace")

plt.tight_layout()
plt.show()
