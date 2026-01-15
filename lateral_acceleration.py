# lateral_acceleration.py
"""
Lateral (centripetal) acceleration calculations for vehicle dynamics.
"""

def lateral_acceleration(speed_ms, turn_radius_m):
    """
    Calculate lateral acceleration during steady-state cornering.

    Parameters:
    - speed_ms (float): Vehicle speed in meters per second
    - turn_radius_m (float): Radius of the turn in meters (positive)
    
    Returns:
    - float: Lateral acceleration in m/s^2 (always positive)
    
    Raises:
    - ValueError: If turn_radius_m <= 0
    """
    if turn_radius_m <= 0:
        raise ValueError("Turn radius must be positive")
    
    return (speed_ms ** 2) / turn_radius_m


def lateral_acceleration_from_kmh(speed_kmh, turn_radius_m):
    """
    Calculate lateral acceleration with km/h input.
    
    Parameters:
    - speed_kmh (float): Speed in km/h
    - turn_radius_m (float): Turn radius in meters
    
    Returns:
    - float: Lateral acceleration in m/s^2
    """
    speed_ms = speed_kmh / 3.6  # km/h → m/s
    return lateral_acceleration(speed_ms, turn_radius_m)


def lateral_acceleration_g(speed_ms, turn_radius_m):
    """
    Calculate lateral acceleration in g-forces.
    
    Parameters:
    - speed_ms (float): Speed in m/s
    - turn_radius_m (float): Turn radius in meters
    
    Returns:
    - float: Lateral acceleration in g's (1g = 9.81 m/s²)
    """
    accel_ms2 = lateral_acceleration(speed_ms, turn_radius_m)
    return accel_ms2 / 9.81


def max_speed_for_lateral_g(turn_radius_m, max_lateral_g):
    """
    Calculate maximum speed for a given turn radius and lateral g limit.
    
    Parameters:
    - turn_radius_m (float): Turn radius in meters
    - max_lateral_g (float): Maximum lateral acceleration in g's
    
    Returns:
    - float: Maximum speed in m/s
    """
    max_accel_ms2 = max_lateral_g * 9.81
    return (max_accel_ms2 * turn_radius_m) ** 0.5


# Example usage
if __name__ == "__main__":
    # Your original example
    v = 20   # m/s (~72 km/h)
    r = 50   # m
    result = lateral_acceleration(v, r)
    print(f"Lateral acceleration: {result:.2f} m/s^2")
    print(f"Lateral acceleration: {lateral_acceleration_g(v, r):.2f} g")
    
    # More practical examples
    print("\n--- Practical Examples ---")
    
    # Example 1: Highway off-ramp
    speed_kmh = 80
    radius = 100  # typical highway ramp
    accel = lateral_acceleration_from_kmh(speed_kmh, radius)
    print(f"Highway ramp at {speed_kmh} km/h, radius {radius}m:")
    print(f"  Lateral acceleration: {accel:.2f} m/s^2 = {accel/9.81:.2f} g")
    
    # Example 2: Racing corner
    speed_kmh = 120
    radius = 50  # tight racing corner
    accel = lateral_acceleration_from_kmh(speed_kmh, radius)
    print(f"\nRacing corner at {speed_kmh} km/h, radius {radius}m:")
    print(f"  Lateral acceleration: {accel:.2f} m/s^2 = {accel/9.81:.2f} g")
    
    # Example 3: What's the speed limit for 0.8g in a 30m radius turn?
    max_speed = max_speed_for_lateral_g(30, 0.8)
    print(f"\nFor a 30m radius turn at 0.8g limit:")
    print(f"  Max speed: {max_speed:.1f} m/s = {max_speed*3.6:.1f} km/h")
    
    # Example 4: Error handling
    try:
        bad_result = lateral_acceleration(20, 0)
    except ValueError as e:
        print(f"\nError handling: {e}")
