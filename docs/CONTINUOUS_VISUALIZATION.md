# Continuous Visualization Features

This document describes the new continuous, real-time visualization features added to the Ecosystem Simulation.

## Overview

The ecosystem simulation now supports continuous, real-time visualization that updates every iteration instead of saving plots intermittently. This provides a smooth, continuous viewing experience.

## Features

### 1. Continuous Visualization Mode

Enable real-time plotting that updates every iteration:

```python
from ecosystem_simulation.simulations.headless import run_simulation

# Enable continuous visualization
stats = run_simulation(
    iterations=50,
    continuous_viz=True,
    framerate=0.1  # Update every 0.1 seconds
)
```

### 2. Framerate Control

Control how fast the visualization updates:

```python
# Fast updates (0.05s between frames)
run_simulation(continuous_viz=True, framerate=0.05)

# Slower updates (0.2s between frames) 
run_simulation(continuous_viz=True, framerate=0.2)
```

### 3. Optional Plot Saving

Disable plot saving for better performance:

```python
# Continuous visualization without saving files
run_simulation(
    continuous_viz=True,
    save_plots=False,  # No PNG files saved
    framerate=0.05
)
```

### 4. Interactive Mode Enhancements

The interactive mode now supports framerate control and optional saving:

```python
from ecosystem_simulation.simulations.interactive import main

# Custom framerate for interactive mode
main(framerate=0.05)

# Interactive mode with plot saving
main(framerate=0.1, save_plots=True)
```

## Convenience Scripts

### Traditional Mode (unchanged)
```bash
python run_headless.py
```
- Saves plots every 5 iterations
- No real-time visualization
- Compatible with headless environments

### Continuous Mode
```bash
python run_continuous.py
```
- Real-time visualization every iteration
- Reasonable framerate (0.1s)
- Saves plots every 5 iterations

## Parameters

### `run_simulation()` Parameters

- `iterations` (int): Number of simulation iterations (default: 10)
- `save_plots` (bool): Whether to save PNG files (default: True)
- `world_size` (int): Size of simulation world (default: 60)
- `continuous_viz` (bool): Enable continuous visualization (default: False)
- `framerate` (float): Time between updates in seconds (default: 0.05)

### `main()` Parameters (Interactive)

- `framerate` (float): Time between visual updates (default: 0.1)
- `save_plots` (bool): Whether to save plots periodically (default: False)

## Performance Considerations

- **Continuous visualization**: Slightly slower due to real-time plotting
- **Framerate**: Lower values (faster updates) use more CPU
- **Plot saving**: Disabling saves improves performance significantly
- **World size**: Smaller worlds render faster

## Examples

### High-Performance Mode
```python
# Fast simulation with minimal overhead
run_simulation(
    iterations=100,
    continuous_viz=True,
    save_plots=False,
    framerate=0.01,
    world_size=30
)
```

### Observation Mode
```python
# Slower updates for better observation
run_simulation(
    iterations=50,
    continuous_viz=True,
    save_plots=True,
    framerate=0.2,
    world_size=60
)
```

### Traditional Mode (Backward Compatible)
```python
# Original behavior - unchanged
run_simulation(iterations=20, save_plots=True)
```

## Migration from Previous Version

All existing code continues to work unchanged. To add continuous visualization:

**Before:**
```python
run_simulation(iterations=50, save_plots=True)
```

**After (with continuous visualization):**
```python
run_simulation(
    iterations=50, 
    save_plots=True,
    continuous_viz=True,
    framerate=0.1
)
```