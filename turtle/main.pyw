from turtle import *
import fonctions.formes as formes
import objets.Immeuble as immeuble
import objets.exterieur as exterieur
import math
import time


# fonction de lancement du programme
def lancement() -> None:
    """ pos_x est la position a gauche de la fenetre pour permettre de se reperer """

    # definir les parametres de base de l'ecran
    screen = Screen()
    screen.setup(width=1050, height=525)
    screen.setworldcoordinates(0, 0, 1400, 700)
    title("les immeubles de turtle")

    # initialiser la turtle
    penup()
    tracer(False)
    hideturtle()
    speed(0)

    # definir l'arriere plan
    bgcolor("#98d1e9")
    exterieur.dessin_base(0)

    # definir la turtle du soleil
    soleil = Turtle()
    soleil.hideturtle()

    i = 0

    # dessiner les bases
    rue(0)
    exterieur.lampadaire(0)

    boucle(soleil, i, screen)
    mainloop()


# la boucle princiale elle se relance toute seule avec ontimer
def boucle(soleil, i:int, screen) -> None:
    # effacer les anciens dessins pour eviter les lags importants
    if i % 10 == 0 and i != 0:
        clear()
        exterieur.dessin_base(i*1400)

    # dessiner la rue suivante
    rue(i+1)
    # dessiner les lampadaires de la rue suivante
    exterieur.lampadaire(i+1)

    if i % 2 == 0:
        exterieur.couleur_ciel(time.time(), "nuit")
    else :
        exterieur.couleur_ciel(time.time(), "jour")
    
    update()

    exterieur.soleil_obj(i, soleil, screen, ("soleil" if i % 2 == 0 else "lune"), time.time())

    i += 1

    deplacement_camera(i, time.time())

    
    screen.ontimer(lambda:boucle(soleil, i, screen), int(8e3))



# dessine une seule rue avec ses immeubles
def rue(nombre:int):
    """ affiche la rue avec nombre le numero de la rue """
    nombre_immeubles = 5
    decalage = nombre * 1400
    decalage_cote = 150
    decalage_batiments = 100
    width_batiment = 140


    for i in range(nombre_immeubles):
        immeuble.immeuble(decalage+decalage_cote+i*(decalage_batiments+width_batiment))






def deplacement_camera(i:int, temps_depart:int) -> None:
    """ deplace la camera """
    temps = time.time() - temps_depart
    if 1 < temps < 6:
        decalage = (temps - 1) * 1400 / 5
        setworldcoordinates((i-1)*1400+decalage, 0, (i)*1400+decalage, 700)
        update()
        ontimer(lambda:deplacement_camera(i, temps_depart), 1)
    elif temps <= 1:
        ontimer(lambda:deplacement_camera(i, temps_depart), 1)









lancement()