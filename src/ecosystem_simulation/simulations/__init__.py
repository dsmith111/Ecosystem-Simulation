"""
Ecosystem Simulation - Simulation runners

Contains the main simulation scripts (interactive and headless modes).
"""

from .interactive import main as run_interactive
from .headless import run_simulation

__all__ = ['run_interactive', 'run_simulation']