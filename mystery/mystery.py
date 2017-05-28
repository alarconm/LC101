import turtle

def mystery_turtle():
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-300, -300, 300, 300)
    directions = open("mystery.txt", "r")

    for line in directions:
        aline = line.split()
        if aline[0] == "UP":
            t.penup()
        elif aline[0] == "DOWN":
            t.pendown()
        else:
            t.goto(int(aline[0]), int(aline[1]))
     
    wn.exitonclick()

mystery_turtle()