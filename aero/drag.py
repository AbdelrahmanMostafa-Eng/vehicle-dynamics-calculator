#drag.py

"""
Aerodynamic drag force calculations
"""

def drag_force(rho: float, Cd: float, A: float, v: float) -> float:
    """
    Calculate aerodynamic drag force.

    Parameters:
        rho (float): Air density [kg/m^3]
        Cd (float): Drag coefficient [-]
        A (float): Frontal/reference area [m^2]
        v (float): Vehicle speed [m/s]

    Returns:
        float: Drag force [N]
    """
    return 0.5 * rho * Cd * A * v**2


def drag_power(Fd: float, v: float) -> float:
    """
    Calculate power required to overcome drag.

    Parameters:
        Fd (float): Drag force [N]
        v (float): Vehicle speed [m/s]

    Returns:
        float: Power [W]
    """
    return Fd * v


# Example usage
if __name__ == "__main__":
    rho = 1.225   # kg/m^3 (sea level)
    Cd = 0.32     # typical road car; race car lower but with more downforce devices
    A = 2.0       # m^2
    v = 50.0      # m/s (~180 km/h)

    Fd = drag_force(rho, Cd, A, v)
    P = drag_power(Fd, v)
    print(f"Drag force: {Fd:.1f} N, Drag power: {P/1000:.1f} kW")
