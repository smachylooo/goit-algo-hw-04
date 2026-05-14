import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)

        koch_curve(t, order - 1, size / 3)
        t.right(120)

        koch_curve(t, order - 1, size / 3)
        t.left(60)

        koch_curve(t, order - 1, size / 3)

def koch_snowflake(order, size):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    screen.mainloop()

level = int(input("Enter recursion level: "))

koch_snowflake(level, 300)