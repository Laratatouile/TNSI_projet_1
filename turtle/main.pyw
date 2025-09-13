from turtle import *
import fonctions.formes as formes
import objets.Immeuble as immeuble
import math


def lancement() -> None:
    """ pos_x est la position a gauche de la fenetre pour permettre de se reperer """

    # definir les parametres de base de l'ecran
    screen = Screen()
    screen.setup(width=1050, height=525)
    screen.setworldcoordinates(0, 0, 1400, 700)

    # initialiser la turtle
    penup()
    tracer(False)
    hideturtle()
    speed(0)

    # definir l'arriere plan
    formes.rectangle(-100, -100, 1000000, 250, "#13721e", True, "#13721e")
    bgcolor("#98d1e9")

    # definir la turtle du soleil
    soleil = Turtle()
    soleil.hideturtle()

    global arret_deplacement
    arret_deplacement = False

    num_boucle = 0
    boucle(soleil, num_boucle, screen)
    mainloop()



def boucle(soleil, num_boucle:int, screen) -> None:
    global arret_deplacement
    arret_deplacement = True
    rue(num_boucle)

    if num_boucle % 2 == 0:
        bgcolor("#98d1e9")
    else :
        bgcolor("#000000")
    
    update()

    soleil_obj(num_boucle*1400, soleil, (num_boucle+1)*1400, screen, ("soleil" if num_boucle % 2 == 0 else "lune"))

    num_boucle += 1

    arret_deplacement = False
    deplacement_camera(num_boucle, -200)
    
    screen.ontimer(lambda:boucle(soleil, num_boucle, screen), int(1.4e4))




def rue(nombre:int):
    """ affiche la rue avec nombre le numero de la rue """
    nombre_immeubles = 5
    decalage = nombre * 1400
    decalage_cote = 150
    decalage_batiments = 100
    width_batiment = 140


    for i in range(nombre_immeubles):
        immeuble.immeuble(decalage+decalage_cote+i*(decalage_batiments+width_batiment))



# le soleil
def soleil_obj(x:int, soleil, fin:int, screen, type:str) -> None:
    """ fait bouger le soleil et la lune """
    if x < fin:
        # effacer l'ancien soleil
        soleil.clear()
        

        # afficher le nouveau
        if type == "soleil":
            formes.cercle(x+50, fonction_soleil_lune(x), 25, "#e2d257", True, "#ffe312", soleil)
        elif type == "lune":
            formes.cercle(x+50, fonction_soleil_lune(x), 25, "#555555", True, "#c1c1c1", soleil)


        screen.ontimer(lambda:soleil_obj(x+6, soleil, fin, screen, type), 20)




def fonction_soleil_lune(x:int) -> int:
    """ calcule l'arc de cercle du soleil """
    return 250 * abs(math.sin((math.pi*x)/1400)) + 400




def deplacement_camera(i:int, decalage:int) -> None:
    """ deplace la camera """
    global arret_deplacement
    if arret_deplacement:
        print("arret du deplacement pour ne pas gener l'utilisateur")
    elif 0 < decalage < 1400:
        setworldcoordinates((i-1)*1400+decalage, 0, (i)*1400+decalage, 700)
        update()
        ontimer(lambda:deplacement_camera(i, decalage+4), 1)
    elif decalage <= 0:
        ontimer(lambda:deplacement_camera(i, decalage+4), 1)



lancement()