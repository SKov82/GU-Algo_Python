from random import randint
import cProfile

# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой, так и различаться.


def get_array(size):
    a = [randint(-10000, 10000) for _ in range(size)]
    return a


def task_1(size):
    a = get_array(size)
    len_ = len(a)

    for j in range(1, len_):
        for i in range(len_ - j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    min = a[:2]


def task_2(size):
    a = get_array(size)
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


def task_3(size):
    a = get_array(size)
    min1 = min(a)
    a.remove(min1)
    min2 = min(a)


def task_4(size):
    a = get_array(size)
    min1 = min(a)
    i = a.index(min1)
    min2 = min(a[:i] + a[i+1:])


# python -m timeit -n 200 -s "import task_11" "task_11.task_1(N)"

# task_1(n)
# 200 loops, best of 3: 17.2 usec per loop - 10
# 100 loops, best of 3: 183 usec per loop - 50
# 200 loops, best of 3: 617 usec per loop - 100
# 100 loops, best of 3: 14.7 msec per loop - 500
# 200 loops, best of 3: 65.2 msec per loop - 1000
# cProfile.run('task_1(500)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       500    0.000    0.000    0.001    0.000 random.py:217(randint)
#         1    0.000    0.000    0.001    0.001 task_11.py:12(get_array)
#         1    0.015    0.015    0.016    0.016 task_11.py:17(task_1)
#       822    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('task_1(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1000    0.000    0.000    0.001    0.000 random.py:217(randint)
#         1    0.000    0.000    0.002    0.002 task_11.py:12(get_array)
#         1    0.066    0.066    0.067    0.067 task_11.py:17(task_1)
#      1618    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Теоретически сложноть O(n^2) в худшем случае, т.к. два вложенных цикла.
# Но т.к. с каждым шагом внешнего цикла, внутренний цикл на шаг короче, реальная
# сложность где-то между квадратичной и линеарифметической O(n log n)

# task_2(n)
# 100 loops, best of 3: 11 usec per loop - 10
# 100 loops, best of 3: 103 usec per loop - 100
# 100 loops, best of 3: 516 usec per loop - 500
# 100 loops, best of 3: 1.03 msec per loop - 1000
# cProfile.run('task_2(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1000    0.000    0.000    0.001    0.000 random.py:217(randint)
#         1    0.000    0.000    0.002    0.002 task_11.py:12(get_array)
#         1    0.000    0.000    0.002    0.002 task_11.py:28(task_2)
#      1628    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# cProfile.run('task_2(10000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     10000    0.002    0.000    0.014    0.000 random.py:217(randint)
#         1    0.000    0.000    0.016    0.016 task_11.py:12(get_array)
#         1    0.001    0.001    0.016    0.016 task_11.py:28(task_2)
#     16352    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

# Сложноть O(n), т.е. имеет линейную зависимость от размера входных данных.

# task_3(n)
# 100 loops, best of 3: 10.8 usec per loop - 10
# 100 loops, best of 3: 101 usec per loop - 100
# 100 loops, best of 3: 522 usec per loop - 500
# 100 loops, best of 3: 1.05 msec per loop - 1000
# cProfile.run('task_3(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1000    0.000    0.000    0.001    0.000 random.py:217(randint)
#         1    0.000    0.000    0.002    0.002 task_11.py:12(get_array)
#         1    0.000    0.000    0.002    0.002 task_11.py:43(task_3)
#      1721    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
# cProfile.run('task_3(10000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     10000    0.003    0.000    0.017    0.000 random.py:217(randint)
#         1    0.000    0.000    0.019    0.019 task_11.py:12(get_array)
#         1    0.000    0.000    0.020    0.020 task_11.py:43(task_3)
#     16332    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

# Сложноть O(n), т.е. имеет линейную зависимость от размера входных данных.

# task_4(n)
# 100 loops, best of 3: 11.3 usec per loop - 10
# 100 loops, best of 3: 101 usec per loop - 100
# 100 loops, best of 3: 1.01 msec per loop - 1000
# 100 loops, best of 3: 10.1 msec per loop - 10000
# cProfile.run('task_4(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1000    0.000    0.000    0.001    0.000 random.py:217(randint)
#         1    0.000    0.000    0.001    0.001 task_11.py:12(get_array)
#         1    0.000    0.000    0.002    0.002 task_11.py:50(task_4)
#      1565    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# cProfile.run('task_4(10000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     10000    0.002    0.000    0.014    0.000 random.py:217(randint)
#         1    0.000    0.000    0.015    0.015 task_11.py:12(get_array)
#         1    0.000    0.000    0.016    0.016 task_11.py:50(task_4)
#     16454    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# Сложноть O(n), т.е. имеет линейную зависимость от размера входных данных.

# Результат на лицо, либо 2-й вариант, либо встроенные методы
