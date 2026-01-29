#downforce.py

"""

Module for calculating aerodynamic downforce from wing elements in Formula 1.
Includes support for angle of attack (AoA), DRS effects, and multi-element wings.

"""

from dataclasses import dataclass
import numpy as np

@dataclass
class WingElement:
    area: float
    base_cl: float
    aoa_sensitivity: float
    drs_effect: float

    def cl(self, aoa_deg: float, drs_active: bool = False) -> float:
        """Calculate lift coefficient based on AoA and DRS state."""
        cl = self.base_cl + self.aoa_sensitivity * aoa_deg
        if drs_active:
            cl *= (1 - self.drs_effect)
        return cl

    def downforce(self, velocity: float, aoa_deg: float, rho: float, drs_active: bool = False) -> float:
        """Calculate downforce (N) at given velocity (m/s)."""
        return 0.5 * rho * velocity**2 * self.area * self.cl(aoa_deg, drs_active)


# Example usage

if __name__ == "__main__":
    rho = 1.225  # kg/m³
    wing = WingElement(area=1.5, base_cl=2.0, aoa_sensitivity=0.05, drs_effect=0.25)

    print("=== Downforce Example ===")
    for v in [100, 200, 300]:  # km/h
        v_ms = v / 3.6
        df = wing.downforce(v_ms, aoa_deg=8, rho=rho, drs_active=False)
        print(f"Velocity {v} km/h → Downforce = {df:.1f} N")
