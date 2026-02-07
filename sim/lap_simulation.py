#lap_simulation.py

"""

Module for simulating lap times in Formula 1.
Includes speed profile, braking zones, and lap time estimation.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class LapSimulation:
    track_length: float   # m
    avg_speed: float      # km/h
    braking_zones: int    # number of braking zones

    def lap_time(self) -> float:
        """Estimate lap time (s)."""
        return self.track_length / (self.avg_speed / 3.6)


# Example usage and visualization

if __name__ == "__main__":
    sim = LapSimulation(track_length=5300, avg_speed=210, braking_zones=12)
    speeds = np.linspace(150, 250, 50)
    lap_times = [LapSimulation(5300, v, 12).lap_time() for v in speeds]

    print("Lap Simulation Example:")
    print(f"Lap Time at 210 km/h → {sim.lap_time():.1f} s")

    plt.plot(speeds, lap_times, color="blue")
    plt.xlabel("Average Speed (km/h)")
    plt.ylabel("Lap Time (s)")
    plt.title("Lap Time vs Average Speed")
    plt.show()
