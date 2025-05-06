from .shape import Shape
from decorator.logger import logger


class Square(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def get_type(cls) -> str:
        return cls.__name__

    @logger
    def get_opp(self) -> float:
        """"get opp"""
        return float(self.x * self.y)  # afdwingen van float return type
