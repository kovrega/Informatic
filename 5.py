"""
1. Внимательно прочитать по какому числу (начальному или двоичному) проводится проверка на делимость
2. Нужно записывать все ответы которые возвращает функция и ТОЛЬКО ПОТОМ выбирать минимальное
3. Внимательно прочитать, что нужно вывести в ответ: R или some_func(R)
"""
from bisect import insort_right


# def some_func(N) -> int:
#     BN = bin(N)[2:]
#
#     if int(N) % 3 == 0:
#         BN += BN[-3:]
#     else:
#         BN += bin((int(N) % 3) * 3)[2:]
#
#     res = int(BN, 2)
#     return res
#
# l = []
# for R in range(1, 100):
#     if some_func(R) > 151:
#         l.append(some_func(R))               # -> Такой подход учитывает случай, когда минимальное число может быть не первым
#         # print(some_func(R))                  -> А такой подход выведет ПЕРВОЕ число, А НЕ МИНИМАЛНОЕ
#         # break
# print(min(l))




# sdo_1580



# def f(N: str):
#     s1 = int(N[0]) + int(N[1])
#     s2 = int(N[1]) + int(N[2])
#     s3 = int(N[2]) + int(N[3])
#     s = sorted([s1, s2, s3])[1:]
#
#     r = ''.join(map(str, s))
#     return r
#
#
# for i in range(9999, 999, -1):
#     if f(str(i)) == '1315':
#         print(i)
#         break
# print(f('1982'))




def cc(x, c):
    r = ''
    while x > 0:
        r = str(x % c) + r
        x //= c

    return r



# def f(N):
#     n3 = cc(N, 3) + str(N % 3)
#     R = int(n3, 3)
#     return R
#
#
# l = []
# for i in range(1, 1000000):
#     if len(RR := str(f(i))) == 4:
#         l.append(RR)
#
# print(min(l))






# def f(N : str):
#     s1 = int(N[0]) * int(N[1])
#     s2 = int(N[1]) * int(N[2])
#     s = sorted([s1, s2])
#     r = ''.join(map(str, s))
#     return r
# # print(f('631'))
#
# for i in range(100, 999 + 1):
#     if f(str(i)) == '621':
#         print(i)
#         break








# def f(N: str):
#     s1 = int(N[0]) + int(N[1])
#     s2 = int(N[1]) + int(N[2])
#     s = sorted([s1, s2], reverse=True)
#
#     r = ''.join(map(str, s))
#     return r
#
# # print(f('348'))
# for i in range(100, 999 + 1):
#     if f(str(i)) == '157':
#         print(i)
#         break







# def f(a : str, b : str):
#     s1 = int(a[2]) + int(b[2])
#     s2 = int(a[1]) + int(b[1])
#     s3 = int(a[0]) + int(b[0])
#
#     s = sorted([s1, s2, s3], reverse=True)
#     r  = ''.join(map(str, s))
#     return r
#
# # print(f('835', '196'))
# for i in range(100, 999 + 1):
#     if f('857', str(i)) == '16148':
#         print(i)
#         break





# def f(N):
#     n2 = bin(N)[2:]
#     n2 += n2[-2]
#     n2 += n2[1]
#     r = int(n2, 2)
#     return r
#
# # print(f(13))
#
#
# for i in range(2, 10000):
#     if f(i) > 180:
#         print(i)
#         break





# def f(N):
#     n2 = bin(N)[2:]
#     s = sum(int(x) for x in n2)
#     n2 += str(s % 2)
#     s = sum(int(x) for x in n2)
#     n2 += str(s % 2)
#
#     r = int(n2, 2)
#     if r > 83:
#         return r
#     return None
#
#
# l = []
# for i in range(2, 100000):
#     if (r :=f(i)):
#         l.append(r)
# print(min(l))



