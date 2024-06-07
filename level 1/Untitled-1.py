from turtle import *
#walls
width(7)
begin_fill()
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#door
begin_fill()
forward(70)
left(90)

color("orange")
forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()
#moving the turtle
penup()

goto(200, 200)

pendown()

#roof
begin_fill()
color("blue")

right(150)
forward(200)

left(120)
forward(200)
end_fill()

#left window
speed(1)
penup()

goto(50, 150)
pendown()

begin_fill()

right(150)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

end_fill()

#right window
penup()

goto(110, 150)
pendown()

begin_fill()

right(180)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill()





exitonclick 