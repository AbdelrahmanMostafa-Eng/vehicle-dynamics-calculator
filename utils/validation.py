#validation.py

"""
Input validation helpers
"""

def validate_positive(value: float, name: str = "value") -> None:
    """Ensure a value is positive."""
    if value <= 0:
        raise ValueError(f"{name} must be positive, got {value}")

def validate_nonnegative(value: float, name: str = "value") -> None:
    """Ensure a value is non-negative."""
    if value < 0:
        raise ValueError(f"{name} must be non-negative, got {value}")

def validate_percentage(value: float, name: str = "percentage") -> None:
    """Ensure a value is between 0 and 1."""
    if not (0 <= value <= 1):
        raise ValueError(f"{name} must be between 0 and 1, got {value}")


# Example usage
if __name__ == "__main__":
    try:
        validate_positive(-5, "speed")
    except ValueError as e:
        print(e)

    try:
        validate_nonnegative(-1, "fuel")
    except ValueError as e:
        print(e)

    try:
        validate_percentage(1.5, "grip")
    except ValueError as e:
        print(e)
