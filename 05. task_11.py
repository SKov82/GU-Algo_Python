from collections import Counter

# 1. Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

n = int(input('Введите кол-во предприятий: '))
cnt = Counter()

for i in range(n):
    name = input(f'Введите наименование {i+1}-го предприятия: ')
    for j in ('1234'):
        cnt[name] += int(input(f'Введите прибыль {name} за {j}-й кв., '
                                 f'тыс.руб.: '))
    cnt['avg_income'] += cnt[name] / n

gt = []
lt = []
for i in cnt:
    if cnt[i] > cnt['avg_income']:
        gt.append(f'{i} - {cnt[i]:,.2f} тыс.руб.')
    elif cnt[i] < cnt['avg_income']:
        lt.append(f'{i} - {cnt[i]:,.2f} тыс.руб.')

print(f'Средняя прибыль - {cnt["avg_income"]:,.2f} тыс.руб.',
      'Предприятия, с прибылью выше средней', gt,
      'Предприятия, с прибылью ниже средней', lt, sep='\n')
