


# def f(kol_p, kol_h, h0, h1, h2):
#     '''
#     :param kol_p: Кол-во подарков
#     :param kol_h: Какой ход по счету
#     :param h0: Текущий ход
#     :param h1: Ход противник
#     :param h2: Предыдущий
#     :return:
#     '''
#
#     """
#     '+2' - 0
#     '+5' - 1
#     '+12' - 2
#     '*2' - 3
#     """
#
#
#     if kol_p >= 121:    return kol_h % 2 == 0
#     if kol_h == 0:      return 0
#
#
#     moves = [
#         f(kol_p, kol_h - 1, i, h0, h1) for i in range(4) if i != h2
#     ]
#
#     return any(moves) if (kol_h - 1) % 2 == 0 else all(moves)
#
#
#
#
#
# print('19 = ', [s for s in range(1, 120  + 1) if f(s, 1, 9, 9, 9)])
# print('20 = ', [s for s in range(1, 120  + 1) if (f(s, 1, 9, 9, 9) and not f(s, 1, 9, 9, 9))])
# print('21 = ', [s for s in range(1, 120  + 1) if f(s, 1, 9, 9, 9) and not f(s, 1, 9, 9, 9)])












# Задачи для решения на уроке

# Ex 1

def strategy(s: int,  n: int):
    # pl = 1 - n % 2 # текущий игрок: 1 - победитель | 0 - соперник

    if s >= 37 :    return n % 2 == 0
    if n == 0:     return 0

    moves = [s + 1, s + 2, s * 2]
    cases = [strategy(m, n - 1) for m in moves]
    return any(cases) if n % 2 != 0 else all(cases)



# print(*[s for s in range(1, 68) if strategy(s, 1)])
# print(*[s for s in range(1, 68) if not strategy(s, 1) and strategy(s, 3)])
print(*[s for s in range(1, 38) if  not strategy(s, 1) and strategy(s, 3)])









