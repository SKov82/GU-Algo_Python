from random import randint


def mem_size(*args):
    def show_size(x, level=0, total=0):
        print('\t' * level, f'{type(x)}, size={x.__sizeof__()}, obj={x}')
        total += x.__sizeof__()
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for k, v in x.items():
                    total += k.__sizeof__()
                    show_size(k, level + 1)
                    total += v.__sizeof__()
                    show_size(v, level + 1)
            elif not isinstance(x, str):
                for item in x:
                    total += item.__sizeof__()
                    show_size(item, level + 1)
        return total

    total = 0
    for var in args:
        total += show_size(var)
    print(total)


# 3-7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой, так и различаться.

SIZE = 20
MIN_LIMIT = -500
MAX_LIMIT = 500

# Вариант 1 - 1048
a = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(a)

for j in range(1, SIZE):
    for i in range(SIZE - j):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

min_ = a[:2]
print(min_)

mem_size(SIZE, MIN_LIMIT, MAX_LIMIT, a, j, i, min_)


# Вариант 2 - 1024
a = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(a)
len_ = len(a)
min1, min2 = (a[0], a[1]) if a[1] > a[0] else (a[1], a[0])

for i in range(2, len_):
    if a[i] < min1:
        spam = min1
        min1 = a[i]
        if spam < min2:
            min2 = spam
    elif a[i] < min2:
        min2 = a[i]
print(min1, min2)

mem_size(SIZE, MIN_LIMIT, MAX_LIMIT, a, len_, min1, min2, i, spam)


# Вариант 3 - 912
a = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(a)
min1 = min(a)
a.remove(min1)
min2 = min(a)
print(min1, min2)

mem_size(SIZE, MIN_LIMIT, MAX_LIMIT, a, min1, min2)


# Вариант 4 - 968
a = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(a)
min1 = min(a)
i = a.index(min1)
min2 = min(a[:i] + a[i+1:])
print(min1, min2)

mem_size(SIZE, MIN_LIMIT, MAX_LIMIT, a, min1, min2, i)

# 1048
# 1024
# 912
# 968
