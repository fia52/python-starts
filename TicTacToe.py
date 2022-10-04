import random


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not self.value


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2

    def __init__(self):
        self.pole = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(Cell())
            self.pole.append(row)

    def init(self):
        self.pole = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(Cell())
            self.pole.append(row)

    def __getitem__(self, item):
        if item[0] not in range(3) or item[1] not in range(3) or type(item[0]) is not int or type(item[1]) is not int:
            raise IndexError('некорректно указанные индексы')
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if key[0] not in range(3) or key[1] not in range(3) or type(key[0]) is not int or type(key[1]) is not int:
            raise IndexError('некорректно указанные индексы')
        self.pole[key[0]][key[1]].value = value

    def human_go(self):
        h = 1
        while h:
            i = int(input('Введите ряд\n'))
            j = int(input('Введите столбец\n'))
            if self.pole[i][j]:
                self.pole[i][j].value = self.HUMAN_X
                h = 0

    def computer_go(self):
        h = 1
        while h:
            i, j = random.randint(0, 2), random.randint(0, 2)
            if self.pole[i][j]:
                self.pole[i][j].value = self.COMPUTER_O
                h = 0

    def show(self):
        for i in range(3):
            for j in range(3):
                if self.pole[i][j].value == 1:
                    print("+", end=' ')
                elif self.pole[i][j].value == 2:
                    print("0", end=' ')
                else:
                    print('%', end=" ")
            print()
        print()

    def __bool__(self):
        if game.is_human_win:
            return False
        elif game.is_computer_win:
            return False
        for i in self.pole:
            for j in i:
                if j.value == 0:
                    return True
        return False

    def check(self):
        for i in self.pole:
            if all(map(lambda x: x.value == self.HUMAN_X, i)):
                return 1
            if all(map(lambda x: x.value == self.COMPUTER_O, i)):
                return 2
        for j in range(3):
            if all(x.value == self.HUMAN_X for x in [self.pole[i][j] for i in range(3)]):
                return 1
            if all(x.value == self.COMPUTER_O for x in [self.pole[i][j] for i in range(3)]):
                return 2
        d1 = []
        d2 = []
        for i in range(3):
            for j in range(3):
                if i == j:
                    d1.append(self.pole[i][j])
                if j == 2 - i:
                    d2.append(self.pole[i][j])
        if all(x.value == self.HUMAN_X for x in d1):
            return 1
        if all(x.value == self.COMPUTER_O for x in d2):
            return 2
        if all(x.value == self.HUMAN_X for x in d1):
            return 1
        if all(x.value == self.COMPUTER_O for x in d2):
            return 2
        return 0

    @property
    def is_human_win(self):
        return self.check() == 1

    @property
    def is_computer_win(self):
        return self.check() == 2

    @property
    def is_draw(self):
        if self:
            return False
        return self.check() == 0


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
