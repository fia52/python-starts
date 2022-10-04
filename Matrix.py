class Matrix:
    def __init__(self, *args):
        if len(args) == 1:
            self.box = args[0]
            ln = len(self.box[0])
            for i in self.box:
                if len(i) != ln or any(map(lambda x: type(x) not in (float, int), i)):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.rows = len(self.box)
            self.cols = len(self.box[0])
        else:
            self.rows = args[0]
            self.cols = args[1]
            if type(args[2]) not in (int, float):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.fill_value = args[2]
            self.box = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row += [self.fill_value]
                self.box += [row]

    def __getitem__(self, item):
        if item[0] not in range(self.rows) or item[1] not in range(self.cols) or type(item[0]) is not int or type(item[1]) is not int:
            raise IndexError('недопустимые значения индексов')
        if type(self.box[item[0]][item[1]]) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')

        return self.box[item[0]][item[1]]

    def __setitem__(self, key, value):
        if key[0] not in range(self.rows) or key[1] not in range(self.cols) or type(key[0]) is not int or type(key[1]) is not int:
            raise IndexError('недопустимые значения индексов')
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.box[key[0]][key[1]] = value

    def __add__(self, other):
        res = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                if type(other) is Matrix:
                    if self.rows != other.rows or self.cols != other.cols:
                        raise ValueError('операции возможны только с матрицами равных размеров')
                    new_row += [self.box[i][j] + other.box[i][j]]
                else:
                    new_row += [self.box[i][j] + other]
            res += [new_row]
        return Matrix(res)

    def __sub__(self, other):
        res = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                if type(other) is Matrix:
                    if self.rows != other.rows or self.cols != other.cols:
                        raise ValueError('операции возможны только с матрицами равных размеров')
                    new_row += [self.box[i][j] - other.box[i][j]]
                else:
                    new_row += [self.box[i][j] - other]
            res += [new_row]
        return Matrix(res)