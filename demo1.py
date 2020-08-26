# print("Hi,this is Python 365.")
# name = input("May I know your name?")
# print("Welcome,{}!".format(name))
# a = input("请输入第一个数字")
# # b = input("请输入第二个数字")
# # s = float(a) + float(b)
# # print("{0}+{1}={2}".format(a,b,s))
# import  math
# num = input("请输入一个数字")
# num_sqrt = pow(float(num),0.5)
# print("{0:0.5f}是{1}的平方根".format(num_sqrt,num))
# 1，计算机三角形面积（海伦公式）

# # 计算三角形变长
# s = ( a + b + c) / 2
# # 计算面积
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print('三角形面积为{:0.2f}'.format(area))
# 2，计算三角形面积（内角计算）
# import math
# a = float(input('请输入三角形第一条边长： '))
# b = float(input('请输入三角形第二条边长： '))
# c = float(input('请输入三角形第三条边长： '))
# cos_A = (b**2+c**2-a**2)/(2*b*c)
# cos_B = (a**2+c**2-b**2)/(2*a*c)
# cos_C = (a**2+b**2-c**2)/(2*a*b)
# A = int(math.degrees(math.acos(cos_A)))
# B = int(math.degrees(math.acos(cos_B)))
# C = int(math.degrees(math.acos(cos_C)))
# print(A,B,C)
# import turtle
# turtle.fillcolor("lightgreen")
# turtle.speed(0.1)
# turtle.begin_fill()
# turtle.forward(c*20)# 绘制线
# turtle.left(180-B)
# turtle.forward(a*20)
# turtle.left(180-C)
# turtle.forward(b*20)
# turtle.delay(500)
# turtle.end_fill()
# import math
# a=float(input("请输入长方形的长： "))
# b=float(input("请输入长方形的宽： "))
# # 计算面积
# area = a*b
# print('长方形的面积为{:0.3f}'.format(area))
# import turtle
# turtle.screensize(500,500,"lightgreen")
# turtle.fillcolor("yellow")
# turtle.shape("blue")
# turtle.speed(1)
# turtle.begin_fill()
# turtle.forward(a*20)
# turtle.left(90)
# turtle.forward(b*20)
# turtle.left(90)
# turtle.forward(a*20)
# turtle.left(90)
# turtle.forward(b*20)
# turtle.delay(1000)
# turtle.begin_end()
# !/usr/bin/env python
# coding:utf-8

from turtle import *
import time


def setTurtle():
    # 窗口大小
    screensize(900, 700, 'pink')
    # 颜色
    color('red', 'pink')
    # 笔粗细
    pensize(3)
    # 速度
    speed(6)
    # 提笔
    penup()


def getStart(h):
    # 去到的坐标,窗口中心为0,0
    goto(0, -180)
    r = h / 5
    drawBigL(r, h)
    drawBigArc(r, 140)
    drawBigArc(r, 70)
    drawBigR(r, h)
    centerRange()
    drawHope()
    drawName()


def drawBigL(r, h):
    colors = ['red', 'orange', 'yellow', '#87CEEB', 'violet', 'red']
    for i in range(int(240 / h) + 1):
        seth(0)
        color(colors[i], colors[i + 1])
        drawHeart(r)
        seth(140)
        fd(h)


def drawBigArc(r, rad):
    colors = ['red', 'orange', 'yellow', 'SkyBlue', 'violet', 'red']
    for i in range(50):
        if (i % 10 == 0):
            color(colors[int(i / 10)], colors[int(i / 10) + 1])
            seth(0)
            drawHeart(r)
            seth(rad - (i + 1) * 4)
        rt(4)
        fd(10.5)


def drawBigR(r, h):
    colors = ['red', 'orange', 'yellow', 'SkyBlue', 'violet', 'red']
    for i in range(int(240 / h) + 1):
        color(colors[i], colors[i + 1])
        seth(0)
        drawHeart(r)
        setheading(220)
        fd(h)


def drawHeart(r):
    down()
    begin_fill()
    factor = 180
    seth(45)
    circle(-r, factor)
    fd(2 * r)
    right(90)
    fd(2 * r)
    circle(-r, factor)
    end_fill()
    up()


# 在心中写字
def centerRange():
    for i in range(6):
        drawCenter(i)
        time.sleep(1)


def drawCenter(i):
    goto(0, 0)
    colors = ['red', 'orange', 'yellow', 'SkyBlue', 'violet', 'red']
    pencolor(colors[i])
    # 在心中写字 font可以设置字体自己电脑有的都可以设 align开始写字的位置
    # write('love ...', font=('gungsuh', 30,), align="center")
    up()


# 写寄语
# def drawHope():
#     pencolor('black')
#     goto(-300, -220)
#     showturtle()
#     write('，', font=('华文行楷', 25,), align="center", move=True)
#     goto(-300, -270)
#     write('也没有我想你那么想。', font=('华文行楷', 25,), align="center", move=True)


# 写署名
def drawName():
    pencolor('black')
    goto(250, -250)
    showturtle()
    write('付常乐 qq：876274474', font=('gungsuh', 20,), align="center", move=True)


setTurtle()
getStart(80)

# 点击窗口关闭
window = Screen()
window.exitonclick()