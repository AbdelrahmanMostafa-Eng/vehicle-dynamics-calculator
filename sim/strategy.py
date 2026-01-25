#strategy.py

"""
strategy.py — Race strategy planning (standalone version)
"""

# Lap simulation
def lap_time(distance: float, avg_speed: float) -> float:
    if avg_speed <= 0:
        raise ValueError("Average speed must be positive")
    return distance / avg_speed

def fuel_burn(fuel_rate: float, lap_time: float) -> float:
    return fuel_rate * lap_time


# Stint simulation
def tire_degradation(initial_grip: float, laps: int, degradation_rate: float) -> float:
    grip = initial_grip - degradation_rate * laps
    return max(0.0, grip)

def fuel_mass(initial_fuel: float, fuel_per_lap: float, laps: int) -> float:
    fuel = initial_fuel - fuel_per_lap * laps
    return max(0.0, fuel)

def stint_summary(initial_grip: float, initial_fuel: float,
                  laps: int, degradation_rate: float,
                  fuel_per_lap: float) -> dict:
    grip = tire_degradation(initial_grip, laps, degradation_rate)
    fuel = fuel_mass(initial_fuel, fuel_per_lap, laps)
    return {"final_grip": grip, "remaining_fuel": fuel}


# Race strategy
def race_strategy(lap_distance: float, avg_speed: float,
                  fuel_rate: float, initial_fuel: float,
                  initial_grip: float, degradation_rate: float,
                  fuel_per_lap: float, stints: list,
                  pit_stop_time: float) -> dict:
    total_time = 0.0
    grip = initial_grip
    fuel = initial_fuel

    for i, laps in enumerate(stints):
        lt = lap_time(lap_distance, avg_speed)
        stint_time = lt * laps
        total_time += stint_time

        summary = stint_summary(grip, fuel, laps, degradation_rate, fuel_per_lap)
        grip = summary["final_grip"]
        fuel = summary["remaining_fuel"]

        if i < len(stints) - 1:
            total_time += pit_stop_time

    return {"total_time": total_time, "final_grip": grip, "remaining_fuel": fuel}


# Example run
if __name__ == "__main__":
    stints = [15, 20, 20]  # three stints
    result = race_strategy(lap_distance=5300, avg_speed=65,
                           fuel_rate=0.08, initial_fuel=100.0,
                           initial_grip=1.2, degradation_rate=0.02,
                           fuel_per_lap=2.5, stints=stints,
                           pit_stop_time=22.0)

    print(f"Total race time = {result['total_time']:.1f} s")
    print(f"Final grip = {result['final_grip']:.2f}, Remaining fuel = {result['remaining_fuel']:.1f} kg")
