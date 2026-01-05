from math import sqrt, atan2, degrees, radians

class Vec2():
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __repr__(self) -> str:
        return f'Vec2({self.x:.2f}, {self.y:.2f})'
    
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
            raise ZeroDivisionError('Division by zero!')
        else:
            return Vec2(self.x / a, self.y / a)

    def length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self) -> float:
        return self / self.length()
    
    def angle(self) -> float:
        return degrees(atan2(self.y, self.x))

class Shape2():
    def __init__(self):
        pass

class Rect2(Shape2):
    def __init__(self, x: float, y: float, w: float, h: float):
        self.pos: Vec2 = Vec2(x, y)
        self.size: Vec2 = Vec2(w, h)

    def __repr__(self) -> str:
        return f'Rect2({self.pos.x:.2f}, {self.pos.y:.2f}, {self.size.x:.2f}, {self.size.y:.2f})'
    
class Circle2(Shape2):
    def __init__(self, x: float, y: float, r: float):
        self.pos: Vec2 = Vec2(x, y)
        self.r: float = r

    def __repr__(self) -> str:
        return f'Circle2({self.pos.x:.2f}, {self.pos.y:.2f}, {self.r:.2f})'
    
class CircleSector2(Shape2):
    def __init__(self, x: float, y: float, r: float, ray: float, central_angle: float):
        self.pos: Vec2 = Vec2(x, y)
        self.r = r
        self.ray = ray
        self.c = central_angle

    def __repr__(self) -> str:
        return f'CS2({self.pos.x:.2f}, {self.pos.y:.2f}, {self.r:.2f}, {self.ray:.2f}, {self.c:.2f})'