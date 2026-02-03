#downforce.py

"""

Module for calculating aerodynamic downforce from wing elements in Formula 1.
Includes support for angle of attack (AoA), DRS effects, and multi-element wings.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

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


# Example usage and plotting

if __name__ == "__main__":
    rho = 1.225  # kg/m³
    wing = WingElement(area=1.5, base_cl=2.0, aoa_sensitivity=0.05, drs_effect=0.25)
    
    velocities = np.linspace(50, 350, 50)  # km/h
    velocities_ms = velocities / 3.6

    df_no_drs = [wing.downforce(v, aoa_deg=8, rho=rho, drs_active=False) for v in velocities_ms]
    df_drs = [wing.downforce(v, aoa_deg=8, rho=rho, drs_active=True) for v in velocities_ms]

    # Print default outputs
    print("Downforce Example:")
    for v, df in zip([100, 200, 300], [wing.downforce(v/3.6, 8, rho, False) for v in [100, 200, 300]]):
        print(f"Velocity {v} km/h → Downforce = {df:.1f} N")

    # Plot
    plt.plot(velocities, df_no_drs, label="Wing Downforce (DRS Off)")
    plt.plot(velocities, df_drs, label="Wing Downforce (DRS On)", linestyle="--")
    plt.xlabel("Velocity (km/h)")
    plt.ylabel("Downforce (N)")
    plt.title("Downforce vs Speed")
    plt.legend()
    plt.show()
