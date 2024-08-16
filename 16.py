

# 1 вариант
def F(n):
    # if n == 1: return 1
    # if n == 2: return 2
    # if n == 3: return 3

    if n > 2024: return n
    if n <= 2024: return n * F(n + 1)

a = F(2022)
b = F(2024)
print(a / b)


# 2 вариант
F = []
for _ in range(1, 2051):
    F.append(_)

for n in range(2024, 1, -1):
    if n <= 2024:
        F[n] = n * F[n + 1]


a = F[2022]
b = F[2024]

print(a / b)
