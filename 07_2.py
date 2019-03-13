from random import randint, uniform

# SIZE = 15
MIN_LIMIT = 0
MAX_LIMIT = 50

# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


def merge(array):
    if len(array) > 1:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]

        merge(left)
        merge(right)

        i = li = ri = 0
        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                array[i] = left[li]
                li += 1
            else:
                array[i] = right[ri]
                ri += 1
            i += 1

        while li < len(left):
            array[i] = left[li]
            li += 1
            i += 1

        while ri < len(right):
            array[i] = right[ri]
            ri += 1
            i += 1

    return array


array = [uniform(MIN_LIMIT, MAX_LIMIT) for _ in range(randint(5, 10))]
print(array)

print(merge(array))
