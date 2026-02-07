#strategy.py

"""

Module for simulating race strategy in Formula 1.
Includes pit stops, stint management, and total race time.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class RaceStrategy:
    stint_model: object
    pit_stop_time: float   # s
    num_stints: int

    def total_race_time(self) -> float:
        """Estimate total race time (s)."""
        total = 0
        for s in range(self.num_stints):
            laps = self.stint_model.max_laps
            total += sum(self.stint_model.lap_time(l) for l in range(1, laps+1))
            if s < self.num_stints - 1:
                total += self.pit_stop_time
        return total


# Example usage and plotting

if __name__ == "__main__":
    from stint import StintSimulation
    stint = StintSimulation(base_lap_time=80.0, degradation_rate=0.15, max_laps=20)
    strategy = RaceStrategy(stint_model=stint, pit_stop_time=22.0, num_stints=3)

    print("Race Strategy Example:")
    print(f"Total Race Time → {strategy.total_race_time()/60:.1f} min")

    stints = range(1, strategy.num_stints+1)
    times = [sum(stint.lap_time(l) for l in range(1, stint.max_laps+1)) for _ in stints]

    plt.bar(stints, times, color="green")
    plt.xlabel("Stint Number")
    plt.ylabel("Total Stint Time (s)")
    plt.title("Stint Times in Race Strategy")
    plt.show()
