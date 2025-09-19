import random


"""
n = int(input("n :"))

print("X " * n)
for i in range(n - 2):
    print("X " + "  "*(n-2) +"X ")
print("X "*n)
"""
"""
def carre_croix(n):
print("X " * n)
for i in range(n - 2):
    print("X " + "  "*(n-2) +"X ")
print("X "*n)
"""

"""
def triangle(n):
    for i in range(1, n+1):
        if i == 1:  
            print("  " * (n-i) + "X ")
        elif i == n:  
            print("X " * (2*i-1))
        else:  
            print("  " * (n-i) + "X " + "  " * (2*i-3) + "X ")

triangle(6)

"""
"""
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
"""

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

