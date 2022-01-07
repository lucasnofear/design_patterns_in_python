from threading import Lock, Thread

class SingletonMeta(type):
    """
    This is a thread-safe implementation of singleton
    """

    _instances = {}

    _lock: Lock = Lock()