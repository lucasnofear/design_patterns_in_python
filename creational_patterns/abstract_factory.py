from abc import ABCMeta, abstractmethod
from factory import SmallChair, MediumChair, BigChair

from factory import ChairFactory

class IFurnitureFactory(metaclass=ABCMeta):
    "Abstract Furniture Factory Interface"

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        "The static Abstract factory interface method"

class FurnitureFactory(IFurnitureFactory):
    "The Abstract Factory Concrete Class"

    @staticmethod
    def get_furniture(furniture):
        try:
            if furniture in ['SmallChair', 'MediumChair', 'BigChair', 'NormalChair']:
                return ChairFactory.get_chair(furniture)
            if furniture in ['SmallTable', 'MediumTable', 'BigTable']:
                return TableFactory.get_table(furniture)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None 

class ChairFactory:
    
    @staticmethod
    def get_chair(chair):
        try:
            if chair == 'BigChair':
                return BigChair()
            if chair == 'MediumChair':
                return MediumChair()
            if chair == 'SmallChair':
                return SmallChair()
            raise Exception('Chair Not Found')
        except Exception as _e:
            print(_e)
        return None 

if __name__ == "__main__":
    # notice the Table Factory is not implemented but it will be exact the same as the Chair Factory
    # and the Chair Factory is from the factory.py (an example of factory pattern)
    furniture = FurnitureFactory.get_furniture("SmallChair")
    print(f"{furniture.__class__} : {furniture.get_dimensions()}")

    furniture = FurnitureFactory.get_furniture("NormalChair")
