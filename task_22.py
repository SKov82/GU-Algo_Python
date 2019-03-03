import cProfile

# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»


def simple1(n):
    lst = [2, 3, 5, 7]

    if n < 5:
        return lst[n]
    i = 7
    num = 4

    while num != n:
        i += 2
        if i % 10 == 5 or i % 3 == 0 or i % 7 == 0:
            continue
        for j in lst[4:]:
            if i % j == 0:
                break
        else:
            lst.append(i)
            num += 1

    return i


def simple2(n):
    lst = [2]
    i = 3

    while len(lst) != n:
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
        i += 2

    return lst[-1]


def sieve(n):  # максимум 168
    end = 1001  # как у Эратосфена до числа 1000
    s = [i for i in range(end)]
    s[1] = 0

    for i in range(2, end):
        if s[i] != 0:
            j = i + i
            while j < end:
                s[j] = 0
                j += i

    result = [i for i in s if i != 0]
    return result[n-1]


def my_sieve(n):
    end = 9999
    s = [i for i in range(end)]
    s[1] = 0

    for i in range(2, end):
        if s[i] != 0:
            j = i + i
            while j < end:
                s[j] = 0
                j += i

    result = [i for i in s if i != 0]
    return result[n-1]


# python -m timeit -n 100 -s "import task_22" "task_22.simple1(N)"

# print(simple1(50))
# 200 loops, best of 3: 58.4 usec per loop - 50
# 200 loops, best of 3: 218 usec per loop - 100
# 200 loops, best of 3: 481 usec per loop - 150
# 200 loops, best of 3: 5.29 msec per loop - 500
# 200 loops, best of 3: 21.8 msec per loop - 1000
# cProfile.run('simple1(100)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 task_22.py:8(simple1)
#        96    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('simple1(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.022    0.022    0.022    0.022 task_22.py:8(simple1)
#       996    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# print(simple2(50))
# 200 loops, best of 3: 45.1 usec per loop - 50
# 200 loops, best of 3: 125 usec per loop - 100
# 200 loops, best of 3: 219 usec per loop - 150
# 200 loops, best of 3: 1.2 msec per loop - 500
# 200 loops, best of 3: 3.14 msec per loop - 1000
# cProfile.run('simple2(100)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 task_22.py:30(simple2)
#       271    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('simple2(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    0.004    0.004 task_22.py:30(simple2)
#      3960    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# print(sieve(50))  # максимум 168
# 200 loops, best of 3: 205 usec per loop - 50
# 200 loops, best of 3: 205 usec per loop - 100
# 200 loops, best of 3: 210 usec per loop - 150
# cProfile.run('sieve(50)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 task_22.py:48(sieve)
# cProfile.run('sieve(150)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 task_22.py:48(sieve)

# print(my_sieve(50))
# 200 loops, best of 3: 2.3 msec per loop - 50
# 200 loops, best of 3: 2.3 msec per loop - 100
# 200 loops, best of 3: 2.29 msec per loop - 500
# 200 loops, best of 3: 2.32 msec per loop - 1000
# cProfile.run('my_sieve(100)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.002    0.002 task_22.py:64(my_sieve)
# cProfile.run('my_sieve(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.002    0.002 task_22.py:64(my_sieve)

# № 1 сложность O(n^2) - квадратичная
# № 2 сложность O(n log n) - линейно-логарифмическая
# № 3 и № 4 - для алгоритма решето Эратосфена теоретически сложность
# (n log (log n)) для составления списка простых чисел, но фактически в данном
# случае при поиске i-го элемента сложность константная O(1)
