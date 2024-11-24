# https://cses.fi/problemset/task/2183
n = int(input())
x = list(map(int, input().split()))

x.sort()


def f():
    k = 1
    for el in x:
        if el > k:
            return k

        k += el
    return k

print(f())

# for i in range(x[-1] ** 2):
#     a = sum(x[:i + 1])
#     b = x[i]
#     if a - b > 1:
#         print(x[i + 1] - 1)
#         break





