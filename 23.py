


# 8
# def F(n):
#     if n + 2 == 32:
#         return 1
#     if n + 2 > 32:
#         return 0
#     else:
#         return F(n + 1) + F(n * 2)
#
# print(F(5))



# 9
# def F(n, c = 0):
#     if c == 4:
#     # if c == 3:
#     # if c == 2:
#     # if c == 1:
#         return {n}
#     if c > 4:
#         return {None}
#     else:
#         return F(n + 1, c + 1) | F(n * 2, c + 1)
#
# print(sorted(F(1)))



# 10

def F(n):
    if n == 98:
        return 1
    if n > 98:
        return 0
    if n in (7, 23, 76, 86):
        return 0
    else:
        return F(n + 1) + F(n * 2) + F(n ** 2)


print(F(3))