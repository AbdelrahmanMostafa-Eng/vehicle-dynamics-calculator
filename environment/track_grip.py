#track_grip.py

"""
track_grip.py — Track surface grip modeling
"""

def grip_coefficient(base_grip: float, condition: str) -> float:
    """
    Adjust grip coefficient based on track condition.

    Parameters:
        base_grip (float): Base grip coefficient [-]
        condition (str): Track condition ("dry", "wet", "rubbered", "dusty")

    Returns:
        float: Adjusted grip coefficient [-]
    """
    condition = condition.lower()
    if condition == "dry":
        return base_grip
    elif condition == "wet":
        return base_grip * 0.6
    elif condition == "rubbered":
        return base_grip * 1.1
    elif condition == "dusty":
        return base_grip * 0.8
    else:
        return base_grip


def combined_grip(base_grip: float, condition: str, temp_effect: float) -> float:
    """
    Combine track condition and temperature effect.

    Parameters:
        base_grip (float): Base grip coefficient [-]
        condition (str): Track condition
        temp_effect (float): Grip multiplier from temperature

    Returns:
        float: Final grip coefficient [-]
    """
    return grip_coefficient(base_grip, condition) * temp_effect


# Example usage
if __name__ == "__main__":
    base = 1.2
    condition = "wet"
    temp_effect = 0.95

    g = combined_grip(base, condition, temp_effect)
    print(f"Grip coefficient under {condition} = {g:.3f}")
