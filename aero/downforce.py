#downforce.py

"""
Aerodynamic downforce calculations
"""

def downforce(rho: float, Cl: float, A: float, v: float) -> float:
    """
    Calculate aerodynamic downforce.

    Parameters:
        rho (float): Air density [kg/m^3]
        Cl (float): Lift coefficient (positive for lift, negative for downforce)
        A (float): Reference area [m^2]
        v (float): Vehicle speed [m/s]

    Returns:
        float: Downforce [N]
    """
    return 0.5 * rho * Cl * A * v**2


def downforce_distribution(front_Cl: float, rear_Cl: float,
                           rho: float, A_front: float, A_rear: float, v: float) -> dict:
    """
    Calculate front and rear downforce separately.

    Parameters:
        front_Cl (float): Front lift coefficient
        rear_Cl (float): Rear lift coefficient
        rho (float): Air density [kg/m^3]
        A_front (float): Front wing area [m^2]
        A_rear (float): Rear wing area [m^2]
        v (float): Vehicle speed [m/s]

    Returns:
        dict: {"front": front_downforce, "rear": rear_downforce, "total": total_downforce}
    """
    front = 0.5 * rho * front_Cl * A_front * v**2
    rear = 0.5 * rho * rear_Cl * A_rear * v**2
    return {"front": front, "rear": rear, "total": front + rear}


# Example usage
if __name__ == "__main__":
    rho = 1.225
    Cl = -3.0   # negative for downforce
    A = 1.6
    v = 60.0    # m/s (~216 km/h)

    Df = downforce(rho, Cl, A, v)
    print(f"Total downforce = {Df:.1f} N")

    dist = downforce_distribution(front_Cl=-1.2, rear_Cl=-1.8,
                                  rho=1.225, A_front=0.6, A_rear=1.0, v=60)
    print(f"Front = {dist['front']:.1f} N, Rear = {dist['rear']:.1f} N, Total = {dist['total']:.1f} N")
