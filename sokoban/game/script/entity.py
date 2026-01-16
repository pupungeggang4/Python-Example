class Entity():
    def __init__(self):
        self.pos: list[int] = [0, 0]
        self.floor: bool = False
        self.pushable: bool = False