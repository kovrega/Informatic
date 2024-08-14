"""1 задание"""
# C = float(input())

# eps = 10 ** -6
# left = 1
# right = 10 ** 18
# m = (left + right) / 2
#
# def f(x):
#     return x ** 2 - x ** 0.5



# while abs(d := (f(m) - C)) > eps:
#     if d > 0:
#         right = m
#     else:
#         left = m
#     m = (left + right) / 2
#
# print(f"{m:.6f}")


"""2 задание"""
# N, K = list(map(int, input().split()))
# n = list(map(int, input().split()))
# k = list(map(int, input().split()))
#
#
# for q in k:
#     l = 0
#     r = N - 1
#     if n[-1] < q:
#         print(N + 1)
#         continue
#     while l < r:
#         mid = (l + r) // 2
#         if n[mid] >= q:
#             ans = mid
#             r = mid - 1
#         else:
#             l = mid + 1
#
#     print(ans + 1)


"""3 задание"""
w, h, n = list(map(int, input().split()))











