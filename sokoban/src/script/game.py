import pygame

class Game():
    def __init__(self):
        self.window: pygame.surface.Surface = None
        self.clock: pygame.time.Clock = None
        self.fps: int = 60
        self.menu: bool = False
