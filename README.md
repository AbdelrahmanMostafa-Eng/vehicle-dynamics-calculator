# 🏎️ Vehicle Dynamics Calculator

A modular Python project for calculating and simulating vehicle dynamics — designed for motorsport applications and as a strong foundation for Formula SAE (FSAE) or Formula Student projects.

---

## 📘 Features

- **Core Physics**
  - Braking distance calculator
  - Weight transfer (longitudinal and lateral)
  - Lateral acceleration estimation
  - Simple tire load sensitivity model

- **Tires**
  - Heat model (temperature rise and cooling)
  - Grip degradation with wear

- **Aerodynamics**
  - Drag and downforce estimation
  - Ground effect (ride height sensitivity)

- **Suspension & Chassis**
  - Spring/damper wheel rate calculation
  - Roll stiffness and geometry utilities

- **Powertrain**
  - Engine torque → wheel force
  - Gear ratios and traction‑limited acceleration
  - ERS/KERS energy recovery (planned)

- **Simulation**
  - Lap segment timing
  - Stint pace degradation
  - Pit stop strategy modeling

- **Telemetry & Visualization**
  - Speed, acceleration, and tire traces
  - Matplotlib plots for performance comparison

---

## 🎯 Why This Project Matters
- ***Applies real physics to code →*** Combines vehicle dynamics theory with practical Python implementation.
- ***Builds a foundation for motorsport work →*** Uses calculations directly relevant to FSAE and race engineering. 
- ***Start simple, build complexity →*** Simple enough to start, modular enough to expand into full simulations.
- ***Portfolio impact*** → Demonstrates authentic growth and engineering thinking for university applications and beyond.

---

## ⚙️ How to Run
1. Clone or download the repository  
2. Install dependencies (numpy, matplotlib if plotting is used)  
3. Run and enter vehicle parameters (mass, speed, tire coefficient, etc.)  
4. View calculated results in the terminal or graphs

---

## 🚧 Future Improvements
- Add advanced graphical visualization (matplotlib plots)  
- Expand to include aerodynamics effects  
- Build a simple GUI for user input  
- Integrate with telemetry data in future projects
- Add race strategy simulation
- Monte Carlo strategy optimizer for probabilistic race outcomes.
