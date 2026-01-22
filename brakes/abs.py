#abs.py

"""
Anti-lock braking system (ABS) logic
"""

def slip_ratio(wheel_speed: float, vehicle_speed: float) -> float:
    """
    Calculate slip ratio.

    Parameters:
        wheel_speed (float): Wheel circumferential speed [m/s]
        vehicle_speed (float): Vehicle speed [m/s]

    Returns:
        float: Slip ratio [-]
    """
    if vehicle_speed < 1e-6:
        return 0.0
    return (vehicle_speed - wheel_speed) / vehicle_speed


def abs_active(slip: float, threshold: float = 0.2) -> bool:
    """
    Check if ABS should activate.

    Parameters:
        slip (float): Current slip ratio [-]
        threshold (float): Slip threshold for ABS activation (default 0.2)

    Returns:
        bool: True if ABS active, False otherwise
    """
    return slip > threshold


def abs_modulated_force(brake_force: float, slip: float,
                        threshold: float = 0.2) -> float:
    """
    Modulate brake force if ABS is active.

    Parameters:
        brake_force (float): Requested brake force [N]
        slip (float): Current slip ratio [-]
        threshold (float): Slip threshold for ABS activation

    Returns:
        float: Adjusted brake force [N]
    """
    if abs_active(slip, threshold):
        # Reduce brake force to bring slip back under control
        return brake_force * (threshold / slip)
    return brake_force


# Example usage
if __name__ == "__main__":
    wheel_speed = 15.0   # m/s
    vehicle_speed = 20.0 # m/s
    brake_force = 5000.0 # N

    slip = slip_ratio(wheel_speed, vehicle_speed)
    print(f"Slip ratio = {slip:.2f}")

    active = abs_active(slip)
    print(f"ABS active? {active}")

    mod_force = abs_modulated_force(brake_force, slip)
    print(f"Modulated brake force = {mod_force:.1f} N")
