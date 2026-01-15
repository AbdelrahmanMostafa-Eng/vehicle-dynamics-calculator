# lateral_acceleration.py

def lateral_acceleration(speed, radius):
    """
    Calculate lateral (centripetal) acceleration for a vehicle in a turn.

    Parameters:
        speed (float): Vehicle speed in m/s.
        radius (float): Turn radius in m.

    Returns:
        float: Lateral acceleration in m/s².
    """
    if radius <= 0:
        raise ValueError("Turn radius must be greater than zero.")
    return (speed ** 2) / radius

# Example usage
if __name__ == "__main__":
    v = 20   # m/s (~72 km/h)
    r = 50   # m
    result = lateral_acceleration(v, r)
    print(f"Lateral acceleration: {result:.2f} m/s²")
