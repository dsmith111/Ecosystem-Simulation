#!/usr/bin/env python3
"""
Test script to demonstrate the new continuous visualization features
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ecosystem_simulation.simulations.headless import run_simulation

def test_traditional_mode():
    """Test traditional headless mode (saves plots every 5 iterations)"""
    print("=== Testing Traditional Mode ===")
    stats = run_simulation(
        iterations=10, 
        save_plots=True, 
        continuous_viz=False,
        world_size=30  # Smaller world for faster testing
    )
    print(f"✅ Traditional mode completed: {len(stats)} iterations\n")

def test_continuous_mode():
    """Test continuous visualization mode"""
    print("=== Testing Continuous Visualization Mode ===")
    stats = run_simulation(
        iterations=10, 
        save_plots=False,  # Disable saving for performance
        continuous_viz=True,
        framerate=0.02,  # Fast framerate for testing
        world_size=30
    )
    print(f"✅ Continuous mode completed: {len(stats)} iterations\n")

def test_continuous_with_saving():
    """Test continuous mode with plot saving"""
    print("=== Testing Continuous Mode with Plot Saving ===")
    stats = run_simulation(
        iterations=10, 
        save_plots=True,
        continuous_viz=True, 
        framerate=0.02,
        world_size=30
    )
    print(f"✅ Continuous mode with saving completed: {len(stats)} iterations\n")

if __name__ == "__main__":
    print("Testing new continuous visualization features...\n")
    
    test_traditional_mode()
    test_continuous_mode()
    test_continuous_with_saving()
    
    print("✅ All new features tested successfully!")
    print("\nFeatures demonstrated:")
    print("- Traditional mode: intermittent plot saving (every 5 iterations)")
    print("- Continuous visualization: real-time display every iteration")
    print("- Framerate control: customizable update speed") 
    print("- Optional saving: can disable plot files for performance")