N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]


def fff(l):
    c = sum(l[0])
    for el in range(1, len(l)):
        if sum(l[el]) != c:
            return 'NO'
    return 'YES'

print(fff(l))