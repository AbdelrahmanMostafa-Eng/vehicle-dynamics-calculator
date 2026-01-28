# Modeling Assumptions

## General
- Track length is fixed (e.g., 5300 m).
- Average speed per lap is treated as constant for simplicity.
- Fuel burn rate is linear with lap time.
- Environmental effects (weather, altitude, track temperature) are ignored.

## Tires
- Grip decreases linearly with lap count.
- No distinction between tire compounds (soft, medium, hard).
- No recovery of grip during pit stops.
- Tire wear is modeled as a simple percentage reduction, not compound-specific degradation curves.

## Fuel
- Fuel consumption is constant per lap.
- No effect of fuel weight on lap time (simplification).
- Refueling is not allowed (modern F1 rules).

## Strategy
- Pit stop time is fixed (e.g., 22 s).
- Race is divided into predefined stints.
- No safety car, red flags, or weather interruptions are considered.
- Driver behavior (overtakes, mistakes) is not modeled.
