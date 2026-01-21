#drivetrain.py

"""
Gear ratios and traction limit calculations
"""

def wheel_torque(engine_torque: float, gear_ratio: float,
                 final_drive: float, driveline_eff: float = 0.95) -> float:
    """
    Calculate torque at the driven wheels.

    Parameters:
        engine_torque (float): Engine torque [Nm]
        gear_ratio (float): Selected gear ratio [-]
        final_drive (float): Final drive ratio [-]
        driveline_eff (float): Driveline efficiency (default 0.95)

    Returns:
        float: Wheel torque [Nm]
    """
    return engine_torque * gear_ratio * final_drive * driveline_eff


def traction_limit(mu: float, normal_force: float, wheel_radius: float) -> float:
    """
    Calculate maximum transmissible wheel torque before slip.

    Parameters:
        mu (float): Tire-road friction coefficient [-]
        normal_force (float): Normal load on driven axle [N]
        wheel_radius (float): Wheel radius [m]

    Returns:
        float: Maximum wheel torque [Nm]
    """
    return mu * normal_force * wheel_radius


def is_traction_limited(engine_torque: float, gear_ratio: float,
                        final_drive: float, mu: float,
                        normal_force: float, wheel_radius: float,
                        driveline_eff: float = 0.95) -> bool:
    """
    Check if wheel torque exceeds traction limit.

    Returns:
        bool: True if traction-limited, False otherwise
    """
    Tw = wheel_torque(engine_torque, gear_ratio, final_drive, driveline_eff)
    Tmax = traction_limit(mu, normal_force, wheel_radius)
    return Tw > Tmax


# Example usage
if __name__ == "__main__":
    engine_tq = 300.0     # Nm
    gear = 3.5
    final_drive = 4.0
    mu = 1.2              # sticky tires
    normal_force = 4000.0 # N on driven axle
    wheel_radius = 0.33   # m

    Tw = wheel_torque(engine_tq, gear, final_drive)
    Tmax = traction_limit(mu, normal_force, wheel_radius)
    limited = is_traction_limited(engine_tq, gear, final_drive,
                                  mu, normal_force, wheel_radius)

    print(f"Wheel torque = {Tw:.1f} Nm")
    print(f"Traction limit = {Tmax:.1f} Nm")
    print(f"Traction limited? {limited}")
