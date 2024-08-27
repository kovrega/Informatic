n, x, y = tuple(map(int, input().split()))
# n, x, y = 4, 1, 1
# n, x, y = 5, 1, 2
# n, x, y = 7, 1, 3 # 6
l = -1
r = max(x, y) * n

def check(t) -> bool:
    mi = min(x, y)
    ma = x + y - mi
    N = 0

    # Печатаем 1-ю копию
    t -= mi
    N += 1

    # Кол-во копий быстрого принтера
    N += (t // mi)

    # Кол-во копий медленного принтера
    N += t // ma


    if N >= n:
        return True
    return False




while l + 1 < r:
    m = (l + r) // 2

    if check(m):
        r = m
    else:
        l = m


print(r)



