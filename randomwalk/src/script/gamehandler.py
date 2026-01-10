import pygame, sys

from .game import Game
from .scene import Scene

class GameHandler():
    @staticmethod
    def run(game: Game) -> None:
        pygame.init()
        pygame.font.init()

        game.window = pygame.display.set_mode([800, 600], pygame.SCALED, vsync = 1)
        pygame.display.set_caption('Random Walk')
        game.clock = pygame.time.Clock()
        game.font = pygame.font.Font('asset/font/neodgm.ttf', 32)
        game.button_start = pygame.image.load('asset/image/buttonstart.png').convert()
        game.button_4_dir = pygame.image.load('asset/image/button4dir.png').convert()
        game.button_all = pygame.image.load('asset/image/buttonall.png').convert()

        Scene.generate_point(game, 0)
        GameHandler.loop(game)

    @staticmethod
    def loop(game: Game) -> None:
        while 1:
            game.clock.tick(game.fps)
            GameHandler.handle_input(game)
            GameHandler.handle_scene(game)

    @staticmethod
    def handle_scene(game: Game) -> None:
        Scene.loop(game)

    @staticmethod
    def handle_input(game: Game) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos: list[int] = pygame.mouse.get_pos()
                button: int = event.button
                Scene.mouse_up(game, pos, button)

            if event.type == pygame.KEYDOWN:
                key: int = event.key
                Scene.key_down(game, key)