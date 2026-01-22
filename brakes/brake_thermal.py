#brake_thermal.py

"""
Brake disc thermal model
"""

def brake_temperature(initial_temp: float, braking_energy: float,
                      mass: float, specific_heat: float,
                      cooling_coeff: float, dt: float) -> float:
    """
    Estimate brake disc temperature after a braking event.

    Parameters:
        initial_temp (float): Initial disc temperature [°C]
        braking_energy (float): Energy absorbed [J]
        mass (float): Brake disc mass [kg]
        specific_heat (float): Specific heat capacity [J/(kg·K)]
        cooling_coeff (float): Cooling coefficient [W/K]
        dt (float): Time step [s]

    Returns:
        float: Updated brake disc temperature [°C]
    """
    # Temperature rise from braking
    delta_T = braking_energy / (mass * specific_heat)

    # Cooling effect (linear approximation)
    cooling = (cooling_coeff * dt) / (mass * specific_heat)

    return initial_temp + delta_T - cooling


def repeated_braking(temp: float, events: int, braking_energy: float,
                     mass: float, specific_heat: float,
                     cooling_coeff: float, dt: float) -> float:
    """
    Simulate repeated braking events.

    Parameters:
        temp (float): Initial disc temperature [°C]
        events (int): Number of braking events
        braking_energy (float): Energy per event [J]
        mass (float): Brake disc mass [kg]
        specific_heat (float): Specific heat capacity [J/(kg·K)]
        cooling_coeff (float): Cooling coefficient [W/K]
        dt (float): Time step per event [s]

    Returns:
        float: Final brake disc temperature [°C]
    """
    for _ in range(events):
        temp = brake_temperature(temp, braking_energy, mass,
                                 specific_heat, cooling_coeff, dt)
    return temp


# Example usage
if __name__ == "__main__":
    T1 = brake_temperature(initial_temp=200, braking_energy=50000,
                           mass=8.0, specific_heat=500,
                           cooling_coeff=50, dt=1.0)
    print(f"Brake disc temperature after one stop = {T1:.1f} °C")

    T2 = repeated_braking(temp=200, events=5, braking_energy=50000,
                          mass=8.0, specific_heat=500,
                          cooling_coeff=50, dt=1.0)
    print(f"Brake disc temperature after 5 stops = {T2:.1f} °C")
