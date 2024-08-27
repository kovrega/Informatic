m, n = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# m, n = tuple(map(int, '6 7'.split()))
# a = list(map(int, '1 6 9 13 18 18'.split()))
# b = list(map(int, '2 3 8 13 15 21 25'.split()))

# m, n = tuple(map(int, '4 2'.split()))
# a = list(map(int, '1 1 2 19'.split()))
# b = list(map(int, '0 7'.split()))



c = []
i = 0
j = 0


while i < m and j < n:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

if i < m:
    c.extend(a[i:])
else:
    c.extend(b[j:])


print(*c)

