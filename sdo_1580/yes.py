# with open(input()) as f:
#     S, D  = map(int , f.readline().strip().split())
#     cont = sorted(list(map(int, f.read().split())))
#
#
# i = 0
# s = []
# while sum(s) + cont[i] <= S:
#     s.append(cont[i])
#     i += 1
#
# k = cont[i:]
#
# print(len(k), sum(k))
#
#
#

# with open(input()) as f:
#     N  = int(f.readline().strip())
#     prod = sorted(list(map(int, f.read().split())), reverse= True)
#
# exp = [prod[i] for i in range(N // 9)]
#
# prod.reverse()
#
# cheap = []
# delta = [0] + [9] * (N // 9 - 1)
# for j in range(N // 9):
#     cheap += [ prod[j + delta[j]] ]
#
# print(sum(prod) - sum(exp), sum(prod) - sum(cheap))




# with open(input()) as f:
#     N  = int(f.readline().strip())
#     prod = sorted(list(map(int, f.read().split())), reverse= True)
#
# exp = [prod[i] for i in range(N // 4)]
# prod.reverse()
# cheap = [prod[j] for j in range(N // 4)]
#
# print(sum(prod) - sum(exp)//2, sum(prod) - sum(cheap)//2)
#



#
#
# with open(input()) as f:
#     N, S  = map(int , f.readline().strip().split())
#     dock = sorted(list(map(int, f.read().split())), reverse=True)
#
#
#
# s = []
# i = -1
#
# while i + 2 < N - 1:
#     i += 1
#     s_ = [dock[i]]
#
#     while sum(s_) + dock[i + 1] <= S:
#         s_.append(dock[i + 1])
#         i += 1
#
#     for j in range(i, N - 1):
#         if sum(s_) + dock[j + 1] <= S:
#             s_.append(dock[j + 1])
#             i += 1
#             dock[j + 1], dock[i] = dock[i], dock[j + 1]
#
#     s.append(s_)
#
# if i + 1 == N - 1:
#     s.append([dock[i + 1]])
#
#
# print(len(s), sum(s[-1]))


with open('file.txt') as f:
    S, N = map(float, f.readline().strip().split())
    prod_all = sorted(list(map(int, f.read().split())))
from collections import Counter

pprod = []

for el in prod_all:
    if el not in pprod:
        c = prod_all.count(el)
        if c > 1:
            for k in range(c): pprod.append(el)


def f(b: list, i: int):
    while sum(b) + pprod[i] <= S:
        c = pprod.count(pprod[i])
        if sum(b) + c * pprod[i] <= S:
            b.extend([pprod[i]] * c)
            if i + c < len(pprod):
                i += c

        else:
            break
    return b, i

b, i0 = f([], 0)
rprod = b.copy()
if len(pprod) - i0 >= 2:
    c1 = b.count(b[-1])
    b1 , j1 = f(b[:-c1], i0)


    c2 = b.count(b[0])
    b2, j = f(b[c2:], i0)

    l = []
    l.append(b)
    l.append(b1)
    l.append(b2)
    rprod = sorted(l, key = lambda x :  (-len(x), -max(x)) )[0]


print(max(rprod), Counter(rprod).most_common()[0][-1])


# with open(input()) as f:
#     N  = int(f.readline().strip())
#     prod = sorted(list(map(int, f.read().split())), reverse= True)
#
# sp = sum(prod)
# exp = [prod[i] for i in range(N // 9)]
#
# prod.reverse()
# # cheap = []
#
#
# # for j in range(8, len(prod), 9):
# #     cheap.append(prod[j])
# cheap = list(prod[8::9])
#
# print(sp - sum(exp), sp - sum(cheap))

# 20
# 80
# 10
# 10
# 20
# 20
# 20
# 20
# 10
# 10
# 20
# 90
# 10
# 30
# 30
# 30
# 30
# 30
# 30
# 30
# 30





#
# s = []
# i = -1
#
# while i + 2 < N - 1:
#     i += 1
#     s_ = [prod[i]]
#
#     while sum(s_) + prod[i + 1] <= S:
#         s_.append(prod[i + 1])
#         i += 1
#
#     for j in range(i, N - 1):
#         if sum(s_) + prod[j + 1] <= S:
#             s_.append(prod[j + 1])
#             i += 1
#             prod[j + 1], prod[i] = prod[i], prod[j + 1]
#
#     s.append(s_)
#
# if i + 1 == N - 1:
#     s.append([prod[i + 1]])


