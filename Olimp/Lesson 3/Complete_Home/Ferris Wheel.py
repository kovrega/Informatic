# https://cses.fi/problemset/task/1090








n, x = map(int, input().split())
p = list(map(int, input().split()))
l = []
p.sort()
c = 0

i = 0
j = 1  # --- Переместить в конец
while j <= n:
    if i == n - 1 and j == n:
        if p[i] <= x:
            c += 1
            break

    elif p[i] >= x:
        c += 1
        i += 1
        j += 1

    elif p[i] + p[j] <= x:
        c += 1
        i += 2
        j += 2

    elif p[i] + p[j] > x:
        c += 1
        i += 1
        j += 1
#
# if j == n:
#     c += 1

# for i in range(0 , n - 1):
#     if p[i] + p[i + 1] <= x and p[i] not in l:
#         c += 1
#         l.append(p[i])
#         l.append(p[i + 1])
#     if p[i] + p[i + 1] > x:
#         c += 1
#         l.append(p[i])


print(c)