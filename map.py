import numpy as np
from materials import materials

class Map:
    def __init__(self, width, height, food_count):
        self.width = width
        self.height = height
        self.food_count = food_count
        self.map = np.full((width, height), materials.Empty)  # Initialize an empty map
        self.spawn_food()

    def spawn_food(self):
        # Randomly place food on the map
        food_indices = np.random.choice(self.width * self.height, self.food_count, replace=False)
        food_coords = np.unravel_index(food_indices, (self.width, self.height))
        for x, y in zip(*food_coords):
            self[x, y] = materials.Food

    def display(self):
        for row in self.map:
            print(' '.join(cell.symbol for cell in row))

    def copy(self):
        new_self = Map(self.width, self.height, self.food_count)
        new_self.map = self.map.copy()
        return new_self
    
    def __getitem__(self, key):
        return self.map[key]

    def __setitem__(self, key, value):
        if value not in materials:
            raise ValueError(f"Invalid material. Got {value}, expected one of {materials}")
        self.map[key] = value
# Example usage
if __name__ == "__main__":
    width = 10
    height = 10
    food_count = 15

    world = Map(width, height, food_count)
    world.display()
    print("\n")
    world.spawn_food()
    world.display()
    
