import pygame, sys

from .game import Game
from .render import Render

class Scene():
    @staticmethod
    def loop(game: Game) -> None:
        Scene.render(game)

    @staticmethod
    def render(game: Game) -> None:
        game.window.fill([255, 255, 255])
        Render.render_board(game, game.board)
        pygame.display.flip()

    @staticmethod
    def key_down(game: Game, key: int) -> None:
        pass

    @staticmethod
    def key_up(game: Game, key: int) -> None:
        pass


