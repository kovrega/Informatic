# from turtle import *
# # tracer(0)
# speed(1)
# x, y, k = 0, 0, 10
#
#
# pendown()
# begin_fill()
# goto(x + k*3, y + k*6)
# x += k*3
# y += k * 6
# goto( x + k*7, y - k*2)
# x += k*7
# y += k * -2
# goto( x - k*10, y - k*4)
# x += k*-10
# y += k * -4
#
#
#
#
# end_fill()
# penup()
# canvas =getcanvas()
# c = 0
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         if canvas.find_overlapping(x*k,y*k, x*k,y*k) == (5,):
#             c += 1
# print(c)
#
# done()



# 2
# from turtle import *
# x, y, k = 0, 0, 25
#
# pendown()
# # for i in range(5):
# begin_fill()
# goto(x + 6*k, y + 8*k)
# x += 6*k
# y += 8*k
# goto(x - 8*k, y + 4*k)
# x += -8*k
# y += 4*k
# goto(x + 2*k, y - 12*k)
# x += 2*k
# y += -12*k
#
# end_fill()
# penup()
#
# print((6 ** 2 + 8 ** 2)**0.5 + (8 ** 2 + 4 ** 2)**0.5+ (2 ** 2 + 12 ** 2)**0.5)





# 3
# from turtle import *
#
# # tracer(0)
# k = 10
# left(90)
# pendown()
# begin_fill()
# # forward(100)
# for i in range(4):
#     right(90)
#     forward(50* k)
# end_fill()
# c = 0
# penup()
# canvas = getcanvas()
# for x in range(-1000, 1000):
#     for y in range(-1000, 1000):
#         if canvas.find_overlapping(x*k,y*k, x*k,y*k) == (5,):
#             c += 1
# print(c)
# print(49* 49)
# done()





# 4
# from turtle import *
#
# tracer(0)
# k = 50
# left(90)
# pendown()
# begin_fill()
# # forward(100)
# for i in range(36):
#     right(60)
#     forward(1* k)
#     right(60)
#     forward(1* k)
#     right(270)
# end_fill()
# penup()
#
# done()










# 5
# from turtle import *
#
# tracer(0)
# k = 50
# left(90)
# pendown()
# # begin_fill()
# for i in range(3):
#     forward(5 * k)
#     right(90)
#     forward(9 * k)
#     right(90)
#
# right(360 -315)
#
#
# for i in range(4):
#     forward(11 * k)
#     right(90)
#     forward(5 * k)
#     right(90)
# # end_fill()
# penup()
#
#
#
# color('red')
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*k, y*k)
#         dot(5)
#
# done()








# 6
# from turtle import *
#
# tracer(0)
# k = 50
# left(90)
# pendown()
# begin_fill()
# for i in range(2):
#     forward(10 * k)
#     right(120)
#     forward(10 * k)
#     right(60)
#
# end_fill()
# penup()
# c = 0
# canvas = getcanvas()
# for x in range(-700, 700):
#     for y in range(-700, 700):
#         if canvas.find_overlapping(x*k,y*k, x*k,y*k) == (5,):
#             c += 1
# print(c)
#
# done()






# 7
# from turtle import *
#
# tracer(0)
# k = 30
# left(90)
# pendown()
# # begin_fill()
#
# for i in range(6):
#     forward(10 * k)
#     right(90)
#
# forward(2 * k)
# right(90)
#
# for i in range(2):
#     forward(15 * k)
#     right(90)
#     forward(4 * k)
#     right(90)
#
# penup()
# color('red')
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*k, y*k)
#         dot(5)
#
# done()





# 8
# from turtle import *
#
# tracer(0)
# k = 15
# left(90)
#
# pendown()
#
# for i in range(2):
#     forward(24 * k)
#     right(90)
#     forward(16 * k)
#     right(90)
# penup()
# forward(10 * k)
# right(90)
# forward(8 * k)
# left(90)
# pendown()
#
# for i in range(2):
#     forward(15 * k)
#     right(90)
#     forward(28 * k)
#     right(90)
#
#
# penup()
# color('red')
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*k, y*k)
#         dot(5)
# done()



# 9
# from turtle import *
#
# tracer(0)
# k = 15
# left(90)
# pendown()
#
# for i in range(2):
#     forward(10 * k)
#     right(90)
#     forward(20 * k)
#     right(90)
# penup()
# forward(3 * k)
# right(90)
# forward(5 * k)
# left(90)
# pendown()
#
# for i in range(2):
#     forward(70 * k)
#     right(90)
#     forward(80 * k)
#     right(90)
#
# penup()
# color('green')
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*k, y*k)
#         dot(5)
# done()


# 10
from turtle import *


k = 10
penup()
for i in range(7):
    for j in range(2):
        forward(3 * k)
    dot(5)
    backward(4* k)
    dot(5)



done()










