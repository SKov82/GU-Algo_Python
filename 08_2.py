from collections import Counter

# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

S = 'Клара украла кораллы'


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


table = {}
array = [(k, v) for k, v in sorted(Counter(S).items(), key=lambda x: x[1])]

while len(array) > 1:
    node = MyNode(array[0][1] + array[1][1], array.pop(0)[0], array.pop(0)[0])

    for i in range(len(array)):
        if node.value <= array[i][1]:
            array.insert(i, (node, node.value))
            break
    else:
        array.append((node, node.value))


def get_code(array, code=''):
    if isinstance(array, MyNode):
        get_code(array.left, code + '0')
        get_code(array.right, code + '1')
    else:
        table[array] = code


get_code(array[0][0])

for i in S:
    print(i, table[i], end='\n')
