# https://cses.fi/problemset/task/1091
n, m = map(int, input().split())
h = list(map(int, input().split())) # ticket
t = list(map(int, input().split())) # client
c = 0

h_ = h.copy()
t_ = t.copy()


h.sort()
t.sort()


i = 0
j = 0

p = []
ind = [0 for _ in range(m)]



while i < n and j < m:
    if h[i] > t[j]:

        if h[i - 1] in p:
            p.append(-1)
            ind[t_.index(t[j])] = -1


        else:
            p.append(h[i - 1])
            ind[t_.index(t[j])] = h[i - 1]

        j += 1
    else:
         i += 1

if len(p) < m:
    if h[-1] <= t[-1]:
        p.append(h[-1])
        ind[t_.index(t[-1])] = t[-1]
    else:
        p.append(-1)
        ind[t_.index(t[-1])] = -1

for el in ind[::-1]:
    print(el)




# while i < n and j < m:
#     if h[i] <= t[j]:
#         p.append(h[i])
#         i += 1
#         j += 1
#     else:
#         j += 1

