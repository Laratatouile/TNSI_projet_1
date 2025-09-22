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





# le soleil et la lune
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
    