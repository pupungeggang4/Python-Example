import pygame, sys

from .game import Game
from .scene import Scene

class GameHandler():
    @staticmethod
    def run(game: Game) -> None:
        game.window = pygame.display.set_mode([800, 600], pygame.SCALED, vsync = 1)
        pygame.display.set_caption('Sokoban Example')
        game.clock = pygame.time.Clock()
        GameHandler.loop(game)

    @staticmethod
    def loop(game: Game) -> None:
        while 1:
            game.clock.tick(game.fps)
            GameHandler.handle_scene(game)
            GameHandler.handle_input(game)

    @staticmethod
    def handle_scene(game: Game) -> None:
        Scene.loop(game)

    @staticmethod
    def handle_input(game: Game) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
