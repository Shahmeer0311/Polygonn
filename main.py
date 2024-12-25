import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
x = turtle.Turtle()
n = int(input("Enter sides of the polygon"))
side_length = 70
angle = 360 / n
for i in range(n): 
    x.forward(side_length)
    x.right(angle)
turtle.done()