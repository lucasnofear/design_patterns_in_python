from abc import ABCMeta, abstractmethod

class IProtoType(metaclass=ABCMeta):
    "interface with clone method"

    @abstractmethod
    def clone(self, mode):
        """The clone method, deep or shallow, up to your implementation.
        """
        pass 

