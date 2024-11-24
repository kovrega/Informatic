N, M = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(M)]


"""Wrong answer	24"""

l = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    l[s[i][0] - 1][s[i][-1] - 1] += 1

'''
0 1 1 0 1
0 0 1 0 1
0 0 0 0 0
1 1 1 0 1
0 0 1 0 0
'''
def ff(l):
    if M  != ((N - 1) * N) // 2:
        return 'NO'


    for i in range(N):
        for j in range(N):
            if i != j:
                if l[i][j] == l[j][i] or (l[i][j] > 1 or l[j][i] > 1):
                    return 'NO'

    return 'YES'

print(ff(l))
