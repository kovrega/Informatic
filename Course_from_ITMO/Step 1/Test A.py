N, K = tuple(map(int, input().split()))
n = list(map(int, input().split()))
k = list(map(int, input().split()))
# N, K = tuple(map(int, '10 10'.split()))
# n = list(map(int, '1 61 126 217 2876 6127 39162 98126 712687 1000000000'.split()))
# k = list(map(int, '100 6127 1 61 200 -10000 1 217 10000 1000000000'.split()))


for q in k:
    l = 0
    r = N - 1
    global mid

    if n[-1] < q or n[0] > q:
        print('NO')
        continue
    while l <= r:
        mid = (l + r) // 2

        if n[mid] == q:
            break
        elif n[mid] < q:
            l = mid + 1
        elif n[mid] > q:
            r = mid - 1

    if n[mid] == q:
        print('YES')
    if n[mid] != q:
        print('NO')
