'''https://cses.fi/problemset/task/1640'''


n, x = map(int, input().split())
N = list(map(int, input().split()))
# l = {N[i] : i + 1 for i in range(n)}
l = [(N[i], i + 1) for i in range(n)]


l.sort()

"""
4 8
2 7 5 1

6 2
1 1 1 1 1 1

"""

def f(x):

    i = 0
    j = n - 1

    while i < j:

        if l[i][0] + l[j][0] == x:
            return ' '.join(map(str, sorted((l[i][1], l[j][1]))))
        elif l[i][0] + l[j][0] > x:
            j -= 1
        elif l[i][0] + l[j][0] < x:
            i += 1


    return 'IMPOSSIBLE'
print(f(x))