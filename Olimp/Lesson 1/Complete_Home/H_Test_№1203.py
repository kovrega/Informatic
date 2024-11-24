# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=21&id_topic=49&id_problem=633

N = int(input())
s = [[0 for ii in range(N)] for jj in range(N)]
for strok in range(N):
    els = list(map(int, input().split()))
    for el in els[1:]:
        s[strok][el - 1] = 1

print(N)
for st in s:
    print(*st)






