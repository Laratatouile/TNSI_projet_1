```python
def sapin(taille):
# Étape 1 : triangle + tronc
    print("sapin 1 :")
    print(" " * taille + "^")  
    for i in range(1, taille + 1):
        print(" " * (taille - i) + "/" + " " * (2 * i - 1) + "\\")
    for k in range(3):  
        print(" " * (taille - 1) + "|||")


# Étape 2 : étoile
    print("\nsapin 2 :")
    print(" " * taille + "*")   
    print(" " * taille + "^")   
    for i in range(1, taille + 1):
        print(" " * (taille - i) + "/" + " " * (2 * i - 1) + "\\")
    for k in range(3):
        print(" " * (taille - 1) + "|||")


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


# Étape 4 : décorations aléatoires
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