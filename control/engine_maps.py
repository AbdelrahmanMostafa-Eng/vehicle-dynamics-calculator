#engine_maps.py

"""

Module for modeling engine torque and fuel consumption maps in Formula 1.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class EngineMap:
    max_torque: float      # Nm
    efficiency_peak: float # optimal efficiency RPM
    fuel_rate_base: float  # base fuel rate (g/s)

    def torque(self, rpm: float) -> float:
        """Return torque at given RPM."""
        return self.max_torque * np.exp(-((rpm - self.efficiency_peak)/4000)**2)

    def fuel_rate(self, rpm: float, throttle: float) -> float:
        """Return fuel consumption rate at given RPM and throttle (0–1)."""
        return self.fuel_rate_base * (1 + (rpm/10000)) * throttle


# Example usage and plotting

if __name__ == "__main__":
    engine = EngineMap(max_torque=800, efficiency_peak=11000, fuel_rate_base=0.5)
    rpms = np.linspace(8000, 15000, 100)
    torques = [engine.torque(r) for r in rpms]
    fuel_rates = [engine.fuel_rate(r, throttle=0.8) for r in rpms]

    print("Engine Map Example:")
    print(f"Torque at 11000 RPM → {engine.torque(11000):.1f} Nm")
    print(f"Fuel Rate at 12000 RPM, 80% throttle → {engine.fuel_rate(12000, 0.8):.2f} g/s")

    plt.figure(figsize=(10,5))
    plt.plot(rpms, torques, label="Torque Curve")
    plt.plot(rpms, fuel_rates, label="Fuel Rate (80% throttle)")
    plt.xlabel("Engine Speed (RPM)")
    plt.ylabel("Torque (Nm) / Fuel Rate (g/s)")
    plt.title("Engine Torque & Fuel Map")
    plt.legend()
    plt.show()
