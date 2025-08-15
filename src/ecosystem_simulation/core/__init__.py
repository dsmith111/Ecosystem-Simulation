"""
Ecosystem Simulation - Core modules

Contains the core classes and functionality for the ecosystem simulation.
"""

from .creature import Creature
from .herbivore import Herbivore
from .predator import Predator
from .plant import Plant
from .world_manager import WorldManager

__all__ = ['Creature', 'Herbivore', 'Predator', 'Plant', 'WorldManager']