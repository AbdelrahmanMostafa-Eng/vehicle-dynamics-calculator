#plots.py

"""

Module for visualizing telemetry data in Formula 1.

"""

import matplotlib.pyplot as plt

class TelemetryPlots:

    @staticmethod
    def plot_speed(time, speed):
        plt.plot(time, speed, color="blue")
        plt.xlabel("Time (s)")
        plt.ylabel("Speed (km/h)")
        plt.title("Speed Trace")
        plt.show()

    @staticmethod
    def plot_inputs(time, throttle, brake):
        plt.plot(time, throttle, label="Throttle", color="green")
        plt.plot(time, brake, label="Brake", color="red")
        plt.xlabel("Time (s)")
        plt.ylabel("Input Level")
        plt.title("Driver Inputs")
        plt.legend()
        plt.show()

    @staticmethod
    def plot_gears(time, gear):
        plt.step(time, gear, where="post", color="purple")
        plt.xlabel("Time (s)")
        plt.ylabel("Gear")
        plt.title("Gear Trace")
        plt.show()


# Plotting

if __name__ == "__main__":
    import numpy as np
    # Example synthetic data
    time = np.linspace(0, 90, 500)
    speed = 300 * (np.sin(2*np.pi*time/90)*0.4 + 0.6)
    throttle = np.clip(np.sin(4*np.pi*time/90), 0, 1)
    brake = np.clip(-np.sin(4*np.pi*time/90), 0, 1)
    gear = np.floor(1 + 6*(speed/300)).astype(int)

    print("Telemetry Plots Example:")
    print("Plotting speed, inputs, and gear traces...")

    TelemetryPlots.plot_speed(time, speed)
    TelemetryPlots.plot_inputs(time, throttle, brake)
    TelemetryPlots.plot_gears(time, gear)
