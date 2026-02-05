#track_grip.py

"""

Module for modeling track grip coefficient based on surface conditions and rubber buildup.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class TrackGripModel:
    base_mu: float       # Base friction coefficient
    rubber_gain: float   # Grip increase per lap
    wet_penalty: float   # Grip reduction factor when wet

    def grip(self, laps: int, wet: bool = False) -> float:
        """Return grip coefficient after given laps, considering wet conditions."""
        mu = self.base_mu + self.rubber_gain * laps
        if wet:
            mu *= (1 - self.wet_penalty)
        return mu


# Example usage and plotting

if __name__ == "__main__":
    model = TrackGripModel(base_mu=1.4, rubber_gain=0.01, wet_penalty=0.4)
    laps = np.arange(0, 50)
    grip_dry = [model.grip(l, wet=False) for l in laps]
    grip_wet = [model.grip(l, wet=True) for l in laps]

    print("Track Grip Example:")
    print(f"Grip after 10 laps (dry) → {model.grip(10, False):.2f}")
    print(f"Grip after 10 laps (wet) → {model.grip(10, True):.2f}")

    plt.plot(laps, grip_dry, label="Dry Track")
    plt.plot(laps, grip_wet, label="Wet Track", linestyle="--")
    plt.xlabel("Laps")
    plt.ylabel("Grip Coefficient (μ)")
    plt.title("Track Grip Evolution")
    plt.legend()
    plt.show()
