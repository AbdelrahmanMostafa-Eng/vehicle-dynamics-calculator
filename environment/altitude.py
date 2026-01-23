#altitude.py

"""
altitude.py — Altitude effects on air density and performance
"""

import math

def air_density_at_altitude(altitude: float, temp: float = 15.0) -> float:
    """
    Calculate air density at a given altitude using ISA model.

    Parameters:
        altitude (float): Altitude above sea level [m]
        temp (float): Sea-level temperature [°C] (default 15 °C)

    Returns:
        float: Air density [kg/m^3]
    """
    # Constants
    T0 = temp + 273.15       # sea-level temperature [K]
    P0 = 101325.0            # sea-level pressure [Pa]
    L = 0.0065               # temperature lapse rate [K/m]
    R = 287.05               # specific gas constant [J/(kg·K)]
    g = 9.80665              # gravity [m/s^2]

    # Temperature at altitude
    T = T0 - L * altitude

    # Pressure at altitude (barometric formula)
    P = P0 * (1 - (L * altitude) / T0) ** (g / (R * L))

    # Density
    rho = P / (R * T)
    return rho


def engine_power_correction(base_power: float, altitude: float) -> float:
    """
    Correct engine power for altitude effects.

    Parameters:
        base_power (float): Sea-level engine power [kW]
        altitude (float): Altitude above sea level [m]

    Returns:
        float: Corrected engine power [kW]
    """
    rho0 = air_density_at_altitude(0.0)
    rho = air_density_at_altitude(altitude)
    return base_power * (rho / rho0)


# Example usage
if __name__ == "__main__":
    alt = 2000.0  # meters
    rho = air_density_at_altitude(alt)
    print(f"Air density at {alt:.0f} m = {rho:.3f} kg/m^3")

    base_power = 600.0  # kW
    corrected = engine_power_correction(base_power, alt)
    print(f"Engine power at {alt:.0f} m = {corrected:.1f} kW")
