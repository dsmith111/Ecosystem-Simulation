#!/usr/bin/env python3
"""
Convenience script to run the ecosystem simulation with continuous visualization
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

# Check if running in a display environment
import matplotlib
import os

def detect_display_environment():
    """Properly detect if we can use interactive matplotlib backends"""
    
    # Check for DISPLAY environment variable (Unix-like systems)
    if os.name == 'posix' and not os.environ.get('DISPLAY'):
        return False
    
    # Test interactive backends in order of preference
    interactive_backends = ['TkAgg', 'Qt5Agg', 'Qt4Agg', 'GTKAgg']
    
    for backend in interactive_backends:
        try:
            # Set the backend
            matplotlib.use(backend, force=True)
            
            # Try to import pyplot and create a figure
            import matplotlib.pyplot as plt
            fig = plt.figure()
            plt.close(fig)
            
            # If we get here, the backend works
            print(f"Using interactive backend: {backend}")
            return True
            
        except Exception as e:
            # This backend doesn't work, try the next one
            continue
    
    # No interactive backend worked, fall back to Agg
    matplotlib.use('Agg', force=True)
    return False

display_available = detect_display_environment()

if __name__ == "__main__":
    print("Starting continuous ecosystem simulation...")
    
    if display_available:
        print("🖥️  Interactive display detected - real-time visualization will be shown")
        print("Press Ctrl+C to stop the simulation")
        print()
        
        # Use interactive module for real-time visualization
        from ecosystem_simulation.simulations.interactive import main
        main(
            framerate=0.1,     # Reasonable framerate for observation
            save_plots=True,   # Save plots periodically 
            iterations=50      # Number of iterations to run
        )
    else:
        print("📱 Headless environment detected - using optimized headless mode")
        print("Visualization will be saved to PNG files every 5 iterations")
        print("Press Ctrl+C to stop the simulation")
        print()
        
        # Use headless module for better performance in headless environments
        from ecosystem_simulation.simulations.headless import run_simulation
        run_simulation(
            iterations=50,
            save_plots=True,
            world_size=60
        )
        
    print("\n✅ Continuous ecosystem simulation completed successfully!")