#tire_heat.py

"""
tire_heat.py - Tire thermal modeling

Models tire temperature changes due to frictional heating and cooling effects.
"""

def tire_temperature(prev_temp: float, speed: float, Fx: float, Fy: float,
                     ambient_temp: float = 25.0, dt: float = 1.0) -> float:
    """
    Calculate tire surface temperature at the next timestep.

    Parameters:
        prev_temp (float): Previous tire temperature [°C]
        speed (float): Vehicle speed [m/s]
        Fx (float): Longitudinal force [N]
        Fy (float): Lateral force [N]
        ambient_temp (float): Ambient air temperature [°C]
        dt (float): Time step [s]

    Returns:
        float: Updated tire temperature [°C]
    """
    # Heat generation proportional to friction work
    heat_gen = 0.0005 * (abs(Fx) + abs(Fy)) * speed

    # Cooling proportional to difference from ambient
    cooling = 0.01 * (prev_temp - ambient_temp)

    # Net temperature change
    new_temp = prev_temp + (heat_gen - cooling) * dt
    return new_temp


# Example usage
if __name__ == "__main__":
    temp = 80.0  # initial °C
    for t in range(1, 6):
        temp = tire_temperature(temp, speed=30, Fx=2000, Fy=1500, ambient_temp=25, dt=1.0)
        print(f"Time {t}s: Tire temp = {temp:.2f} °C")
