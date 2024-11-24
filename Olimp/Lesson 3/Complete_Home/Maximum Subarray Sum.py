n = int(input())
x = list(map(int, input().split()))

# n = 9
# x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]



i = 0
j = 0
best_sum = float('-inf')
cur_sum = 0
for el in x:
    cur_sum = max(el, cur_sum + el)
    best_sum = max(cur_sum, best_sum)



# while j < n - 1:
#     if i == j:
#         if x[i] > s:
#             s = x[i]
#         j += 1
#     elif i < j:
#         if sum(x[i : j + 1]) > s:
#             s = sum(x[i : j + 1])
#         if x[j + 1] > 0:
#             j += 1
#         else:
#             i += 1
#
#
# if len(x) == 1:
#     s = x[0]
#
# elif x[-1] > 0:
#     s += x[-1]


print(best_sum)


