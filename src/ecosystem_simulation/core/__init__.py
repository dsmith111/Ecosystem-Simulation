"""
Ecosystem Simulation - Core modules

Contains the core classes and functionality for the ecosystem simulation.
Organized into logical subdirectories:
- animal: creature classes (Creature, Herbivore, Predator)
- plant: plant-related classes (Plant)
- environment: world management (WorldManager)
"""

from .animal import Creature, Herbivore, Predator
from .plant import Plant
from .environment import WorldManager

__all__ = ['Creature', 'Herbivore', 'Predator', 'Plant', 'WorldManager']