import numpy as np


class Agent:
    def __init__(self, sensors, actions, initial_x=None, initial_y=None):
        self.sensors = sensors
        self.actions = actions
        self.pos_x = initial_x
        self.pos_y = initial_y
        self.health = 100
        self.max_health = 100

    def brain(self, input):
        return np.random.rand(len(self.actions))

    def decide(self, input):
        output = self.brain(input)
        decision = np.random.choice(len(output), p=output / np.sum(output, axis=None))
        return self.actions[decision]

    def move(self, destination):
        self.pos_x = destination[0]
        self.pos_y = destination[1]

    def eat(self, energy):
        self.health += energy
        self.health = min(self.health, self.max_health)

    def lose_energy(self, energy):
        self.health -= energy

    def __repr__(self) -> str:
        return f"Agent {id(self)} at ({self.pos_x}, {self.pos_y}) with {self.health} health"


# Example usage
if __name__ == "__main__":
    agent = Agent(
        sensors=["is_food"],
        actions=["move_up", "move_down", "move_left", "move_right", "eat", "idle"],
        initial_x=0,
        initial_y=0,
    )
    print(agent)
    print(agent.decide([1]))
