# https://cses.fi/problemset/task/1629
n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
s = []
for a, b in x:
    s.append((a, 1))
    s.append((b, -1))
s.sort()
"""TIME LIMITED"""

c = 0
k = 0
for el, p in s:
    if c < 0:
        c = 0

    if c + p < c and c > 0:
        k += 1
        c = 0
    else:
        c += p

print(k)



