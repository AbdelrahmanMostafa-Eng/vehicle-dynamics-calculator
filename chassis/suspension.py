#suspension.py

"""
Suspension modeling (springs, dampers, anti-roll bar)
"""

def spring_force(k: float, deflection: float) -> float:
    """
    Calculate spring force.

    Parameters:
        k (float): Spring stiffness [N/m]
        deflection (float): Spring compression/extension [m]

    Returns:
        float: Spring force [N]
    """
    return k * deflection


def damper_force(c: float, velocity: float) -> float:
    """
    Calculate damper (shock absorber) force.

    Parameters:
        c (float): Damping coefficient [N·s/m]
        velocity (float): Suspension velocity [m/s]

    Returns:
        float: Damper force [N]
    """
    return c * velocity


def arb_force(stiffness: float, roll_angle: float) -> float:
    """
    Calculate anti-roll bar force.

    Parameters:
        stiffness (float): ARB stiffness [N·m/rad]
        roll_angle (float): Body roll angle [rad]

    Returns:
        float: Anti-roll bar resisting force [N·m]
    """
    return stiffness * roll_angle


# Example usage
if __name__ == "__main__":
    F_spring = spring_force(k=30000, deflection=0.05)
    F_damper = damper_force(c=1500, velocity=0.2)
    F_arb = arb_force(stiffness=5000, roll_angle=0.05)

    print(f"Spring force = {F_spring:.1f} N")
    print(f"Damper force = {F_damper:.1f} N")
    print(f"Anti-roll bar torque = {F_arb:.1f} N·m")
