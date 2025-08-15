#!/usr/bin/env python3
"""
Convenience script to run the interactive ecosystem simulation
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from ecosystem_simulation.simulations.interactive import main

if __name__ == "__main__":
    main()