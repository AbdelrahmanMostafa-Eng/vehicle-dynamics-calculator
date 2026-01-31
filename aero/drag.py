#drag.py

"""

Module for calculating aerodynamic drag forces in Formula 1.
Includes base drag, induced drag, and cooling drag contributions.

"""

from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

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

    velocities = np.linspace(50, 350, 50)  # km/h
    velocities_ms = velocities / 3.6
    drag_forces = [drag_model.drag_force(v, rho) for v in velocities_ms]

    # Print default outputs
    print("Drag Example:")
    for v in [100, 200, 300]:
        print(f"Velocity {v} km/h → Drag Force = {drag_model.drag_force(v/3.6, rho):.1f} N")

    # Plot
    plt.plot(velocities, drag_forces, color="red")
    plt.xlabel("Velocity (km/h)")
    plt.ylabel("Drag Force (N)")
    plt.title("Drag Force vs Speed")
    plt.show()
