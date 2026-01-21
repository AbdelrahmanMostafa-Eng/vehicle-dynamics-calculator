#engine.py

"""
Engine torque maps
"""

from typing import Dict

def torque_map(rpm: int, torque_curve: Dict[int, float]) -> float:
    """
    Get engine torque at a given RPM using a torque curve.

    Parameters:
        rpm (int): Engine speed [RPM]
        torque_curve (Dict[int, float]): Mapping of RPM to torque [Nm]

    Returns:
        float: Torque [Nm]
    """
    # Find nearest RPM point in curve
    closest_rpm = min(torque_curve.keys(), key=lambda x: abs(x - rpm))
    return torque_curve[closest_rpm]


def power_output(rpm: int, torque: float) -> float:
    """
    Calculate engine power from torque and RPM.

    Parameters:
        rpm (int): Engine speed [RPM]
        torque (float): Torque [Nm]

    Returns:
        float: Power [kW]
    """
    return (torque * rpm * 2 * 3.1416 / 60) / 1000


# Example usage
if __name__ == "__main__":
    curve = {1000: 150, 3000: 250, 6000: 300, 9000: 280}
    rpm = 6000
    tq = torque_map(rpm, curve)
    pw = power_output(rpm, tq)

    print(f"At {rpm} RPM → Torque = {tq:.1f} Nm, Power = {pw:.1f} kW")
