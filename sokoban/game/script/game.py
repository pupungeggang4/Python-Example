import pygame

from .board import Board

class Game():
    def __init__(self):
        self.window: pygame.surface.Surface = None
        self.clock: pygame.time.Clock = None
        self.fps: int = 60
        self.menu: bool = False

        self.board: Board = Board()
        self.board.cell = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
