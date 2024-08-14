with open('17.txt', 'r') as f:
    l_ = f.readlines()


l = [_ for _ in l_]
l = list(map(int, l))
m = float('inf')
c = 0

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

def f(x , c):
    s = ''
    while x > 0:
        s = str(x % c) + s
        x = x // c
    return s

print(f(6 * 343 ** 5 + 5 * 49 ** 7 - 50, 7).count('6'))