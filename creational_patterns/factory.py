from abc import ABCMeta, abstractmethod

class IChair(metaclass=ABCMeta):
    "The Chair Interface (Product)"

    #@staticmethod
    @abstractmethod
    def get_dimensions(self):
        "A static interface method"

class SmallChair(IChair):
    "The Small Chair Concrete Class that implements the IChair interface"

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40
    
    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

class MediumChair(IChair):
    "The Medium Chair Concrete Class that implements the IChair interface"

    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60
    
    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

class BigChair(IChair):
    "The Big Chair Concrete Class that implements the IChair interface"

    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80
    
    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

class ChairFactory:
    "The Factory Class"

    @staticmethod
    def get_chair(chair):
        "A static method to get a chair"
        if chair == 'BigChair':
            return BigChair()
        if chair == 'MediumChair':
            return MediumChair()
        if chair == 'SmallChair':
            return SmallChair()
        return None 

if __name__ == "__main__":
    chair = ChairFactory.get_chair("SmallChair")
    print(chair.get_dimensions())
        