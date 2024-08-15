w, h, n = tuple(map(int, input().split()))
# w, h, n = tuple(map(int, '2 3 9'.split()))


# w - ширина
# h - высота

def check(x):
    if (x // w) * (x // h) >= n:
        return True
    else:
        return False


l = 0
r = 10 ** 15
while l + 1 < r:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m

print(r)