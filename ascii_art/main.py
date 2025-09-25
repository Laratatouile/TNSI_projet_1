import random

def carre_diagonale(n):
    for i in range(n):
        ligne = ""
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j :
                ligne += "X "
            elif j == i:
                 i + j 
            else:
                ligne += "  "
        print(ligne)

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

def carre(cote):
    # Première ligne
    print("X " * cote)

    # Lignes du milieu
    for i in range(cote - 2):
        print("X " + "  " * (cote - 2) + "X ")

    # Dernière ligne
    if cote > 1:  # pour éviter un double affichage quand le coté est égale a 1
        print("X " * cote)



n = int(input("Longueur du côté : "))
carre(n)

def carre_croix(cote):
    for i in range(cote):
        ligne = ""
        for j in range(cote):
            # les bordures du carré
            if i == 0 or i == cote - 1 or j == 0 or j == cote - 1:
                ligne += "X "
            # Ligne centrale horizontale pour la croix
            elif i == cote // 2:
                ligne += "X "
            # Ligne centrale verticale pour la croix
            elif j == cote // 2:
                ligne += "X "
            # Espaces
            else:
                ligne += "  "
        print(ligne)


# Exemple d'utilisation 
n = int(input("Longueur du côté : "))
carre_croix(n)

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


# Exemple au choix
n = int(input("Longueur du côté : "))
origami(n)
# Triangle vide en croix

def triangle(n):
    for i in range(1, n+1):
        if i == 1:  # la première ligne = 1 X
            print(" " * (n-i) + "X")
        elif i == n:  # la dernière ligne sera pleine
            print("X" * (2*i-1))
        else:  # lignes intermédiaires = X ... X
            print(" " * (n-i) + "X" + " " * (2*i-3) + "X")


triangle(9)


