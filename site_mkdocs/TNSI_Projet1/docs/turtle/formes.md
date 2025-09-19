# le fichier formes.pyw
## le fichier en petites etapes

### la fonction `carre`
```python
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
```
Cette fonction prend en charge une grande liste d'arguments : <br>
 - x : la position $x$ en haut a gauche du carré<br>
 - y : la position $y$ en haut a gauche du carré<br>
 - cote : la longueur d'un cote (par defaut False)<br>
 - color : la couleur du carré<br>
 - fill : un booléen qui permet de savoir si on rempli ou pas le carré<br>
 - fill_color : la couleur de remplissage (par defaut blandc)<br>
 - turtle : la turtle qui permet de dessiner le carré (par defaut la turtle de base)<br>



### la fonction `rectangle`
```python
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
```

Cette fonction prend en charge une grande liste d'arguments : <br>
 - x : la position $x$ en haut a gauche du rectangle<br>
 - y : la position $y$ en haut a gauche du rectangle<br>
 - width : la largeur du recrangle <br>
 - height : la hauteur du rectangle <br>
 - color : la couleur du rectangle<br>
 - fill : un booléen qui permet de savoir si on rempli ou pas le rectangle<br>
 - fill_color : la couleur de remplissage (par defaut blandc)<br>
 - turtle : la turtle qui permet de dessiner le rectangle (par defaut la turtle de base)<br>



### la fonction `cercle`
```python
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
```

Cette fonction prend en charge une grande liste d'arguments : <br>
 - x : la position $x$ a gauche du cercle<br>
 - y : la position $y$ a gauche du cercle<br>
 - radius : le rayon du cercle<br>
 - color : la couleur du cercle<br>
 - fill : un booléen qui permet de savoir si on rempli ou pas le cercle<br>
 - fill_color : la couleur de remplissage (par defaut blandc)<br>
 - turtle : la turtle qui permet de dessiner le cercle (par defaut la turtle de base)<br>



### la fonction `triangle`
```python
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
    return None
```

Cette fonction prend en charge une grande liste d'arguments : <br>
 - x1 : la position $x$ du premier point<br>
 - y1 : la position $y$ du premier point<br>
 - x2 : la position $x$ du deuxième point<br>
 - y2 : la position $y$ du deuxième point<br>
 - x3 : la position $x$ du troisième point<br>
 - y3 : la position $y$ du troisième point<br>
 - color : la couleur du triangle<br>
 - fill : un booléen qui permet de savoir si on rempli ou pas le triangle<br>
 - fill_color : la couleur de remplissage (par defaut blandc)<br>
 - turtle : la turtle qui permet de dessiner le triangle (par defaut la turtle de base)<br>



### la fonction `ligne`
```python
def ligne(x1:int, y1:int, x2:int, y2:int, color:str, turtle=turtle) -> None:
    """ trace une ligne en x1, y1, x2, y2 """
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2, y2)
    turtle.penup()
    return None
```

Cette fonction prend en charge une grande liste d'arguments : <br>
 - x1 : la position $x$ du premier point<br>
 - y1 : la position $y$ du premier point<br>
 - x2 : la position $x$ du deuxième point<br>
 - y2 : la position $y$ du deuxième point<br>
 - color : la couleur du triangle<br>
 - turtle : la turtle qui permet de dessiner le triangle (par defaut la turtle de base)<br>



### la fonction `trace_porte_arrondie`
```python
def trace_porte_arrondie(x:int, y:int, color:str, fill_color:str, turtle=turtle):
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
```

Cette fonction prend en charge une grande liste d'arguments : <br>
 - x : la position $x$ en bas a gauche de la porte<br>
 - y : la position $y$ en bas a gauche de la porte<br>
 - color : la couleur de la porte<br>
 - fill_color : la couleur de remplissage (par defaut blandc)<br>
 - turtle : la turtle qui permet de dessiner la porte (par defaut la turtle de base)<br>



