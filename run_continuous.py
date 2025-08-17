#!/usr/bin/env python3
"""
Convenience script to run the ecosystem simulation with continuous visualization
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

# Check if running in a display environment
import matplotlib
display_available = False
try:
    # Try to use the default backend first
    import matplotlib.pyplot as plt
    # If we can create a figure, we likely have display support
    plt.figure()
    plt.close()
    display_available = True
except:
    # Fallback to Agg backend for headless environments
    matplotlib.use('Agg')
    display_available = False

from ecosystem_simulation.simulations.interactive import main

if __name__ == "__main__":
    print("Starting continuous ecosystem simulation...")
    
    if display_available:
        print("🖥️  Display environment detected - continuous visualization will be shown")
    else:
        print("📱 Headless environment detected - visualization will be saved to PNG files")
        
    print("Press Ctrl+C to stop the simulation")
    print()
    
    # Run with continuous visualization enabled using interactive mode
    # This provides real-time visualization that the user can see (if display available)
    # or saves plots for headless environments
    main(
        framerate=0.1,     # Reasonable framerate for observation
        save_plots=True,   # Save plots periodically 
        iterations=50      # Number of iterations to run
    )
    print("\n✅ Continuous ecosystem simulation completed successfully!")