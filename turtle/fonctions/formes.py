from turtle import *



def carre(x:int, y:int, cote:int, color:str, fill:bool=False, fill_color:str="#ffffff") -> None:
    """ dessine un carre """
    goto(x, y)
    pencolor(color)
    pendown()
    if fill:
        fillcolor(fill_color)
        begin_fill()
    setheading(0)
    for _ in range(4):
        forward(cote)
        left(90)
    if fill:
        end_fill()
    penup()
    update()
    return None



def rectangle(x:int, y:int, width:int, height:int, color:str, fill:bool=False, fill_color:str="#ffffff") -> None:
    """ dessine un rectangle """
    goto(x, y)
    pencolor(color)
    pendown()
    if fill:
        fillcolor(fill_color)
        begin_fill()
    setheading(0)
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    if fill:
        end_fill()
    penup()
    update()
    return None
    


def cercle(x:int, y:int, radius:int, color:str, fill:bool=False, fill_color:str="#ffffff") -> None:
    """ dessine un cercle """
    setheading(90)
    goto(x - radius, y)
    pencolor(color)
    pendown()
    if fill:
        fillcolor(fill_color)
        begin_fill()
    circle(radius)
    if fill:
        end_fill
    penup()
    update()
    return None
    


def triangle(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int, color:str, fill:bool=False, fill_color:str="#ffffff") -> None:
    """ dessine un triangle """
    goto(x1, y1)
    pendown()
    pencolor(color)
    if fill:
        fillcolor(fill_color)
        begin_fill()
    goto(x2, y2)
    goto(x3, y3)
    goto(x1, y1)
    if fill:
        end_fill()
    penup()
    update()



def ligne(x1:int, y1:int, x2:int, y2:int, color:str) -> None:
    """ trace une ligne en x1, y1, x2, y2 """
    goto(x1, y1)
    pendown()
    pencolor(color)
    goto(x2, y2)
    penup()



def trace_porte_arrondie(x, y, color:str, fill_color:str):
    goto(x, y+35)
    pendown()
    setheading(-90)
    fillcolor(fill_color)
    begin_fill()
    circle(15)
    end_fill()
    penup()
    goto(x, y)
    pencolor(color)
    pendown()
    begin_fill()
    setheading(0)
    forward(30)
    left(90)
    forward(35)
    left(90)
    forward(30)
    left(90)
    forward(35)
    left(90)
    end_fill()
    penup()
    update()
    return None