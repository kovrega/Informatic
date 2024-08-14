
# def move(n: int, lim: int, s: int, t: int) -> int:
#     """
#     :param n: Номер хода
#     :param lim: Лимит ходов
#     :param s: Кол-во камней в куче
#     :param t: История сделанных ходов
#     :return: Игрок/Соперник/Проигрыш обоих
#     """
#
#     """
#     1 2 3
#     П В П
#     """
#
#     # 1 - игрок ходит сейчас
#     # 2 - игрок ходит следующим
#     player = 2 - n % 2
#     rival = 3 - player
#
#     if s >= 50: return rival
#     if n > lim: return 0
#
#     # Список возможных ходов
#     pos = [(s + 1, 0), (s + 2, 1), (s * 2, 2)]
#
#
#     # Условие того, что игрок не может сделать предыдущий ход соперника
#     if len(t) > 0: del pos[t[-1]]
#
#
#     # Все возможные исходы
#     res = [move(n + 1, lim, x[0], t + [x[1]]) for x in pos]
#
#
#     if any([x == player for x in res]): return player
#     if all([x == rival for x in res]): return rival
#
#     return 0
#
#
# print('№_19:', *[s for s in range(1, 50) if move(1, 2, s, []) == 2])
# print('№_20:', *[s for s in range(1, 50) if move(1, 1, s, []) == 0 and move(1, 3, s, []) == 1])
# print('№_21:', *[s for s in range(1, 50) if move(1, 2, s, []) == 0 and move(1, 4, s, []) == 2])



def move(n: int, lim: int, s: tuple, t: int) -> int:
    """
    :param n: Номер хода
    :param lim: Лимит ходов
    :param s: Кол-во камней в куче
    :param t: История сделанных ходов
    :return: Игрок/Соперник/Проигрыш обоих
    """

    """
    1 2 3
    П В П
    """

    # 1 - игрок ходит сейчас
    # 2 - игрок ходит следующим
    player = 2 - n % 2
    rival = 3 - player

    if sum(s) >= 77: return rival
    if n > lim: return 0

    # Список возможных ходов
    pos = [(s[0] + 1, s[1], 0), (s[0] * 2, s[1], 1), (s[0], s[1] + 1, 2), (s[0], s[1] * 2, 3)]


    # Условие того, что игрок не может сделать предыдущий ход соперника
    # if len(t) > 0: del pos[t[-1]]


    # Все возможные исходы
    res = [move(n + 1, lim, (x[0], x[1]), t + [x[-1]]) for x in pos]

    ps = [x == player for x in res]
    rs = [x == rival for x in res]
    if any(ps): return player
    if any(rs): return rival #  №_19
    # if all(rs): return rival # №_20-21

    return 0


print('№_19:', *[ move(1, 2, (s, 7), []) for s in range(18, 70)])
print('№_20:', *[s for s in range(1, 70) if move(1, 1, (s, 7), []) == 0 and move(1, 3, (s, 7), []) == 1])
print('№_21:', *[s for s in range(1, 70) if move(1, 2, (s, 7), []) == 0 and move(1, 4, (s, 7), []) == 2])







# print("x", "y", "z", "w")
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if (((x <= y) <= z ) or (not (w))) == 0:
#                     print(x, y, z, w)
#
#



#
# def F(N):
#     b = str(bin(N))[2:]
#
#     if b.count('1') % 2 == 0:
#         b += '0'
#         b = '10' + b[3:]
#     else:
#         b += '1'
#         b = '11' + b[3:]
#
#     R = int(b, 2)
#     return  R
#
# for N in range(1000000, 0, -1):
#     if F(N) < 35:
#         print(N)
#         break


#
# s = '7' * 108
#
# while '33333' in s or '777' in s:
#     if '33333' in s:
#         s = s.replace('33333', '7',1)
#     else:
#         s = s.replace('777', '3', 1)
#
# print(s)


# def F(x, y):
#     if x % y == 0:
#         return 1
#     else:
#         return 0
#
#
# for A in range(1, 100):
#     for x in range(0, 10000):
#         if ((F(x, 2) <= (not (F(x, 5)))) or (x + A >= 70)) == 1:
#             print(A)
#             break
#         else:
#             break







#
#
# d = [1, 4]
# for i in range(0, 2024):
#     d.append(d[i - 1] * 2 * i)
#
# m = [1, 4]
# for i in range(0, 2023):
#     m.append(m[i - 1] * 2 * m)
#
# b = [1,4]
# for i in range(0, 2022):
#     b.append(b[i - 1] * 2 * i)
#
#
#
#
#
# print((d[-1] - 4*m[-1])/b[-1])




# def moves(h):
#   a, b = h
#   return (a+1, b), (a, b+1), (a + 2, b), (a, b + 2), (a * 2, b), (a, b * 2)


# def game(h, p, m):
#     if h == 2 and p >= 50:
#         return True
#     elif h > 2:
#         return False
#     elif h == 1 and p >= 50:
#         return False
#
#     if (h + 1) % 2 == 1:
#         return game(h + 1, p + 1, 1) and game(h + 1, p + 2, 2) and game(h + 1, p*2, 3)
#     else:
#         if m == 1:
#             return game(h + 1, p + 2, 2) or game(h + 1, p*2, 3)
#         elif m == 2:
#             return game(h + 1, p + 1, 1) or game(h + 1, p * 2, 3)
#         elif m == 3:
#             return game(h + 1, p + 1, 1) or game(h + 1, p + 2, 2)
#         else:
#             return game(h + 1, p + 1, 1) or game(h + 1, p + 2, 2) or game(h + 1, p*2, 3)
#
#
# for S in range(1, 50):
#     if game(0, S, 0):
#         print(S)
#         break

"""
h 1 2 3 4
    П В П
"""

#
#
#
#
# #
# # def game(n, lim, s):
# #     pl = 2 - n % 2
# #     riv = 3 - pl
#
#
#
# def g(x, h):
#     if (h == 2 or h == 4) and x >= 65:
#         return True
#     elif (h == 1 or h == 3) and x >= 65:
#         return False
#     elif h > 4:
#         return False
#
#     pos = (x + 1, x + 2, x * 3)
#
#     if (h + 1) % 2 == 0:
#         return any([g(p, h + 1) for p in pos])
#     else:
#         return all([g(p, h + 1) for p in pos])
#
#
# def g1(x , h):
#     if h == 2 and x >= 65:
#         return True
#     if h == 2 and x < 65:
#         return False
#     if h > 2:
#         return False
#     if h == 1 and x >= 65:
#         return False
#
#     pos = (x + 1, x + 2, x * 3)
#
#     if (h + 1) % 2 == 0:
#         return any([g(p, h + 1) for p in pos])
#     else:
#         return all([g(p, h + 1) for p in pos])
#
#
# for s in range(1, 65):
#     if g(s, 0) and not (g1(s, 0)):
#         print(s)
#         break
