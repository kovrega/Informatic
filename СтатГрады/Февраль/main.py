# 2
# print('x y z w')
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if not (
#                         (w <= (not(z == y))) and (z or (y <= x))
#                 ):
#                     print(x, y, z, w)



# 5  -> 3323607
# def perevod(N, c = 3):
#     r = ''
#     while N > 0:
#         r = str(N % c) + r
#         N //= c
#     return r
#
# def F(N):
#     N3 = perevod(N)
#     r = ''
#     for el in N3:
#         if el == '0':
#             r += '2'
#         elif el == '2':
#             r += '0'
#         else:
#             r += el
#
#     R = abs(int(r, 3) - N)
#
#     if R == 1_864_246:
#         return True
#     return False
#
# for N in range(1, 100000000):
#     if F(N):
#         print(N)
#         break









# 7
# from turtle import *
# # k = 15
# # left(90)
# # tracer(1)
# #
# # pendown()
# # begin_fill()
# # for i in range(2):
# #     forward(19 * k)
# #     right(90)
# #     forward(3 * k)
# #     right(90)
# # end_fill()
# # penup()
# #
# # canvas1 = getcanvas()
# # c1 = 0
# # for x in range(-20, 20):
# #     for y in range(-20, 20):
# #         if canvas1.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
# #             c1 += 1
# # print(c1) #36
# # done()
#
#
# k = 15
# left(90)
# tracer(1)
# pendown()
# begin_fill()
#
# for i in range(2):
#     forward(5 * k)
#     right(90)
#     forward(11 * k)
#     right(90)
# end_fill()
# penup()
#
# canvas2 = getcanvas()
# c2 = 0
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         if canvas2.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
#             c2 += 1
# print(c2) # 40
#
# done()
# res = 40 : 40 > 36



# 7
# PyDev console: starting.
# Python 3.13.1
# n = 2
# v = 32000
# i = 16
# V_posle = 25 * (2 ** 23) * 60
# V_do = n * v * i * ( (1.5 * (2 ** 23)) / (1.5 * (2 ** 13)) ) * 60
# otv = 1 - V_posle / V_do
# otv = 1 - (V_posle / V_do)
# (1.5 * (2 ** 23)) / (1.5 * (2 ** 13))
# (1.5 * (2 ** 23)) / (1.5 * (2 ** 13))
# 1024.0
# otv
# 0.8



# 8 -> 20867280
# def F(N):
#     dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D'}
#     r = set()
#     r.add("alfa")
#     while N > 0 and (len(r) - 1) < 9:
#         d = N % 14
#         # r.add(str(d) if d < 10 else dic[d])
#         r.add(str(d) if d < 10 else 'alfa')
#         N //= 14
#     if len(r) == 8:
#         return True
#     return False
#
#
# c = 0
# for n in range(1, 738_000_000 + 1):
#     if F(n):
#         c += 1
#
# print(c)




# 9
# with open('9.csv') as f:
#     l = list(list(map(int, _.split(';'))) for _ in f.readlines())
#
# def F(st : list):
#     if st.count(ms := max(st)) == 1:
#         if ms in st[:4]:
#             if (m1 := (sum(st[:4]) / 4)) < (m2 := (sum(st[4:]) / 4)):
#                 return True
#
#     return False
#
# c = 0
# for st in l:
#     if F(st):
#         c += 1
#
# print(c)


# 10
# История 1: 4
# История 2: 19
# История 3: 9

# 11 Гроб с прошлого статграда

# 12 Гроб с прошлого статграда

# def F(s : str):
#     while '111' in s or '22' in s:
#         s = s.replace('111', '2', 1)
#         s = s.replace('222', '1', 1)
#         s = s.replace('221', '1', 1)
#         s = s.replace('112', '1', 1)
#         s = s.replace('22', '2', 1)






# 13 -> 35
# from ipaddress import ip_address, ip_network
#
# node = ip_address('68.30.20.77')
# netw = None
# for mask in range(33):
#     net = ip_network(f'{node}/{mask}', 0)
#     if f'{net.network_address:b}'[2:].count('1') == f'{net.netmask:b}'.count('0'):
#         netw = net
#         print(net)
#
#     # print(f'{net.network_address} : {net.netmask}')
#     # print(f'{node:b}')
#
# c = 0
# for ip_add in netw:
#     if f'{ip_add:b}'[2:].count('1') == 10:
#         c += 1
#
# print(c)







# 14
def perevod(N : str, c = 14) -> int:
    dic = {chr(i + ord('A')): i + 10 for i in range(26)}
    r = 0
    N = N[::-1]
    for i in range(len(N)):
        if N[i].isdigit():
            r += int(N[i]) * (c ** i)
        else:
            r += dic[N[i]] * (c ** i)

    return r


    # dic = {chr(i + ord('A')) : i + 1 for i in range(26)}
    # while len(N) > 0:
    #     d = N % 14
    #     r += str(d) if d < 10 else dic[d]
    #     N //= c
    #
    # return r[::-1]




# for c in range(9, 50):
#     for x in '123456789ABCDEFGHIGKLMNOPQRSTVWXYZ'[:c - 1]:
#         for y in '123456789ABCDEFGHIGKLMNOPQRSTVWXYZ'[:c - 1]:
#             for w in '123456789ABCDEFGHIGKLMNOPQRSTVWXYZ'[:c - 1]:
#                 for z in '0123456789ABCDEFGHIGKLMNOPQRSTVWXYZ'[:c - 1]:
#                     r1 = perevod(f'{y}27{x}', c)
#                     r2 = perevod(f'{w}{y}86', c)
#                     r3 = perevod(f'{x}{x}{z}3{y}', c)
#                     # r1 = int(f'{y}27{x}', c)
#                     # r2 = int(f'{w}{y}86', c)
#                     # r3 = int(f'{x}{x}{z}3{y}', c)
#                     if r1 + r2 == r3:
#                         print(f"c {c}")
#                         print(perevod(f'{x}{y}{z}{w}', c))

# # 15 -> 546
# def f(x, A):
#     return  ((x & 5160 > 0) or (x & 3650 > 0) ) <= ( (x & 9545 == 0) <= (x & A > 0) )
#
#
# for A in range(0, 10000):
#     if all(f(x, A) for x in range(0, 1000)):
#         print(A)
#         break


# 16 -> 268435199

# F = [0]
# for n in range(1, 1_000_000_000):
#     if n % 4 < 2:
#         F.append(
#             F[n//4] + n % 4
#         )
#     elif n % 4 >= 2:
#         F.append(
#             F[n // 4] + n % 4 - 1
#         )
#
# i = 0
# while (F[i] != 27 or F[i + 1] != 20 ) and i + 1 < len(F):
#      i += 1
#
# print(i)


# 23
"""
495073
48507813
405707653
495007613
495568073
"""
from fnmatch import fnmatch
re = '4?5*07*3'
for x in range(1, 1_000_000_000):
    if fnmatch(str(x), re):
        if x % 9341 == 0:
            print(x)





