N = int(input())
n = list(map(int, input().split())).sort()
K = int(input())
k = [tuple(map(int, input().split())) for _ in range(K)]


for q in k:
    a, b = q
    l = 0
    r = N - 1

    while l + 1 < r:
        m = (l + r) // 2

        if

