from math import sqrt

class Vec2():
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __add__(self, v: 'Vec2') -> 'Vec2':
        return Vec2(self.x + v.x, self.y + v.y)
    
    def __sub__(self, v: 'Vec2') -> 'Vec2':
        return Vec2(self.x - v.x, self.y - v.y)
    
    def __mul__(self, a: float) -> 'Vec2':
        return Vec2(self.x * a, self.y * a)

    def __rmul__(self, a: float) -> 'Vec2':
        return Vec2(self.x * a, self.y * a)
    
    def __truediv__(self, a: float) -> 'Vec2':
        if a == 0:
            raise ZeroDivisionError('Divide by zero.')
        return Vec2(self.x / a, self.y / a)

    def __repr__(self) -> str:
        return f'Vec2({self.x}, {self.y})'

    def length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

class Rect2():
    def __init__(self, x: float, y: float, w: float, h: float):
        self.pos: Vec2 = Vec2(x, y)
        self.size: Vec2 = Vec2(w, h)

    def __repr__(self) -> str:
        return f'Rect2({self.pos.x}, {self.pos.y}, {self.size.x}, {self.size.y})'