from Constants import *
import math


class Item:
        def __init__(self, name: str="player 1", x: int=0, y: int=0) -> None:
            self.name = name
            self.x = x
            self.y = y
            self.size = 10
    
        @property
        def name(self) -> str:
            return self._name 
    
        @name.setter
        def name(self, value: str) -> None:
            if len(value) >= 2:
                self._name = value
            else:
                self._name = "player 1"
        
        @property
        def x(self) -> int:
            return self._x

        @x.setter
        def x(self, value: int) -> None:
            if value > WIDTH - 75:
                self._x = WIDTH - 75

            elif value >= 0:
                self._x = value    
            
            else:
                self._x = 0

        @property
        def y(self) -> int:
            return self._y

        @y.setter
        def y(self, value: int) -> None:
            if value > HEIGHT:
                self._y = HEIGHT
            
            elif value >= 0:
                self._y = value
            
            else:
                self._y = 0
        
        @property
        def size(self) -> int:
            return self._size 
        
        @size.setter
        def size(self, value: int) -> None:
            if value >= 1:
                self._size = value

        def goLeft(self, distance: int=1) -> None:
            self.x -= distance

        def goRight(self, distance: int=1) -> None:
            self.x += distance
        
        def goUp(self, distance: int=1) -> None:
            self.y -= distance
        
        def goDown(self, distance: int=1) -> None:
            self.y += distance

        def getDistance(self, person:object) -> float:
            return math.sqrt((self.x - person.x)**2 + (self.y - person.y)**2)
        
        def __str__(self) -> str:
            return f"Person({self.name}): \t size = {self.size},\t x = {self.x} \t y = {self.y}"