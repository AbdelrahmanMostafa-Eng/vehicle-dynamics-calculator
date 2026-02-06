#ers.py

"""

Module for modeling Energy Recovery System (ERS) in Formula 1.
Includes harvesting and deployment of electrical energy.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class ERSModel:
    capacity: float       # kJ
    efficiency: float     # harvesting efficiency (0–1)
    deploy_rate: float    # kW

    def harvest(self, braking_energy: float) -> float:
        """Harvest energy from braking (kJ)."""
        return min(braking_energy * self.efficiency, self.capacity)

    def deploy(self, duration: float) -> float:
        """Deploy energy over given duration (s)."""
        energy_used = self.deploy_rate * duration
        return min(energy_used, self.capacity)


# Example usage and plotting

if __name__ == "__main__":
    ers = ERSModel(capacity=4000, efficiency=0.7, deploy_rate=120)
    braking_events = np.linspace(0, 6000, 50)
    harvested = [ers.harvest(e) for e in braking_events]

    times = np.linspace(0, 40, 50)
    deployed = [ers.deploy(t) for t in times]

    print("ERS Example:")
    print(f"Harvest from 3000 kJ braking → {ers.harvest(3000):.1f} kJ")
    print(f"Deploy over 20s → {ers.deploy(20):.1f} kJ")

    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.plot(braking_events, harvested, color="green")
    plt.xlabel("Braking Energy (kJ)")
    plt.ylabel("Harvested Energy (kJ)")
    plt.title("ERS Harvesting")

    plt.subplot(1,2,2)
    plt.plot(times, deployed, color="orange")
    plt.xlabel("Deployment Duration (s)")
    plt.ylabel("Deployed Energy (kJ)")
    plt.title("ERS Deployment")

    plt.tight_layout()
    plt.show()
