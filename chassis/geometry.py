#geometry.py

"""

Module for calculating chassis geometry parameters in Formula 1.
Includes roll center height, anti-dive, and anti-squat characteristics.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class ChassisGeometry:
    track_width: float     # m
    cg_height: float       # m
    suspension_arm_angle: float  # degrees
    wheelbase: float       # m

    def roll_center_height(self) -> float:
        """Approximate roll center height based on suspension arm angle."""
        return self.cg_height - (self.track_width / 2) * np.tan(np.radians(self.suspension_arm_angle))

    def anti_dive_percentage(self, caster_angle: float) -> float:
        """Calculate anti-dive percentage based on caster angle and geometry."""
        return np.tan(np.radians(caster_angle)) * (self.cg_height / self.wheelbase) * 100

    def anti_squat_percentage(self, swing_arm_angle: float) -> float:
        """Calculate anti-squat percentage based on swing arm angle and geometry."""
        return np.tan(np.radians(swing_arm_angle)) * (self.cg_height / self.wheelbase) * 100

# Example usage and plotting

if __name__ == "__main__":
    geometry = ChassisGeometry(track_width=1.6, cg_height=0.35, suspension_arm_angle=10, wheelbase=3.6)

    print("Geometry Example:")
    print(f"Roll Center Height → {geometry.roll_center_height():.3f} m")
    print(f"Anti-Dive (caster=6°) → {geometry.anti_dive_percentage(6):.1f} %")
    print(f"Anti-Squat (swing=8°) → {geometry.anti_squat_percentage(8):.1f} %")

    angles = np.linspace(0, 15, 50)
    roll_centers = [ChassisGeometry(1.6, 0.35, a, 3.6).roll_center_height() for a in angles]

    plt.plot(angles, roll_centers, color="blue")
    plt.xlabel("Suspension Arm Angle (°)")
    plt.ylabel("Roll Center Height (m)")
    plt.title("Roll Center vs Suspension Arm Angle")
    plt.show()
