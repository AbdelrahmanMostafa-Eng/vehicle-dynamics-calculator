#example_usages.py

"""

Integration demo for simulation modules:
- lap_simulation.py
- stint.py
- strategy.py

"""

import numpy as np
import matplotlib.pyplot as plt
from lap_simulation import LapSimulation
from stint import StintSimulation
from strategy import RaceStrategy

# === Lap Simulation ===
lap_sim = LapSimulation(track_length=5300, avg_speed=210, braking_zones=12)
speeds = np.linspace(150, 250, 50)
lap_times = [LapSimulation(5300, v, 12).lap_time() for v in speeds]

# === Stint Simulation ===
stint = StintSimulation(base_lap_time=80.0, degradation_rate=0.15, max_laps=20)
laps = np.arange(1, stint.max_laps+1)
stint_times = [stint.lap_time(l) for l in laps]

# === Race Strategy ===
strategy = RaceStrategy(stint_model=stint, pit_stop_time=22.0, num_stints=3)
total_race_time = strategy.total_race_time()

# === Print Sample Outputs ===
print("=== Simulation Integration Example ===")
print(f"Lap Time at 210 km/h → {lap_sim.lap_time():.1f} s")
print(f"Lap Time at Lap 10 → {stint.lap_time(10):.2f} s")
print(f"Total Race Time → {total_race_time/60:.1f} min")

# === Plotting ===
plt.figure(figsize=(12, 8))

# Lap Simulation
plt.subplot(2, 2, 1)
plt.plot(speeds, lap_times, color="blue")
plt.xlabel("Average Speed (km/h)")
plt.ylabel("Lap Time (s)")
plt.title("Lap Time vs Average Speed")

# Stint Simulation
plt.subplot(2, 2, 2)
plt.plot(laps, stint_times, color="red")
plt.xlabel("Lap Number")
plt.ylabel("Lap Time (s)")
plt.title("Lap Time Evolution During Stint")

# Race Strategy Stint Times
stints = range(1, strategy.num_stints+1)
stint_totals = [sum(stint.lap_time(l) for l in range(1, stint.max_laps+1)) for _ in stints]
plt.subplot(2, 2, 3)
plt.bar(stints, stint_totals, color="green")
plt.xlabel("Stint Number")
plt.ylabel("Total Stint Time (s)")
plt.title("Stint Times in Race Strategy")

plt.tight_layout()
plt.show()
