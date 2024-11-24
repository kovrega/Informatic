N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]


s = []
for i in range(N):  # - строка
    for j in range(N): # - столбец
        for z in range(N): # - строка
            for y in range(N):  # - столбец
                if l[i][j] != 0 and l[z][j] != 0 and l[z][y] != 0:
                    if l[i][j] != l[z][j] != l[z][y]:
                        s.append(sum([l[i][j], l[z][j], l[z][y]]))


print(min(s))



