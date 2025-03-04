from functools import lru_cache


# 8
# def f(n, r):
#     if n == r: return 1
#     if n == 54: return 0
#     if n > r:   return 0
#     return f(n + 1, r) + f(int(f'{n}2'), r) + f(n * 3, r) + f(n * 4, r)
#
#
# print(f(1, 87))
# 9
# def F(n, c = 0):
#     # if c == 4:
#     if c == 3:
#     # if c == 2:
#     # if c == 1:
#         return {n}
#     if c > 4:
#         return {None}
#     else:
#         return F(n + 2, c + 1) | F(n * 3, c + 1)
#
# print((len(sorted(F(2)))))



# 10
# def F(n):
#     if n == 98:
#         return 1
#     if n > 98:
#         return 0
#     if n in (7, 23, 76, 86):
#         return 0
#     else:
#         return F(n + 1) + F(n * 2) + F(n ** 2)
#
#
# print(F(3))




# def f(n, r, p = 0, h = 0):
#     """
#
#     :param n: текущее число
#     :param r: результат
#     :param p: предыдущий ход
#     :param h: текущий ход
#     :return:
#     """
#     if n == r and p == 1:  return 1
#     if n > r:   return 0
#     return f(n + 1, r, h, 1) + f(n * 2, r, h, 2)
#
#
# print(f(5, 32))




# @lru_cache(None)
# def f(n, r, c = 0):
#     if n == r and c <= 10:  return [c]
#     if n > r or c > 10: return [100000000]
#     return f(n + 1, r, c + 1) + f(n + 5, r, c + 1) + f(n * 3, r , c + 1)
#
# l = f(1, 111)
# print(l[:100])
# print(sorted(l))
# print(l.count(min(l)))








# самостоятельная работа?




# def f(n, c = 0):
#     if c == 4: return {n}
#     if c > 4:   return {None}
#     else:
#         return f(n * 5, c + 1) | f(n / 3, c + 1)


# def f(n, r):
#     if n == r: return 1
#     if n > r:   return 0
#
#     else:
#         return f(n * 5, r) + f(n / 3, r)
#
# print(f(5, 11) * f(11, 26))



# print(len(f(81)))
# print(f(5, 11) * f(11, 26))
# print(f(5, 12) * f(12, 40))










