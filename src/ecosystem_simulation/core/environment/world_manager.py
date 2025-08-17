import matplotlib.pyplot as plt
import numpy as np
from typing import List, Any, Optional, Tuple


class WorldManager:
    """Construct or update world map"""
    
    @staticmethod
    def update_list(object_list: List[Any]) -> List[Any]:
        """Update the list of objects, removing dead creatures and eaten plants"""
        i = 0
        
        while i < len(object_list):
            obj = object_list[i]
            
            if obj.type in ["herbivore", "predator"]:
                # Check health, hunger, remove if dead
                obj.hunger_level -= 0.02
                
                if obj.health_level <= 0:
                    obj.alive = False
                
                if obj.hunger_level <= 0:
                    obj.hunger_level = 0
                    obj.hurt()
                
                if not obj.alive:
                    object_list.pop(i)
                    continue
                
                # Age the creature
                if obj.age < 50:
                    obj.age += 1
                else:
                    obj.age += 1
                    obj.hurt()
            
            elif obj.type == "plant":
                if obj.eaten:
                    object_list.pop(i)
                    continue
            
            i += 1
        
        return object_list
    
    @staticmethod
    def draw_map(map_size: int, object_list: List[Any]):
        """Draw the current state of the ecosystem"""
        plt.clf()
        plt.xlim(1, map_size)
        plt.ylim(1, map_size)
        
        # Separate objects by type for plotting
        herbivores = []
        predators = []
        plants = []
        
        for obj in object_list:
            if obj.type == "herbivore":
                herbivores.append(obj.location)
            elif obj.type == "predator":
                predators.append(obj.location)
            elif obj.type == "plant":
                plants.append(obj.location)
        
        # Plot each type with different markers and colors
        if herbivores:
            herbivores = np.array(herbivores)
            plt.scatter(herbivores[:, 1], herbivores[:, 0], 
                       c='blue', marker='*', s=50, label='Herbivores')
        
        if predators:
            predators = np.array(predators)
            plt.scatter(predators[:, 1], predators[:, 0], 
                       c='red', marker='x', s=50, label='Predators')
        
        if plants:
            plants = np.array(plants)
            plt.scatter(plants[:, 1], plants[:, 0], 
                       c='green', marker='^', s=30, label='Plants')
        
        plt.legend()
        plt.title('Ecosystem Simulation')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.grid(True, alpha=0.3)
        plt.pause(0.01)  # Small pause to allow real-time updating

    @staticmethod
    def setup_continuous_plot(map_size: int) -> Tuple[Any, Any]:
        """Setup matplotlib for continuous plotting with better performance"""
        plt.ion()  # Turn on interactive mode
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(1, map_size)
        ax.set_ylim(1, map_size)
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        return fig, ax

    @staticmethod 
    def update_continuous_plot(ax: Any, object_list: List[Any], iteration: int, framerate: float = 0.05, map_size: int = 60):
        """Efficiently update the plot for continuous visualization"""
        ax.clear()
        ax.set_xlim(1, map_size)
        ax.set_ylim(1, map_size)
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        ax.grid(True, alpha=0.3)
        
        # Separate objects by type for plotting
        herbivores = []
        predators = []
        plants = []
        
        for obj in object_list:
            if obj.type == "herbivore":
                herbivores.append(obj.location)
            elif obj.type == "predator":
                predators.append(obj.location)
            elif obj.type == "plant":
                plants.append(obj.location)
        
        # Plot each type with different markers and colors
        if herbivores:
            herbivores = np.array(herbivores)
            ax.scatter(herbivores[:, 1], herbivores[:, 0], 
                      c='blue', marker='*', s=50, label='Herbivores')
        
        if predators:
            predators = np.array(predators)
            ax.scatter(predators[:, 1], predators[:, 0], 
                      c='red', marker='x', s=50, label='Predators')
        
        if plants:
            plants = np.array(plants)
            ax.scatter(plants[:, 1], plants[:, 0], 
                      c='green', marker='^', s=30, label='Plants')
        
        ax.legend()
        ax.set_title(f'Ecosystem Simulation - Iteration {iteration}')
        
        plt.pause(framerate)  # Control framerate