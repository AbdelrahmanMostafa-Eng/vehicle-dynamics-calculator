#geometry.py

"""
Suspension geometry calculations
"""

def roll_center(front_track: float, rear_track: float,
                front_ic_height: float, rear_ic_height: float,
                cg_height: float) -> float:
    """
    Estimate roll center height.

    Parameters:
        front_track (float): Front track width [m]
        rear_track (float): Rear track width [m]
        front_ic_height (float): Front instant center height [m]
        rear_ic_height (float): Rear instant center height [m]
        cg_height (float): Center of gravity height [m]

    Returns:
        float: Approximate roll center height [m]
    """
    # Simplified average of front and rear instant centers relative to CG
    return (front_ic_height * rear_track + rear_ic_height * front_track) / (front_track + rear_track)


def anti_dive(susp_angle: float, cg_height: float, wheelbase: float) -> float:
    """
    Calculate anti-dive percentage.

    Parameters:
        susp_angle (float): Suspension angle relative to horizontal [rad]
        cg_height (float): Center of gravity height [m]
        wheelbase (float): Wheelbase [m]

    Returns:
        float: Anti-dive [%]
    """
    return (cg_height / wheelbase) * (susp_angle * 100)


def anti_squat(susp_angle: float, cg_height: float, wheelbase: float) -> float:
    """
    Calculate anti-squat percentage.

    Parameters:
        susp_angle (float): Suspension angle relative to horizontal [rad]
        cg_height (float): Center of gravity height [m]
        wheelbase (float): Wheelbase [m]

    Returns:
        float: Anti-squat [%]
    """
    return (cg_height / wheelbase) * (susp_angle * 100)


# Example usage
if __name__ == "__main__":
    rc = roll_center(front_track=1.6, rear_track=1.5,
                     front_ic_height=0.15, rear_ic_height=0.20,
                     cg_height=0.30)
    print(f"Roll center height = {rc:.3f} m")

    ad = anti_dive(susp_angle=0.05, cg_height=0.30, wheelbase=3.0)
    print(f"Anti-dive = {ad:.1f} %")

    asq = anti_squat(susp_angle=0.04, cg_height=0.30, wheelbase=3.0)
    print(f"Anti-squat = {asq:.1f} %")
