#lap_simulation.py

"""
Single lap performance model
"""

def lap_time(distance: float, avg_speed: float) -> float:
    """
    Estimate lap time.

    Parameters:
        distance (float): Lap length [m]
        avg_speed (float): Average speed [m/s]

    Returns:
        float: Lap time [s]
    """
    if avg_speed <= 0:
        raise ValueError("Average speed must be positive")
    return distance / avg_speed


def fuel_burn(fuel_rate: float, lap_time: float) -> float:
    """
    Estimate fuel consumed in one lap.

    Parameters:
        fuel_rate (float): Fuel consumption rate [kg/s]
        lap_time (float): Lap time [s]

    Returns:
        float: Fuel consumed [kg]
    """
    return fuel_rate * lap_time


# Example usage
if __name__ == "__main__":
    distance = 5300.0   # m
    avg_speed = 65.0    # m/s (~234 km/h)
    rate = 0.08         # kg/s

    t = lap_time(distance, avg_speed)
    fuel = fuel_burn(rate, t)

    print(f"Lap time = {t:.1f} s, Fuel burn = {fuel:.2f} kg")
