import pickle

import pygame
from pygame.locals import *

from world import World
from agents import Agent
from map import Map
from materials import materials


class GameGUI:
    def __init__(self, history):
        pygame.init()
        self.history = history

        map = history[0]["map"]
        ratio = map.width / map.height
        self.height = 600
        self.width = int(self.height * ratio)
        if self.width > 1200:
            self.width = 1200
            self.height = int(self.width / ratio)
        self.pixel_width = self.width / map.width
        self.pixel_height = self.height / map.height

        self.window_size = (self.width, self.height)
        self.window = pygame.display.set_mode(self.window_size)

        self.clock = pygame.time.Clock()
        self.is_running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False

    def display(self, map, agents, timepoint):
        self.window.fill((255, 255, 255))
        
        for y in range(map.height):
            for x in range(map.width):
                material = map[x,y]
                color = (0, 0, 0) if material == materials.Empty else (0, 255, 0)
                pygame.draw.rect(
                    self.window,
                    color,
                    (
                        x * self.pixel_width,
                        y * self.pixel_height,
                        self.pixel_width,
                        self.pixel_height,
                    ),
                )

        for agent in agents:
            radius = min(self.pixel_width, self.pixel_height) / 2
            inner_radius = radius * 0.9
            pygame.draw.circle(
                self.window,
                (255, 0, 0),
                (
                    agent.pos_x * self.pixel_width + self.pixel_width / 2,
                    agent.pos_y * self.pixel_height + self.pixel_height / 2,
                ),
                radius,
                0,
            )
            pygame.draw.circle(
                self.window,
                (255 * (agent.health / 100), 0, 0),
                (
                    agent.pos_x * self.pixel_width + self.pixel_width / 2,
                    agent.pos_y * self.pixel_height + self.pixel_height / 2,
                ),
                inner_radius,
            )

        font = pygame.font.Font(None, 36)
        text = font.render(str(timepoint), 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = self.window.get_rect().centerx
        self.window.blit(text, textpos)

        
        pygame.display.update()

    def run(self):
        for t, frame in enumerate(self.history):
            self.handle_events()
            if not self.is_running:
                break
            self.display(frame["map"], frame["agents"], t)
            self.clock.tick(10)

        pygame.quit()

# Example usage
if __name__ == "__main__":
    history = pickle.load(open("history.pkl", "rb"))
    gui = GameGUI(history)
    gui.run()
