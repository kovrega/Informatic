N, M = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(M)]

# X = [0, 1, 3]
# for i in range(3, N):
#     X.append(X[i - 1] + i)
# X : [0, 1, 3, 6, 10]

r = [set() for _ in range(N - 1)]

for i in range(M):
    r[l[i][0] - 1].add(l[i][1])
# print(r)


# print(r)
# c = 0
# for el in r:
#     if el[0] == r.index(el) + 2:
#         c += 1
s = 0
for el in r:
    s += len(el)



if N * (N - 1) == 2 * s :
    print('YES')
else:
    print("NO")

