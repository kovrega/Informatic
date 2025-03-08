


# 2
# print('x y z w')
# for x in range(0,2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if (
#                     (w == (not(z == y))) and (z == (y <= x))
#                     ):
#                     print(x, y, z, w)
#
#
# '''
# x y z w
# 0 0 1 1
# 0 1 0 1
# 1 0 1 1
# 1 1 1 0
# '''





# 5

# def f(N):
#     N2 = bin(N)[2:]
#     if N2.count('0') >  N2.count('1'):
#         N2 = N2.replace('0', '1', 1)
#     else:
#         N2 = N2[::-1].replace('1', '0', 1)[::-1]
#
#     r_ = int(N2, 2)
#
#     R = abs(N - r_)
#
#     return R
# # print(f(17)) # -> 8
# # print(f(28)) # -> 4
#
#
#
#
#
# res = (0, 0)
# for N in range(1, 10**9 + 1):
#     if (rr := f(N)) > res[-1]:
#         res = (N, rr)
#
# print(res)
# # (536870912, 268435456)




# 7

# I1 = 1920 * 1080 * 24
# I_ = 0.2 * I1
# V = 750 * (2 ** 23) / 600
# Opis = V -I_
# Opis * (2 ** 13)
# 4362076160.0
# Opis / (2 ** 13)
# 65.0



# 8
# pass



# # 9   218
# import csv
# with open('9 (1).csv') as f:
#     l = [tuple(map(int, s)) for s in csv.reader(f, delimiter=';')]
#
#
# cnt = 0
# for st in l:
#     if sum(x if x % 2 == 0 else -x for x in st) > 0:
#         sr = sum(st) / 8
#         nw_st = [x for x in st if x > sr]
#
#         if sum(1 if x % 2 == 0 else 0 for x in nw_st) < sum(1 if x % 2 != 0 else 0 for x in nw_st):
#             cnt += 1
#
# print(cnt)






# 12

# def f(s : str):
#
#     while '111' in s or '222' in s:
#         s = s.replace('111', '22', 1)
#         s = s.replace('222', '11', 1)
#         s = s.replace('11', '2', 1)
#         s = s.replace('22', '1', 1)
#
#     return s
#
#
# r = set()
#
#
# for i in range(1, 2000):
#     r.add(f('2' * i))
#
# print(len(r))



# 13
# from ipaddress import *
#
# r = []
# for mask in  range(31, 1, -1):
#     net = ip_network(f'130.0.5.80/{mask}', 0)
#     c_net =  f'{net.network_address:b}'.count('1')
#     cnt = 0
#     for ip in net:
#         if f'{ip:b}'.count('1') == c_net:
#             cnt += 1
#
#     r.append(cnt)
#
# print(sorted(r))


# 14
# # p >= 12
#
#
# for p in range(12, 30):
#
#     for x in '0123456789ABCDEFGHIGKLMNOPQRSTVWXYZ'[:p]:
#         for y in '0123456789ABCDEFGHIGKLMNOPQRSTVWXYZ'[:p]:
#             for z in '123456789ABCDEFGHIGKLMNOPQRSTVWXYZ'[:p - 1]:
#                 if  int(f'{z}{x}', p) + int(f'{x}{y}', p) == int(f'{z}{y}B', p):
#                     print(int(f'{x}{y}{z}', p), p) #-> 1585 12
#
#



# 15
# import math
#
#
# def f(x, a1, a2):
#     A = a1 <= x <= a2
#     P = 167242 <= x <= 514210
#     Q = 403149 <= x <= 718530
#     R = 522897 <= x <= 816282
#
#     return Q <= ((P or R) <= A)
#
#
# ctrl_val = [el for x in [167242, 514210, 403149, 718530, 522897, 816282] for el in (x, x + 0.1, x - 0.1)]
#
#
# res = []
# for a1 in ctrl_val:
#     for a2 in ctrl_val:
#         if a2 >= a1 and all(f(x, a1, a2) for x in ctrl_val):
#             res.append(math.floor(a2) - math.ceil(a1) + 1)
#
#
# print((min(res)))  # -> 315382






# 16

# F = [0]
#
# for n in range(1, 6 * (10 ** 7) + 1):
#     if  n % 2 == 0:
#         F.append(F[n // 10] + n % 10)
#     else:
#         F.append(F[n // 10])
#
# print(F[:15])
#
# c = 0
# for n in range(10 ** 7,  6 * (10 ** 7) + 1):
#     if F[n] == 0:
#         c += 1
#
# print(c) #->839808










# with open('17.txt') as f:
#     l = list(int(x) for x in f.read().split())
#
# max_el = max(l)
# min_el = min(l)
#
# r = []
# for i in range(2, len(l)):
#     s = (l[i - 2], l[i - 1], l[i])
#     if sum(1 if len(str(x)) == 4 else 0 for x in s) >= 2:
#         if any(1 if x % 10 == max_el % 10 else 0 for x in s):
#             if sum(1 if x % 10 == min_el % 10 else 0  for x in s) == 0:
#                 r.append(sum(s))
#
#
# print(len(r), max(r)) # -> 46 113153









# 19


# def movs(s):
#     m = set()
#     m.add(s)
#     m.add(1)
#     for k in range(2, int(s **0.5) ** 2 + 1):
#         if s % k == 0:
#             m.add(k)
#             m.add(s // k)
#     return m
#
#
#
# def f(s, c):
#     if s > 111:   return c % 2 == 0
#     if c <= 0:  return 0
#
#     moves = [f(s + h, c - 1) for h in movs(s)]
#
#     return any(moves) if c % 2 != 0 else all(moves)
#
#
# print(min([s for s in range(1, 112) if  f(s, 2)]))
# print(   *[s for s in range(1, 112) if not f(s, 1) and f(s, 3)])
# print(min([s for s in range(1, 112) if not f(s, 2) and f(s, 4)]))











# 21

# def f(x):
#     if x == 36: return 1
#     if x > 36:  return 0
#     if '2' in str(x): return 0
#     else:
#         return f(x + 1) + f(2 * x)
#
#
# print(f(3)) 13





# 22
from fnmatch import fnmatch

# import re
# reg = r'D\d+\[+-]{1}'
re = '4?28*8*3'
for x in range(1, 10**9 + 1):
    if fnmatch(str(x), re):
    # if re.find(reg)
        if x % 9111 == 0:
            print(x)














