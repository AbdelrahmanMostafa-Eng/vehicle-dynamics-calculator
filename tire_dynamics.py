# tire_dynamics.py
"""
Tire grip and load sensitivity models for vehicle dynamics.
Based on Pacejka "Magic Formula" and real tire data trends.
"""

def linear_grip_model(load_n, base_mu=1.0, reference_load_n=4000, sensitivity_per_n=0.00001):
    """
    Linear tire grip model (your original, improved).
    
    Parameters:
    - load_n (float): Vertical load in Newtons
    - base_mu (float): Friction coefficient at reference load (typical: 1.0-1.2)
    - reference_load_n (float): Load where base_mu is measured (typical: 3000-5000N)
    - sensitivity_per_n (float): Grip loss per Newton above reference (typical: 1e-5)
    
    Returns:
    - float: Effective friction coefficient
    
    Note: Linear model underestimates grip at low loads, overestimates at high loads.
    """
    effective_mu = base_mu * (1 - sensitivity_per_n * (load_n - reference_load_n))
    # Add reasonable bounds
    return max(0.1, min(2.0, effective_mu))


def pacejka_grip_model(load_n, d=1.0, c=1.65, b=10, reference_load=4000):
    """
    Simplified Pacejka "Magic Formula" for tire grip.
    
    Parameters:
    - load_n (float): Vertical load in Newtons
    - d (float): Peak value factor (typically 1.0-1.3)
    - c (float): Shape factor (typically 1.65 for grip curve)
    - b (float): Stiffness factor (typically 10-15)
    - reference_load (float): Normalization load
    
    Returns:
    - float: Normalized grip coefficient (0 to ~1.3)
    
    Note: Simplified version of: μ = D * sin(C * arctan(B * x))
    where x = (load / reference_load)
    """
    import math
    x = load_n / reference_load
    # Simplified Pacejka formula
    mu = d * math.sin(c * math.atan(b * x))
    return mu


def real_tire_grip(load_n, tire_type='street'):
    """
    Empirical tire grip models based on real tire data.
    
    Parameters:
    - load_n (float): Vertical load in Newtons
    - tire_type (str): 'street', 'performance', 'race_slick', 'rain'
    
    Returns:
    - float: Estimated friction coefficient
    
    Based on tire testing data trends:
    - Grip increases with load but at a decreasing rate
    - Peak grip typically around optimal load (varies by tire)
    - Overload reduces grip significantly
    """
    # Convert to kg for easier reference (car tires typically 300-800 kg each)
    load_kg = load_n / 9.81
    
    # Empirical models based on tire testing data
    if tire_type == 'street':
        # Typical all-season tire
        optimal_load_kg = 450
        peak_mu = 0.9
        if load_kg <= optimal_load_kg:
            mu = peak_mu * (load_kg / optimal_load_kg) ** 0.5
        else:
            mu = peak_mu * (optimal_load_kg / load_kg) ** 0.3
    
    elif tire_type == 'performance':
        # Summer performance tire
        optimal_load_kg = 400
        peak_mu = 1.1
        if load_kg <= optimal_load_kg:
            mu = peak_mu * (load_kg / optimal_load_kg) ** 0.6
        else:
            mu = peak_mu * (optimal_load_kg / load_kg) ** 0.4
    
    elif tire_type == 'race_slick':
        # Racing slick (very load sensitive)
        optimal_load_kg = 350
        peak_mu = 1.4
        if load_kg <= optimal_load_kg:
            mu = peak_mu * (load_kg / optimal_load_kg) ** 0.7
        else:
            mu = peak_mu * (optimal_load_kg / load_kg) ** 0.5
    
    elif tire_type == 'rain':
        # Wet weather tire
        optimal_load_kg = 400
        peak_mu = 0.7
        if load_kg <= optimal_load_kg:
            mu = peak_mu * (load_kg / optimal_load_kg) ** 0.4
        else:
            mu = peak_mu * (optimal_load_kg / load_kg) ** 0.2
    
    else:
        raise ValueError(f"Unknown tire type: {tire_type}")
    
    return mu


def axle_total_grip(front_left_load, front_right_load, rear_left_load, rear_right_load, 
                   tire_type='street', consider_camber=False, camber_angle_deg=0):
    """
    Calculate total cornering/braking capacity of an axle considering load transfer.
    
    Parameters:
    - Loads in Newtons for each tire
    - tire_type (str): Type of tire
    - consider_camber (bool): Include camber effects
    - camber_angle_deg (float): Camber angle in degrees (negative = negative camber)
    
    Returns:
    - dict: Contains per-tire grip and total axle grip
    """
    # Calculate individual tire grips
    fl_grip = real_tire_grip(front_left_load, tire_type)
    fr_grip = real_tire_grip(front_right_load, tire_type)
    rl_grip = real_tire_grip(rear_left_load, tire_type)
    rr_grip = real_tire_grip(rear_right_load, tire_type)
    
    # Apply camber effects if requested
    if consider_camber:
        import math
        # Camber gain: typically 0.01-0.02 μ per degree of negative camber
        camber_gain = 0.015 * abs(camber_angle_deg)
        if camber_angle_deg < 0:  # Negative camber improves cornering grip
            cornering_gain = 1.0 + camber_gain
            # Camber hurts straight-line braking slightly
            braking_factor = 1.0 - 0.005 * abs(camber_angle_deg)
        else:
            cornering_gain = 1.0
            braking_factor = 1.0
    
    # Total cornering force capacity (sum of lateral forces)
    total_cornering_capacity = (
        fl_grip * front_left_load +
        fr_grip * front_right_load +
        rl_grip * rear_left_load +
        rr_grip * rear_right_load
    )
    
    # Total braking force capacity
    total_braking_capacity = (
        fl_grip * front_left_load * (braking_factor if consider_camber else 1.0) +
        fr_grip * front_right_load * (braking_factor if consider_camber else 1.0) +
        rl_grip * rear_left_load * (brazing_factor if consider_camber else 1.0) +
        rr_grip * rear_right_load * (brazing_factor if consider_camber else 1.0)
    )
    
    return {
        'front_left': {'load_n': front_left_load, 'mu': fl_grip, 'force_n': fl_grip * front_left_load},
        'front_right': {'load_n': front_right_load, 'mu': fr_grip, 'force_n': fr_grip * front_right_load},
        'rear_left': {'load_n': rear_left_load, 'mu': rl_grip, 'force_n': rl_grip * rear_left_load},
        'rear_right': {'load_n': rear_right_load, 'mu': rr_grip, 'force_n': rr_grip * rear_right_load},
        'total_cornering_n': total_cornering_capacity,
        'total_braking_n': total_braking_capacity,
        'average_mu': total_cornering_capacity / (front_left_load + front_right_load + 
                                                 rear_left_load + rear_right_load)
    }


# Example usage
if __name__ == "__main__":
    print("=== TIRE GRIP MODELS COMPARISON ===")
    
    # Test loads (typical car: 3500-4500 N per tire)
    test_loads = [2000, 3000, 4000, 5000, 6000]  # N
    
    print("Load (N) | Linear Model | Pacejka | Street Tire | Race Tire")
    print("-" * 60)
    
    for load in test_loads:
        linear = linear_grip_model(load, base_mu=1.0, reference_load_n=4000, sensitivity_per_n=0.00001)
        pacejka = pacejka_grip_model(load, d=1.2, reference_load=4000)
        street = real_tire_grip(load, 'street')
        race = real_tire_grip(load, 'race_slick')
        
        print(f"{load:7.0f} | {linear:12.3f} | {pacejka:7.3f} | {street:10.3f} | {race:9.3f}")
    
    print("\n=== KEY INSIGHT ===")
    print("Notice how grip INCREASES with load initially, then decreases.")
    print("Your linear model shows only decrease, which is unrealistic.")
    
    print("\n=== REAL-WORLOAD EXAMPLE ===")
    # Simulate braking weight transfer
    static_load = 4000  # N per tire (typical midsize car)
    brake_transfer = 800  # N transferred from rear to front during braking
    
    front_load_braking = static_load + brake_transfer
    rear_load_braking = static_load - brake_transfer
    
    print(f"During hard braking:")
    print(f"  Front tire load: {front_load_braking:.0f} N")
    print(f"  Rear tire load: {rear_load_braking:.0f} N")
    
    front_grip = real_tire_grip(front_load_braking, 'performance')
    rear_grip = real_tire_grip(rear_load_braking, 'performance')
    
    print(f"  Front tire μ: {front_grip:.3f}")
    print(f"  Rear tire μ: {rear_grip:.3f}")
    
    # Calculate total braking force
    total_braking_force = 2 * (front_grip * front_load_braking + rear_grip * rear_load_braking)
    vehicle_weight = 4 * static_load  # N
    deceleration_g = total_braking_force / vehicle_weight
    
    print(f"  Total braking force: {total_braking_force/1000:.1f} kN")
    print(f"  Deceleration: {deceleration_g:.2f} g")
    
    print("\n=== CORNERING EXAMPLE ===")
    # During cornering, outside tires get more load
    front_outside = 5000  # N
    front_inside = 3000   # N
    rear_outside = 4500   # N
    rear_inside = 3500    # N
    
    axle_grip = axle_total_grip(front_inside, front_outside, rear_inside, rear_outside, 'performance')
    
    print(f"During cornering with load transfer:")
    print(f"  Front outside: {axle_grip['front_right']['force_n']/1000:.1f} kN (μ={axle_grip['front_right']['mu']:.3f})")
    print(f"  Front inside:  {axle_grip['front_left']['force_n']/1000:.1f} kN (μ={axle_grip['front_left']['mu']:.3f})")
    print(f"  Total cornering capacity: {axle_grip['total_cornering_n']/1000:.1f} kN")
    print(f"  Average μ: {axle_grip['average_mu']:.3f}")
