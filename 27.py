# https://inf-ege.sdamgia.ru/problem?id=27891
# with open('27-A_1.txt', 'r') as f1:
#     l = f1.readlines()
# l1 = [int(_) for _ in l][1:]
#
#
# with open('27-B_1.txt', 'r') as f2:
#     d = f2.readlines()
# l2 = [int(_) for _ in d][1:]
#
#
#
#
# def find(l):
#     m2 = 0
#     m7 = 0
#     m14 = 0
#     m = 0
#
#
#     for i in l:
#
#         if i % 2 == 0 and i % 7 != 0 and i > m2:
#             m2 = i
#         if i % 7 == 0 and i % 2 != 0 and i > m7:
#             m7 = i
#         if i % 14 == 0 and i > m14:
#             if m14 > m:
#                 m = m14
#             m14 = i
#         elif i > m:
#             m = i
#     return max(m7 * m2, m14 * m)
#
#
#
# print(find(l1))
# print(find(l2))





