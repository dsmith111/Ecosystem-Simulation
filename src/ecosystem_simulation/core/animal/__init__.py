"""
Ecosystem Simulation - Animal modules

Contains creature-related classes including the base creature class
and specific animal types like herbivores and predators.
"""

from .creature import Creature
from .herbivore import Herbivore
from .predator import Predator

__all__ = ['Creature', 'Herbivore', 'Predator']