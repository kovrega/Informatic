#
# from turtle import *
#
# from math import atan, tan
# print(atan(1.0))
# print(tan(45))
# # tracer(1)
# # k = 10
# # pendown()
#
#
# # right(1 / 5)
# # right(atan(45))
# # forward(5 * k)
#
# # left((10 / -2) -  )
#
#
#
#
# # done()
# #







# # 17




with open('24.txt') as f:
    N = int(f.readline())
    l_ = []
    for i in range(N):
        l_.append(f.readline().strip())

l = []
for el in l_:
    el = el.split()
    l.append((el[0], int(el[1])))

l.sort(key= lambda x: x[0])
i = 0
for i in range(N):
    if l[i][0] == 'B':
        print(i)
        break
    i+= 1

ind_B= 5821

print(N, l[:5])
A = sorted(el[1] for el in l[:ind_B])
B = sorted(el[1] for el in l[ind_B:])


c = []

for i in range(len(B)):
    if abs(A[i]- B[i]) <= 20:
        c.append(A[i] + B[i])


print(len(c), sum(c))












































