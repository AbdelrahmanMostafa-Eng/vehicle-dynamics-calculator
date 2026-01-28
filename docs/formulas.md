# Core Formulas for Race Simulation

## Lap Time
t_lap = d_lap / v_avg  
- d_lap: lap distance [m]  
- v_avg: average speed [m/s]  

## Fuel Burn
m_fuel = fuel_rate * t_lap  
- fuel_rate: fuel burn rate [kg/s]  
- t_lap: lap time [s]  

## Tire Degradation
grip_final = grip_initial - degradation_rate * laps  
- grip_initial: initial grip coefficient  
- degradation_rate: rate per lap  
- laps: number of laps  

## Stint Summary
Remaining Fuel = fuel_initial - fuel_per_lap * laps  
Final Grip = grip_initial - degradation_rate * laps
