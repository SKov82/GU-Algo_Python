from random import randint

# SIZE = 15
MIN_LIMIT = -100
MAX_LIMIT = 100

# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).


def bubble(array, step=0):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
            step += 1
        n += 1
    print(f'{array} за {step} шагов.')


def my_bubble(array, step=0):
    for j in range(1, len(array)):
        skip = True

        for i in range(len(array) - j):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                skip = False
            step += 1

        if skip:
            break
    print(f'{array} за {step} шагов.')


def bubbles(array, step=0):
    pass


array = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(randint(10, 20))]
print(array)

bubble(array)
my_bubble(array)
