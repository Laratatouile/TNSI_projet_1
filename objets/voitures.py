import time
import random
from turtle import *


def voitures(heure_depart:float, t_voiture:Turtle, screen, liste_voitures:list=[[], []]) -> None:
    """ affiche les voitures """
    # variables
    proba_voiture = [5, 100]
    v_voiture = 5


    # definition des points ecrates le plus proche possible de la camera pour eviter le lag
    x_instant = round((time.time() - heure_depart) //8 * 1400)
    x_min = x_instant - 20
    x_max = x_min + 2800


    # verifier et generer les voitures sur la ligne du dessus
    if liste_voitures[0] != []:
        if not x_max - liste_voitures[0][-1] < 175:
            # generer aleatoirement une voiture
            if random.choice(range(proba_voiture[1])) < proba_voiture[0]:
                liste_voitures[0].append(x_max-5)
    else:
        if random.choice(range(proba_voiture[1])) < proba_voiture[0]:
            liste_voitures[0].append(x_max-5)
    # la ligne du dessous
    if liste_voitures[1] != []:
        if not x_min - liste_voitures[1][-1] < 175:
            # generer aleatoirement une voiture
            if random.choice(range(proba_voiture[1])) < proba_voiture[0]:
                liste_voitures[1].append(x_min+5)
    else:
        if random.choice(range(proba_voiture[0])) < proba_voiture[0]:
            liste_voitures[1].append(x_min+5)

            

    # supprimer les voitures si il y a des voitures
    if liste_voitures[0] != []:
        for i in reversed(range(len(liste_voitures[0]))):
            if not x_min < liste_voitures[0][i] < x_max:
                liste_voitures[0].pop(i)
    if liste_voitures[1] != []:
        for i in reversed(range(len(liste_voitures[1]))):
            if not x_min < liste_voitures[1][i] < x_max:
                liste_voitures[1].pop(i)

    # tout clear
    t_voiture.clear()


    # dessiner les voitures
    for i in range(len(liste_voitures[0])):
        liste_voitures[0][i] -= v_voiture
        t_voiture.shape("./turtle/images/voiture.gif")
        t_voiture.goto(liste_voitures[0][i], 120)
        t_voiture.stamp()
    for i in range(len(liste_voitures[1])):
        liste_voitures[1][i] += v_voiture
        t_voiture.shape("./turtle/images/voiture.gif")
        t_voiture.goto(liste_voitures[1][i], 85)
        t_voiture.stamp()


    screen.ontimer(lambda:voitures(heure_depart, t_voiture, screen, liste_voitures), 1)
