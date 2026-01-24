#brake_migration.py

"""
Dynamic brake bias adjustment
"""

def brake_migration(initial_bias: float, migration_rate: float,
                    brake_pressure: float, max_pressure: float) -> float:
    """
    Calculate dynamic brake bias under braking.

    Parameters:
        initial_bias (float): Static front brake bias fraction (0–1)
        migration_rate (float): Bias shift rate per unit brake pressure [-]
        brake_pressure (float): Current brake pressure [bar]
        max_pressure (float): Maximum brake pressure [bar]

    Returns:
        float: Adjusted front brake bias fraction (0–1)
    """
    # Normalize brake pressure
    pressure_fraction = brake_pressure / max_pressure

    # Bias shift proportional to brake pressure
    migrated_bias = initial_bias - migration_rate * pressure_fraction

    # Clamp to [0, 1]
    return max(0.0, min(1.0, migrated_bias))


# Example usage
if __name__ == "__main__":
    initial = 0.60       # 60% front bias
    migration_rate = 0.05
    brake_pressure = 80  # bar
    max_pressure = 100   # bar

    bias = brake_migration(initial, migration_rate, brake_pressure, max_pressure)
    print(f"Dynamic brake bias = {bias:.3f} (fraction front)")
