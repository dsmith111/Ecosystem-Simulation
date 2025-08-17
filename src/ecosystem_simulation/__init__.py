"""
Ecosystem Simulation - A port of the MATLAB ecosystem simulation

This package implements a complex predator-prey ecosystem simulation with
intelligent creature behavior, following Lotka-Volterra dynamics.

Main modules:
- core.creature: Base creature class with AI behavior
- core.herbivore: Herbivore creature subclass
- core.predator: Predator creature subclass  
- core.plant: Plant entity class
- core.world_manager: World state management and visualization
- simulations.interactive: Main interactive simulation
- simulations.headless: Non-interactive simulation for testing

Usage:
    from ecosystem_simulation.simulations import run_interactive
    run_interactive()
    
    from ecosystem_simulation.simulations import run_simulation
    run_simulation()
"""

__version__ = "1.0.0"
__author__ = "Ported from MATLAB by AI Assistant"

# Import core classes for easy access
from .core import Creature, Herbivore, Predator, Plant, WorldManager
from .simulations import run_interactive, run_simulation

__all__ = ['Creature', 'Herbivore', 'Predator', 'Plant', 'WorldManager', 'run_interactive', 'run_simulation']