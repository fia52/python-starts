from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
        else:
            x = self._top
            while x.next is not None:
                x = x.next
            x.next = obj

    def pop_back(self):
        if self._top.next:
            x = self._top.next
            end = self._top
            while x.next is not None:
                end = x
                x = x.next
            end.next = None
            return x
        else:
            c = self._top
            self._top = None
            return c


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, n):
        self._data = n


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

from abc import ABC, abstractmethod


it = iter(range(1, 1000))


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        """Абстрактный метод класса"""

    def get_info(self):
        return "Базовый класс Model"


class ModelForm(Model):
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = next(it)

    def get_pk(self):
        return self._id