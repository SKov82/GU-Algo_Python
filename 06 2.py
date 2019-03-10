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


# 2-3. Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, для числа 3486 надо вывести число 6843.

# Вариант 1 - 52
num = int(input('Введите натуральное число: '))
new = 0

while num:
    new = new * 10 + num % 10
    num //= 10

print(new)

mem_size(num, new)


# Вариант 2 - 83
num = input('Введите натуральное число: ')
new = int(num[::-1])
print(new)

mem_size(num, new)


# Вариант 3 - 56
num = [i for i in input('Введите натуральное число: ')]

for i in range(len(num)//2):
    num[i], num[-i - 1] = num[-i - 1], num[i]
num = int(''.join(num))

print(num)

mem_size(num, i)

# 52
# 83, на самом деле еще больше, если убрать int()
# 56
