import pygame, sys

from .game import Game

class GameHandler():
    @staticmethod
    def run(game: Game) -> None:
        pygame.init()
        game.window = pygame.display.set_mode([800, 600], pygame.SCALED, vsync=1)
        pygame.display.set_caption('Lights Out')
        game.clock = pygame.time.Clock()
        game.img_off = pygame.image.load('asset/image/off.png').convert_alpha()
        game.img_on = pygame.image.load('asset/image/on.png').convert_alpha()
        GameHandler.loop(game)

    @staticmethod
    def loop(game: Game) -> None:
        while 1:
            game.clock.tick(game.fps)
            GameHandler.handle_scene(game)
            GameHandler.handle_input(game)

    @staticmethod
    def handle_scene(game: Game) -> None:
        pass

    @staticmethod
    def handle_input(game: Game) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
