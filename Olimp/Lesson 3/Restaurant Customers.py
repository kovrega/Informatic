# https://cses.fi/problemset/task/1619/
n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
'''TIME LIMITED'''




st_p = [(el[0], 1) for el in x]
end_p = [(el[-1], -1) for el in x]
s = sorted(st_p + end_p)
s.sort()


c = 0
m = -1
i = 0

for el, p in s:
    c = max(p, c + p)
    m = max(m, c)


print(m)