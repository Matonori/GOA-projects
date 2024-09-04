from turtle import*
speed (0)
width (4)
def drawsquare():
    pendown
    for i in range(4):
        forward(200)
        left(90)
drawsquare()

def move_pen(x, y):
    penup
    goto(x, y)

move_pen(0, -230)
drawsquare()

move_pen(-300, -230)
drawsquare()

move_pen(-300, 0)
drawsquare()

    
    
exitonclick()