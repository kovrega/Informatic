

# 1 вариант задания
a = []
for x in '0123456789ABCDEFGHI':
    r = int('98897' + x + '21', 19) + int('2' + x + '923', 19)
    if r % 18 == 0:
        a.append(r // 18)
print(max(a))


print('ИЛИ')

# 2 вариант задания
x = 3 * (3125**8) + 2 * (625**7) - 4 * (625**6) + 3 * (125**5) - 2 * (25**4) - 2024
c = 25
def F(x, c) -> str:
    r = ''
    while x > 0:
        r = str(x % c) + r
        x //= c
    return r

print(F(x, 25).count('0'))