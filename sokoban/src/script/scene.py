import pygame, sys

from .game import Game

class Scene():
    @staticmethod
    def loop(game: Game) -> None:
        Scene.render(game)

    @staticmethod
    def render(game: Game) -> None:
        game.window.fill([255, 255, 255])
        pygame.display.flip()

    @staticmethod
    def key_down(game: Game, key: int) -> None:
        pass

    @staticmethod
    def key_up(game: Game, key: int) -> None:
        pass


