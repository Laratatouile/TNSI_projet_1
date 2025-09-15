from turtle import *
import fonctions.formes as formes
import objets.Immeuble as immeuble
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
    formes.rectangle(-100, -100, 1000000, 250, "#13721e", True, "#13721e")
    bgcolor("#98d1e9")

    # definir la turtle du soleil
    soleil = Turtle()
    soleil.hideturtle()

    i = 0
    boucle(soleil, i, screen)
    mainloop()


# la boucle princiale elle se relance toute seule avec ontimer
def boucle(soleil, i:int, screen) -> None:
    rue(i)

    if i % 2 == 0:
        couleur_ciel(time.time(), "nuit")
    else :
        couleur_ciel(time.time(), "jour")
    
    update()

    soleil_obj(i, soleil, screen, ("soleil" if i % 2 == 0 else "lune"), time.time())

    i += 1

    deplacement_camera(i, time.time())

    # effacer les anciens dessins pour eviter les lags importants
    if i % 10 == 0:
        clear()
        formes.rectangle(-100, -100, 1000000, 250, "#13721e", True, "#13721e")
    
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



# le soleil
def soleil_obj(i:int, soleil:Turtle, screen, type:str, temps:float) -> None:
    """ fait bouger le soleil et la lune """
    temps_reste = time.time() - temps
    if temps_reste <= 5:
        # effacer l'ancien soleil
        soleil.clear()
        soleil_x = (i)*1400 + temps_reste*1400 / 5
        

        # afficher le nouveau
        if type == "soleil":
            formes.cercle(soleil_x, fonction_soleil_lune(soleil_x), 25, "#e2d257", True, "#ffe312", soleil)
        elif type == "lune":
            formes.cercle(soleil_x, fonction_soleil_lune(soleil_x), 25, "#555555", True, "#c1c1c1", soleil)


        screen.ontimer(lambda:soleil_obj(i, soleil, screen, type, temps), 20)




def fonction_soleil_lune(x:int) -> int:
    """ calcule l'arc de cercle du soleil """
    return 250 * abs(math.sin((math.pi*x)/1400)) + 400




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



# changement de la couleur du ciel le matin et le soir
def couleur_ciel(temps_depart:float, heure:str):
    """ change la couleur du ciel le matin ou le soir """
    temps = time.time() - temps_depart
    if temps <= 5:
        ontimer(lambda:couleur_ciel(temps_depart, heure), 50)
    elif 5 < temps < 8:
        couleur1 = (39, 245, 242)
        couleur2 = (0, 0, 0)
        etat_changement = (temps-5)/3
        direction = (True if heure == "jour" else False)
        couleur = _calcul_couleur(couleur1, couleur2, etat_changement, direction)
        bgcolor(couleur)
        ontimer(lambda:couleur_ciel(temps_depart, heure), 1)


def _calcul_couleur(couleur1:tuple, couleur2:tuple, multiplicateur:float, direction:bool) -> str:
    """
        calcule une proportion entre la couleur 1 et 2
        multiplicateur est entre 0 et 1
        direction defini si on passe de la 1 a la 2 => True sinon false
    """
    couleur_return = ""
    for i in range(3):
        val = round((couleur1[i] - couleur2[i]) * (multiplicateur if direction else 1 - multiplicateur))
        hex_val = hex(val)[2:]  # conversion en chaîne hex sans le "0x"
        if len(hex_val) == 1:
            hex_val = "0" + hex_val
        couleur_return += hex_val
    return f"#{couleur_return}"




lancement()