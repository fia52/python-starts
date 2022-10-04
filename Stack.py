class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.box = []
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            x = self.top
            while x.next is not None:
                x = x.next
            x.next = obj

    def push_front(self, obj):
        if self.top is None:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __setitem__(self, key, value):
        if key not in range(len(self)-1):
            raise IndexError('неверный индекс')
        x = self.top
        for i in range(key):
            x = x.next
        x.data = value

    def __getitem__(self, item):
        if item not in range(len(self)):
            raise IndexError('неверный индекс')
        x = self.top
        for i in range(item):
            x = x.next
        return x.data

    def __len__(self):
        if self.top is None:
            return 0
        x = self.top
        i = 1
        while x.next is not None:
            x = x.next
            i += 1
        return i

    def __iter__(self):
        x = self.top
        for i in range(len(self)):
            j = x
            x = x.next
            yield j


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


