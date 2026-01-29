#drag.py

"""

Module for calculating aerodynamic drag forces in Formula 1.
Includes base drag, induced drag, and cooling drag contributions.

"""

from dataclasses import dataclass
import numpy as np

@dataclass
class DragModel:
    frontal_area: float
    cd_base: float
    cl_total: float
    aspect_ratio: float
    cooling_drag: float

    def induced_drag(self) -> float:
        """Calculate induced drag coefficient from lift."""
        return self.cl_total**2 / (np.pi * self.aspect_ratio)

    def total_cd(self) -> float:
        """Return total drag coefficient (base + induced)."""
        return self.cd_base + self.induced_drag()

    def drag_force(self, velocity: float, rho: float) -> float:
        """Calculate drag force (N) at given velocity (m/s)."""
        return 0.5 * rho * velocity**2 * self.frontal_area * self.total_cd() + self.cooling_drag


# Example usage

if __name__ == "__main__":
    rho = 1.225
    drag_model = DragModel(frontal_area=1.6, cd_base=0.9, cl_total=3.5, aspect_ratio=5.0, cooling_drag=50)

    print("=== Drag Example ===")
    for v in [100, 200, 300]:  # km/h
        v_ms = v / 3.6
        df = drag_model.drag_force(v_ms, rho)
        print(f"Velocity {v} km/h → Drag Force = {df:.1f} N")
