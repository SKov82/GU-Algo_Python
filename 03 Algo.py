from random import randint

SIZE = 12
MIN_LIMIT = -50
MAX_LIMIT = 50

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9.


def task_1():
    print('\nЗадача 1:\n')

    array = [[] for _ in range(8)]

    for i in range(2, 10):
        for j in range(2, 100):
            if j % i == 0:
                array[i - 2].append(j)

    for i in range(8):
        print(f'В диапазоне 2-99 числу {i+2} кратно {len(array[i])} чисел:',
              array[i], sep='\n')


# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5 ,
# т.к. именно в этих позициях первого массива стоят четные числа.


def task_2():
    print('\nЗадача 2:\n')

    even = []
    array = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]

    for i in range(SIZE):
        if array[i] % 2 == 0:
            even.append(i)

    print(array, even, sep='\n')


# 3. В массиве случайных целых чисел поменять местами миним и максим элементы.


def task_3():
    print('\nЗадача 3:\n')

    array = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
    print(array)
    min_ = max_ = array[0]
    min_i = max_i = 0

    for i in range(1, SIZE):
        if array[i] < min_:
            min_ = array[i]
            min_i = i
        elif array[i] > max_:
            max_ = array[i]
            max_i = i

    array[min_i], array[max_i] = max_, min_
    print(array)


# 4. Определить, какое число в массиве встречается чаще всего.


def task_4():
    print('\nЗадача 4:\n')

    array = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
    print(array)
    num = None
    max_cnt = 1

    for i in set(array):
        cnt = 0

        for j in array:
            if i == j:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt
            num = i
        elif cnt == max_cnt:  # Если таких чисел > 1
            max_cnt = 1       # то считаем, что самого частого числа нет

    if max_cnt > 1:
        print(f'Число {num} встречается {max_cnt} раз(а).')


# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


def task_5():
    print('\nЗадача 5:\n')

    array = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
    print(array)
    max_neg = MIN_LIMIT
    max_i = None

    for i in range(SIZE):
        if max_neg < array[i] < 0:
            max_neg = array[i]
            max_i = i

    if max_i:
        print(f'Значение = {max_neg}, Индекс: {max_i}')
    else:
        print('В массиве нет отрицательных элементов.')


# 6. В одномерном массиве найти сумму элементов, между минимальн и максимальн
# элементами. Сами минимальный и максимальный элементы в сумму не включать.


def task_6():
    print('\nЗадача 6:\n')

    array = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
    print(array)
    min_ = max_ = array[0]
    min_i = max_i = sum_ = 0

    for i in range(1, SIZE):
        if array[i] < min_:
            min_ = array[i]
            min_i = i
        elif array[i] > max_:
            max_ = array[i]
            max_i = i

    if min_i > max_i:
        min_i, max_i = max_i, min_i

    for i in range(min_i + 1, max_i):
        sum_ += array[i]

    print(array[min_i + 1:max_i], f'Сумма = {sum_}', sep='\n')


# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой, так и различаться.


def task_7():
    print('\nЗадача 7:\n')

    array = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
    print(array)

    for j in range(1, SIZE):
        for i in range(SIZE - j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    print(array[:2])


# 8. Матрица 5x4 заполняется с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.


def task_8():
    print('\nЗадача 8:\n')

    matrix = []
    for i in range(4):
        row = []
        sum_ = 0

        for j in range(4):
            num = int(input('Введите целое число: '))
            sum_ += num
            row.append(num)

        row.append(sum_)
        matrix.append(row)

    for i in range(4):
        for j in range(5):
            print(f'{matrix[i][j]:>5}', end='')
        print('')


# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


def task_9():
    print('\nЗадача 9:\n')

    array = [[randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
             for _ in range(SIZE)]
    max_ = MIN_LIMIT
    if len(str(MIN_LIMIT)) > len(str(MAX_LIMIT)):
        len_ = len(str(MIN_LIMIT))
    else:
        len_ = len(str(MAX_LIMIT))

    for j in range(SIZE):
        min_ = MAX_LIMIT

        for i in range(SIZE):
            if array[i][j] < min_:
                min_ = array[i][j]
            print(f'{array[j][i]:>{len_ + 2}}', end='')
        print('')

        if min_ > max_:
            max_ = min_

    print(f'\nМаксимальный элемент = {max_}')


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
task_7()
task_8()
task_9()
