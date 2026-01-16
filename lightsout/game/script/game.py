import pygame

class Game():
    def __init__(self):
        self.window: pygame.surface.Surface = None
        self.clock: pygame.time.Clock = None
        self.fps: float = 60
        self.menu: bool = None
        self.board: list[list[int]] = []
        self.img_off: pygame.surface.Surface = None
        self.img_on: pygame.surface.Surface = None

