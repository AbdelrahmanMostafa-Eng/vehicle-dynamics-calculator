#lift_balance.py

"""

Module for calculating aerodynamic balance in Formula 1.
Provides downforce distribution and center of pressure (CoP) position.

"""

from dataclasses import dataclass

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


if __name__ == "__main__":
    # Example usage
    rho = 1.225
    balance = AeroBalanceModel(front_cl=2.0, rear_cl=2.5, front_area=1.5, rear_area=2.0, wheelbase=3.6)

    print("=== Lift Balance Example ===")
    for v in [100, 200, 300]:  # km/h
        v_ms = v / 3.6
        cop = balance.center_of_pressure(v_ms, rho)
        print(f"Velocity {v} km/h → CoP = {cop:.2f} m from front axle")
