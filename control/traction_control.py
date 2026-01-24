#traction_control.py

"""
Traction control system (TCS) logic
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
    return (wheel_speed - vehicle_speed) / vehicle_speed


def tcs_active(slip: float, threshold: float = 0.1) -> bool:
    """
    Check if traction control should activate.

    Parameters:
        slip (float): Current slip ratio [-]
        threshold (float): Slip threshold for TCS activation (default 0.1)

    Returns:
        bool: True if TCS active, False otherwise
    """
    return slip > threshold


def modulated_torque(engine_torque: float, slip: float,
                     threshold: float = 0.1) -> float:
    """
    Reduce engine torque if TCS is active.

    Parameters:
        engine_torque (float): Requested engine torque [Nm]
        slip (float): Current slip ratio [-]
        threshold (float): Slip threshold for TCS activation

    Returns:
        float: Adjusted engine torque [Nm]
    """
    if tcs_active(slip, threshold):
        return engine_torque * (threshold / slip)
    return engine_torque


# Example usage
if __name__ == "__main__":
    wheel_speed = 25.0   # m/s
    vehicle_speed = 20.0 # m/s
    engine_tq = 400.0    # Nm

    slip = slip_ratio(wheel_speed, vehicle_speed)
    print(f"Slip ratio = {slip:.2f}")

    active = tcs_active(slip)
    print(f"TCS active? {active}")

    mod_tq = modulated_torque(engine_tq, slip)
    print(f"Modulated torque = {mod_tq:.1f} Nm")
