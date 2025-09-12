from turtle import *
import fonctions.formes as formes
import objets.Immeuble as immeuble



def lancement(pos_x:int):
    """ pos_x est la position a gauche de la fenetre pour permettre de se reperer """
    screen = Screen()
    screen.setup(width=1050, height=525)
    screen.setworldcoordinates(0, 0, 1400, 700)
    penup()
    tracer(0, 0)
    speed(0)


    formes.rectangle(-100, -100, 1000000, 250, "#13721e", True, "#13721e")
    bgcolor("#98d1e9")
    #formes.rectangle(-100, 150, 1000000, 1000, "#98d1e9", True, "#98d1e9")

    rue(0)



def rue(nombre:int):
    """ affiche la rue avec nombre le numero de la rue """
    nombre_immeubles = 5
    decalage = nombre * 1400
    decalage_cote = 150
    decalage_batiments = 100
    width_batiment = 140


    for i in range(nombre_immeubles):
        immeuble.immeuble(decalage+decalage_cote+i*(decalage_batiments+width_batiment))





lancement(0)
goto(-100, 0)
bgcolor("#000000")
update()
exitonclick()