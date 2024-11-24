N = int(input())
l = [list(map(int, input().split())) for i in range(N)]



c = 0
for i in range(N):
    for j in range(i + 1, N):
        c += l[i][j]

print(c)
