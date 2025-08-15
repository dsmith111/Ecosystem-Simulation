"""
Ecosystem Simulation - A port of the MATLAB ecosystem simulation

This package implements a complex predator-prey ecosystem simulation with
intelligent creature behavior, following Lotka-Volterra dynamics.

Project Structure:
- src/ecosystem_simulation/core/: Core simulation classes
- src/ecosystem_simulation/simulations/: Simulation runners
- tests/: Test files  
- examples/: Example usage scripts
- docs/: Documentation

Quick Start:
    # Run interactive simulation
    python run_interactive.py
    
    # Run headless simulation  
    python run_headless.py
    
    # Run examples
    python examples/example.py

Programmatic Usage:
    import sys; sys.path.insert(0, 'src')
    from ecosystem_simulation import run_simulation
    stats = run_simulation(iterations=50)
"""

__version__ = "1.0.0"
__author__ = "Ported from MATLAB by AI Assistant"

# This file serves as documentation for the project structure
# For actual usage, import from src.ecosystem_simulation