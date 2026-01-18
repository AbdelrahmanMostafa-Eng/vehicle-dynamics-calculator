#tire_degradation.py

"""
Tire wear and performance degradation

Models tire wear progression and its effect on grip.
"""

def tire_wear(prev_wear: float, distance_km: float, hardness: float = 1.0) -> float:
    """
    Update tire wear level based on distance traveled.

    Parameters:
        prev_wear (float): Previous wear level [0 = new, 1 = fully worn]
        distance_km (float): Distance traveled [km]
        hardness (float): Compound hardness (soft=0.8, medium=1.0, hard=1.2)

    Returns:
        float: Updated wear level (clamped between 0 and 1)
    """
    wear_rate = 0.0001 * hardness
    new_wear = prev_wear + wear_rate * distance_km
    return min(1.0, max(0.0, new_wear))


def mu_with_wear(base_mu: float, wear: float) -> float:
    """
    Reduce friction coefficient based on wear level.

    Parameters:
        base_mu (float): Base friction coefficient
        wear (float): Wear level [0 = new, 1 = fully worn]

    Returns:
        float: Effective friction coefficient
    """
    degradation_factor = 1 - 0.2 * wear  # 20% loss at full wear
    return base_mu * degradation_factor


# Example usage
if __name__ == "__main__":
    wear = 0.0
    base_mu = 1.1
    for lap in range(1, 6):
        wear = tire_wear(wear, distance_km=5, hardness=1.0)
        mu_eff = mu_with_wear(base_mu, wear)
        print(f"Lap {lap}: wear={wear:.3f}, effective μ={mu_eff:.3f}")
