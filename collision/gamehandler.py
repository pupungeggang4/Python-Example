from shape import Vec2, Shape2, Circle2, Rect2

class GameHandler():
    UI: dict[str, list[int]] = {
        'button_rect': [],
        'button_circle': [],
        'button_circle_sector': []
    }

    @staticmethod
    def run() -> None:
        pass

    @staticmethod
    def loop() -> None:
        pass
    
    @staticmethod
    def render_target_shape(shape: Shape2) -> None:
        pass

    @staticmethod
    def render_circle_list(circle_list: list[Circle2]) -> None:
        pass