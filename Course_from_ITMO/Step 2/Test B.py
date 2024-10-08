N, K = tuple(map(int, input().split()))
s = [int(input()) for _ in range(N)]
# N, K = 4, 11
# s = [802, 743, 457, 539]

eps = 10 ** -6
l = 0
r = 10 ** 16
ans = 0

def check(r) -> bool:
    c = 0
    for q in s:
        c += q // r

    if c >= K:
        return True
    else:
        return False


while (r - l) > eps:
# for it in range(100):
    m = (r + l) / 2

    if check(m):
        l = m
        # ans = m
    else:
        r = m

# print(f"{m:.6f}")
print(round(m, 6))