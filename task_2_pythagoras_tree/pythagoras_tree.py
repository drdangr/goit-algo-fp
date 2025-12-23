import turtle


def draw_tree(branch_length, level):
    if level == 0:
        return

    turtle.forward(branch_length)

    turtle.left(45)
    draw_tree(branch_length * 0.7, level - 1)

    turtle.right(90)
    draw_tree(branch_length * 0.7, level - 1)

    turtle.left(45)
    turtle.backward(branch_length)


def main():
    level = int(input("Введіть рівень рекурсії: "))
    
    screen = turtle.Screen()
    screen.setup(width=800, height=800)

    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -180)
    turtle.pendown()

    draw_tree(180, level)

    turtle.done()


if __name__ == "__main__":
    main()
