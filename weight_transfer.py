# weight_transfer.py

def weight_transfer(mass, deceleration, cg_height, wheelbase):
    """
    Calculate longitudinal weight transfer during braking.

    Parameters:
    - mass (kg): Vehicle mass
    - deceleration (m/s^2): Braking deceleration
    - cg_height (m): Center of gravity height
    - wheelbase (m): Distance between front and rear axles

    Returns:
    - delta_weight (N): Weight transferred to front axle
    """
    g = 9.81  # gravity (m/s^2)
    delta_weight = (cg_height * mass * deceleration) / wheelbase
    return delta_weight

# Example usage
if __name__ == "__main__":
    m = 1200       # kg
    a = 9.0        # m/s^2 deceleration
    h = 0.5        # m (CG height)
    L = 2.5        # m (wheelbase)

    result = weight_transfer(m, a, h, L)
    print(f"Weight transfer during braking: {result:.2f} N")
