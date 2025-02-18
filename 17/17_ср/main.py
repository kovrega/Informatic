with open('17-4 (6).txt') as f:
    l = list(map(int, f.read().split()))

r = []
for el in l:

    if sum(int(b) for b in str(el)) % 5 == 0:
        rr = ''
        elel = el
        for i in range(2):
            rr += str(elel % 3)
            elel //= 3
        if rr != '00':
            r.append(el)


print(len(r), max(r))












# with open('17-1 (3).txt') as f:
#     l = list(map(int, f.read().split()))
#
#
# sr = sum(l) / len(l)
#
# def check_1(a):
#     if a < sr:  return True
#     return False
#
#
# def check_2(b: int):
#     if str(b)[-2:] == '13': return True
#     return False
#
# r = []
# for i in range(1, len(l)):
#     if any([check_1(l[i - 1]), check_1(l[i])]):
#         if any([check_2(l[i - 1]), check_2(l[i])]):
#             r.append(l[i - 1] + l[i])
# print(len(r), max(r))
#
#
#
# print('122'[-2:])










# with open('17-278.txt') as f:
#     l = list(map(int, f.read().split()))
#
# gc = 0
# for el in l:
#     if el % 12 == 0:
#         gc += (str(el).count('9') * 10)
#
#
#
# def check_1(a, b):
#     if a > gc and b > gc:   return True
#     return False
#
# r = []
# for i in range(1, len(l)):
#     if check_1(l[i - 1], l[i]):
#         r.append(l[i - 1] + l[i])
# print(len(r), max(r))







# with open('17-1 (4).txt') as f:
#     l = list(map(int, f.read().split()))
#
# sr = sum(l) / len(l)
#
# def check_1(a):
#     if a < sr: return True
#     return False
#
# def check_2(b):
#     if '8' in str(b):   return True
#     return False
#
#
#
#
# r = []
# for i in range(2, len(l)):
#     if any([ check_1(l[i- 2]), check_1(l[i - 1]), check_1(l[i]) ]):
#         if any([check_2(l[i - 2]), check_2(l[i - 1]), check_2(l[i])]):
#             r.append(l[i - 2] + l[i - 1] + l[i])
#
# print(len(r), max(r))





