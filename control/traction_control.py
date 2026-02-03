#traction_control.py

"""

Module for simulating traction control in Formula 1.
Limits wheel slip by reducing engine torque.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class TractionControlModel:
    slip_threshold: float   # slip ratio threshold
    reduction_gain: float   # torque reduction per slip above threshold

    def adjusted_torque(self, slip_ratio: float, engine_torque: float) -> float:
        """Return adjusted torque based on slip ratio."""
        if slip_ratio <= self.slip_threshold:
            return engine_torque
        else:
            reduction = self.reduction_gain * (slip_ratio - self.slip_threshold)
            return max(0.0, engine_torque * (1 - reduction))


# Example usage and plotting

if __name__ == "__main__":
    tc_model = TractionControlModel(slip_threshold=0.12, reduction_gain=3.0)
    slip_ratios = np.linspace(0, 0.3, 50)
    torques = [tc_model.adjusted_torque(s, 700) for s in slip_ratios]

    print("Traction Control Example:")
    for s in [0.1, 0.15, 0.25]:
        print(f"Slip Ratio {s:.2f} → Adjusted Torque = {tc_model.adjusted_torque(s, 700):.1f} Nm")

    plt.plot(slip_ratios*100, torques, color="red")
    plt.axvline(tc_model.slip_threshold*100, color="black", linestyle="--", label="Slip Threshold")
    plt.xlabel("Slip Ratio (%)")
    plt.ylabel("Adjusted Torque (Nm)")
    plt.title("Traction Control Torque Reduction")
    plt.legend()
    plt.show()
