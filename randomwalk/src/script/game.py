import pygame

class Game():
    def __init__(self):
        self.window: pygame.surface.Surface = None
        self.clock: pygame.time.Clock = None
        self.fps: int = 60
        self.font: pygame.font.Font = None
        self.button_4_dir: pygame.surface.Surface = None
        self.button_all: pygame.surface.Surface = None
        self.button_start: pygame.surface.Surface = None

        self.mode: int = 0
        self.mode_edit: int = 0
        self.step_num: int = 10
        self.step_size: float = 80
        self.points: list[list[float]] = []
