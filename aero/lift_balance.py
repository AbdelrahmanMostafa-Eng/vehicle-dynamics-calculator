#lift_balance.py

"""
Aerodynamic balance calculations
"""

def aero_balance(front_downforce: float, rear_downforce: float) -> float:
    """
    Calculate aerodynamic balance (front vs rear).

    Parameters:
        front_downforce (float): Front axle downforce [N]
        rear_downforce (float): Rear axle downforce [N]

    Returns:
        float: Balance ratio (0 = all rear, 1 = all front)
    """
    total = front_downforce + rear_downforce
    return front_downforce / total if total > 1e-9 else 0.0


def balance_shift(balance: float, delta_front: float, delta_rear: float) -> float:
    """
    Calculate new balance after aero adjustments.

    Parameters:
        balance (float): Current balance ratio
        delta_front (float): Change in front downforce [N]
        delta_rear (float): Change in rear downforce [N]

    Returns:
        float: Updated balance ratio
    """
    front_new = balance + delta_front
    rear_new = (1 - balance) + delta_rear
    total = front_new + rear_new
    return front_new / total if total > 1e-9 else 0.0


# Example usage
if __name__ == "__main__":
    balance = aero_balance(front_downforce=1200, rear_downforce=1800)
    print(f"Aero balance = {balance:.2f}")

    new_balance = balance_shift(balance, delta_front=100, delta_rear=-50)
    print(f"Updated balance = {new_balance:.2f}")
