
# N, K = tuple(map(int, input().split()))
# n = list(map(int, input().split()))
# k = list(map(int, input().split()))
N, K = tuple(map(int, '5 5'.split()))
n = list(map(int, '3 3 5 8 9'.split()))
k = list(map(int, '2 4 8 1 10'.split()))




for q in k:
    l = -1
    r = N

    if n[-1] < q:
        print(N + 1)
        continue

    while l + 1 < r:
        m = (l + r) // 2

        if n[m] < q:
            l = m
        elif n[m] >= q:
            r = m

    print(r + 1)
