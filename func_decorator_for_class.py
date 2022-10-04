def name_caller_decorator(func, box):
    """во время вызова функции из класса, их имя будет сохраняться в списке(box)"""
    def wrapper(*args):
        box.append(func.__name__)
        func(*args)
    return wrapper


def class_log(box):
    def class_log_dec(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, name_caller_decorator(v, box))

        return cls
    return class_log_dec


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)