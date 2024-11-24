N, M = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(M)]


s = [[] for el in range(N)]

for el in l:
    i, j = el
    s[i - 1].append(j - 1)
    s[j - 1].append(i - 1)

    # s[i].append(j)
    # s[j].append(i)

# s : [[2, 1], [0, 2], [0, 1], [4], [3], []]
# print(s)

c_s = {}
# for i in range(M):
#     c = 0
#     for el in s[i]:
#         if i in el:
#             c += 1
#     c_s[c] =






