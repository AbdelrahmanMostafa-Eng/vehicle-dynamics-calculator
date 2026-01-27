#units.py

"""
Unit conversion helpers
"""

def kmh_to_ms(speed_kmh: float) -> float:
    """Convert km/h to m/s."""
    return speed_kmh / 3.6

def ms_to_kmh(speed_ms: float) -> float:
    """Convert m/s to km/h."""
    return speed_ms * 3.6

def kg_to_lbs(mass_kg: float) -> float:
    """Convert kilograms to pounds."""
    return mass_kg * 2.20462

def lbs_to_kg(mass_lbs: float) -> float:
    """Convert pounds to kilograms."""
    return mass_lbs / 2.20462


# Example usage
if __name__ == "__main__":
    print(f"100 km/h = {kmh_to_ms(100):.2f} m/s")
    print(f"27.8 m/s = {ms_to_kmh(27.8):.1f} km/h")
    print(f"50 kg = {kg_to_lbs(50):.1f} lbs")
    print(f"110 lbs = {lbs_to_kg(110):.1f} kg")
