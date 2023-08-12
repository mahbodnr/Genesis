import numpy as np

class Agent:
    def __init__(self, inputs, actions, initial_x, initial_y):
        self.inputs = inputs
        self.actions = actions
        self.x = initial_x
        self.y = initial_y
        self.health = 100

    def brain(self, input):
        return np.random.rand(len(self.actions))

    def decide(self, input):
        output = self.brain(input)
        decision = np.random.choice(len(output), p=output/np.sum(output, axis=None))
        return decision
    
    def move(self, destination):
        self.x = destination[0]
        self.y = destination[1]

    def __repr__(self) -> str:
        return f"Agent {id(self)} at ({self.x}, {self.y}) with {self.health} health"

# Example usage
if __name__ == "__main__":
    agent = Agent(
        inputs=["is_food"],
        actions=["move_up", "move_down", "move_left", "move_right", "eat", "idle"],
        initial_x=0,
        initial_y=0
    )
    print(agent)
    print(agent.decide([1]))