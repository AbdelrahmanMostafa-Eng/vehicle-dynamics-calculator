#engine_maps.py

"""
Engine power delivery modes
"""

def engine_map(base_torque: float, mode: str) -> float:
    """
    Adjust engine torque based on selected map.

    Parameters:
        base_torque (float): Base engine torque [Nm]
        mode (str): Engine mode ("qualifying", "race", "conserve", "wet")

    Returns:
        float: Adjusted engine torque [Nm]
    """
    mode = mode.lower()
    if mode == "qualifying":
        return base_torque * 1.10   # extra aggressive
    elif mode == "race":
        return base_torque * 1.00   # balanced
    elif mode == "conserve":
        return base_torque * 0.85   # fuel/ERS saving
    elif mode == "wet":
        return base_torque * 0.75   # smoother delivery
    else:
        return base_torque


def fuel_consumption(base_rate: float, mode: str) -> float:
    """
    Adjust fuel consumption rate based on engine mode.

    Parameters:
        base_rate (float): Base fuel consumption [kg/s]
        mode (str): Engine mode

    Returns:
        float: Adjusted fuel consumption [kg/s]
    """
    mode = mode.lower()
    if mode == "qualifying":
        return base_rate * 1.20
    elif mode == "race":
        return base_rate * 1.00
    elif mode == "conserve":
        return base_rate * 0.80
    elif mode == "wet":
        return base_rate * 0.90
    else:
        return base_rate


# Example usage
if __name__ == "__main__":
    tq = engine_map(base_torque=300.0, mode="qualifying")
    fc = fuel_consumption(base_rate=0.08, mode="qualifying")

    print(f"Qualifying mode → Torque = {tq:.1f} Nm, Fuel rate = {fc:.3f} kg/s")
