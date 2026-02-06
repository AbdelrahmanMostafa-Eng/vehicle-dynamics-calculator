#engine.py

"""

Module for modeling engine power output in Formula 1.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class EngineModel:
    max_power: float   # kW
    max_rpm: float     # RPM
    torque_peak: float # Nm

    def torque_curve(self, rpm: float) -> float:
        """Return torque at given RPM."""
        return self.torque_peak * np.exp(-((rpm - self.max_rpm/2)/3000)**2)

    def power_curve(self, rpm: float) -> float:
        """Return power (kW) at given RPM."""
        torque = self.torque_curve(rpm)
        return (torque * rpm * 2*np.pi/60) / 1000


# Example usage and plotting

if __name__ == "__main__":
    engine = EngineModel(max_power=750, max_rpm=15000, torque_peak=800)
    rpms = np.linspace(5000, 15000, 100)
    torques = [engine.torque_curve(r) for r in rpms]
    powers = [engine.power_curve(r) for r in rpms]

    print("Engine Example:")
    print(f"Torque at 8000 RPM → {engine.torque_curve(8000):.1f} Nm")
    print(f"Power at 12000 RPM → {engine.power_curve(12000):.1f} kW")

    plt.figure(figsize=(10,5))
    plt.plot(rpms, torques, label="Torque Curve")
    plt.plot(rpms, powers, label="Power Curve")
    plt.xlabel("Engine Speed (RPM)")
    plt.ylabel("Torque (Nm) / Power (kW)")
    plt.title("Engine Torque & Power Curve")
    plt.legend()
    plt.show()
