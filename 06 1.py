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


# 1-9. Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

# Вариант 1 - 156
num = [int(input('Введите 3 разных числа: ')) for _ in range(3)]

if (num[1] < num[0] < num[2]) or (num[1] > num[0] > num[2]):
    print(f'Среднее: {num[0]}')
elif (num[0] < num[1] < num[2]) or (num[0] > num[1] > num[2]):
    print(f'Среднее: {num[1]}')
else:
    print(f'Среднее: {num[2]}')

mem_size(num)


# Вариант 2 - 84
a = int(input('Введите 3 разных числа: '))
b = int(input('Введите 3 разных числа: '))
c = int(input('Введите 3 разных числа: '))

if (b < a < c) or (b > a > c):
    print(f'Среднее: {a}')
elif (a < b < c) or (a > b > c):
    print(f'Среднее: {b}')
else:
    print(f'Среднее: {c}')

mem_size(a, b, c)


# Вариант 3 - 156
num = [int(input('Введите 3 разных числа: ')) for _ in range(3)]
num.sort()
print(num[1])

mem_size(num)

# 156
# 84
# 156
