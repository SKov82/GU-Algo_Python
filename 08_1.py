import hashlib

# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

S = 'papas'
N = len(S)

subs = set()
subsh = set()
for i in range(N):
    for j in range(N, i, -1):
        if S[i:j] != S:
            subs.add(S[i:j])
            subsh.add(hashlib.sha3_256(S[i:j].encode('utf-8')).hexdigest())

print(f'В строке "{S}" {len(subsh)} подстрок', sorted(tuple(subs)))
