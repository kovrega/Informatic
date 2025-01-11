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
# for i in range(500_000_000 ,1_00, -1):
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
# k = 10
# left(90)
# # speed(0)
#
# pendown()
# begin_fill()
# for i in range(2):
#     forward(15 * k)
#     right(90)
#     forward(8 * k)
#     right(90)
# end_fill()
# penup()
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
#     sr_ar = sum(stroka) // 6
#     for i in range(6):
#         el = stroka[i]
#         if stroka.count(el) < 2:
#             if el > sr_ar:
#                 c = 0
#                 # for st in range(len(k)):
#                 #     if k[st][i] == el:
#                 #         c += 1
#                 #
#                 #     if c >= 330:
#                 #         inter_cnt.append(el)
#                 #         break
#                 if column_counts[i][el] >= 330:
#                     inter_cnt.append(el)
#                     break
#
#     if len(inter_cnt) > 0:
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


# 11

# PyDev console:
# код_партии = 26 * (i := 5)
#
# кол_во_изделий = 2
# while 20 * (2 ** 13) >= кол_во_изделий * (40 * 8 + код_партии) + sum(j for j in range(1, кол_во_изделий + 1)):
#     кол_во_изделий += 1
# print(кол_во_изделий - 1)





# 12
# from random import choice
#
# def F(x : str) -> str:
#     while '111' in x or '22' in x:
#         x = x.replace('111', '2', 1)
#         x = x.replace('222', '1', 1)
#         x = x.replace('221', '1', 1)
#         x = x.replace('122', '1', 1)
#         x = x.replace('22', '2', 1)
#     return x
#
# c = 0
# for i in range(5000):
#     s = ''.join(choice('12') for _ in range(i))
#     # s = '1' * i + '2' * i # -> 0
#
#
#     res = F(''.join(s))
#     if res.count('2') == 9:
#         c += 1
#
# print(c)








# 13
from ipaddress import  *
from ipaddress import IPv4Address, ip_address, ip_network


print(f"{184:b}")
print(f"{185:b}")
print(int('11111', 2))
node = ip_address('157.220.185.237')
mask = ip_address('255.255.31.0')

print(f'{int(node):b}')
print(f'{int(mask):b}')
# node = IPv4Address('157.220.185.237')
# mask = IPv4Network('255.255.31.0', False )
# print(f'Адрес сети: {ip_network(f"{node}/{mask}", False) }')
# Находим сеть
# Находим сеть

