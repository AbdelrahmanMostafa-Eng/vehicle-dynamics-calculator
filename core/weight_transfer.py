# weight_transfer.py
"""
Longitudinal weight transfer calculations for vehicle dynamics.
"""

def longitudinal_weight_transfer(mass, acceleration, cg_height, wheelbase):
    """
    Calculate longitudinal weight transfer during acceleration/braking.
    
    Parameters:
    - mass (float): Mass of the vehicle in kg.
    - acceleration (float): Longitudinal acceleration in m/s².
      Use NEGATIVE value for braking/deceleration.
    - cg_height (float): Height of the center of gravity in meters.
    - wheelbase (float): Wheelbase of the vehicle in meters.
    
    Returns:
    - float: Weight transfer force in Newtons.
      Negative value = weight transfers FORWARD (braking)
      Positive value = weight transfers REARWARD (acceleration)
      
    Formula: ΔW = (h × m × a) / L
    where h = CG height, m = mass, a = acceleration, L = wheelbase
    """
    # Validate inputs
    if mass <= 0:
        raise ValueError("Mass must be positive")
    if wheelbase <= 0:
        raise ValueError("Wheelbase must be positive")
    if cg_height <= 0:
        raise ValueError("CG height must be positive")
    
    delta_weight = (cg_height * mass * acceleration) / wheelbase
    return delta_weight


def longitudinal_weight_transfer_g(mass_kg, acceleration_g, cg_height_m, wheelbase_m):
    """
    Calculate longitudinal weight transfer using g-forces.
    
    Parameters:
    - mass_kg (float): Mass in kg.
    - acceleration_g (float): Acceleration in g-forces (negative for braking).
    - cg_height_m (float): CG height in meters.
    - wheelbase_m (float): Wheelbase in meters.
    
    Returns:
    - float: Weight transfer in kg (not Newtons).
    """
    g = 9.81  # m/s²
    acceleration_ms2 = acceleration_g * g
    delta_weight_n = longitudinal_weight_transfer(mass_kg, acceleration_ms2, 
                                                 cg_height_m, wheelbase_m)
    # Convert Newtons to kg for more intuitive understanding
    delta_weight_kg = delta_weight_n / g
    return delta_weight_kg


def interpret_weight_transfer(delta_weight_n, vehicle_weight_n=None):
    """
    Interpret weight transfer result in human-readable form.
    
    Parameters:
    - delta_weight_n (float): Weight transfer force in Newtons.
    - vehicle_weight_n (float, optional): Total vehicle weight in Newtons.
    
    Returns:
    - dict: Interpretation of the result.
    """
    g = 9.81
    delta_kg = delta_weight_n / g
    
    interpretation = {
        'force_n': delta_weight_n,
        'mass_kg': delta_kg,
        'direction': 'FORWARD' if delta_weight_n < 0 else 'REARWARD',
        'magnitude_kg': abs(delta_kg)
    }
    
    if vehicle_weight_n:
        static_weight_kg = vehicle_weight_n / g
        percentage = (abs(delta_kg) / static_weight_kg) * 100
        interpretation['percentage_of_vehicle'] = percentage
    
    return interpretation


# Example usage with enhanced output
if __name__ == "__main__":
    print("=== LONGITUDINAL WEIGHT TRANSFER CALCULATION ===\n")
    
    # Vehicle parameters
    m = 1200                # kg
    a_braking = -9.0        # m/s² (deceleration, negative)
    h = 0.5                 # m (CG height)
    L = 2.5                 # m (wheelbase)
    
    # Calculate using main function
    delta_n = longitudinal_weight_transfer(m, a_braking, h, L)
    
    # Calculate in g's
    a_g = a_braking / 9.81  # Convert to g-forces
    delta_kg = longitudinal_weight_transfer_g(m, a_g, h, L)
    
    # Interpretation
    total_weight_n = m * 9.81
    interpretation = interpret_weight_transfer(delta_n, total_weight_n)
    
    print(f"VEHICLE PARAMETERS:")
    print(f"  Mass: {m} kg")
    print(f"  CG height: {h} m")
    print(f"  Wheelbase: {L} m")
    print(f"  Braking deceleration: {abs(a_braking):.1f} m/s² ({abs(a_g):.2f} g)\n")
    
    print(f"WEIGHT TRANSFER RESULTS:")
    print(f"  Transfer force: {delta_n:.1f} N")
    print(f"  Transfer mass: {interpretation['magnitude_kg']:.1f} kg")
    print(f"  Direction: {interpretation['direction']}")
    
    if 'percentage_of_vehicle' in interpretation:
        print(f"  Percentage of total mass: {interpretation['percentage_of_vehicle']:.1f}%\n")
    
    print(f"INTERPRETATION:")
    if interpretation['direction'] == 'FORWARD':
        print(f"  During braking, {interpretation['magnitude_kg']:.0f} kg transfers")
        print(f"  from the rear axle to the front axle.")
        print(f"  Front tires gain load, rear tires lose load.")
    else:
        print(f"  During acceleration, {interpretation['magnitude_kg']:.0f} kg transfers")
        print(f"  from the front axle to the rear axle.")
        print(f"  Rear tires gain load, front tires lose load.")
    
    # Show effect on individual axles (simplified)
    print(f"\nEFFECT ON AXLE LOADS (assuming 50/50 static distribution):")
    static_axle_load_kg = m / 2
    if interpretation['direction'] == 'FORWARD':
        front_after = static_axle_load_kg + interpretation['magnitude_kg']
        rear_after = static_axle_load_kg - interpretation['magnitude_kg']
        print(f"  Front axle: {static_axle_load_kg:.0f} → {front_after:.0f} kg (+{interpretation['magnitude_kg']:.0f} kg)")
        print(f"  Rear axle:  {static_axle_load_kg:.0f} → {rear_after:.0f} kg (-{interpretation['magnitude_kg']:.0f} kg)")
    else:
        front_after = static_axle_load_kg - interpretation['magnitude_kg']
        rear_after = static_axle_load_kg + interpretation['magnitude_kg']
        print(f"  Front axle: {static_axle_load_kg:.0f} → {front_after:.0f} kg (-{interpretation['magnitude_kg']:.0f} kg)")
        print(f"  Rear axle:  {static_axle_load_kg:.0f} → {rear_after:.0f} kg (+{interpretation['magnitude_kg']:.0f} kg)")
