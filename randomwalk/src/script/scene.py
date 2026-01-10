import math, pygame, random
from .game import Game
from .ui import UI
from .util import Util

class Scene():
    @staticmethod
    def loop(game: Game) -> None:
        Scene.render(game)

    @staticmethod
    def render(game: Game) -> None:
        game.window.fill([255, 255, 255])
        for i in range(len(game.points) - 1):
            pygame.draw.line(game.window, [0, 0, 0], game.points[i], game.points[i + 1], 5)
        game.window.blit(game.font.render(f'Step Size: {game.step_size}', False, [0, 0, 0]), UI.screen['text_step_size'])
        game.window.blit(game.font.render(f'Step Num: {game.step_num}', False, [0, 0, 0]), UI.screen['text_step_num'])
        game.window.blit(game.button_4_dir, UI.screen['button_4_dir'])
        game.window.blit(game.button_all, UI.screen['button_all'])
        game.window.blit(game.button_start, UI.screen['button_start'])
        pygame.display.flip()

    @staticmethod
    def mouse_up(game: Game, pos: list[float], button: int) -> None:
        if button == 1:
            if Util.point_inside_rect_ui(pos, UI.screen['button_start']):
                Scene.generate_point(game, game.mode)
            elif Util.point_inside_rect_ui(pos, UI.screen['button_4_dir']):
                game.mode = 1
            elif Util.point_inside_rect_ui(pos, UI.screen['button_all']):
                game.mode = 0
            elif Util.point_inside_rect_ui(pos, UI.screen['area_step_size']):
                game.mode_edit = 1
            elif Util.point_inside_rect_ui(pos, UI.screen['area_step_num']):
                game.mode_edit = 2

    @staticmethod
    def key_down(game: Game, key: int) -> None:
        if game.mode_edit == 1:
            if key >= pygame.K_0 and key <= pygame.K_9:
                game.step_size = game.step_size * 10 + (key - pygame.K_0)
                if game.step_size > 200:
                    game.step_size = 200
            elif key == pygame.K_BACKSPACE:
                game.step_size //= 10
        elif game.mode_edit == 2:
            if key >= pygame.K_0 and key <= pygame.K_9:
                game.step_num = game.step_num * 10 + (key - pygame.K_0)
                if game.step_num > 999:
                    game.step_num = 999
            elif key == pygame.K_BACKSPACE:
                game.step_num //= 10

    @staticmethod
    def generate_point(game: Game, mode: int) -> None:
        game.points = [[400, 300]]
        current_pos: list[int] = [400, 300]
        if mode == 0:
            for i in range(game.step_num):
                angle = random.randint(0, 359)
                angle *= math.pi / 180
                current_pos[0] += game.step_size * math.cos(angle)
                current_pos[1] += game.step_size * math.sin(angle)
                game.points.append([current_pos[0], current_pos[1]])
        else:
            for i in range(game.step_num):
                direction = random.randint(0, 3)
                if direction == 0:
                    current_pos[0] += game.step_size
                elif direction == 1:
                    current_pos[0] -= game.step_size
                elif direction == 2:
                    current_pos[1] += game.step_size
                else:
                    current_pos[1] -= game.step_size
                game.points.append([current_pos[0], current_pos[1]])