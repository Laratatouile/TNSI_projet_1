### <u><span style="color:#d51515">1)Fonction triangle</span></u><br>
Ce programme nous permet de creer un triangle sous forme de fonction, l'utilisateur peut modifier a 
n'importe quel moment le code en modifiant la valeur 6 dans la dernière ligne du programme
```python
def triangle(n):
    for i in range(1, n+1):
        if i == 1:  # la première ligne = 1 X
            print(" " * (n-i) + "X")
        elif i == n:  # la dernière ligne = pleine
            print("X" * (2*i-1))
        else:  # lignes intermédiaires = X ... X
            print(" " * (n-i) + "X" + " " * (2*i-3) + "X")


triangle(9)
```
