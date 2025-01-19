# # 2
# print("x", 'y', "w", "z")
# for x in range(0,2):
#     for y in range(0,2):
#         for w in range(0,2):
#             for z in range(0,2):
#                 if not (
#                         (x == (y <= z)) and (y == (not(z <= w)))
#                     ):
#                     print(x, y, w, z)

# """
# x y w z
# 1 0 0 0
# 1 0 1 0
# 1 0 1 1
# 1 1 0 1
#
# x y w z
# 0 0 0 0
# 0 0 0 1
# 0 0 1 0
# 0 0 1 1
# 0 1 0 0
# 0 1 0 1
# 0 1 1 0
# 0 1 1 1 *
# 1 0 0 1
# 1 1 0 0
# 1 1 1 0 *
# 1 1 1 1
# """



# 5
# def F(N : int) -> bool:
#     N2 = bin(N)[2:]
#     c0 = bin(N2.count('0'))[2:]
#     c1 = bin(N2.count('1'))[2:]
#
#     n2 = c1 + c0
#
#     R = int(n2, 2)
#     if R == 214:
#         return True
#     return False
#
# for i in range(1_00 ,1_000_000_000):
#     if F(i):
#         print(i)
#         break




# 6
# Пример
# from turtle import *
# k = 10
# left(90)
# pendown()
# # tracer(0)
#
# begin_fill()
# right(90)
# for i in range(3):
#     right(45)
#     forward(12 * k)
#     right(45)
#
# right(315)
# forward(12 * k)
# for j in range(2):
#     right(90)
#     forward(12 * k)
#
# end_fill()
#
# c = 0
# canvas = getcanvas()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         if canvas.find_overlapping(x*k,y*k, x*k,y*k) == (5,):
#             c += 1
# print(c)
# done()



# 6
# from turtle import  *
#
# k = 100
# # left(90)
# speed(0)
# # tracer(0)
#
# pendown()
# begin_fill()
# for i in range(2):
#     forward(8 * k)
#     right(90)
#     forward(8 * k)
#     right(90)
# end_fill()
# penup()
#
#
#
#
# canvas = getcanvas()
# c = 0
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
#             c += 1
#
# print(c)
# done()



# 7
# PyDev console: starting.
# Python 3.13.1
# K = 150 * 150
# K4 = K * 0.6
# i = (6 * (2 ** 23)) / K4
# K_ = 300 * 300
# (12 * (2 ** 23)) / (K_ * i)
# 0.3


# 8
# V_do = 26 + (26 * 26) + (26 * 26 * 26) + (26 * 26 * 26 * 26) + (26 * 26 * 26 * 26 * 26)
# sl  = {0 : 'A',
#        1 : 'B',
#        2 : 'C',
#        3 : 'D',
#        4 : 'E',
#        5 : 'F'}
#
# s = "FEDABC"
# k = int('543012', 26)
# print(k + 1 + V_do)


# 9
# from collections import Counter
#
# with open("Материалы/09.csv", encoding='UTF-8') as f:
#     l = f.readlines()
#
# k = []
# for i in range(len(l)):
#     k.append(list(map(int, l[i].strip().split(';'))))
#
# column_counts = [Counter() for _ in range(6)]
#
# # print(k[:10])
# for row in k:
#     for col in range(6):
#         column_counts[col].update([row[col]])
#
# def check(stroka : list) -> int:
#     """
#     :return: кол-во интересных ячеек в строке
#     """
#
#     inter_cnt = []
#
#     sr_ar = sum(stroka) / 6
#     for i in range(6):
#         el = stroka[i]
#         if stroka.count(el) < 2:
#             if el > sr_ar:
#                 # c = 0
#                 # for st in range(len(k)): # -> 4783
#                 #     if k[st][i] == el:
#                 #         c += 1
#                 #
#                 #     if c >= 330:
#                 #         inter_cnt.append(el)
#                 #
#                 if column_counts[i][el] > 330: # -> 4175
#                 # if column_counts[i][el] >= 2: # ->
#                     inter_cnt.append(el)
#
#
#     if len(inter_cnt) == 1:
#         return True
#     return False
#
# cc = 0
# for ind_stroka in range(len(k)):
#     if check(k[ind_stroka]):
#         cc += 1
# print(cc)


# 10
# PyDev console:
# VSE = 2423
# целиком = 196
# Заголовок = 129
# Ответ = VSE - целиком
# Ответ
# 2227
# Ответ - Заголовок
# 2098


# 11 (386)
# from math import log2, ceil
# # PyDev console:
# код_партии = 19 * (i := 5)
# k = 2 # кол-во изделий
# x = ceil(log2(k + 1)) # кол-во бит под хранение k
# while 20 * (2 ** 10) >= k * (ceil((x + код_партии)/8) + 40):
#     k += 1
#     x = ceil(log2(k + 1))
# print(k - 1) # -> 386





# 12
from random import choice

def F(x : str) -> str:
    while '111' in x or '22' in x:
        x = x.replace('111', '2', 1)
        x = x.replace('222', '1', 1)
        x = x.replace('221', '1', 1)
        x = x.replace('122', '1', 1)
        x = x.replace('22', '2', 1)
    return x

# Генерировать различные варианты, которые не изменялись бы F. Динамически варианты сохранять.
# Всего вариантов на которые действует F конечно. Всего нужных вариантов тоже конечно, т.к. всего 9 двоек
"""
112
121
211
212
2112
2
1
1121
1211
"""
c = 0
for i in range(5000):
    s = ''.join(choice('12') for _ in range(i))
    # s = '1' * i + '2' * i # -> 0


    res = F(''.join(s))
    if res.count('2') == 9:
        c += 1

print(c)








# 13
# from ipaddress import  *
# 
# node_1 = ip_address('157.220.185.237')
# node_2 = ip_address('157.220.184.230')
# # 10011101.11011100.10111001.11101101
# # 10011101.11011100.10111000.11100110
# 
# # for mask in range(33):
# #     net_1 = ip_network(f'157.220.185.237/{mask}', 0)
# #     net_2 = ip_network(f'157.220.184.230/{mask}', 0)
# #     if net_1 == net_2:
# #         print(net_1.netmask)
# 
# mask = ip_address('255.255.254.0')
# 
# # print(ip_network(f'157.220.185.237/{mask}', False)) # -> 157.220.184.0/22
# 
# ip_nodes = list(add for add in ip_network(f'157.220.185.237/{mask}', False))
# c = 0
# for add in ip_nodes:
#     if f'{add:b}'.count('1') == 15:
#         c += 1
# 
# print(c)





# 14
# def f(x: int, c: int = 7) -> str:
#     res = ''
#     while x > 0:
#         res = str(x % c) + res
#         x //= c
#
#     return res
#
#
#
# for x in range(1, 100_000_000): # -> 29_059_314
#     s = 4 * (7 ** 24) + 6 * (7 ** 13) + 5 * (49 ** 4) + 2 * (343 ** 2) + 10 - x
#     s7 = f(s)
#     if s7.count('6') > s7.count('0'):
#         print(x)
#         break



# 15
# def f(x, a1, a2):
#     P = 153697 <= x <= 780411
#     Q = 275071 <= x <= 904082
#     R = 722050 <= x <= 984086
#     A = a1 <= x <= a2
#     return  (not A) <= ((P == Q) <= (R == Q))
#
#
# res = []
# ctrl_val = [y for x in (153697, 780411, 275071, 904082, 722050, 984086) for y in (x, x - 0.1, x + 0.1)]
#
# for a1 in ctrl_val:
#     for a2 in ctrl_val:
#         if a2 >= a1 and all(f(x, a1, a2) for x in ctrl_val):
#             res.append(a2 - a1)
#
# print(min(res))




# 16
# F = [0, 3, 5]
# for n in range(4, 100_000_000): # -> 18874368
#
#     if n % 2 == 0:
#         F.append(F[n//2 - 1] + 3)
#     elif n % 2 != 0 and n % 3 == 0:
#         F.append(F[n//3 - 1] + 2)
#     elif n % 2 != 0 and n % 3 != 0:
#         F.append(0)
#
#     if F[n - 1] == 70:
#         print(n)
#         break



# 17
# with open('Материалы/17.txt') as f:
#     s = list(map(int, f.read().strip().split()))
#
#
# def condition_1():
#     r = []
#     ost_min_t = min_t % 3
#     for el in (t1, t2, t3):
#         if el % 3 == ost_min_t:
#             r += [1]
#
#     if sum(r) == 1: # Если не считать деление минимального на самого себя
#     # if sum(r) == 2:
#         return True
#     return False
#
#
# def condition_2():
#     r = []
#     ost_max_t = max_t % 7
#     for el in (t1, t2, t3):
#         if el % 7 == ost_max_t:
#             r += [1]
#
#     if sum(r) == 2: # Если не считать деление минимального на самого себя
#     # if sum(r) == 3:
#         return True
#     return False
#
#
# cnt = 0
# t_sum = []
# for t in range(2, len(s), 3):
#     t1, t2, t3 = s[t], s[t - 1], s[t - 2]
#     min_t = min(t1, t2, t3)
#     max_t = max(t1, t2, t3)
#     if condition_1():
#         if condition_2():
#             cnt += 1
#             t_sum.append(sum((t1, t2, t3)))
#
# print(cnt, max(t_sum)) # -> 36 254224






# 23
# def f(x, y) -> int:
#     if x < y:
#         return 0
#     if x == y:
#         return 1
#     return f(x - 3, y) + f(x // 2 if x % 2 == 0 else x - 5, y)
#
#
# print(f(36, 3) - f(36, 12) * f(12, 3))




# 25
# from fnmatch import fnmatch
# # from re import search
#
# def check_div(n):
#     if int(n ** 0.5) ** 2 == n:
#         for i in range(2, int(x ** 0.5)):
#             if n % i == 0:
#                 return False
#         return True
#
#     return False
#
# res = []
# # reg = r'\d{1}\d*42\d*81'
# for x in range(10 ** 8, 2 * (10 ** 8) + 1):
#     # if search(reg, str(x)):
#     if fnmatch(str(x), '?*42*81'):
#         if check_div(x):
#             res.append(x)
#
# print(res)  # -> [114297481, 141824281, 142587481, 149842081]








