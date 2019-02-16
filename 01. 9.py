# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num = [float(input('Введите 3 разных числа: ')) for _ in range(3)]

if (num[1] < num[0] < num[2]) or (num[1] > num[0] > num[2]):
    print(f'Среднее: {num[0]}')
elif (num[0] < num[1] < num[2]) or (num[0] > num[1] > num[2]):
    print(f'Среднее: {num[1]}')
else:
    print(f'Среднее: {num[2]}')
