# Ecosystem Simulation

Ecosystem Simulation is a Python-based complex predator-prey ecosystem simulation with intelligent creature behavior. It's a port from MATLAB that implements Lotka-Volterra dynamics with individual creature AI.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

- Bootstrap and install dependencies:
  - `pip install --upgrade pip`
  - `pip install -r requirements.txt` -- takes 45 seconds. NEVER CANCEL. Set timeout to 90+ seconds.
- Install package in development mode:
  - `pip install -e .` -- takes 5 seconds. NEVER CANCEL. Set timeout to 30+ seconds.
- Run all tests:
  - `python tests/test_ecosystem.py` -- takes 1 second. Tests core creature behavior and mini simulation.
  - `python tests/test_visual.py` -- takes 1 second. Tests matplotlib plotting in headless environment.
- Run simulations:
  - Headless: `python run_headless.py` -- takes 2 seconds for 10 iterations. NEVER CANCEL. Set timeout to 30+ seconds.
  - Examples: `python examples/example.py` -- takes 3 seconds for multiple simulation runs. NEVER CANCEL. Set timeout to 30+ seconds.
  - Console script: `ecosystem-headless` (after pip install -e .)
- Syntax check all Python files:
  - `find . -name "*.py" -exec python -m py_compile {} \;` -- takes 2 seconds. NEVER CANCEL. Set timeout to 30+ seconds.

## Validation

- ALWAYS run the complete test suite after making changes to core simulation logic.
- ALWAYS manually validate ecosystem simulations by running through complete scenarios:
  - Run `python run_headless.py` and verify PNG plots are generated (ecosystem_iteration_001.png, etc.)
  - Check that creature populations change realistically over iterations
  - Verify simulation statistics show reasonable population dynamics (herbivores: ~20, predators: ~8, plants: ~30 in default 60x60 world)
- ALWAYS test both direct script execution and package installation scenarios:
  - Test `python run_headless.py` (direct execution)
  - Test `pip install -e . && ecosystem-headless` (package installation)
- The simulation runs in headless mode using matplotlib 'Agg' backend - no display required.
- Generated PNG files demonstrate that visualization is working correctly.
- You cannot run the interactive mode (`python run_interactive.py` or `ecosystem-interactive`) in headless environments.

## Common Tasks

The following are outputs from frequently run commands. Reference them instead of viewing, searching, or running bash commands to save time.

### Repository Structure
```
├── .gitignore                         # Python, IDE, and generated file exclusions
├── __init__.py                        # Root package marker
├── docs/
│   └── README.md                     # Comprehensive project documentation
├── examples/
│   ├── __init__.py
│   └── example.py                    # Demonstration script with multiple configurations
├── requirements.txt                   # numpy>=1.20.0, matplotlib>=3.5.0, scipy>=1.7.0
├── run_headless.py                   # Convenience script for headless simulation
├── run_interactive.py                # Convenience script for interactive mode (requires display)
├── setup.py                          # Package installation with console script entry points
├── src/
│   └── ecosystem_simulation/         # Main package
│       ├── __init__.py
│       ├── core/                     # Core simulation classes
│       │   ├── __init__.py
│       │   ├── creatures/            # Creature implementations
│       │   │   ├── __init__.py
│       │   │   ├── creature.py       # Base creature class with AI behavior
│       │   │   ├── herbivore.py      # Herbivore creature subclass
│       │   │   ├── plant.py          # Plant entity class
│       │   │   └── predator.py       # Predator creature subclass
│       │   └── environment/          # World management
│       │       ├── __init__.py
│       │       └── world_manager.py  # World state management and visualization
│       └── simulations/              # Simulation runners
│           ├── __init__.py
│           ├── headless.py           # Non-interactive simulation for testing/automation
│           └── interactive.py        # Interactive simulation with matplotlib (requires display)
└── tests/
    ├── __init__.py
    ├── test_ecosystem.py             # Main functionality tests
    └── test_visual.py                # Visualization tests
```

### Dependencies (requirements.txt)
```
numpy>=1.20.0
matplotlib>=3.5.0
scipy>=1.7.0
```

### Console Script Entry Points (from setup.py)
```
ecosystem-interactive=ecosystem_simulation.simulations.interactive:main
ecosystem-headless=ecosystem_simulation.simulations.headless:run_simulation
```

### Key Simulation Parameters
- Default world size: 60x60
- Default creatures: ~20 herbivores, ~8 predators, ~30 plants
- Iteration time: ~0.002 seconds per iteration (very fast)
- Typical simulation: 10 iterations takes ~2 seconds total

## Project Behavior and Architecture

### Ecosystem Dynamics
- Predator-prey relationships following Lotka-Volterra dynamics
- Individual creature intelligence affects survival and reproduction
- Creatures have sight, stress processing, decision making, and action systems
- Population cycles emerge from individual behaviors rather than top-down equations

### Creature Types
- **Herbivores**: Blue stars (*) - eat plants, avoid predators, can reproduce
- **Predators**: Red X marks (x) - hunt herbivores, can reproduce
- **Plants**: Green triangles (^) - stationary, can be consumed by herbivores

### Simulation Modes
- **Interactive**: Real-time visualization with matplotlib GUI (requires display)
- **Headless**: Non-interactive mode suitable for automation and testing
- **Example**: Demonstrates different configurations and parameter sets

### File Outputs
- PNG plots saved every 5 iterations: ecosystem_iteration_001.png, ecosystem_iteration_006.png, etc.
- Console output shows population statistics and timing for each iteration
- Simulation returns statistics dictionary with iteration data

## Troubleshooting

### Common Issues
- **Import errors**: Always run `pip install -r requirements.txt` first
- **Display errors with interactive mode**: Use headless mode (`python run_headless.py`) in server environments
- **Package not found**: Run `pip install -e .` to install in development mode
- **Permission errors**: Use `pip install --user` if system installation fails

### Expected Behaviors
- Console script `ecosystem-headless` exits with code 1 (this is normal - it prints results and exits)
- Matplotlib uses 'Agg' backend in headless mode (no display required)
- PNG files are generated in the current working directory
- Simulation iterations are very fast (~0.002s each) but dependency installation takes time

### Performance Expectations
- Fresh dependency install: 45 seconds
- Package development install: 5 seconds  
- Test suite: 1 second total
- Headless simulation (10 iterations): 2 seconds
- Individual iterations: 0.002 seconds (extremely fast)

## Development Guidelines

### When Making Changes
- ALWAYS run the test suite first to understand baseline behavior
- ALWAYS validate changes with both test scripts AND manual simulation runs
- ALWAYS check that PNG visualization files are generated correctly
- Test both direct script execution and package installation workflows
- Use the headless simulation mode for automated testing and validation

### Code Style
- No formal linting tools configured - use `python -m py_compile` for syntax checking
- Follow existing code patterns and naming conventions
- Maintain compatibility with Python 3.7+ as specified in setup.py

### Testing Strategy
- `tests/test_ecosystem.py`: Validates core creature behavior and simulation logic
- `tests/test_visual.py`: Validates matplotlib functionality in headless environment
- `examples/example.py`: Integration test with multiple simulation configurations
- Manual validation: Always run complete simulation scenarios and verify outputs