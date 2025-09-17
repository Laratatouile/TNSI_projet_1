import turtle



def carre(x:int, y:int, cote:int, color:str, fill:bool=False, fill_color:str="#ffffff", turtle=turtle) -> None:
    """ dessine un carre """
    turtle.goto(x, y)
    turtle.pencolor(color)
    turtle.pendown()
    if fill:
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
    turtle.setheading(0)
    for _ in range(4):
        turtle.forward(cote)
        turtle.left(90)
    if fill:
        turtle.end_fill()
    turtle.penup()
    turtle.update()
    return None



def rectangle(x:int, y:int, width:int, height:int, color:str, fill:bool=False, fill_color:str="#ffffff", turtle=turtle) -> None:
    """ dessine un rectangle """
    turtle.goto(x, y)
    turtle.pencolor(color)
    turtle.pendown()
    if fill:
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
    turtle.setheading(0)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    if fill:
        turtle.end_fill()
    turtle.penup()
    turtle.update()
    return None
    


def cercle(x:int, y:int, radius:int, color:str, fill:bool=False, fill_color:str="#ffffff", turtlle=turtle) -> None:
    """ dessine un cercle """
    turtlle.setheading(90)
    turtlle.goto(x - radius, y)
    turtlle.pencolor(color)
    turtlle.pendown()
    if fill:
        turtlle.fillcolor(fill_color)
        turtlle.begin_fill()
    turtlle.circle(radius)
    if fill:
        turtlle.end_fill()
    turtlle.penup()
    turtle.update()
    return None
    


def triangle(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int, color:str, fill:bool=False, fill_color:str="#ffffff", turtle=turtle) -> None:
    """ dessine un triangle """
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    if fill:
        turtle.fillcolor(fill_color)
        turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    if fill:
        turtle.end_fill()
    turtle.penup()
    turtle.update()



def ligne(x1:int, y1:int, x2:int, y2:int, color:str, turtle=turtle) -> None:
    """ trace une ligne en x1, y1, x2, y2 """
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)
    turtle.penup()



def trace_porte_arrondie(x, y, color:str, fill_color:str, turtle=turtle):
    turtle.goto(x, y+35)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(35)
    turtle.left(90)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(35)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.update()
    return None