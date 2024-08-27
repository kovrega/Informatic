m, n = tuple(map(int, input().split()))
l = [tuple(map(int, input().split())) for _ in range(n)]








def check(T):
    min_time = 0
    count_ball = 0
    for u in l:
        t, z, y = u

        min_time += t
        count_ball += z


