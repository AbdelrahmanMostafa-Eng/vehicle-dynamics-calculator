#generator.py

"""

Module for generating synthetic telemetry data in Formula 1.
Includes speed, throttle, brake, and gear traces.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class TelemetryGenerator:
    lap_time: float   # s
    max_speed: float  # km/h

    def generate(self, n_points: int = 1000):
        """Generate synthetic telemetry arrays."""
        time = np.linspace(0, self.lap_time, n_points)
        speed = self.max_speed * (np.sin(2*np.pi*time/self.lap_time) * 0.4 + 0.6)
        throttle = np.clip(np.sin(4*np.pi*time/self.lap_time), 0, 1)
        brake = np.clip(-np.sin(4*np.pi*time/self.lap_time), 0, 1)
        gear = np.floor(1 + 6*(speed/self.max_speed)).astype(int)
        return time, speed, throttle, brake, gear


# Example usage and plotting

if __name__ == "__main__":
    gen = TelemetryGenerator(lap_time=90.0, max_speed=320)
    time, speed, throttle, brake, gear = gen.generate()

    print("Telemetry Generator Example:")
    print(f"Lap Time → {gen.lap_time:.1f} s")
    print(f"Max Speed → {max(speed):.1f} km/h")
    print(f"Sample Gear Trace → {gear[:10]}")

    plt.figure(figsize=(10,5))
    plt.plot(time, speed, label="Speed (km/h)")
    plt.plot(time, throttle*300, label="Throttle (scaled)")
    plt.plot(time, brake*300, label="Brake (scaled)")
    plt.xlabel("Time (s)")
    plt.ylabel("Telemetry Values")
    plt.title("Synthetic Telemetry Data")
    plt.legend()
    plt.show()
