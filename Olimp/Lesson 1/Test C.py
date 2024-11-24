#https://acmp.ru/asp/do/index.asp?main=topic&id_course=2&id_section=21&id_topic=49

N = int(input())
l = [list() for _ in range(N)]
c = 0
for el in range(N):
    s = input().split()

    for i in range(N):
        if int(s[i]):
            l[el].append(i + 1)
            c += 1

print(N, c)

for i in range(N):
    if l[i]:
        for el in l[i]:
            print(i + 1, el)




