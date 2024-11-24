"""https://cses.fi/problemset/task/1084"""


n, m, k = map(int, input().split())
N = list(map(int, input().split()))  # desired apartments size
M = list(map(int, input().split())) # apartments size
c = 0
N.sort()
M.sort()



i = 0 # desired apartments size
j = 0 # apartments size


while i < n and j < m:

    if abs(N[i] - M[j]) > k:
        if N[i] > M[j]:
             j += 1
        else:
            i += 1

    else:
        c += 1
        i += 1
        j += 1


print(c)



