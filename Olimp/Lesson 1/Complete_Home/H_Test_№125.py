N = int(input())
s = [list(map(int, input().split())) for i in range(N)]
u = input()
k = list(map(int, input().split()))



'''
0 1 0 0 0 1 1
1 0 1 0 0 0 0
0 1 0 0 1 1 0
0 0 0 0 0 0 0
0 0 1 0 0 1 0
1 0 1 0 1 0 0
1 0 0 0 0 0 0
'''

c = 0
for i in range(N):
    for j in range(N):

        if s[i][j] == 1:
            if i != j:
                if k[i] != k[j]:
                    c += 1

print(c//2)