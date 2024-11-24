"""https://cses.fi/problemset/task/1074"""

n = int(input())
N = list(map(int, input().split()))

N.sort()
m = N[n // 2]



s = 0
for el in N:
    s += abs(el - m)

print(s)

