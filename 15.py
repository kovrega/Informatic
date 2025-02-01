
# def f(x, a1, a2):
#     A = a1 <= x <= a2
#     P = 12 <= x <= 62
#     Q = 52 <= x <= 92
#     return not(not(A) and P) or Q
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
# print(round(min(res)))






# def f(x, A):
#     return   ((x % 45 == 0) and (not(x %  15 == 0))) <= (not(x %  A == 0))
#
#
# for A in range(1, 1000000):
#     if all(f(x, A) for x in range(1, 100000)):
#         print(A)
#         break



#
# def f(x, y,  A):
#     return (y < A)   or   (x < A)   or   (x + 2 * y > 115)
#
# for A in range(0, 10000):
#     if all(f(x /3, y / 3, A) for x in range(-10, 100) for y in range(-10, 100)):
#         print(A)
#         break