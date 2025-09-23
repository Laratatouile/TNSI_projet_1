# <span style="color:white; background-color:#6b6b6bff; padding:190px; padding-top:25px; padding-bottom:25px;font-size:35px">le fichier lumieres.py</span>

## <u><span style="color:#d51515">le fichier en petites etapes</span></u><br>

Ce fichier possède plusieures fonctions
### <u><span style="color:#d51515">1) la fonction</span></u> `couleur_ciel`<br>
```python
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
```

Cette fonction permet de changer la couleur du ciel le matin et lel soir.<br>
Cette fonction est récurcive avec la methode ontimer de screen.<br>

Cette fonction prend en charges plusieurs arguments:<br>
 - `temps_depart` : le temps "time.time()" au début des itérations.<br>
 - `heure` : "jour" ou "nuit" qui permet de savoir si on passe vers la nuit ou le jour.<br>
 - `screen` : la methode qui permet de faire des ontimer.<br>


### <u><span style="color:#d51515">1) la fonction</span></u> `_calcul_couleur_`<br>
Le '_' devant le nom de la fonction permet de donner l'information a l'utilisateur que la fonction ne lui est pas destinée.<br>

```python
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
```

Cette fonction permet de passer d'une couleur a une autre progressivement.<br>
Elle prend en chage plusieurs arguments:<br>
 - `couleur1` : la première couleur<br>
 - `couleur2` : la deuxième couleur<br>
 - `multiplicateur` : un flottant entre 0 et 1 qui permet de définir le niveau d'avancement du changement de couleur<br>
 - `direction` : un booleen True passe de la couleur 1 a la 2 et False l'inverse<br>



