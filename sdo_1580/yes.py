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










from collections import Counter
with open(input()) as f:
    S, N  = map(int , f.readline().strip().split())
    prod_all = sorted(list(map(int, f.read().split())))



pprod = [] # [10, 10, 10, 20, 20, 30, 30]
rprod = []
for el in prod_all:
    if el not in pprod:
        c = prod_all.count(el)
        if c > 1:
            for k in range(c): pprod.append(el)


# b = [] # [10, 10, 10, 20, 20]
# i = 0
def f(b: list , i : int):
    while sum(b) + pprod[i] <= S:
        c = pprod.count(pprod[i])
        if sum(b) + 2 * pprod[i] <= S:
            b.extend([pprod[i], pprod[i]])
            i += 2
            for k in range(2, c):
                if sum(b) + pprod[i] <= S:
                    b.append(pprod[i])
                    i += 1
            if i >= len(pprod) - 1:
                break
        else:
            break
    return b, i

b, i = f([], 0)

if  len(pprod) - i >= 2:
    c = b.count(b[-1])
    b_, j = f(b[:-c], i)
    if b_ != b:
        rprod = b_.copy()


print(max(rprod), Counter(rprod).most_common()[0][-1])










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


