import turtle as t
jam = t.Turtle()
screen = t.Screen()
is_over = True


def forward():
    jam.forward(10)


def backward():
    jam.backward(10)


def clockwise():
    new = jam.heading()+10
    jam.setheading(new)


def anticlockwise():
    new = jam.heading() - 10
    jam.setheading(new)


def clear():
    jam.clear()
    jam.penup()
    jam.setpos(0, 0)
    jam.down()


screen.listen()
screen.onkey(fun=forward, key='w')
screen.onkey(fun=backward, key='s')
screen.onkey(fun=anticlockwise, key='a')
screen.onkey(fun=clockwise, key='d')
screen.onkey(fun=clear, key='c')
screen.exitonclick()
