

# Задание 2  !!! Можно проверить обновив страничку
# def count_divisors(x):
#     d = set()
#
#     for i in range(1, x):
#         if len(d) > 6:
#             return False
#         if x % i == 0:
#             if i % 2 == 0:
#                 d.add(i)
#             elif int(x // i) % 2 == 0:
#                 d.add(int(x // i))
#
#     dd = list(d.copy())
#     dd.sort()
#
#     if len(dd) == 6:
#         return dd
#
#
# res = []
# for el in range(95632, 95701):
#     r = count_divisors(el)
#     if r:
#         res.append([el])
#         res.append(r)
#
# for id in range(len(res)):
#     print(*res[id])
#


# Задание 3
# def count_divisors(x):
#     ds = set()
#
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             ds.add(i)
#             ds.add(x // i)
#
#     return sorted(list(ds))
#
#
# r = []
# for el in range(84052, 84131):
# # for el in range(2, 49):
#     k = count_divisors(el)
#     r.append((len(k), k, el))
#
# r.sort(key=lambda x:(x[0], -x[-1]), reverse=True)
# print(r[0])



# Задание 4
# for i in range(0, 10**10 + 1, 5321):
#
#     i = str(i)
#     if i[:2] == '12':
#         ind = i.find('135')
#         if ind != -1:
#             if i[-1] == '9':
#                 # if int(i) % 5321 == 0:
#                 print(i, int(i) // 5321)

# from fnmatch import *
# for x in range(0, 10**10 + 1, 5321): # Перебераем все числа от 0 с шагом 273, будут полученны числа кратные 273
#     if fnmatch(str(x), '12*135*9'):# Проверяем полученное число соответствию заданию
#         print(x, x // 5321)



# Задание 5
# r = []
# for m in range(1, 50, 2):
#     for n in range(0, 50, 2):
#         x = (2 ** m) * (7 ** n)
#         if 100000000 <= x <= 300000000:
#             r.append((x ,m + n))
#
#
# r.sort(key=lambda x:x[0])
# for el in r:
#     print(*el)


# Задание 6
# def count_divisors(x):
#     min_d = 1
#     max_d = 1
#
#     i = 2
#     j = x - 1
#     while min_d == 1 and i < x:
#         if x % i == 0 and i != 1:
#             min_d = i
#         else:
#             i += 1
#
#     while max_d == 1 and j > 1:
#         if x % j == 0 and j != x - 1:
#             max_d = j
#         else:
#             j -= 1
#
#     M = min_d + max_d
#     if M % 7 == 3:
#         return M
#     else:
#         return False
#
#
# c = 5
# s = 452022
# res = []
# while c > 0:
#     d = count_divisors(s)
#     if d:
#         res.append((s, d))
#         s += 1
#         c -= 1
#     else:
#         s += 1
#
# print(res)

# Задание 7
# def count_divisors(x):
#     good_d = []
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             if abs(x // i - i) <= 110:
#                 good_d.append(max((x // i,  i)))
#
#     if len(good_d) >= 3:
#         return max(good_d)
#
#     return False
#
#
# for i in range(1000000,  1500001):
#     gd = count_divisors(i)
#     if gd:
#         print(i, gd)


# Задание 8
# def count_divisors(x):
#     good_d = set()
#     if int(x ** 0.5)**2 == x:
#         good_d.add(int(x ** 0.5))
#         for i in range(2, int(x ** 0.5)):
#             if x % i == 0:
#                 good_d.add(x // i)
#                 good_d.add(i)
#
#         if len(good_d) == 3:
#             return max(good_d)
#
#     return False
#
#
# for i in range(1523467,  4157813):
#     gd = count_divisors(i)
#     if gd:
#         print(i, gd)


# Задание 9

# def count_divisors(x):
#     good_d = set()
#
#     if not (int(x ** 0.5)**2 == x):
#         # good_d.add(int(x ** 0.5))
#         for i in range(2, int(x ** 0.5)):
#             if x % i == 0:
#                 good_d.add(x // i)
#                 good_d.add(i)
#
#         if len(good_d) == 4:
#             return good_d
#
#     return False
#
# for i in range(22908,  22916):
#     gd = count_divisors(i)
#     if gd:
#         print(i, sorted(gd , reverse=True))


# Задание 10
def count_divisors(x):
    good_d = set()


        # good_d.add(int(x ** 0.5))
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            good_d.add(x // i)
            good_d.add(i)

    if len(good_d) == 4:
        return good_d

    return False

c = 0
m = float('inf')
s = 0
for i in range(108703,  118220):
    gd = count_divisors(i)
    if gd:
        c += 1
        if i < m:
            m = i
            s = sum(gd)

print(c, m, s)

        # print(i, sorted(gd , reverse=True))


