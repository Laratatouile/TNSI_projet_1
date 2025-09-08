import random
import fonctions.formes as formes


class Immeuble:
    def __init__(self):
        """ charge les variables de base de la classe """
        self.height_etage = 60
        self.width_etage = 140
        self.etage = Etage()
        self.toit = Toit()


    def draw(self, x:int) -> None:
        couleur = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        nombre_etages = random.randint(1, 5)

        for i in range(nombre_etages):
            self.etage.draw(x, i, couleur)
        self.toit.draw(x, nombre_etages)







class Etage:
    def __init__(self):
        """ charge les variables de base de la classe """
        self.height = 60
        self.width = 140
        self.hauteur_rue = 150
        self.fenetre = Fenetre()
        self.porte = Porte()
        self.balcon = Balcon()


    def draw(self, x:int, numero_etage:int, couleur_etage:str):
        """ dessine l'etage a x """
        formes.rectangle(x,
                         numero_etage * self.height + self.hauteur_rue,
                         self.width,
                         self.height,
                         "#000000",
                         True,
                         couleur_etage)
        if numero_etage == 0:
            position_porte = random.randint(0, 2)
            for i in range(3):
                if i == position_porte:
                    self.porte.draw(x, numero_etage*self.height+self.hauteur_rue, i)
                    continue
                self.fenetre.draw(x, numero_etage*self.height+self.hauteur_rue, i)
        else:
            for i in range(3):
                type_fenetre = random.randint(0, 1)
                if type_fenetre == 0:
                    self.fenetre.draw(x, numero_etage*self.height+self.hauteur_rue, i)
                else:
                    self.balcon.draw(x, numero_etage*self.height+self.hauteur_rue, i)







class Fenetre:
    def __init__(self):
        """ charge les variables de base de la classe """
        self.taille = 30
        self.decalage_mur = 15
        self.decalage_objets = 10
        self.decalage_hauteur = 20
        self.couleur = "#3799c3"


    def draw(self, x:int, y:int, nombre_fenetre:int):
        """ dessine la fenetre """
        decalage_x = self.decalage_mur + nombre_fenetre*(self.decalage_objets + self.taille)
        formes.carre(x + decalage_x,
                     y+self.decalage_hauteur,
                     self.taille,
                     "#000000",
                     True,
                     self.couleur)
        



class Balcon:
    def __init__(self):
        """ charge les variables de base de la classe """
        self.fenetre_w = 30
        self.fenetre_h = 50
        self.decalage_mur = 15
        self.decalage_objets = 10
        self.couleur = "#3799c3"
        self.balcon_hauteur = 25


    def draw(self, x:int, y:int, nombre_fenetre:int):
        """ dessine la fenetre et le balcon """
        decalage_x = self.decalage_mur + nombre_fenetre*(self.decalage_objets + self.fenetre_w)
        formes.rectangle(x + decalage_x,
                        y,
                        self.fenetre_w,
                        self.fenetre_h,
                        "#000000",
                        True,
                        self.couleur)
        formes.ligne(x+decalage_x-5, y+self.balcon_hauteur, x+decalage_x+ self.fenetre_w+5, y+self.balcon_hauteur, "#000000")
        for i in range(0, 42, 3):
            formes.ligne(x+decalage_x-5+i, y+self.balcon_hauteur, x+decalage_x-5+i, y, "#000000")


        


class Porte:
    def __init__(self):
        self.height = 50
        self.width = 30
        self.decalage_mur = 15
        self.decalage_objets = 10

    def draw(self, x:int, y:int, nombre_fenetre:int) -> None:
        """ dessine la porte """
        couleur = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        formes.rectangle(x+self.decalage_mur+(nombre_fenetre*(self.width+self.decalage_objets)), y, self.width, self.height, "#000000", True, couleur)








class Toit:
    def __init__(self):
        self.couleur = "#851a29"
        self.width_etage = 140
        self.height_etage = 60
        self.depassement_cote = 20
        self.hauteur_rectangulaire_base = 15
        self.hauteur_rectangulaire_haut = 10
        self.hauteur_rue = 150
        self.hauteur_triangle = 30


    def draw(self, x:int, nombre_etages:int):
        """ dessine un toit sur l'immeuble """
        type_toit = random.randint(0, 1)
        # toit rectangulaire
        if type_toit == 0:
            formes.rectangle(x,
                             nombre_etages*self.height_etage + self.hauteur_rue,
                             self.width_etage,
                             self.hauteur_rectangulaire_base,
                             "#000000",
                             True,
                             self.couleur)
            formes.rectangle(x - self.depassement_cote,
                             nombre_etages*self.height_etage + self.hauteur_rectangulaire_base + self.hauteur_rue,
                             self.width_etage + 2*self.depassement_cote,
                             self.hauteur_rectangulaire_haut,
                             "#000000",
                             True,
                             self.couleur)
        # toit triangulaire
        if type_toit == 1:
            formes.rectangle(x,
                             nombre_etages*self.height_etage + self.hauteur_rue,
                             self.width_etage,
                             self.hauteur_rectangulaire_base,
                             "#000000",
                             True,
                             self.couleur)
            formes.triangle(x-self.depassement_cote,
                            nombre_etages*self.height_etage + self.hauteur_rectangulaire_base + self.hauteur_rue,
                            x+self.width_etage//2,
                            nombre_etages*self.height_etage + self.hauteur_rectangulaire_base + self.hauteur_rue + self.hauteur_triangle,
                            x+self.width_etage + self.depassement_cote,
                            nombre_etages*self.height_etage + self.hauteur_rectangulaire_base + self.hauteur_rue,
                            "#000000",
                            True,
                            self.couleur)