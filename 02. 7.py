# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input('Введите натуральное число: '))
sum_ = 0

for i in range(1, n + 1):
    sum_ += i

f = n * (n + 1) / 2

print(f'Для 1+2+...+n = n(n+1)/2, где n = {n}',
      f'{sum_} = {int(f)}', sum_ == f, sep='\n')
