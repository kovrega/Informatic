

# with open('17-4 (7).txt') as f:
#     l = list(map(int, f.read().split()))
#
#
# r = []
#
#
# for el in l:
#     if el % 10 == 5 or el % 10 == 7:
#         if el % 9 != 0 and el % 11 != 0:
#             r.append(el)
#
#
# print(len(r), min(r) + max(r))









# with open('17-243 (4).txt') as f:
#     l = list(map(int, f.read().split()))
#
# s = 0
# for el in l:
#     if el % 33 == 0:
#         s += sum(int(b) for b in str(el))
#
#
# r = []
# for i in range(1, len(l)):
#     a = l[i - 1]
#     b = l[i]
#     if a > s or b > s:
#         r.append(a + b)
#
# print(len(r), min(r))











# with open('17-243 (5).txt') as f:
#     l = list(map(int, f.read().split()))
#
# s = 0
# for el in l:
#     if el % 35 == 0:
#         s += sum(int(b) for b in str(el))
#
#
# def check(x, y):
#     if x > s and y <= s:
#         if hex(y)[-2:] == 'ef':
#             print('yes ' + hex(y)[2:])
#             return True
#         # else:
#             # print('no ' + hex(y)[2:])
#             # print('no')
#     return False
#
#
# r = []
# for i in range(1, len(l)):
#     a = l[i - 1]
#     b = l[i]
#     if check(a, b) or check(b, a):
#         r.append(a + b)
#
# print(len(r), min(r))
# print('efsff'[-2:])



with open('17-1 (5).txt') as f:
    l = list(map(int, f.read().split()))



sr = sum(l) / len(l)
r = []
for i in range(2, len(l)):
    a = l[i - 2]
    b = l[i - 1]
    c = l[i]
    if sum(x < sr for x in (a, b, c)) >= 2:
        if sum('1' in y for y in (str(a), str(b), str(c))) == 3:
            r.append(sum((a, b, c)))


print(len(r), max(r))

















