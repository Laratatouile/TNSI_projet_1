
### <u><span style="color:#d51515">1)Création d'un carré</span></u><br>
On commence par tracer un carré :

La première et la dernière ligne sont entièrement remplies de `X`.

Les lignes du milieu ne gardent que les bords, ce qui forme un carré creux.
```python
def carre(cote):
    # Première ligne du carré
    print("X " * cote)

    # les lignes du milieux
    for i in range(cote - 2):
        print("X " + "  " * (cote - 2) + "X ")

    # Dernière ligne du carré
    if cote > 1:  # pour éviter un double affichage du carré quand le cote est egale a 1
        print("X " * cote)

# permet de choisir n'importe quel nombre de "X" pour le carré
n = int(input("Longueur du côté : "))
carre(n)
```

### <u><span style="color:#d51515">2)Carré avec une diagonale au milieu</span></u><br>
On reprend le carré vide et on ajoute la diagonale principale du haut a gauche jusqu'en bas a droite.
Cela dessine une ligne traversant le carré en plus de son contour.ce qui va formé un carré avec une diagonale au milieu.
```python
def carre_diagonale(n):
    for i in range(n):
        ligne = ""
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j :
                ligne += "X "
            else:
                ligne += "  "
        print(ligne)

carre_diagonale(7)
```

### <u><span style="color:#d51515">3)Carré ave une croix</span></u><br>
Ici, le carré est complété par deux axes centraux :

Une ligne horizontale au milieu.
Une ligne verticale au milieu.
On obtient un carré en forme de croix.
```python
def carre_croix(cote):
    for i in range(cote):
        ligne = ""
        for j in range(cote):
            # Bordures
            if i == 0 or i == cote - 1 or j == 0 or j == cote - 1:
                ligne += "X "
            # Ligne centrale horizontale
            elif i == cote // 2:
                ligne += "X "
            # Ligne centrale verticale
            elif j == cote // 2:
                ligne += "X "
            # les espaces
            else:
                ligne += "  "
        print(ligne)


# Exemple d'utilisation de notre fonction
n = int(input("Longueur du côté : "))
carre_croix(n)
```

### <u><span style="color:#d51515">4)carré origami</span></u><br>
Enfin pour ce carré,on va ajouter deux diagonales  :

- Une diagonale descendante et complète.

- Et une diagonale montante qui s’arrête au centre.
Le tout donne un effet “origami” à l’intérieur du carré.
```python
def origami(cote):
    for i in range(cote):
        ligne = ""
        for j in range(cote):
            if i == 0 or i == cote - 1 or j == 0 or j == cote - 1:  # bordures
                ligne += "X "
            elif i == j:  # diagonale descendante complète
                ligne += "X " 
            elif i + j == cote - 1 and i <= cote // 2:  # diagonale montante arrêtée au milieu
                ligne += "X "
            else:
                ligne += "  "
        print(ligne)


# Exemple
n = int(input("Longueur du côté : "))
origami(n)
```