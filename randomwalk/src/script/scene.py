from .game import Game

class Scene():
    @staticmethod
    def loop(game: Game) -> None:
        render(game)

    @staticmethod
    def render(game: Game) -> None:
        pass

    @staticmethod
    def mouse_up(game: Game, pos: list[float], button: int) -> None:
        pass
