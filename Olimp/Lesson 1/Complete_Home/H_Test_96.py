N = int(input())
l = [list(map(int, input().split())) for i in range(N)]

def F(l):
    for i in range(N):
        if l[i][i] != 0:
            return 0

    for i in range(N):
        for j in range(i, N):
            a = l[i][j]
            b = l[j][i]
            if a != b:
                return 1

    return 0


if F(l):
    print('YES')
else:
    print('NO')





# if c - N == (N ** 2):
#     print('NO')
# else:
#     print('YES')



'''
0 0 1 0 0
0 0 1 0 1
1 1 0 0 0
0 0 0 0 0
0 1 0 0 0
'''

