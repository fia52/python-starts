from random import choice, randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1 for i in range(length)]

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def cells(self):
        return self._cells

    @property
    def tp(self):
        return self._tp

    @property
    def length(self):
        return self._length

    def set_start_coords(self, x, y):
        self._x, self._y = x, y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            else:
                self._y += go

    def listing_of_coords(self):
        list_of_coords = []

        if self._tp == 2:
            for i in range(self.x-1, self.x + self.length+1):
                for t in (-1, 0, 1):
                    coord = (i, self.y+t)
                    list_of_coords.append(coord)

        else:
            for i in range(self.y-1, self.y + self.length+1):
                for t in (-1, 0, 1):
                    coord = (self.x+t, i)
                    list_of_coords.append(coord)

        return list_of_coords

    def is_collide(self, ship):
        if ship.tp == 2:
            list_of_coords2 = [(x, ship.y) for x in range(self.x, self.x + self.length)]
        else:
            list_of_coords2 = [(ship.x, y) for y in range(self.y, self.y + self.length)]
        for i in self.listing_of_coords():
            if i in list_of_coords2:
                return True
        return False

    def is_out_pole(self, size):
        if self._x not in range(size) and self._y not in range(size):
            return True
        if self._tp == 2:
            if self._x + self.length not in range(size):
                return True
        else:
            if self._y + self.length not in range(size):
                return True
        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = []
        self._ready_ships = []

    def check_surrounding(self, ship):
        for j in self._ready_ships:
            if ship.is_collide(j):
                return True
        return False

    def init(self):
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(3, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2))]

        '''clear pole creating'''
        for i in range(self._size):
            line = []
            for j in range(self._size):
                line.append(0)
            self._pole.append(line)
        '''...................'''

        available_coords = [(x, y) for x in range(self._size-1) for y in range(self._size-1)]

        for i in self._ships:
            cont = True
            while cont:
                x, y = choice(available_coords)
                if len(available_coords) > 1:
                    available_coords.remove((x, y))
                try:
                    i.set_start_coords(x, y)
                    "проверка на столкновение с другими короблями"
                    if self.check_surrounding(i):
                        continue
                    "............................................"
                    if i.tp == 1:
                        self._pole[x][y:y + i.length] = i.cells
                        self._ready_ships.append(i)
                    else:
                        for l in range(x, x + i.length):
                            self._pole[l][y] = 1
                        self._ready_ships.append(i)
                    cont = False
                except IndexError:
                    continue

    def get_ships(self):
        return self._ships

    def move_ships(self): ...


    def show(self):
        for i in self._pole:
            for j in i:
                print(j, end=' ')
            print()

    def get_pole(self): ...


pol = GamePole(10)
pol.init()
pol.show()

# s1 = Ship(4, 1, 0, 0)
# s2 = Ship(3, 1, 3, 0)
# print(s1.is_collide(s2))
















