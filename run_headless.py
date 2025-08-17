#!/usr/bin/env python3
"""
Convenience script to run the headless ecosystem simulation
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ecosystem_simulation.simulations.headless import run_simulation

if __name__ == "__main__":
    # Run a sample simulation with traditional behavior (saves plots every 5 iterations)
    stats = run_simulation(iterations=10, save_plots=True, continuous_viz=False)
    print("\n✅ Ecosystem simulation completed successfully!")
    print("For continuous visualization, try: python run_continuous.py")