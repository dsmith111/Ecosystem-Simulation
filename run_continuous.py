#!/usr/bin/env python3
"""
Convenience script to run the ecosystem simulation with continuous visualization
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ecosystem_simulation.simulations.headless import run_simulation

if __name__ == "__main__":
    # Run with continuous visualization enabled
    stats = run_simulation(
        iterations=50, 
        save_plots=True, 
        continuous_viz=True, 
        framerate=0.1  # Reasonable framerate for observation
    )
    print("\n✅ Continuous ecosystem simulation completed successfully!")