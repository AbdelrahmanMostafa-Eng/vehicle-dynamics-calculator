#ers.py

"""
Energy Recovery System (ERS) modeling
"""

class ERS:
    def __init__(self, capacity_kJ: float, efficiency: float = 0.9):
        """
        Initialize ERS system.

        Parameters:
            capacity_kJ (float): Maximum energy storage capacity [kJ]
            efficiency (float): Harvest/deploy efficiency (default 0.9)
        """
        self.capacity = capacity_kJ
        self.efficiency = efficiency
        self.energy = 0.0  # current stored energy [kJ]

    def harvest(self, input_energy_kJ: float) -> float:
        """
        Harvest energy into ERS.

        Parameters:
            input_energy_kJ (float): Energy harvested [kJ]

        Returns:
            float: Actual stored energy [kJ]
        """
        stored = input_energy_kJ * self.efficiency
        self.energy = min(self.energy + stored, self.capacity)
        return self.energy

    def deploy(self, request_kJ: float) -> float:
        """
        Deploy energy from ERS.

        Parameters:
            request_kJ (float): Requested energy [kJ]

        Returns:
            float: Delivered energy [kJ]
        """
        available = min(request_kJ, self.energy)
        delivered = available * self.efficiency
        self.energy -= available
        return delivered

    def state_of_charge(self) -> float:
        """
        Get current state of charge (SOC).

        Returns:
            float: SOC as fraction of capacity [0–1]
        """
        return self.energy / self.capacity if self.capacity > 0 else 0.0


# Example usage
if __name__ == "__main__":
    ers = ERS(capacity_kJ=4000, efficiency=0.9)

    ers.harvest(1000)
    print(f"Stored energy = {ers.energy:.1f} kJ, SOC = {ers.state_of_charge():.2f}")

    delivered = ers.deploy(500)
    print(f"Delivered energy = {delivered:.1f} kJ, Remaining = {ers.energy:.1f} kJ")
