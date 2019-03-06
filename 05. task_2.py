# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# Каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

HEX = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
       '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
DEC = ('0', '1', '2', '3', '4', '5', '6', '7',
       '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def main(a, b):
    a, b = ([i for i in j.upper()] for j in (a, b))
    print(a, b)
    a, b = get_dec(a, b)
    add = a + b
    mul = a * b
    return get_hex(add, mul)


def get_dec(a, b):
    num = [0, 0]
    pos = 0

    for digit in (a, b):
        for i in range(len(digit)):
            num[pos] += HEX[digit.pop()] * 16 ** i
        pos += 1

    return num


def get_hex(add, mul):
    num = [[], []]
    pos = 0

    for digit in (add, mul):
        while digit > 0:
            num[pos].insert(0, DEC[digit % 16])
            digit //= 16
        pos += 1

    return num


if __name__ == '__main__':
    a, b = (input(f'Введите число {i + 1}: ') for i in range(2))
    print(main(a, b))
