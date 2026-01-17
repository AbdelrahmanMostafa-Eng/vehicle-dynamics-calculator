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


class FrictionModels:
    """Friction models with empirical parameters."""
    
    BASE_MU = {
        TireType.STREET:      {"mu_x": 0.9,  "mu_y": 0.85, "Fz_ref": 4000},
        TireType.PERFORMANCE: {"mu_x": 1.1,  "mu_y": 1.05, "Fz_ref": 4000},
        TireType.RACE_SLICK:  {"mu_x": 1.4,  "mu_y": 1.35, "Fz_ref": 3500},
        TireType.RAIN:        {"mu_x": 0.7,  "mu_y": 0.65, "Fz_ref": 4000},
        TireType.WINTER:      {"mu_x": 0.65, "mu_y": 0.6,  "Fz_ref": 4000}
    }
    
    LOAD_SENSITIVITY = {
        TireType.STREET:      {"exp_x": -0.1, "exp_y": -0.12},
        TireType.PERFORMANCE: {"exp_x": -0.15, "exp_y": -0.18},
        TireType.RACE_SLICK:  {"exp_x": -0.2, "exp_y": -0.25},
        TireType.RAIN:        {"exp_x": -0.08, "exp_y": -0.1},
        TireType.WINTER:      {"exp_x": -0.05, "exp_y": -0.07}
    }
    
    TEMP_PARAMS = {
        "opt_temp": 80.0,
        "cold_temp": 0.0,
        "hot_temp": 120.0,
        "cold_mu": 0.6,
        "hot_mu": 0.8
    }
    
    WEAR_SENSITIVITY = 0.2
    PRESSURE_OPT = 200.0
    PRESSURE_SENSITIVITY = 0.001


class TireLimits:
    """Main class for calculating tire force limits."""
    
    def __init__(self, tire_state: TireState):
        tire_state.validate()
        self.state = tire_state
        self.models = FrictionModels()
    
    def _calculate_temp_factor(self) -> float:
        """Calculate temperature effect on grip."""
        params = self.models.TEMP_PARAMS
        temp = self.state.temperature
        
        if temp <= params["opt_temp"]:
            if temp <= params["cold_temp"]:
                return params["cold_mu"]
            t_norm = (temp - params["cold_temp"]) / (params["opt_temp"] - params["cold_temp"])
            return params["cold_mu"] + (1.0 - params["cold_mu"]) * t_norm
        else:
            if temp >= params["hot_temp"]:
                return params["hot_mu"]
            t_norm = (temp - params["opt_temp"]) / (params["hot_temp"] - params["opt_temp"])
            return 1.0 - (1.0 - params["hot_mu"]) * t_norm
    
    def get_effective_friction(self) -> Dict[str, float]:
        """Calculate effective friction coefficients."""
        base = self.models.BASE_MU[self.state.type]
        load_exp = self.models.LOAD_SENSITIVITY[self.state.type]
        
        Fz_ref = base["Fz_ref"]
        load_ratio = self.state.vertical_load / Fz_ref
        
        mu_x_load = base["mu_x"] * (load_ratio ** load_exp["exp_x"])
        mu_y_load = base["mu_y"] * (load_ratio ** load_exp["exp_y"])
        
        temp_factor = self._calculate_temp_factor()
        wear_factor = 1.0 - self.models.WEAR_SENSITIVITY * self.state.wear
        
        pressure_diff = abs(self.state.pressure - self.models.PRESSURE_OPT)
        pressure_factor = 1.0 - self.models.PRESSURE_SENSITIVITY * pressure_diff
        pressure_factor = max(0.8, min(1.0, pressure_factor))
        
        mu_x_eff = mu_x_load * temp_factor * wear_factor * pressure_factor
        mu_y_eff = mu_y_load * temp_factor * wear_factor * pressure_factor
        
        mu_x_eff = max(0.1, min(2.0, mu_x_eff))
        mu_y_eff = max(0.1, min(2.0, mu_y_eff))
        
        return {
            "mu_x": mu_x_eff,
            "mu_y": mu_y_eff,
            "load_ratio": load_ratio,
            "temp_factor": temp_factor,
            "wear_factor": wear_factor,
            "pressure_factor": pressure_factor,
            "base_mu_x": base["mu_x"],
            "base_mu_y": base["mu_y"],
            "Fz_ref": Fz_ref
        }
    
    def friction_ellipse_limit(self, Fx: float, Fy: float) -> Dict[str, Union[bool, float]]:
        """Elliptical friction model - primary check."""
        mu = self.get_effective_friction()
        Fz = self.state.vertical_load
        
        Fx_max = mu["mu_x"] * Fz
        Fy_max = mu["mu_y"] * Fz
        
        if abs(Fx_max) < 1e-9:
            fx_ratio_sq = float('inf') if abs(Fx) > 1e-9 else 0.0
        else:
            fx_ratio_sq = (Fx / Fx_max) ** 2
        
        if abs(Fy_max) < 1e-9:
            fy_ratio_sq = float('inf') if abs(Fy) > 1e-9 else 0.0
        else:
            fy_ratio_sq = (Fy / Fy_max) ** 2
        
        if fx_ratio_sq == float('inf') or fy_ratio_sq == float('inf'):
            ellipse_value = float('inf')
            usage = float('inf')
        else:
            ellipse_value = fx_ratio_sq + fy_ratio_sq
            usage = math.sqrt(ellipse_value)
        
        return {
            "within_limit": ellipse_value <= 1.0,
            "usage": usage,
            "ellipse_value": ellipse_value,
            "Fx_usage": abs(Fx) / Fx_max if abs(Fx_max) > 1e-9 else float('inf'),
            "Fy_usage": abs(Fy) / Fy_max if abs(Fy_max) > 1e-9 else float('inf'),
            "Fx_max": Fx_max,
            "Fy_max": Fy_max,
            "model": "ellipse"
        }
    
    def combined_slip_limit(self, Fx: float, Fy: float, 
                           coupling_factor: float = 0.3) -> Dict[str, Union[bool, float]]:
        """Combined slip model with proper bidirectional coupling."""
        mu = self.get_effective_friction()
        Fz = self.state.vertical_load
        
        Fx_max_nom = mu["mu_x"] * Fz
        Fy_max_nom = mu["mu_y"] * Fz
        
        coupling = max(0.0, min(0.5, coupling_factor))
        
        # Calculate normalized force usage
        Fx_usage = abs(Fx) / Fx_max_nom if Fx_max_nom > 1e-9 else 0.0
        Fy_usage = abs(Fy) / Fy_max_nom if Fy_max_nom > 1e-9 else 0.0
        
        # Bidirectional coupling: each force reduces opposite capacity
        lateral_reduction = 1.0 - coupling * Fx_usage
        longitudinal_reduction = 1.0 - coupling * Fy_usage
        
        # Apply reasonable limits
        lateral_reduction = max(0.5, min(1.0, lateral_reduction))
        longitudinal_reduction = max(0.5, min(1.0, longitudinal_reduction))
        
        # Effective maximum forces
        Fx_max_eff = Fx_max_nom * longitudinal_reduction
        Fy_max_eff = Fy_max_nom * lateral_reduction
        
        # Slip angle effect on lateral force
        optimal_slip = math.radians(8.0)
        slip_angle = abs(self.state.slip_angle)
        
        if slip_angle <= optimal_slip:
            slip_factor = math.sin(math.pi * slip_angle / (2 * optimal_slip))
        else:
            slip_factor = 1.0 - 0.2 * (slip_angle - optimal_slip) / optimal_slip
        
        slip_factor = max(0.6, min(1.0, slip_factor))
        Fy_max_eff *= slip_factor
        
        # Calculate usage
        if Fx_max_eff < 1e-9:
            fx_ratio_sq = float('inf') if abs(Fx) > 1e-9 else 0.0
        else:
            fx_ratio_sq = (Fx / Fx_max_eff) ** 2
        
        if Fy_max_eff < 1e-9:
            fy_ratio_sq = float('inf') if abs(Fy) > 1e-9 else 0.0
        else:
            fy_ratio_sq = (Fy / Fy_max_eff) ** 2
        
        if fx_ratio_sq == float('inf') or fy_ratio_sq == float('inf'):
            usage_sq = float('inf')
            usage = float('inf')
        else:
            usage_sq = fx_ratio_sq + fy_ratio_sq
            usage = math.sqrt(usage_sq)
        
        return {
            "within_limit": usage_sq <= 1.0,
            "usage": usage,
            "Fx_max_effective": Fx_max_eff,
            "Fy_max_effective": Fy_max_eff,
            "lateral_reduction": lateral_reduction,
            "longitudinal_reduction": longitudinal_reduction,
            "slip_factor": slip_factor,
            "model": "combined_slip"
        }
    
    def stability_assessment(self, Fx: float, Fy: float, 
                            warning_threshold: float = 0.85) -> Dict[str, Union[bool, float, str]]:
        """Comprehensive stability assessment."""
        ellipse_check = self.friction_ellipse_limit(Fx, Fy)
        combined_check = self.combined_slip_limit(Fx, Fy, coupling_factor=0.3)
        
        if ellipse_check["within_limit"]:
            if ellipse_check["usage"] > warning_threshold:
                status = "WARNING"
                color = "🟡"
                action = "APPROACHING LIMIT"
            else:
                status = "STABLE"
                color = "🟢"
                action = "OK"
        else:
            status = "UNSTABLE"
            color = "🔴"
            action = "REDUCE FORCE"
        
        # Force margin calculation
        current_angle = math.atan2(Fy, Fx) if abs(Fx) > 1e-9 else math.copysign(math.pi/2, Fy)
        mu = self.get_effective_friction()
        Fz = self.state.vertical_load
        
        cos_theta = math.cos(current_angle)
        sin_theta = math.sin(current_angle)
        mu_x = mu["mu_x"]
        mu_y = mu["mu_y"]
        
        term1 = (cos_theta / mu_x) ** 2 if mu_x > 1e-9 else float('inf')
        term2 = (sin_theta / mu_y) ** 2 if mu_y > 1e-9 else float('inf')
        
        if term1 == float('inf') or term2 == float('inf'):
            max_force = 0.0
        else:
            denom = math.sqrt(term1 + term2)
            max_force = Fz / denom if denom > 1e-9 else 0.0
        
        current_force = math.hypot(Fx, Fy)
        margin = max_force - current_force
        
        if max_force > 1e-9:
            margin_pct = (margin / max_force) * 100
        else:
            margin_pct = 0.0 if current_force < 1e-9 else -100.0
        
        return {
            "status": status,
            "color": color,
            "action": action,
            "ellipse_usage": ellipse_check["usage"],
            "combined_usage": combined_check["usage"],
            "force_margin_N": margin,
            "force_margin_%": margin_pct,
            "current_angle_deg": math.degrees(current_angle),
            "max_force_at_angle": max_force
        }

