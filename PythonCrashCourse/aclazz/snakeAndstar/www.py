import turtle
import random
import time
def draw_snake():
    turtle.pensize(25) # 设置画笔大小
    turtle.pencolor("green") # 设置画笔颜色
    turtle.screensize(1200, 800)
    turtle.seth(-35)
    for i in range(2):
        turtle.circle(60, 70)
        turtle.circle(-60, 70)
    turtle.circle(60, 35)
    turtle.forward(30)
    turtle.circle(10, 180)
    turtle.forward(10)
    time.sleep(5)

# draw_snake()

def draw_star():
    turtle.screensize(800, 600)
    turtle.pensize(5)
    turtle.pencolor("red")
    for i in range(5):
        turtle.forward(150)
        turtle.right(144)
    time.sleep(5)

# draw_snake()
draw_star()
draw_snake()
# the_num = random.randint(1, 100)
# sign = True
# for i in range(1, 7):
#     print("第{}次猜测".format(i))
#     user_num = int(input("请猜测一个1-100的数字\n"))
#     if user_num > the_num:
#         print("你猜错了， 太大了")
#         continue
#     elif user_num < the_num:
#         print("你猜错了，太小了")
#         continue
#     else:
#         print("你猜对了")
#         sign = False
#         draw_star()
#         break
# if sign:
#     draw_snake()

