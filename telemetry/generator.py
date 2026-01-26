#generator.py

"""
Synthetic telemetry data generator
"""

import random

def generate_lap_data(laps: int, lap_distance: float) -> list:
    """
    Generate synthetic telemetry data for multiple laps.

    Parameters:
        laps (int): Number of laps
        lap_distance (float): Lap length [m]

    Returns:
        list of dict: Each dict contains lap telemetry
    """
    data = []
    for lap in range(1, laps + 1):
        avg_speed = random.uniform(60, 70)  # m/s
        lap_time = lap_distance / avg_speed
        fuel_used = random.uniform(2.3, 2.7)  # kg
        tire_wear = random.uniform(0.01, 0.03) * lap

        data.append({
            "lap": lap,
            "avg_speed": avg_speed,
            "lap_time": lap_time,
            "fuel_used": fuel_used,
            "tire_wear": tire_wear
        })
    return data


# Example usage
if __name__ == "__main__":
    telemetry = generate_lap_data(5, lap_distance=5300)
    for lap in telemetry:
        print(lap)
