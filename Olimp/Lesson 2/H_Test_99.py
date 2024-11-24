N,K = map(int, input().split())
l = [[] for j in range(N)]

n = [0,0]

while len(n) != 1:
    n = list(map(int, input().split()))
    l.append(n)
    # l[n[-1] - 1][n[0] - 1] = 1
    # l[n[0]  - 1][n[-1] - 1] = 1



def DFS(graph, current, visited : set):
    visited.add(current)

    for v in graph[current]:
        if v not in visited:
            DFS(graph, v, visited)

    return len(visited)




if DFS(l, K, set()) == K:
    print('Yes')
else:
    print('No')

# def F(l):
#     s = sum(l[K - 1])
#     for ell in range(N):
#         if ell != K - 1:
#             if sum(l[ell]) >= s:
#                 return "No"
#
#     return 'Yes'
# print(F(l))
# 4 1
# 1 1
# 2 3
# 1 2
# 0

