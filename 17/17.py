# with open('17.txt', 'r') as f:
#     l_ = f.readlines()
#
#
# l = [_ for _ in l_]
# l = list(map(int, l))
# m = float('inf')
# c = 0


# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if (l[i] + l[j]) % 2 != 0:
#             if (l[i] * l[j]) % 3 == 0:
#                 c += 1
#                 if l[i] + l[j] > s:
#                     s = l[i] + l[j]
#                     # res.append(l[j])
#
#
# # print(c, s)
# if len(l) % 3 == 2:
#     l = l[:-2]
# if len(l) % 3 == 1:
#     l = l[:-1]

# max_el = max([el for el in l if el % 100 == 15])
#
# for i in range(0, len(l) - 2):
#     x = 0
#     s = [l[i], l[i + 1], l[i + 2]]
#     for el in s:
#         if len(str(abs(el))) == 4:
#             x += 1
#     if x == 1:
#         if sum(s) < max_el:
#             c += 1
#             if sum(s) < m:
#                 m = sum(s)
#
#
# print(c, m)

# H = float('-inf')
#
# for i in range(0, len(l) - 2):
#     s = [l[i], l[i + 1], l[i + 2]]
#     if sum(s) - max(s) > max(s):
#         c += 1
#     p = sum(s) / 2
#     S = 0.5 ** (p * (p - s[0]) * (p - s[1]) * (p - s[-1]))
#     if S > H:
#         H = S
#

# def f(x , c):
#     s = ''
#     while x > 0:
#         s = str(x % c) + s
#         x = x // c
#     return s

# print(f(6 * 343 ** 5 + 5 * 49 ** 7 - 50, 7).count('6'))




# def F(n):
#     s = set()
#     if int(n ** 0.5) ** 2 == n:
#         s.add(int(n ** 0.5))
#         # return None
#
#     s.add(1)
#     s.add(n)
#     i = 2
#     while len(s) < 36 and i ** 2< n:
#         if n % i == 0:
#             s.add(i)
#             s.add(n // i)
#         i += 1
#
#     if len(s) < 36:
#         return None
#     return list(s)
#
#
# c = 0
# l = 0
# for n in range(56123, 97354 + 1):
#     if R := F(n):
#         c += 1
#         l += n
#
# print(c, l // c )







#



# def D(n):
#     if  n % 15 == 0:
#         if n % 12 != 0 and n % 6 != 0:
#             if ((n // 100) % 10) % 3 == 0:
#                 return True
#     return False
#
#
# l = []
# for n in range(2121, 13469 + 1):
#     if R := D(n):
#         l.append(n)
#
#
# print(min(l) + max(l))



#
# def sev_s(n, c = 7) -> str:
#     r = ''
#
#     while n > 0:
#         r = str(n % c) + r
#         n //= c
#     return r
#
# def F(N):
#     if sev_s(N)[-1] == '6':
#         if N % 32 == 0:
#             return True
#     return False
#
#
# l = []
# cnt = 0
# for i in range(15, 1001):
#     if F(i):
#         cnt += 1
#         l.append(i)
#
# print(cnt, max(l))








# with open('17-4.txt') as f:
#     l = list(map(int, f.readlines()))
#
#
# def F(n):
#     ds = {2, 3, 5, 7}
#
#     c = 0
#     for d in ds:
#         if n % d == 0:
#             c += 1
#     if c == 2:
#         return True
#     return False
#
# r = []
# for el in l:
#     if F(el):
#         r.append(el)
#
# print(len(r), min(r) + max(r))




# f = open('17-272.txt')
# plus_elts = []
# l = []
# for st in f.readlines():
#     if st != '':
#         el = int(st.strip())
#         l.append(el)
#         if el > 0:
#             plus_elts.append(el)
# f.close()
#
# sr_ar = sum(plus_elts) // len(plus_elts)
#
# c = 0
# m = -1
# i = 0
# j = 1
# while j < len(l):
#     if l[i] > sr_ar or  l[j] > sr_ar:
#         c += 1
#
#         if (k := sum(int(_) for _ in str(abs(l[i])))) > m:
#             m = k
#         if (k := sum(int(_) for _ in str(abs(l[j])))) > m:
#             m = k
#     i += 1
#     j += 1
#
#
# print(c, m)









# def dev(n):
#     r = {1, n}
#     i = 2
#     while i**2 <= n and len(r) < 16:
#         if n % i == 0:
#             r.add(i)
#             r.add(n // i)
#         i += 1
#
#     if len(r) > 15:
#         return True
#     return False
#
#
# R = []
# for n in range(12_356, 76435 + 1):
#     if dev(n):
#         R.append(n)
# print(len(R), max(R))



# R = []
# for n in range(31, 2048):
#     if n % 10 != 0:
#         if sum(int(_) for _ in bin(n)[2:]) == 5:
#             if bin(n)[2:][-1] == '0':
#                 R.append(n)
#
# print(len(R), max(R))



# R = []
# for n in range(1206, 14993):
#     if n % 10 == 3 or n % 10 == 6:
#         if n % 3 != 0 and n % 4 != 0 and n % 5 != 0:
#             R.append(n)
#
# print(len(R), R[0])





# R = []
#
# for n in range(251_763, 514827 + 1 ):
#     if n % sum(int(_) for _ in str(n)) == 0:
#         R.append(n)
# print(len(R), min(R))







# R = []
# for n in range(10, 9999 + 1):
#     if bin(n)[-1] == '1':
#         if bin(n)[2:].count('0') == 5:
#             if n % 3 == 0 and n % 11 == 0:
#                 R.append(n)
#
# print(len(R), max(R))



# with open('17-4 (1).txt') as f:
#     l = list(map(int, f.readlines()))
# R = []
# for n in l:
#     if n % 3 == 0:
#         if n % 7 != 0 and n % 17 != 0 and n % 19 != 0 and n % 27 != 0:
#             R.append(n)
#
#
# print(len(R), max(R))







# with open('17-7 (1).txt') as f:
#     l = list(map(int, f.readlines()))
# R = []
#
# for n in l:
#     if (m := oct(n)[2:])[-1] == '7' and  (p :=oct(n)[2:][-2:]) != '27':
#         R.append(n)
#
# print(len(R), max(R))






# with open('17-4 (2).txt') as f:
#     l = list(map(int, f.readlines()))
#
# sr_ar = sum(l) / len(l)
#
# c = 0
# m = float('inf')
# for i in range(len(l) - 1):
#     if l[i] > sr_ar or l[i + 1] > sr_ar:
#         if (k := (l[i] + l[i + 1])) % 10 == 9:
#             c += 1
#             if k < m:
#                 m = k
# print(c, m)



# with open('17-243.txt') as f:
#     l = list(map(int, f.readlines()))
#
# k = l.copy()
# k.sort(reverse=True)
# m = 0
# for el in k:
#     if el % 153 == 0:
#         m = el
#         break
#
# R = []
# for i in range(len(l) - 1):
#     if l[i] > m or l[i + 1] > m:
#         if '1111' in bin(l[i]) or '1111' in bin(l[i + 1]):
#             R.append(l[i] + l[i + 1])
#
# print(len(R), min(R))
#



# with open('17-243 (1).txt') as f:
#     l = list(map(int, f.readlines()))
#
# k = l.copy()
# k.sort(reverse=True)
# m = 0
# for el in k:
#     if el % 211 == 0:
#         m = el
#         break
#
# R = []
# for i in range(len(l) - 1):
#     if l[i] > m or l[i + 1] > m:
#         if '1' in str(l[i]) or '1' in str(l[i + 1]):
#             R.append(l[i] + l[i + 1])
#
# print(len(R), min(R))








# with open('17-1.txt') as f:
#     l = list(map(int, f.readlines()))
#
# sr_ar = sum(l) / len(l)
#
# R = []
# for i in range(len(l) - 2):
#     tr = (l[i], l[i + 1], l[i + 2])
#     if sum(1 if el < sr_ar else 0 for el in tr) >= 2:
#         if sum(1 if abs(ell) % 100 == 14 else 0 for ell in tr) >= 1:
#             R.append(sum(tr))
#
# print(len(R), max(R))





#
# with open('17-1 (1).txt') as f:
#     l = list(map(int, f.readlines()))
#
# sr_ar = sum(l) / len(l)
#
# R = []
# for i in range(len(l) - 2):
#     tr = (l[i], l[i + 1], l[i + 2])
#     if sum(1 if el < sr_ar else 0 for el in tr) >= 2:
#         if sum(1 if abs(ell) % 10 == 8 else 0 for ell in tr) >= 2:
#             R.append(sum(tr))
#
# print(len(R), max(R))





# def dev(n):
#     r = {1, n}
#     i = 2
#     while i**2 <= n and len(r) < 26:
#         if n % i == 0:
#             r.add(i)
#             r.add(n // i)
#         i += 1
#
#     if len(r) > 25:
#         return True
#     return False
#
#
# R = []
# for n in range(35_612, 57354 + 1):
#     if dev(n):
#         R.append(n)
# print(len(R), min(R))







# R = []
# for n in range(100, 10_000 + 1):
#     if n % 10 == 3 and oct(n)[-1] == '7':
#         if n % 13 != 0 and n % 16 != 0 and n % 19 != 0 and  n % 21 == 0:
#             R.append(n)
#
# print(len(R), R[-1])








# with open('17-4 (3).txt') as f:
#     l = list(map(int, f.readlines()))
#
#
#
# R = []
# for n in l:
#     if n % 13 == 4 and n % 8 == 1:
#         R.append(n)
#
# print(sum(R), max(R))








# def dev(n):
#     r = set()
#     i = 2
#     while i**2 < n and sum(r) < 41:
#         if n % i == 0:
#             r.add(i)
#             r.add(n // i)
#         i += 1
#
#     if sum(r) > 40:
#         return True
#     return False
#
# R = []
#
# for n in range(255, 4095 + 1):
#
#     if dev(n) and n % 5 != 0:
#         R.append(n)
#
# print(len(R), R[-1] - R[0])






# def F(n, c =3):
#     r = ''
#     while n > 0:
#         r = str(n % c) + r
#         n //= c
#     return r
#
# R = []
# for n in range(64, 1024 + 1):
#     if n % 8 == 0 and n % 5 != 0:
#         if bin(n).count('1') == 3 and bin(n)[-1] == '0':
#             R.append(n)
#
#
# print(len(R), max(R))



# def F(n, c =5):
#     r = ''
#     while n > 0:
#         r = str(n % c) + r
#         n //= c
#     return r

# with open('17-243 (3).txt') as f:
#     l = list(map(int, f.readlines()))
#
# summa_cifr = 0
# for el in l:
#     if el % 37 == 0:
#         summa_cifr += sum(int(_) for _ in str(el))
#
# R = []
# for i in range(len(l) - 1):
#     if all(1 if p > summa_cifr else 0 for p in (l[i], l[i + 1])):
#         R.append(l[i] + l[i + 1])
#     # if l[i] > summa_cifr and l[i + 1] <= summa_cifr:
#     #     if l[i + 1] % 10 == 7:
#     #         R.append(l[i] + l[i + 1])
#     # elif  l[i + 1] > summa_cifr and l[i] <= summa_cifr:
#     #     if l[i] % 10 == 7:
#     #         R.append(l[i] + l[i + 1])
#
#
# print(len(R), min(R))










#
with open('17-1 (2).txt') as f:
    l = list(map(int, f.readlines()))



sr_ar = sum(l) / len(l)

R = []
for i in range(len(l) - 2):
    tr = (l[i], l[i + 1], l[i + 2])
    if sum(1 if el < sr_ar else 0 for el in tr) >= 1:
        if sum(1 if '8' in str(abs(ell))  else 0 for ell in tr) >= 1:
            R.append(sum(tr))

print(len(R), max(R))





























