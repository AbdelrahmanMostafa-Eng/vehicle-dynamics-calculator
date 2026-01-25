#stint.py

"""
Multi-lap tire & fuel management
"""

def tire_degradation(initial_grip: float, laps: int, degradation_rate: float) -> float:
    """
    Estimate grip after a number of laps.

    Parameters:
        initial_grip (float): Starting grip coefficient [-]
        laps (int): Number of laps completed
        degradation_rate (float): Grip loss per lap [-]

    Returns:
        float: Grip coefficient after laps [-]
    """
    grip = initial_grip - degradation_rate * laps
    return max(0.0, grip)  # clamp to non-negative


def fuel_mass(initial_fuel: float, fuel_per_lap: float, laps: int) -> float:
    """
    Estimate remaining fuel after a number of laps.

    Parameters:
        initial_fuel (float): Starting fuel mass [kg]
        fuel_per_lap (float): Fuel consumed per lap [kg]
        laps (int): Number of laps completed

    Returns:
        float: Remaining fuel mass [kg]
    """
    fuel = initial_fuel - fuel_per_lap * laps
    return max(0.0, fuel)


def stint_summary(initial_grip: float, initial_fuel: float,
                  laps: int, degradation_rate: float,
                  fuel_per_lap: float) -> dict:
    """
    Summarize tire and fuel status after a stint.

    Returns:
        dict: {"final_grip": grip, "remaining_fuel": fuel}
    """
    grip = tire_degradation(initial_grip, laps, degradation_rate)
    fuel = fuel_mass(initial_fuel, fuel_per_lap, laps)
    return {"final_grip": grip, "remaining_fuel": fuel}


# Example usage
if __name__ == "__main__":
    summary = stint_summary(initial_grip=1.2, initial_fuel=100.0,
                            laps=15, degradation_rate=0.02,
                            fuel_per_lap=2.5)
    print(f"After 15 laps → Grip = {summary['final_grip']:.2f}, Fuel = {summary['remaining_fuel']:.1f} kg")
