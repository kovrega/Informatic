# https://cses.fi/problemset/task/1621




n = int(input())
x = list(map(int, input().split()))
c = 1
x.sort()
for i in range(n - 1):
    if x[i] != x[i + 1]:
        c += 1


print(c)

