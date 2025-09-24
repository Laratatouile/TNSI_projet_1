import time
from turtle import *


# changement de la couleur du ciel le matin et le soir
def couleur_ciel(temps_depart:float, heure:str, screen):
    """ change la couleur du ciel le matin ou le soir """
    temps = time.time() - temps_depart
    if temps <= 5:
        ontimer(lambda:couleur_ciel(temps_depart, heure, screen), 50)
    elif 5 < temps < 8:
        couleur1 = (39, 245, 242)
        couleur2 = (0, 0, 0)
        etat_changement = (temps-5)/3
        direction = (True if heure == "jour" else False)
        couleur = _calcul_couleur(couleur1, couleur2, etat_changement, direction)
        bgcolor(couleur)
        ontimer(lambda:couleur_ciel(temps_depart, heure, screen), 1)



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
