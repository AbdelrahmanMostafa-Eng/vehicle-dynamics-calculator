# braking_distance.py
"""
Braking distance calculations for vehicle dynamics.
"""

def theoretical_braking_distance(speed_ms, friction_coefficient, efficiency=1.0):
    """
    Calculate theoretical minimum braking distance.
    
    Parameters:
    - speed_ms (float): Initial speed in m/s
    - friction_coefficient (float): Tire-road friction coefficient (μ)
    - efficiency (float): Brake system efficiency (0.0 to 1.0, default 1.0)
    
    Returns:
    - float: Braking distance in meters
    
    Raises:
    - ValueError: If friction_coefficient <= 0 or efficiency not in (0,1]
    """
    if friction_coefficient <= 0:
        raise ValueError("Friction coefficient must be positive")
    if not 0 < efficiency <= 1.0:
        raise ValueError("Efficiency must be between 0 and 1")
    
    g = 9.81
    effective_mu = friction_coefficient * efficiency
    distance = (speed_ms ** 2) / (2 * effective_mu * g)
    return distance


def braking_distance_from_kmh(speed_kmh, friction_coefficient, efficiency=1.0):
    """
    Calculate braking distance with km/h input.
    """
    speed_ms = speed_kmh / 3.6
    return theoretical_braking_distance(speed_ms, friction_coefficient, efficiency)


def total_stopping_distance(speed_ms, friction_coefficient, reaction_time=1.5, 
                           efficiency=1.0, gradient_percent=0):
    """
    Calculate total stopping distance including reaction time and road gradient.
    
    Parameters:
    - speed_ms (float): Initial speed in m/s
    - friction_coefficient (float): Tire-road friction coefficient
    - reaction_time (float): Driver reaction time in seconds (default 1.5s)
    - efficiency (float): Brake efficiency (default 1.0)
    - gradient_percent (float): Road gradient in % (+ = uphill, - = downhill)
    
    Returns:
    - dict: Contains reaction_distance, braking_distance, and total_distance
    """
    # Reaction distance (distance traveled during reaction time)
    reaction_distance = speed_ms * reaction_time
    
    # Convert gradient % to angle in radians
    import math
    gradient_rad = math.atan(gradient_percent / 100)
    
    # Adjust effective friction coefficient for gradient
    # Downhill: gravity helps braking, Uphill: gravity hinders braking
    g = 9.81
    gradient_factor = math.sin(gradient_rad)
    effective_g = g * (friction_coefficient * math.cos(gradient_rad) + gradient_factor)
    
    # Braking distance with gradient correction
    braking_distance_corrected = (speed_ms ** 2) / (2 * effective_g * efficiency)
    
    return {
        'reaction_distance_m': reaction_distance,
        'braking_distance_m': braking_distance_corrected,
        'total_distance_m': reaction_distance + braking_distance_corrected,
        'reaction_time_s': reaction_time,
        'effective_deceleration_g': effective_g / g
    }


def braking_distance_with_aero(speed_ms, friction_coefficient, mass, 
                              drag_coefficient, frontal_area, air_density=1.225,
                              efficiency=1.0):
    """
    Calculate braking distance including aerodynamic drag (important for high speeds).
    
    Parameters:
    - speed_ms (float): Initial speed in m/s
    - friction_coefficient (float): Tire-road friction coefficient
    - mass (float): Vehicle mass in kg
    - drag_coefficient (float): Cd
    - frontal_area (float): Frontal area in m²
    - air_density (float): Air density in kg/m³ (default 1.225 at sea level)
    - efficiency (float): Brake efficiency
    
    Returns:
    - float: Braking distance in meters
    
    Note: This uses numerical integration for accuracy.
    """
    import numpy as np
    
    g = 9.81
    dt = 0.01  # Time step for integration
    distance = 0
    velocity = speed_ms
    
    # Aerodynamic drag force: F_drag = 0.5 * ρ * Cd * A * v²
    drag_factor = 0.5 * air_density * drag_coefficient * frontal_area
    
    while velocity > 0.1:  # Stop when velocity < 0.1 m/s
        # Braking force: F_brake = μ * m * g * efficiency
        braking_force = friction_coefficient * mass * g * efficiency
        
        # Drag force at current velocity
        drag_force = drag_factor * (velocity ** 2)
        
        # Total decelerating force
        total_force = braking_force + drag_force
        
        # Deceleration
        deceleration = total_force / mass
        
        # Update velocity and distance
        velocity -= deceleration * dt
        distance += velocity * dt
    
    return distance


# Example usage
if __name__ == "__main__":
    print("=== BASIC EXAMPLE (Your Original) ===")
    v = 30  # m/s (~108 km/h)
    mu = 0.9
    result = theoretical_braking_distance(v, mu)
    print(f"Theoretical braking distance: {result:.2f} meters")
    
    print("\n=== PRACTICAL EXAMPLE ===")
    # More realistic scenario
    speed_kmh = 100  # km/h
    mu_dry = 0.8
    mu_wet = 0.4
    
    dry_distance = braking_distance_from_kmh(speed_kmh, mu_dry, efficiency=0.85)
    wet_distance = braking_distance_from_kmh(speed_kmh, mu_wet, efficiency=0.85)
    
    print(f"At {speed_kmh} km/h on dry road (μ={mu_dry}):")
    print(f"  Braking distance: {dry_distance:.1f} m")
    
    print(f"\nAt {speed_kmh} km/h on wet road (μ={mu_wet}):")
    print(f"  Braking distance: {wet_distance:.1f} m")
    print(f"  WET is {wet_distance/dry_distance:.1f}x longer!")
    
    print("\n=== TOTAL STOPPING DISTANCE ===")
    # Including reaction time
    stopping = total_stopping_distance(
        speed_ms=27.8,  # 100 km/h
        friction_coefficient=0.8,
        reaction_time=1.2,  # Alert driver
        gradient_percent=-5  # 5% downhill
    )
    
    print(f"Total stopping distance (100 km/h, 5% downhill, alert driver):")
    print(f"  Reaction distance: {stopping['reaction_distance_m']:.1f} m")
    print(f"  Braking distance: {stopping['braking_distance_m']:.1f} m")
    print(f"  TOTAL: {stopping['total_distance_m']:.1f} m")
    print(f"  Effective deceleration: {stopping['effective_deceleration_g']:.2f} g")
    
    print("\n=== HIGH-SPEED WITH AERODYNAMICS ===")
    # Sports car example
    aero_distance = braking_distance_with_aero(
        speed_ms=80,  # 288 km/h
        friction_coefficient=1.1,  # Racing tires
        mass=1500,
        drag_coefficient=0.3,
        frontal_area=2.2,
        efficiency=0.95
    )
    
    simple_distance = theoretical_braking_distance(80, 1.1, 0.95)
    
    print(f"High-speed braking (288 km/h):")
    print(f"  Simple calculation: {simple_distance:.1f} m")
    print(f"  With aerodynamics: {aero_distance:.1f} m")
    print(f"  Aerodynamics save: {simple_distance-aero_distance:.1f} m ({((simple_distance-aero_distance)/simple_distance*100):.1f}%)")
