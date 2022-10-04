import time


def time_decorator(func):
    def wrapper(spisok, value):
        st = time.time()
        val = func(spisok, value)
        et = time.time()
        print(f"{func.__name__} : {et - st}")
        return val

    return wrapper


@time_decorator
def binary_search(spisok, value):
    low = 0
    high = len(spisok) - 1
    while low <= high:
        mid = (low + high) // 2
        if spisok[mid] == value:
            return mid
        elif spisok[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return None


@time_decorator
def prostoy_poisk(spisok, value):
    for i, x in enumerate(spisok):
        if x == value:
            return i


lst = list(range(10000000))


s1 = binary_search(lst, 100000)


s2 = prostoy_poisk(lst, 100000)


