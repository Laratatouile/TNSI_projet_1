import fonctions.formes as formes
from turtle import *
import time
import math




# les dessins de base
def dessin_base(x:int):
    formes.rectangle(x-100, -100, x+20000, 250, "#13721e", True, "#13721e")
    formes.rectangle(x-100, 35, x+20000, 100, "#323232", True, "#323232")
    for i in range(1000):
        formes.ligne(i*20, 85, i*20+10, 85, "#adadad")




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
    return 400 + abs(250 * math.sin(math.pi * x / 1400 ))




# les lampadaires
def lampadaire(i:int) -> None:
    """ dessine les lampadaires """
    for k in range(6):
        dessin_lampadaire(i*1400+100+k*240)


def dessin_lampadaire(x:int) -> None:
    """ dessine un lampadaire a x """
    formes.ligne(x, 230, x, 150, "#606060")
    formes.triangle(x-3, 230, x+3, 230, x, 235, "#606060", True, "#606060")
    