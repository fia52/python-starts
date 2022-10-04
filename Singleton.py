class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if type(cls) is Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base

        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __del__(self):
        Singleton._instance = None


class Game(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name


s = Game("fdf")
print(s.name)
f = Game("sff")
print(f.name)
print(id(s), id(f))