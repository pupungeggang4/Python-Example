import pygame

class Game():
    def __init__(self):
        self.window: pygame.surface.Surface = None
        self.clock: pygame.time.Clock = None
        self.fps: int = 60

        self.step_num: int = 10
        self.step_size: float = 80
        self.points: list[list[float]] = []
