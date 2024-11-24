#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=21&id_topic=49&id_problem=632

N, M = list(map(int, input().split()))
l = [list() for _ in range(N)]
for el in range(M):
    s = input().split()


    l[int(s[0]) - 1].append(int(s[-1]))

print(N)

for i in range(N):
    print(len(l[i]), *sorted(l[i]))




