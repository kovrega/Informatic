

from itertools import product, permutations

alf = '0123456789ABCDEF'
res = set()

for x in product(alf, repeat = 12):
    # s = ''.join(x)
    # if x[0] != '0':
    if all(int(x[i], 16) > int(x[i + 1], 16)  for i in range(len(x) - 1)):
        if all(int(x[i], 16) % 2 != int(x[i + 1], 16) % 2 for i in range(len(x) - 1)):
            res.add(''.join(x))



print(len(res))





