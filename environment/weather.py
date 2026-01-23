#weather.py

"""
Ambient weather effects
"""

def air_density(temp: float, pressure: float, humidity: float = 0.0) -> float:
    """
    Calculate air density using simplified formula.

    Parameters:
        temp (float): Ambient temperature [°C]
        pressure (float): Atmospheric pressure [Pa]
        humidity (float): Relative humidity fraction (0–1)

    Returns:
        float: Air density [kg/m^3]
    """
    # Convert temperature to Kelvin
    T = temp + 273.15

    # Gas constant for dry air
    R = 287.05

    # Approximate vapor pressure effect from humidity
    vapor_pressure = humidity * 2300  # Pa
    effective_pressure = pressure - vapor_pressure

    return effective_pressure / (R * T)


def track_temp_effect(base_grip: float, track_temp: float) -> float:
    """
    Adjust grip coefficient based on track temperature.

    Parameters:
        base_grip (float): Base grip coefficient [-]
        track_temp (float): Track surface temperature [°C]

    Returns:
        float: Adjusted grip coefficient [-]
    """
    # Assume optimal grip at 30–40 °C
    if track_temp < 30:
        return base_grip * (0.9 + 0.01 * track_temp)
    elif track_temp > 40:
        return base_grip * (1.3 - 0.005 * track_temp)
    else:
        return base_grip * 1.0


# Example usage
if __name__ == "__main__":
    rho = air_density(temp=25, pressure=101325, humidity=0.5)
    print(f"Air density = {rho:.3f} kg/m^3")

    grip = track_temp_effect(base_grip=1.2, track_temp=35)
    print(f"Grip coefficient at 35 °C = {grip:.3f}")
