from random import choice, randint, random


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

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def cells(self):
        return self._cells

    @property
    def tp(self):
        return self._tp

    @tp.setter
    def tp(self, tp):
        self._tp = tp

    @property
    def length(self):
        return self._length

    def set_start_coords(self, x, y):
        self.x, self.y = x, y

    def get_start_coords(self):
        return self.x, self.y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self.x += go
            else:
                self.y += go

    def listing_of_coords(self):
        list_of_coords = []

        if self._tp == 1:
            for i in range(self.x - 1, self.x + self.length + 1):
                for t in (-1, 0, 1):
                    coord = (i, self.y + t)
                    list_of_coords.append(coord)

        else:
            for i in range(self.y - 1, self.y + self.length + 1):
                for t in (-1, 0, 1):
                    coord = (self.x + t, i)
                    list_of_coords.append(coord)

        return list_of_coords

    def is_collide(self, ship):
        if ship.tp == 1:
            list_of_coords2 = [(x, ship.y) for x in range(ship.x, ship.x + ship.length)]
        else:
            list_of_coords2 = [(ship.x, y) for y in range(ship.y, ship.y + ship.length)]
        # print(list_of_coords2)
        # print(self.listing_of_coords())
        for i in list_of_coords2:
            if i in self.listing_of_coords():
                return True
        return False

    def is_out_pole(self, size):
        if self.x not in range(size) and self.y not in range(size):
            return True
        if self._tp == 1:
            if self.x + self.length - 1 not in range(size):
                return True
        else:
            if self.y + self.length - 1 not in range(size):
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
        self._non_available_coords = []

    # def check_surrounding(self, ship):
    #     temp = self._ready_ships[:]
    #     temp.remove(ship)
    #     for j in temp:
    #         if ship.is_collide(j):
    #             return True
    #     return False

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

        available_coords = [(x, y) for x in range(self._size) for y in range(self._size)]
        waiting_ships = self._ships[:]

        for i in self._ships:
            cont = True
            while cont:
                x, y = choice(available_coords)
                if len(available_coords) > 1:
                    available_coords.remove((x, y))
                try:

                    """проверка на наличие достаточных свободных мест"""
                    checking_distance = i.length
                    """.............................................."""

                    if i.tp == 2:
                        if all((x, y + a) not in self._non_available_coords for a in range(i.length)):
                            i.set_start_coords(x, y)
                            if i.is_out_pole(self._size):
                                available_coords.append((x, y))
                                continue
                            self._pole[x][y:y + i.length] = i.cells                                         #??????????????????????????????

                            """обрабатываем вспомогательные списки"""
                            self._non_available_coords.extend(i.listing_of_coords())
                            for g in i.listing_of_coords():
                                if g in available_coords:
                                    if len(available_coords) > 1:
                                        available_coords.remove(g)
                            """..................................."""

                            cont = False
                        else:
                            available_coords.append((x, y))
                            continue
                    else:  # i.tp == 1
                        if all((x + a, y) not in self._non_available_coords for a in range(i.length)):
                            i.set_start_coords(x, y)
                            for l in range(x, x + i.length):
                                self._pole[l][y] = 1
                            cont = False

                            """обрабатываем вспомогательные списки"""
                            self._non_available_coords.extend(i.listing_of_coords())
                            for g in i.listing_of_coords():
                                if g in available_coords:
                                    if len(available_coords) > 1:
                                        available_coords.remove(g)
                            """..................................."""

                        else:
                            available_coords.append((x, y))
                            continue
                except IndexError:
                    available_coords.append((x, y))
                    continue

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for i in self._ships:
            x, y = i.get_start_coords()
            step_list = [1, -1]
            step = choice(step_list)
            step_list.remove(step)
            i.move(step)
            if i.tp == 2:
                if (i.x + step, i.y) in self._non_available_coords or i.is_out_pole(self._size):
                    i.move(step_list[0])
                    i.move(step_list[0])
                    if (i.x + step, i.y) in self._non_available_coords or i.is_out_pole(self._size):
                        i.move(step)
                    else:
                        self._pole[x][y] = 0
                        self._pole[i.x][i.y + i.length - 1] = 1
                else:
                    self._pole[x][y] = 0
                    self._pole[i.x][i.y + i.length - 1] = 1
            else:
                if (i.x, i.y + step) in self._non_available_coords or i.is_out_pole(self._size):
                    i.move(step_list[0])
                    i.move(step_list[0])
                    if (i.x, i.y + step) in self._non_available_coords or i.is_out_pole(self._size):
                        i.move(step)
                    else:
                        self._pole[x][y] = 0
                        self._pole[i.x + i.length - 1][i.y] = 1
                else:
                    self._pole[x][y] = 0
                    self._pole[i.x + i.length - 1][i.y] = 1

    def show(self):
        for i in self._pole:
            for j in i:
                print(j, end=' ')
            print()

    def get_pole(self):
        for i, x in enumerate(self._pole):
            self._pole[i] = tuple(self._pole[i])
        temp = tuple(self._pole)
        return temp


pole_size_8 = GamePole(8)
pole_size_8.init()
pole_size_8.show()