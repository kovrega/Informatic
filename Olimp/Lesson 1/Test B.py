N, M = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(M)]

s = [0 for _ in range(N)]

for t in l:
    i, j = t
    i -= 1
    j -= 1

    s[i] += 1
    s[j] += 1

print(*s)


