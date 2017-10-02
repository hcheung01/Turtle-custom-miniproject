import turtle



def draw_letter():
    window = turtle.Screen()
    window.bgcolor("yellow")

    mom = turtle.Turtle()
    mom.shape("turtle")
    mom.color("blue")
    mom.speed(1)

    mom.right(90)
    mom.forward(200)
    mom.backward(100)
    mom.left(45)
    mom.forward(120)
    mom.backward(120)
    mom.left(90)
    mom.forward(120)

    mom.color("yellow")
    mom.right(45)
    mom.forward(100)
    mom.color("blue")
    mom.forward(100)
    mom.backward(100)
    mom.right(90)
    mom.forward(200)
    mom.left(90)
    mom.forward(100)






    window.exitonclick()

draw_letter()
