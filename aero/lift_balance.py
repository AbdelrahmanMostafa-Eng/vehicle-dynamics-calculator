#lift_balance.py

"""

Module for calculating aerodynamic balance in Formula 1.
Provides downforce distribution and center of pressure (CoP) position.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

@dataclass
class AeroBalanceModel:
    front_cl: float
    rear_cl: float
    front_area: float
    rear_area: float
    wheelbase: float

    def downforce_distribution(self, velocity: float, rho: float) -> tuple:
        """Return front and rear downforce (N) at given velocity (m/s)."""
        df_front = 0.5 * rho * velocity**2 * self.front_area * self.front_cl
        df_rear = 0.5 * rho * velocity**2 * self.rear_area * self.rear_cl
        return df_front, df_rear

    def center_of_pressure(self, velocity: float, rho: float) -> float:
        """Return CoP position (m from front axle)."""
        df_front, df_rear = self.downforce_distribution(velocity, rho)
        total = df_front + df_rear
        return (df_rear / total) * self.wheelbase

# Example usage and plotting

if __name__ == "__main__": 
    rho = 1.225
    balance = AeroBalanceModel(front_cl=2.0, rear_cl=2.5, front_area=1.5, rear_area=2.0, wheelbase=3.6)
    
    velocities = np.linspace(50, 350, 50)  # km/h
    velocities_ms = velocities / 3.6
    cop_positions = [balance.center_of_pressure(v, rho) for v in velocities_ms]


    # Print default outputs
    print("Lift Balance Example:")
    for v in [100, 200, 300]:
        print(f"Velocity {v} km/h → CoP = {balance.center_of_pressure(v/3.6, rho):.2f} m from front axle")

    # Plot
    plt.plot(velocities, cop_positions, color="purple")
    plt.xlabel("Velocity (km/h)")
    plt.ylabel("CoP Position (m from front axle)")
    plt.title("Center of Pressure vs Speed")
    plt.show()
