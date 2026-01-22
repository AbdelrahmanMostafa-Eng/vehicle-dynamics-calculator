#brake_bias.py

"""
Brake bias calculations
"""

from typing import Dict

def brake_force_distribution(total_force: float, bias: float) -> Dict[str, float]:
    """
    Split braking force between front and rear axles.

    Parameters:
        total_force (float): Total braking force [N]
        bias (float): Front brake bias fraction (0–1)

    Returns:
        Dict[str, float]: {"front": front_force, "rear": rear_force}
    """
    bias = max(0.0, min(1.0, bias))  # clamp to [0, 1]
    front = total_force * bias
    rear = total_force * (1 - bias)
    return {"front": front, "rear": rear}


# Example usage
if __name__ == "__main__":
    dist = brake_force_distribution(total_force=8000.0, bias=0.60)
    print(f"Front = {dist['front']:.1f} N, Rear = {dist['rear']:.1f} N")
