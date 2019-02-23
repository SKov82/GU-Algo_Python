# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# Вариант 1
max_n = max_s = 0
while True:
    n = int(input('Введите натуральное число (0 для выхода): '))

    if n:
        sum_ = 0; num = n

        while n != 0:
            sum_ += n % 10
            n //= 10

        if sum_ > max_s:
            max_n = num; max_s = sum_

    else:
        print(f'Число {max_n}. Сумма цифр {max_s}')
        break


# Вариант 2
def sum_d(max_n=0, max_s=0):
    n = int(input('Введите натуральное число (0 для выхода): '))
    sum_ = 0; num = n

    while n:
        sum_ += n % 10
        n //= 10

    if sum_ > max_s:
        max_n = num; max_s = sum_

    sum_d(max_n, max_s) if num else print(f'Число {max_n}. Сумма цифр {max_s}')


sum_d()
