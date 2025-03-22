from itertools import product, permutations

alf = 'БОРИС'
c = 0
for x in product(alf, repeat= 6):
    if all(x.count(i) == 1 for i in 'БР'):
        if x.count('С') <= 1:

            c += 1

print(c)

# alf = '0123456789'
# c = 0
# for x in permutations(alf, r=6):
#     # if all(int(x[i]) > int(x[i + 1])  for i in range(5)):
#     if all(int(x[i]) % 2 != int(x[i + 1]) % 2 for i in range(5)):
#         if x[-1] == '0' or x[-1] == '5':
#             c += 1
#
# print(c)










