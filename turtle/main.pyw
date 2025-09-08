from turtle import *
import fonctions.formes as formes
import objets.Immeuble as immeuble



def lancement(pos_x:int):
    """ pos_x est la position a gauche de la fenetre pour permettre de se reperer """
    screen = Screen()
    screen.setup(width=1050, height=525)
    screen.setworldcoordinates(0, 0, 1400, 700)
    penup()
    speed(0)


    formes.rectangle(-100, -100, 1000000, 250, "#13721e", True, "#13721e")
    formes.rectangle(-100, 150, 1000000, 1000, "#98d1e9", True, "#98d1e9")

    rue = Rue(0)
    rue.draw()

    goto(0, -1000)





class Rue():
    def __init__(self, nombre:int):
        """ affiche la rue avec nombre le numero de la rue """
        self.nombre_immeubles = 5
        self.immeuble = immeuble.Immeuble()
        self.decalage = nombre * 1400
        self.decalage_cote = 150
        self.decalage_batiments = 100
        self.width_batiment = 140

    def draw(self):
        for i in range(self.nombre_immeubles):
            self.immeuble.draw(self.decalage+self.decalage_cote+i*(self.decalage_batiments+self.width_batiment))








lancement(0)
exitonclick()