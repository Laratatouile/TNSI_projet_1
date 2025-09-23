import random
import fonctions.formes as formes
from turtle import *



def immeuble(x:int):
    """ charge les variables de la fonction """

    couleur = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    nombre_etages = random.randint(1, 5)

    for i in range(nombre_etages):
        etage(x, i, couleur)
    toit(x, nombre_etages)






def etage(x:int, numero_etage:int, couleur_etage:str):
    """ dessine un etage """
    height = 60
    width = 140
    hauteur_rue = 150


    formes.rectangle(x,
                        numero_etage * height + hauteur_rue,
                        width,
                        height,
                        "#000000",
                        True,
                        couleur_etage)
    if numero_etage == 0:
        position_porte = random.randint(0, 2)
        for i in range(3):
            if i == position_porte:
                porte(x, numero_etage*height+hauteur_rue, i)
                continue
            fenetre(x, numero_etage*height+hauteur_rue, i)
    else:
        for i in range(3):
            type_fenetre = random.randint(0, 1)
            if type_fenetre == 0:
                fenetre(x, numero_etage*height+hauteur_rue, i)
            else:
                balcon(x+15+i*40, numero_etage*height+hauteur_rue)






def fenetre(x:int, y:int, nombre_fenetre:int):
    """ dessine la fenetre """
    taille = 30
    decalage_mur = 15
    decalage_objets = 10
    decalage_hauteur = 20
    couleur = "#3799c3"


    decalage_x = decalage_mur + nombre_fenetre*(decalage_objets + taille)
    formes.carre(x + decalage_x,
                    y+decalage_hauteur,
                    taille,
                    "#000000",
                    True,
                    couleur)
        


def creer_forme_balcon():
    """ cree une forme pour le balcon """
    balcon_shape = Shape("compound")

    # fenêtre (rectangle rempli bleu)
    fenetre = ((0,0), (23,0), (23,36), (0,36))
    balcon_shape.addcomponent(fenetre, "#3799c3", "black")

    # barre horizontale du balcon
    barre = ((-3,22),(27,22))
    balcon_shape.addcomponent(barre, "black", "black")

    # barres verticales 
    for i in range(0,33,3):
        barre_v = ((-3+i,22), (-3+i,0))
        balcon_shape.addcomponent(barre_v, "black", "black")

    # on enregistre la forme
    register_shape("balcon", balcon_shape)  



def balcon(x:int, y:int):
    """ dessine un balcon """
    setheading(90)
    shape("balcon")
    goto(x, y)
    stamp()


def porte(x:int, y:int, nombre_fenetre:int) -> None:
    """ dessine la porte """
    height = 50
    width = 30
    decalage_mur = 15
    decalage_objets = 10
    clanche_x1 = 23
    clanche_x2 = 28
    clanche_y = 20

    couleur = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    type_porte = random.randint(0, 1)

    if type_porte == 0:
        formes.rectangle(x+decalage_mur+(nombre_fenetre*(width+decalage_objets)), y, width, height, "#000000", True, couleur)
    elif type_porte == 1:
        formes.trace_porte_arrondie(x+decalage_mur+(nombre_fenetre*(width+decalage_objets)), y, "#000000", couleur)
    # clanche
    formes.ligne(x+decalage_mur+(nombre_fenetre*(width+decalage_objets))+clanche_x1,
                 y+clanche_y,
                 x+decalage_mur+(nombre_fenetre*(width+decalage_objets))+clanche_x2,
                 y+clanche_y,
                 "#000000")









def toit(x:int, nombre_etages:int):
    """ dessine un toit sur l'immeuble """
    couleur = "#851a29"
    width_etage = 140
    height_etage = 60
    depassement_cote = 20
    hauteur_rectangulaire_base = 15
    hauteur_rectangulaire_haut = 10
    hauteur_rue = 150
    hauteur_triangle = 30


    type_toit = random.randint(0, 1)
    # toit rectangulaire
    if type_toit == 0:
        formes.rectangle(x,
                            nombre_etages*height_etage + hauteur_rue,
                            width_etage,
                            hauteur_rectangulaire_base,
                            "#000000",
                            True,
                            couleur)
        formes.rectangle(x - depassement_cote,
                            nombre_etages*height_etage + hauteur_rectangulaire_base + hauteur_rue,
                            width_etage + 2*depassement_cote,
                            hauteur_rectangulaire_haut,
                            "#000000",
                            True,
                            couleur)
    # toit triangulaire
    if type_toit == 1:
        formes.rectangle(x,
                            nombre_etages*height_etage + hauteur_rue,
                            width_etage,
                            hauteur_rectangulaire_base,
                            "#000000",
                            True,
                            couleur)
        formes.triangle(x-depassement_cote,
                        nombre_etages*height_etage + hauteur_rectangulaire_base + hauteur_rue,
                        x+width_etage//2,
                        nombre_etages*height_etage + hauteur_rectangulaire_base + hauteur_rue + hauteur_triangle,
                        x+width_etage + depassement_cote,
                        nombre_etages*height_etage + hauteur_rectangulaire_base + hauteur_rue,
                        "#000000",
                        True,
                        couleur)
        



creer_forme_balcon()