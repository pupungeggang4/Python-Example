import pygame

from .game import Game
from .board import Board

class Render():
    @staticmethod
    def render_board(game: Game, board: Board):
        cell: list[list[object]] = board.cell
        for i, row in enumerate(cell):
            for j, thing in enumerate(row):
                pos: list[int] = [40 * j, 40 * i, 40, 40]
                pygame.draw.rect(game.window, [0, 0, 0], pos, 2)