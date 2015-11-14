import turtle


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    patrick = init_turtle("turtle", "yellow", 10)

    # draw_square(patrick)
    draw_square_circle(patrick)

    # angie = init_turtle("arrow", "blue", 2)
    # angie.circle(100)
    window.exitonclick()


def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_square_circle(some_turtle):
    for i in range(37):
        draw_square(some_turtle)
        some_turtle.right(10)


def draw_fractal_main():
    window = turtle.Screen()
    window.bgcolor("red")

    t = init_turtle("arrow", "green", 0)
    length = 256

    # init start position
    t.left(60)

    # draw triple triangle
    draw_fractal(t, length, 6)

    window.exitonclick()


def init_turtle(shape, color, speed):
    temp = turtle.Turtle()
    temp.shape(shape)
    temp.color(color)
    temp.speed(speed)
    return temp


# Smallest level = 1
def draw_fractal(some_turtle, length, level):
    if level > 0:

        # draw the first triangle / fractal
        if level == 1:
            draw_triangle(some_turtle, length)
        else:
            draw_fractal(some_turtle, length / 2, level - 1)

        # Position for 2nd triangle
        some_turtle.forward(length)

        # draw second triangle / fractal
        if level == 1:
            draw_triangle(some_turtle, length)
        else:
            draw_fractal(some_turtle, length / 2, level - 1)

        # Positiion for 3rd triangle
        some_turtle.right(120)
        some_turtle.forward(length)
        some_turtle.left(120)

        # draw third triangle / fractal
        if level == 1:
            draw_triangle(some_turtle, length)
        else:
            draw_fractal(some_turtle, length / 2, level - 1)

        # go back original position
        some_turtle.left(120)
        some_turtle.forward(length)
        some_turtle.right(120)


def draw_triangle(some_turtle, length):
    for i in range(3):
        some_turtle.forward(length)
        some_turtle.right(120)


draw_fractal_main()
