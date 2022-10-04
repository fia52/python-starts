import random


class GamePole:
    __instance = None

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.pole = [[]]

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @property
    def pole(self):
        return self.__pole_cells

    @pole.setter
    def pole(self, t):
        self.__pole_cells = t

    def init_pole(self):
        pol = []
        for i in range(self.N):
            lis = []
            for t in range(self.M):
                lis.append(Cell())
            pol.append(lis)
        self.pole = pol
        self.mining_pol()
        self.mines_around()

    def mines_around(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                n = 0
                for h in range(-1, 2):
                    for u in range(-1, 2):
                        x = i + h
                        y = j + u
                        if x < 0 or x >= self.N or y < 0 or y >= self.M:
                            continue
                        if self.pole[x][y].is_mine:
                            n += 1
                self.pole[i][j].number = n

    def mining_pol(self):
        for t in range(self.total_mines):
            g = random.randrange(self.N)
            h = random.randrange(self.M)
            self.pole[g][h].is_mine = True

    def open_cell(self, i, j):
        try:
            self.pole[i][j].is_open = True
        except:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if self.pole[i][j].is_open:
                    if self.pole[i][j].is_mine:
                        print("*", end = "")
                    else:
                        print(self.pole[i][j].number, end = "")
                else:
                    print("%", end = "")
            print()


class Cell:
    def __init__(self):
        self.is_mine = False
        self.number = 0
        self.is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, d):
        if type(d) is bool:
            self.__is_mine = d
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, m):
        if m in range(9):
            self.__number = m
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, l):
        if type(l) is bool:
            self.__is_open = l
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return not self.is_open


pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
for i in range(len(pole.pole)):
    for j in range(len(pole.pole[i])):
        pole.open_cell(i, j)
#pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
