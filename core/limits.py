#limits.py

"""
Tire force limits and friction models for vehicle dynamics.
Production-ready with realistic physics and robust error handling.
"""

import math
from typing import Dict, Tuple, Optional, Union
from dataclasses import dataclass
from enum import Enum


class TireType(Enum):
    """Tire compound classifications."""
    STREET = "street"
    PERFORMANCE = "performance"
    RACE_SLICK = "race_slick"
    RAIN = "rain"
    WINTER = "winter"


@dataclass
class TireState:
    """Complete state of a tire for accurate limit calculation."""
    vertical_load: float          # Fz [N]
    slip_ratio: float            # κ [-]
    slip_angle: float            # α [rad]
    temperature: float           # T [°C]
    wear: float                  # [0-1]
    pressure: float              # P [kPa]
    type: TireType = TireType.PERFORMANCE
    
    def validate(self):
        """Validate tire state parameters."""
        if self.vertical_load <= 0:
            raise ValueError(f"Vertical load must be positive, got {self.vertical_load}N")
        if not -50 <= self.temperature <= 150:
            raise ValueError(f"Temperature out of range: {self.temperature}°C")
        if not 0 <= self.wear <= 1:
            raise ValueError(f"Wear must be between 0 and 1, got {self.wear}")
        if not 100 <= self.pressure <= 400:
            raise ValueError(f"Pressure out of range: {self.pressure}kPa")
        return True

