from abc import ABCMeta, abstractmethod

class IHouseBuilder(metaclass=ABCMeta):
    "The House Builder interface"

    @abstractmethod
    def set_building_type(self, building_type):
        pass 

    @abstractmethod
    def set_wall_material(self, wall_material):
        pass 

    @abstractmethod
    def set_number_doors(self, number):
        pass 

    @abstractmethod
    def set_number_windows(self, number):
        pass

    @abstractmethod
    def get_result(self):
        "Return the final product"
        pass