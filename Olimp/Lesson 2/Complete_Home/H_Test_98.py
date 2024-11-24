from itertools import dropwhile
from logging.config import valid_ident

N, S = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(N)]
s = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if l[i][j] == 1:
            s[i].append(j)


c = 0

def DFS(graph, current, visited: set):
    global c
    visited.add(current)
    # print('dfs')
    for v in graph[current]:
        if v not in visited:
            c += 1
            DFS(graph, v, visited)

    return c






print(DFS(s, S - 1, set()))
# for st in range(N):
#     for i in range(N):
#         if l[st][i] == 1:
#             s[st].append(i)
#
#
# def fff(S, s):
#     c = 0
#     ells = s[S - 1]
#     for el in ells:
#         c += len(s[el])
#     return c
#
# print(fff(S, s))

# 4 2
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0





