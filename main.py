import turtle
from turtle import Turtle, TurtleScreen
import colorgram
from random import choice

def getColorTuple(inputColor):
    colorTuple = (inputColor.rgb.r, inputColor.rgb.g, inputColor.rgb.b)
    return colorTuple

colors = colorgram.extract('spots.jpeg',20)

spotColors = []

for i in range(len(colors)):
    spotColors.append(getColorTuple(colors[i]))


mickey = Turtle()
mickey_window = turtle.Screen()
turtle.colormode(255)
mickey_window.screensize(300,300)



def draw_spot():
    mickey.penup()
    while mickey.ycor() < 300:
        while mickey.xcor() < 300:
            mickey.dot(20, choice(spotColors))
            mickey.setposition(mickey.xcor()+30, mickey.ycor())
        mickey.setposition(-300, mickey.ycor()+30)


for i in range(10):
    mickey.penup()
    mickey.setposition(-300, -300)
    draw_spot()

# print(mickey_window.screensize())
# mickey.penup()
# mickey.setposition((5,5))
# mickey.dot(20,(249,248,248))
# mickey.setposition((350,250))
# mickey.dot(20,(249,248,248))



mickey_window.exitonclick()







# --------



#
# from random import choice, randint
#
# theTurtle = Turtle()
# theTurtleWindow = Screen()
# colormode(255)
#
# inkColor = ['lime green', 'royal blue', 'peru', 'light salmon', 'chocolate', 'peach puff', 'blue violet', 'magenta']
# directions = [0, 90, 180, 270]
#
# # Drawing a Dashed Line
# # for i in range(10):
# #     if i % 2 == 0:
# #         theTurtle.pendown()
# #         theTurtle.forward(5)
# #     else:
# #         theTurtle.penup()
# #         theTurtle.forward(5)
#
#
# # def randomWalk(color):
# #     theTurtle.pencolor(color)
# #     theTurtle.setheading(choice(directions))
# #     theTurtle.forward(25)
# #
# # for i in range(200):
# #     theTurtle.speed(9)
# #     theTurtle.pensize(15)
# #     randColor = (randint(1,255),randint(1,255),randint(1,255))
# #     print(randColor)
# #     randomWalk(randColor)
#
# theTurtle.speed(10)
#
# def drawcircle(angle):
#     theTurtle.setheading(angle)
#     theTurtle.circle(100)
#
#
# circleAngle = 0
#
# while circleAngle < 360:
#     drawcircle(circleAngle)
#     circleAngle += 3
#
#
#
#
#
#
# # TotalDegree = 360
# # sides = 0
# # angle = 0
# #
# # for i in range(10):
# #     sides = i + 3
# #     angle = TotalDegree / sides
# #     for j in range(sides):
# #         theTurtle.forward(25)
# #         theTurtle.left(angle)
# #         theTurtle.



# theTurtleWindow.exitonclick()
