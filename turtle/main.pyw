import turtle


class App(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hauteur_etage = 60
        self.largeur_etage = 140


        



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