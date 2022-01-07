class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python, including:
    base class, decorator, metaclass. Here will use metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the '__init__'argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass 

if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    print(id(s1), id(s2))