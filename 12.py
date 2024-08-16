"""
1. Заменять надо ОДИН РАЗ. т.е. N = N.replace('num', 'num', 1)
2. Внимательно прочитать, какое финальная проверка должна быть
"""




def func(N : str) -> int:
    while ('52' in N) or ('2222' in N) or ('1122' in N):
        if '52' in N:
            N = N.replace('52', '11', 1)
        if '2222' in N:
            N = N.replace('2222', '5', 1)
        if '1122' in N:
            N = N.replace('1122', '25', 1)

    return sum(list(map(int, (' '.join(N).split()))))  # ->СУММА ЦИФР в строке должна быть равна 64, а НЕ ДЛИНА строки


for n in range(10 ** 3, 3, -1):
    if func('5' + '2' * n) == 64:
        print(n)
        break




print(int('1010000', 2))




