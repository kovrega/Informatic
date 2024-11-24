# N = int(input())
# l = [list(map(int, input().split())) for _ in range(N)]
N = input()
p = [int(input()) for _ in range(2)]


def f(p1, p2):
    P01 = p1

    while p2 > p1 * 2:
        p2 //= 2

    while p2 != p1 + 1:
        if p2 == P01:
            return P01

        p1 //= 2
        p2 = p2 // 2
    if p1 == 0 and p2 == 1:
        return 1
    if p1 % 2 == 0:
        return p1 // 2
    else:
        p1 //= 2
        p2 //= 2
        return f(p1, p2)



print(f(min(p), max(p)))