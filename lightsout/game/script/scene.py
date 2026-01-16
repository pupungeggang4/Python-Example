import pygame, sys

from .game import Game
from .util import Util
from .board import Board

class Scene():
    board_start: list[int] = [120, 20]
    cell_size: list[int] = [80, 80]

    @staticmethod
    def loop(game: Game) -> None:
        Scene.render(game)

    @staticmethod
    def render(game: Game) -> None:
        game.window.fill([255, 255, 255])
        for i in range(7):
            for j in range(7):
                if game.board[i][j] == 0:
                    game.window.blit(game.img_off, [Scene.board_start[0] + Scene.cell_size[0] * j, Scene.board_start[1] + Scene.cell_size[1] * i])
                else:
                    game.window.blit(game.img_on, [Scene.board_start[0] + Scene.cell_size[0] * j, Scene.board_start[1] + Scene.cell_size[1] * i])
        pygame.display.flip()

    @staticmethod
    def mouse_up(game: Game, pos: list[float], button: int) -> None:
        if button == 1:
            for i in range(7):
                for j in range(7):
                    if Util.point_inside_rect_ui(pos, [Scene.board_start[0] + Scene.cell_size[0] * j, Scene.board_start[1] + Scene.cell_size[1] * i, Scene.cell_size[0], Scene.cell_size[1]]):
                        Board.flip(game.board, [i, j])
