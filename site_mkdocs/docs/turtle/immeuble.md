# <span style="color:white; background-color:#6b6b6bff; padding:170px; padding-top:25px; padding-bottom:25px;font-size:35px">le fichier immeubles.py</span>

## <u><span style="color:#d51515">le fichier en petites etapes</span></u><br>
Ce fichier est la base de la création et du dessin des immeubles.<br>
Ce fichier etant complexe a comprendre il bénéficiera d'une attention particulière.<br>



Ce fichier possède plusieures fonctions.
### <u><span style="color:#d51515">1) la fonction</span></u> `immeubles`<br>
Ce fichier est un peu la base de tout le fichier c'est lui qui va donner l'affichages aux etages de l'immeuble.<br>
```python
def immeuble(x:int):
    """ charge les variables de la fonction """

    couleur = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    nombre_etages = random.randint(1, 5)

    for i in range(nombre_etages):
        etage(x, i, couleur)
    toit(x, nombre_etages)
```
Cette fonction prend comme argument:<br>
 - `x` : la position $x$ en haut a gauche de la fenetre<br>


Décortiquons la fonction:<br>
`couleur = "#{:06x}".format(random.randint(0, 0xFFFFFF))`<br>
Cette ligne permet de generer aléatoirement une couleur qui sera composée de 6 chiffres héxadécimaux.<br>
Le .format permet de remplacer le :06x par les nombres aléatoires.<br>

on a également une boucle qui gérère le bon nombre d'étages.<br>
la fonction fini par éxécuter la fonction toit qui dessinera un toit aléatoire.<br>

### <u><span style="color:#d51515">2) la fonction</span></u> `etage`<br>
Cette fonction va generer et dessiner un etage avec les fenetres la porte et les balcons.<br>
```python
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
```
Cette fonction prend en charge plusieurs arguments:<br>
 - `x` : la position $x$ a gauche de l'étage<br>
 - `numero_etage` : le nombre d'étages déjà dessinés<br>
 - `couleur_etage` : la couleur de l'étage<br>



Cette fonction peut se diviser en 3 parties plus simples a comprendre.<br>
<u>De la ligne 1 a la ligne 14</u><br>
La fonction initialise les variables et dessines le sol vert.<br>
<u>De la ligne 15 a la ligne 21</u><br>
Si on est au premier étage.<br>
Il genere la position de la porte.<br>
Et il dessiner 3 objets dont la porte et des fenetres normales.<br>
<u>De la ligne 22 a la ligne 28</u><br>
La fonction génère 3 fenetres ou balcons aléatoirement.<br>


### <u><span style="color:#d51515">3) la fonction</span></u> `fenetre`<br>
```python
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
```
Cette fonction prend en charge plusieurs arguments:<br>
 - `x` : la position $x$ a gauche de la fenetre<br>
 - `y` : la position $y$ en haut de la fenetre<br>
 - `nombre_fenetre` : le nombre de fenetres déjà dessinées<br>


Cette fonction peux aussi etre découpée en parties simples.<br>
<u>De la ligne 1 a la ligne 7</u><br>
La fonction initialise les variables.<br>
<u>De la ligne 10 a la ligne 16</u><br>
La fonction calcule le decalage a avoir avec le cote gauche de l'immeuble.<br>
Puis elle dessine un carre qui est en fait la fentre de 30px de cote.<br>


### <u><span style="color:#d51515">4) la fonction</span></u> `creer_forme_balcon`<br>
Cette fonction enregistre les paires de coordonées des lignes du balcon.<br>
Cela va permettre de créer un 'tampon' avec la forme du balcon qui va pouvoir être posé.<br>

```python
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
```

Cette fonction est déjà expliquée dans le code pour ma compréhension personelle.<br>


### <u><span style="color:#d51515">5) la fonction</span></u> `balcon`<br>
Met un 'tampon' du balcon sur la toile

```python
def balcon(x:int, y:int):
    """ dessine un balcon """
    setheading(90)
    shape("balcon")
    goto(x, y)
    stamp()
```

Cette fonction prend un chage les arguments:<br>
 - `x` : la position $x$ du balcon<br>
 - `y` : la position $y$ du balcon<br>


### <u><span style="color:#d51515">6) la fonction</span></u> `porte`<br>
```python
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
```

Cette fonction peux se découper en trois parties.<br>
<u>De la ligne 1 a la ligne 12</u><br>
La fonction initialise les variables de la fonction<br>

<u>De la ligne 14 a la ligne 17</u><br>
la fonction peux dessiner deux portes différentres l'une rectangulaire, l'autre avec le dessus arrondi.<br>

<u>De la ligne 19 a la ligne 24</u><br>
La fonction dessine la clanche.<br>