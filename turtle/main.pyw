import turtle
import random


class App(turtle.Turtle):
    def __init__(self):
        super().__init__()




class Rue(turtle.Turtle):
    def __init__(self, nombre:int):
        """ affiche la rue avec nombre le numero de la rue """
        self.nombre_immeubles = 5
        self.immeuble = Immeuble()
        self.decalage = nombre * 50

    def draw(self):
        for i in range(self.nombre_immeubles - 1):
            self.immeuble.draw()






class Immeuble(turtle.Turtle):
    def __init__(self):
        """initialise les parametres d'unimmeuble"""
        self.hauteur_etage = 60
        self.largeur_etage = 140


    def draw(self):
        self.couleur = f"#{random.random()}{random.random()}{random.random()}"
        for _ in range(random.randint(1, 5)):
            etage = Etage(self)
            etage.draw()





class Etage(turtle.Turtle):
    def __init__(self, parent):
        self.couleur = parent.couleur

    def draw(self):
        self.begin_fill(self.couleur)
        self.forward(60)
        self.left(90)
        self.forward(140)
        self.left(90)
        self.forward(60)
        self.left(90)
        self.forward(140)

        



class Fenetre(turtle.Turtle):
    def __init__(self):
        self.taille = 30
    
    def draw_etage(self):
        """ dessine un etage de fenetres """
        self.left(90)
        self.forward(15)

    def drawn_fenetre(self):
        self.pendown()
        for _ in range(4):
            self.forward(self.width)
            self.left(90)





App()
turtle.exitonclick()