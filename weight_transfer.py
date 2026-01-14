# weight_transfer.py

def longitudinal_weight_transfer(mass, acceleration, cg_height, wheelbase):
    """
    Calculate longitudinal weight transfer during braking.

    Parameters:
    - Mass (kg): Mass of the vehicle.
    - Acceleration (m/s^2): Acceleration (negative value for deceleration/braking).
    - CG_height (m): Height of the center of gravity.
    - Wheelbase (m): Wheelbase of the vehicle.
    
    Returns:
    - delta_weight (N): Weight transfer force in Newtons.
    """
    
    delta_weight = (cg_height * mass * acceleration) / wheelbase
    return delta_weight

# Example usage
if __name__ == "__main__":
    m = 1200                # kg
    a_braking = -9.0        # m/s^2 (deceleration, negative)
    h = 0.5                 # m (CG height)
    L = 2.5                 # m (wheelbase)

    result = longitudinal_weight_transfer(m,  a_braking, h, L)
    print(f"Weight transfer during braking: {result:.2f} N")
