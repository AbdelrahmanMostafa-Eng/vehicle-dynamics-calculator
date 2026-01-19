#ground_effect.py

"""
Ground effect and ride height maps
"""

def ground_effect_downforce(rho: float, Cl0: float, A: float,
                            v: float, ride_height: float) -> float:
    """
    Calculate downforce with ground effect influence.

    Parameters:
        rho (float): Air density [kg/m^3]
        Cl0 (float): Base lift coefficient (negative for downforce)
        A (float): Reference area [m^2]
        v (float): Vehicle speed [m/s]
        ride_height (float): Ride height [m]

    Returns:
        float: Downforce [N]
    """
    # Base downforce
    base = 0.5 * rho * Cl0 * A * v**2

    # Ground effect multiplier: peak at ~0.05–0.07 m, drops if too low or too high
    if ride_height <= 0:
        return 0.0
    optimal = 0.06  # 6 cm typical F1 optimal ride height
    factor = (optimal / ride_height) * (1 - 0.5 * abs(ride_height - optimal) / optimal)

    return base * max(factor, 0.0)


def ride_height_map(rho: float, Cl0: float, A: float, v: float,
                    heights: list[float]) -> dict:
    """
    Generate a ride height vs downforce map.

    Parameters:
        rho (float): Air density [kg/m^3]
        Cl0 (float): Base lift coefficient
        A (float): Reference area [m^2]
        v (float): Vehicle speed [m/s]
        heights (list): List of ride heights [m]

    Returns:
        dict: {height: downforce}
    """
    return {h: ground_effect_downforce(rho, Cl0, A, v, h) for h in heights}


# Example usage
if __name__ == "__main__":
    rho = 1.225
    Cl0 = -3.0
    A = 1.6
    v = 70.0
    heights = [0.02, 0.04, 0.06, 0.08, 0.10]

    map_data = ride_height_map(rho, Cl0, A, v, heights)
    for h, df in map_data.items():
        print(f"Ride height {h:.2f} m → Downforce {df:.1f} N")
