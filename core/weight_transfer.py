# weight_transfer.py

"""

Module for calculating weight transfer in Formula 1.
Includes longitudinal and lateral transfer due to acceleration and cornering.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class WeightTransferModel:
    mass: float
    cg_height: float
    wheelbase: float
    track_width: float

    def longitudinal_transfer(self, accel_long: float) -> float:
        """Return longitudinal weight transfer (N)."""
        return (self.mass * accel_long * self.cg_height) / self.wheelbase

    def lateral_transfer(self, accel_lat: float) -> float:
        """Return lateral weight transfer (N)."""
        return (self.mass * accel_lat * self.cg_height) / self.track_width


# Example usage and plotting

if __name__ == "__main__":
    model = WeightTransferModel(mass=800, cg_height=0.35, wheelbase=3.6, track_width=1.6)
    accels_long = np.linspace(-10, 10, 50)
    transfers_long = [model.longitudinal_transfer(a) for a in accels_long]

    accels_lat = np.linspace(0, 15, 50)
    transfers_lat = [model.lateral_transfer(a) for a in accels_lat]

    print("Weight Transfer Example:")
    print(f"Longitudinal Transfer at 5 m/s² → {model.longitudinal_transfer(5):.1f} N")
    print(f"Lateral Transfer at 10 m/s² → {model.lateral_transfer(10):.1f} N")

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(accels_long, transfers_long, color="blue")
    plt.xlabel("Longitudinal Acceleration (m/s²)")
    plt.ylabel("Weight Transfer (N)")
    plt.title("Longitudinal Weight Transfer")

    plt.subplot(1, 2, 2)
    plt.plot(accels_lat, transfers_lat, color="green")
    plt.xlabel("Lateral Acceleration (m/s²)")
    plt.ylabel("Weight Transfer (N)")
    plt.title("Lateral Weight Transfer")

    plt.tight_layout()
    plt.show()
