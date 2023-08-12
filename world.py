import numpy as np

from agents import Agent
from map import Map
from materials import materials

class World:
    def __init__(self, map: Map, agents: list[Agent]):
        self.map = map
        self.agents = agents
        self.random_place_agents()

        self.actions = {
                "move_up": lambda agent: agent.move(agent.pos_x, agent.pos_y + 1 % map.height),
                "move_down": lambda agent: agent.move(agent.pos_x, agent.pos_y - 1 % map.height),
                "move_left": lambda agent: agent.move(agent.pos_x - 1 % map.width, agent.pos_y),
                "move_right": lambda agent: agent.move(agent.pos_x + 1 % map.width, agent.pos_y),
                "eat": self._agent_action_eat,
        }
        self.dead_agents = []

    def random_place_agents(self):
        for agent in self.agents:
            # select a random position on the map
            pos_x, pos_y = (
                np.random.randint(0, self.map.width),
                np.random.randint(0, self.map.height),
            )
            agent.move(pos_x, pos_y)

    def update(self):
        for agent in self.agents:
            decision= agent.decide(self._agent_inputs(agent))
            self.take_action(agent, decision)
        self._update_map()
        np.random.shuffle(self.agents) # shuffle agents to avoid bias
        for agent in self.agents:
            agent.lose_energy(1)
            if agent.energy <= 0:
                self.agents.remove(agent)
                self.dead_agents.append(agent)

    def _update_map(self):
        pass        

    def _agent_action_eat(self, agent):
        if self.map[agent.pos_x, agent.pos_y] == materials.Food:
            agent.eat(10)
            self.map[agent.pos_x, agent.pos_y] = materials.Empty


    def _agent_inputs(self, agent):
        input= np.zeros(len(agent.sensors))
        if "is_food" in agent.sensors:
            if self.map[agent.pos_x, agent.pos_y] == materials.Food:
                input[0] = 1
        return input
    
    def take_action(self, agent, action):
        self.actions[action](agent)
