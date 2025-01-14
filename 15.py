
# def f(x, a1, a2):
#     A = a1 <= x <= a2
#     P = 12 <= x <= 62
#     Q = 52 <= x <= 92
#     return  (P or A) <= (Q or A)
#
#
# res = []
# ctrl_val = [y for x in (12, 62, 52, 92) for y in (x, x - 0.1, x + 0.1)]
#
#
# for a1 in ctrl_val:
#     for a2 in ctrl_val:
#         if a2 >= a1 and all(f(x, a1, a2) for x in ctrl_val):
#             res.append(a2 - a1)
#
#
# print((min(res)))






def f(x, A):
    return   (x & 49 != 0) <= ((x & 33 == 0) <= (x & A != 0))

for A in range(1, 1000):
    if all(f(x, A) for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break




# def f(x, A):
#     return (not(x % A == 0)) <= ((x % 6 == 0) <= (not(x % 7 == 0)))
#
#
# for A in range(1000, 1, -1):
#     if all(f(x, A) for x in range(1, 1000)):
#         print(A)
#         break