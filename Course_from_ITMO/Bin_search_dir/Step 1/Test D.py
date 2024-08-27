
# N = int(input())
# n = list(map(int, input().split())).sort()
# K = int(input())
# k = [tuple(map(int, input().split())) for _ in range(K)]

N = 5
n = list(map(int, '10 1 10 3 4'.split()))
K = 4
k = [
    (1, 10),
    (2, 9),
    (3, 4),
    (2, 2)
]
n.sort()

# def A(l, r, n):
#     while l + 1 < r:
#         m = (l + r) // 2
#
#         if n[m] < a:
#             l = m
#         if n[m] >= a:
#             r = m
#     return r + 1
#
# def B(l, r, n):
#     while l + 1 < r:
#         m = (l + r) // 2
#
#         if n[m] <= a:
#             l = m
#         if n[m] > a:
#             r = m
#     return l + 1
#



for q in k:
    a, b = q
    l = -1
    r = N


    # while l < r:






