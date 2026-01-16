#limits.py

"""
limits.py - Basic tire force limit model

Implements the simplest friction circle check:
sqrt(Fx^2 + Fy^2) <= μ * Fz
"""

import math

def friction_circle(mu: float, Fz: float, Fx: float, Fy: float) -> bool:
    """
    Check if combined longitudinal and lateral forces are within the friction circle.

    Parameters:
        mu (float): Friction coefficient (dimensionless)
        Fz (float): Vertical load [N]
        Fx (float): Longitudinal force [N]
        Fy (float): Lateral force [N]

    Returns:
        bool: True if forces are within tire capacity, False otherwise
    """
    if Fz <= 0:
        raise ValueError("Vertical load must be positive")
    if mu <= 0:
        raise ValueError("Friction coefficient must be positive")

    total_force = math.sqrt(Fx**2 + Fy**2)
    max_force = mu * Fz
    return total_force <= max_force


# Example usage
if __name__ == "__main__":
    mu = 1.2
    Fz = 4000   # N
    Fx = 1500   # N
    Fy = 2000   # N

    result = friction_circle(mu, Fz, Fx, Fy)
    print("Within limit:", result)
