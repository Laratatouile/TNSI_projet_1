
### <u><span style="color:#d51515">1) Création du sapin</span></u><br>
Dans cette première étape, on trace la structure du sapin :
on crée le sapin vide

Un petit chapeau `^` au sommet.

Des branches vides avec` / et \`.

Un tronc représenté par trois fois` |||`.

C’est la base de notre sapin de Noël.
```python
def sapin(taille):
# Étape 1 : triangle + tronc
    print("sapin 1 :")
    print(" " * taille + "^")  
    for i in range(1, taille + 1):
        print(" " * (taille - i) + "/" + " " * (2 * i - 1) + "\\")
    for k in range(3):  
        print(" " * (taille - 1) + "|||")
```

### <u><span style="color:#d51515">2)Etoile sur le sapin vide</span></u><br>

On ajoute une étoile `*` au sommet du sapin.
Elle vient se placer juste au-dessus du `^` et rend le sapin plus festif et plus sublime.

```python
# Étape 2 : étoile
    print("\nsapin 2 :")
    print(" " * taille + "*")   
    print(" " * taille + "^")   
    for i in range(1, taille + 1):
        print(" " * (taille - i) + "/" + " " * (2 * i - 1) + "\\")
    for k in range(3):
        print(" " * (taille - 1) + "|||")
```

### <u><span style="color:#d51515">3) ajout des decoration</span></u><br>
Pour donner du style, on remplit les branches avec une alternance de guillemets` ' et "`.
Cela crée un motif régulier à l’intérieur du sapin et simule des décorations accrochées aux branches comme des guirlandes.
```python
# Étape 3 : texture ' et "
    print("\nsapin 3 :")
    print(" " * taille + "*")
    print(" " * taille + "^")
    for i in range(1, taille + 1):
        ligne = ""
        for j in range(2 * i - 1):
            if j % 2 == 0:
                ligne += "'"
            else:
                ligne += '"'
        print(" " * (taille - i) + "/" + ligne + "\\")
    for k in range(3):
        print(" " * (taille - 1) + "|||")
```

### <u><span style="color:#d51515">4)Ajout des boules et décorations aléatoires dans le sapin</span></u><br>
On ajoute plein de décorations en rendant le sapin aléatoire :

Chaque emplacement a 20 % de chance de contenir une boule` o`.

Sinon, il contient un guillemet `' ou "`.

Ainsi, chaque exécution du programme génère un sapin différent, unique et décoré de façon aléatoire se qui rend le tout magique comme la magie de noel.
```python
# Étape 4 : boule et déco aléatoires
    print("\nsapin4! :")
    print(" " * taille + "*")
    print(" " * taille + "^")
    for i in range(1, taille + 1):
        ligne = ""
        for j in range(2 * i - 1):
            if random.random() < 0.2:   # 20% chance d'avoir une boule
                ligne += "o"
            else:
                ligne += random.choice(["'", '"'])
        print(" " * (taille - i) + "/" + ligne + "\\")
    for k in range(3):
        print(" " * (taille - 1) + "|||")



sapin(6)

```