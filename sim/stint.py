#stint.py

"""

Module for simulating tire stints in Formula 1.
Includes degradation, lap time evolution, and stint length.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class StintSimulation:
    base_lap_time: float   # s
    degradation_rate: float # s/lap
    max_laps: int

    def lap_time(self, lap: int) -> float:
        """Return lap time at given lap number."""
        return self.base_lap_time + self.degradation_rate * lap


# Example usage and visualization

if __name__ == "__main__":
    stint = StintSimulation(base_lap_time=80.0, degradation_rate=0.15, max_laps=30)
    laps = np.arange(1, stint.max_laps+1)
    times = [stint.lap_time(l) for l in laps]

    print("Stint Simulation Example:")
    print(f"Lap Time at Lap 10 → {stint.lap_time(10):.2f} s")

    plt.plot(laps, times, color="red")
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (s)")
    plt.title("Lap Time Evolution During Stint")
    plt.show()
