from dataclasses import replace


def func(N : str) -> int:
    while ('52' in N) or ('2222' in N) or ('1122' in N):
        if '52' in N:
            N = N.replace('52', '11')
        if '2222' in N:
            N = N.replace('2222', '5')
        if '1122' in N:
            N = N.replace('1122', '25')

    return len(N)


for n in range(10 ** 4, 3, -1):
    if func('5' + '2' * n) == 64:
        print(n)
        break





print(int('1010000', 2))

# print(bin(240)[2:])
# print(bin(168)[2:])
# print(bin(32)[2:])
# print(bin(160)[2:])



