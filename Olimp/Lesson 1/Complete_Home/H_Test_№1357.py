# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=21&id_topic=49&id_problem=1003



""""""
"""RUNTIME ERROR"""


N = int(input())
s = [list(map(int, input().split())) for _ in range(N)]
# east = [o for o in range(1, N + 1)]
east = []
drain = []



# r = [[] for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if s[i][j] == 1:
#             r[i].append(j)
#
#
#
# for el in range(N):
#     if len(r[el]) == 0:
#         drain.append(el + 1)
#     else:
#         for element in r[el]:
#             del east[east.index(element + 1)]

for i in range(N):
    if sum(s[i]) == 0:
        drain.append(i + 1)
    p = 0
    for j in range(N):
        p += s[j][i]


    if p == 0:
        east.append(i + 1)

                #del east[east.index(j + 1)]




# east = [len(east)] + east
# drain = [len(drain)] + drain


print(len(east), end=' ')
print(*east)

print(len(drain), end=' ')
print(*drain)




"""
0 1
0 0 

0 0 
1 0 

0 0
0 0

0 1
1 0
"""




