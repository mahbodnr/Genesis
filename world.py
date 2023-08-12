import numpy as np
from materials import materials

class World:
    def __init__(self, width, height, food_count):
        self.width = width
        self.height = height
        self.food_count = food_count
        self.map = np.full((height, width), materials.Empty)  # Initialize an empty map
        self.spawn_food()

    def spawn_food(self):
        # Randomly place food on the map
        food_indices = np.random.choice(self.width * self.height, self.food_count, replace=False)
        food_coords = np.unravel_index(food_indices, (self.height, self.width))
        for x, y in zip(*food_coords):
            self.map[y, x] = materials.Food

    def display(self):
        for row in self.map:
            print(' '.join(cell.symbol for cell in row))

    def get_material_at(self, x, y):
        return self.map[y, x]

    def set_material_at(self, x, y, material):
        if material:
            self.map[y, x] = material
        else:
            raise ValueError("Material cannot be None")

# Example usage
if __name__ == "__main__":
    width = 10
    height = 10
    food_count = 15

    world = World(width, height, food_count)
    world.display()
    print("\n")
    world.spawn_food()
    world.display()
    
