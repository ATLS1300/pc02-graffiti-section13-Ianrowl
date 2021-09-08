#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

turtle.speed(10)

turtle.up()
turtle.goto(10,11)
turtle.setheading(280)
turtle.down()

turtle.fillcolor("white")
turtle.begin_fill()

turtle.forward(26)
turtle.left(145)
turtle.forward(15)
turtle.right(125)
turtle.forward(15)
turtle.left(130)
turtle.forward(15)
turtle.right(125)
turtle.forward(15)
turtle.setheading(100)
turtle.forward(28)
turtle.goto(10,11)

turtle.end_fill()

turtle.up()
turtle.goto(15,8)
turtle.setheading(280)
turtle.down()
turtle.color("gray")
turtle.forward(13)

turtle.up()
turtle.goto(25,9.8)
turtle.setheading(281)
turtle.down()
turtle.color("gray")
turtle.forward(13)

turtle.up()
turtle.goto(34,11.5)
turtle.setheading(281)
turtle.down()
turtle.color("gray")
turtle.forward(12.5)


turtle.up()
turtle.goto(111,-90)
turtle.setheading(335)
turtle.down()

turtle.color("yellow")
turtle.pensize(2.5)
turtle.forward(15)
turtle.right(27)
turtle.forward(7)
turtle.left(52)
turtle.forward(14)
turtle.right(39)
turtle.forward(5)
turtle.left(48)
turtle.forward(13)
turtle.right(41)
turtle.forward(8)
turtle.left(37)
turtle.forward(17)
turtle.right(28)
turtle.forward(6)
turtle.left(22)
turtle.forward(4)
turtle.right(45)
turtle.forward(20)
turtle.left(32)
turtle.forward(18)
turtle.right(52)
turtle.forward(6)
turtle.left(40)
turtle.forward(9)
turtle.left(48)
turtle.forward(19)
turtle.right(27)
turtle.forward(12)
turtle.right(37)
turtle.forward(8)
turtle.left(43)
turtle.forward(7)
turtle.right(36)
turtle.forward(16)
turtle.left(37)
turtle.forward(9)
turtle.right(46)
turtle.forward(17)
turtle.right(29)
turtle.forward(8)
turtle.left(61)
turtle.forward(18)
turtle.left(36)
turtle.forward(12)
turtle.right(56)
turtle.forward(9)
turtle.right(35)
turtle.forward(6)
turtle.left(70)
turtle.forward(15)

turtle.up()
turtle.goto(124,-100)
turtle.setheading(296)
turtle.pensize(1.5)
turtle.down()
turtle.forward(10)
turtle.left(43)
turtle.forward(5)
turtle.right(32)
turtle.forward(8)
turtle.left(57)
turtle.forward(4)

turtle.up()
turtle.goto(152,-99)
turtle.setheading(32)
turtle.down()
turtle.forward(11)
turtle.right(36)
turtle.forward(8)
turtle.left(28)
turtle.forward(4)

turtle.up()
turtle.goto(205,-113)
turtle.setheading(35)
turtle.down()
turtle.forward(11)
turtle.right(37)
turtle.forward(8)
turtle.right(45)
turtle.forward(5)

turtle.up()
turtle.goto(248,-138)
turtle.setheading(330)
turtle.down()
turtle.forward(14)
turtle.right(22)
turtle.forward(5)
turtle.right(31)
turtle.forward(7)
turtle.left(58)
turtle.forward(11)
turtle.left(30)
turtle.forward(6)
turtle.right(52)
turtle.forward(9)

turtle.up()
turtle.goto(321,-153)
turtle.setheading(15)
turtle.down()
turtle.forward(14)
turtle.right(37)
turtle.forward(9)
turtle.left(41)
turtle.forward(8)
turtle.right(42)
turtle.forward(6)

turtle.color("black")
turtle.fillcolor("pink")
turtle.pensize(2.5)
turtle.begin_fill()

turtle.up()
turtle.goto(-95,167)
turtle.setheading(75)
turtle.down()
turtle.forward(141)
turtle.setheading(311)
turtle.forward(145)
turtle.goto(-95,167)

turtle.end_fill()

turtle.color("black")
turtle.fillcolor("white")
turtle.pensize(1)
turtle.begin_fill()

turtle.up()
turtle.goto(-81,181)
turtle.down()
turtle.circle(6)
turtle.end_fill()

turtle.end_fill()

turtle.begin_fill()

turtle.up()
turtle.goto(-75,206)
turtle.down()
turtle.circle(8)
turtle.end_fill()

turtle.begin_fill()

turtle.up()
turtle.goto(-53,195)
turtle.down()
turtle.circle(16)
turtle.end_fill()

turtle.begin_fill()

turtle.up()
turtle.goto(-45,235)
turtle.down()
turtle.circle(14)
turtle.end_fill()

turtle.begin_fill()

turtle.up()
turtle.goto(-8,200)
turtle.down()
turtle.circle(10)
turtle.end_fill()

turtle.begin_fill()

turtle.up()
turtle.goto(-58,267)
turtle.down()
turtle.circle(8)
turtle.end_fill()

turtle.begin_fill()

turtle.up()
turtle.goto(-67,236)
turtle.down()
turtle.circle(7)
turtle.end_fill()

turtle.begin_fill()

turtle.up()
turtle.goto(-15,225)
turtle.down()
turtle.circle(7)
turtle.end_fill()

turtle.hideturtle()


#=======Add your code here======




#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
