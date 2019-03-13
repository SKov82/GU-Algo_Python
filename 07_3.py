from random import randint
import statistics

MIN_LIMIT = -50
MAX_LIMIT = 50
m = randint(1, 6)
SIZE = 2 * m + 1

# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом
# Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной
# находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках


def median(array, mid):

    if len(array) == 1 and mid == 0:
        return array[0]

    pivot = array[mid]
    eq = [x for x in array if x == pivot]
    lt = [x for x in array if x < pivot]
    gt = [x for x in array if x > pivot]

    if mid < len(lt):
        return median(lt, mid)
    elif mid < (len(lt) + len(eq)):
        return pivot
    else:
        return median(gt, mid - len(lt) - len(eq))


def median2(array):
    pivot = array[len(array) // 2]
    eq = [x for x in array if x == pivot]
    lt = [x for x in array if x < pivot]
    gt = [x for x in array if x > pivot]

    if len(lt) != len(gt) and len(eq) % 2 != 0:
        return median2(lt + eq + gt)

    return pivot


def median3(array):
    for _ in range(len(array) // 2 + 1):
        pivot = min(array)
        array.remove(pivot)

    return pivot


array = [randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(array)

print(statistics.median(array))
print(median(array, len(array) // 2))
print(median2(array))
print(median3(array))
