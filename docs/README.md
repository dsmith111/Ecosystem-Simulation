# Ecosystem Python

This is a Python port of the MATLAB ecosystem simulation. It implements a complex predator-prey ecosystem following Lotka-Volterra dynamics with intelligent creature behavior.

## Features

- **Grid-based 2D world** (60x60 default)
- **Complex creature AI** with personality traits and decision making
- **Three entity types**:
  - **Herbivores** (blue stars) - eat plants, flee from predators
  - **Predators** (red X's) - hunt herbivores 
  - **Plants** (green triangles) - food for herbivores
- **Real-time visualization** using matplotlib
- **Population dynamics** following predator-prey models

## Creature Behavior

Each creature has complex behavior driven by:

### Physical Stats
- Health level (0-1)
- Hunger level (0-1) 
- Age (affects health over time)
- Stress level (0-1)

### Personality Traits
- Aggressive vs Placid (0-1)
- Fearful vs Brave (0-1)
- Social vs Isolationist (0-1)

### Actions
- **Reproduce** - when healthy, well-fed, unstressed, and near friends
- **Rest** - when unhealthy but well-fed
- **Eat** - when hungry and food is nearby
- **Attack** - when enemies are near and creature is healthy/unstressed
- **Flee** - when threatened or outnumbered
- **Wander** - default movement behavior

## Usage

### Running Simulations

#### Interactive Mode (requires display)
```bash
python run_interactive.py
```

#### Headless Mode
```bash
python run_headless.py
```

#### Examples
```bash
python examples/example.py
```

### Programmatic Usage

```python
# Import the package
import sys
sys.path.insert(0, 'src')
from ecosystem_simulation import run_simulation, Herbivore, Predator, Plant

# Run a headless simulation
stats = run_simulation(iterations=50, world_size=60)

# Create individual creatures
herbivore = Herbivore([10, 10])
predator = Predator([20, 20])
plant = Plant([5, 5])
```

### Testing

```bash
# Run all tests
python tests/test_ecosystem.py
python tests/test_visual.py
```

## Requirements

- Python 3.7+
- numpy >= 1.20.0
- matplotlib >= 3.5.0
- scipy >= 1.7.0

## Project Structure

```
├── src/
│   └── ecosystem_simulation/          # Main package
│       ├── core/                      # Core simulation classes
│       │   ├── creature.py           # Base creature class with AI behavior
│       │   ├── herbivore.py          # Herbivore creature subclass
│       │   ├── predator.py           # Predator creature subclass  
│       │   ├── plant.py              # Plant entity class
│       │   └── world_manager.py      # World state management and visualization
│       └── simulations/               # Simulation runners
│           ├── interactive.py        # Interactive simulation with matplotlib
│           └── headless.py           # Non-interactive simulation for testing
├── tests/                             # Test files
│   ├── test_ecosystem.py             # Main functionality tests
│   └── test_visual.py                # Visualization tests
├── examples/                          # Example usage scripts
│   └── example.py                    # Demonstration of different configurations
├── docs/                              # Documentation
│   └── README.md                     # This file
├── run_interactive.py                 # Convenience script for interactive mode
├── run_headless.py                   # Convenience script for headless mode
├── requirements.txt                   # Python dependencies
└── setup.py                          # Package installation script
```

## Ecosystem Dynamics

The ecosystem demonstrates emergent behavior where:
- Predator populations rise and fall with herbivore availability
- Herbivore populations are limited by plant resources and predation
- Individual creature intelligence affects survival and reproduction
- Population cycles emerge naturally from individual behaviors

This creates a dynamic system that follows classical predator-prey models while being driven by individual creature decision making rather than top-down population equations.