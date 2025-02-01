

# 1 вариант
# def F(n):
#     # if n == 1: return 1
#     # if n == 2: return 2
#     # if n == 3: return 3
#
#     if n > 2024: return n
#     if n <= 2024: return n * F(n + 1)
#
# a = F(2022)
# b = F(2024)
# print(a / b)
#
#
# # 2 вариант
# F = []
# for _ in range(1, 2051):
#     F.append(_)
#
# for n in range(2024, 1, -1):
#     if n <= 2024:
#         F[n] = n * F[n + 1]
#
#
# a = F[2022]
# b = F[2024]
#
# print(a / b)




# F = [None, 1]
#
# for n in range(2, 100000):
#     if n % 2 == 0:
#         F.append(1 + F[n // 2])
#     else:
#         F.append(0)
#
# print(F.index(16))



# F = [None, 2]
# G = [None, 1]
# for n in range(2, 100):
#     F.append(
#         F[n - 1] - G[n - 1]
#     )
#     G.append(
#         F[n - 1] + G[n - 1]
#     )
#
# print(F[5]/G[5])




# F = [None] + [0]* 16 +  [n - 3 for n in range(17, 21)]
#
#
# for n in range(16, 0, -1):
#     F[n] = 2*F[n + 1] + 2 * n + 3
#
# print(F)
# print(14 * 2 + 2 * 16 + 3)






# F = [None, 1, 2, 3]
#
#
# for n in range(4, 101):
#     if n % 2 == 0:
#         F.append(2 * n  + F[n - 1])
#     else:
#         F.append(n* n  + F[n - 2])
#
# c = 0
# for el in F:
#     if el != None:
#         if el % 3 == 0:
#             c += 1
#
# print(c)






# F = [None, 1, 0]
# for n in range(3, 100000):
#     if n % 3 == 0:
#         F.append(F[n // 3] + 1)
#     else:
#         F.append(F[n - 2] + 5)
#
#
# print(F.index(73))





# F = [None] + [0]* 30 +  [n * n + 5 * n + 4 for n in range(31, 1001)]
#
#
# for n in range(30, 0, -1):
#     if n % 2 == 0:
#         F[n] = F[n+1] + 3 * F[n+4]
#
#     else:
#         F[n] = 2 * F[n+2] +  F[n+5]
#
#
# c = 0
# for el in F:
#     if el != None:
#         if sum(int(k) for k in str(el)) == 27:
#             c += 1
#
# print(c)
#






# F = [None, 1]
#
# for n in range(2, 10000):
#     F.append(n**3 + F[n - 1])
# print(F[2025] - F[2022])
#
#








# def F(N : str):
#
#     s1  = int(N[0]) + int(N[1])
#     s2  = int(N[1]) + int(N[2])
#     s3  = int(N[2]) + int(N[3])
#     s = sorted([s1, s2, s3])
#
#     R = str(s[1]) + str(s[2])
#
#     if R == "1315":
#         return True
#     return False
#
#
# for N in range(10000, 999, -1):
#     if F(str(N)):
#         print(N)
#         break











# def F(n1 : str, n2 : str = '365'):
#     s1 = int(n1[0]) + int(n2[0])
#     s2 = int(n1[1]) + int(n2[1])
#     s3 = int(n1[2]) + int(n2[2])
#
#     r_l = sorted([s1, s2, s3])
#     R = ''.join(map(str, r_l))
#     if R == "51014":
#         return True
#     return False
#
# for n1 in range(1000, 99, -1):
#     if F(str(n1)):
#         print(n1)
#         break








# def F(n : str):
#     s1 = int(n[0]) + int(n[1])
#     s2 = int(n[1]) + int(n[2])
#
#     R = ''.join(map(str, sorted([s1, s2], reverse= True)))
#
#
#     if R == '1412':
#         return  True
#     return False
#
# for n in range(100, 1001):
#     if F(str(n)):
#         print(n)
#         break

# print(F('631'))






def F(N : int ):
    N = N // 2 if N % 2 == 0 else N - 1
    N1 = N // 3 if N % 3 == 0 else N - 1
    R = N1 // 5 if N1 % 5 == 0 else N1 - 1

    if R == 1:
        return True
    return False

c = 0
for N in range(1, 1_000_000):
    if F(N):
        c += 1

print(c)

